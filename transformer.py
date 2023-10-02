import math
import torch as th
import torch.nn as nn
import torch.nn.functional as F


class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout, activation):
        super().__init__() 
        self.linear_1 = nn.Linear(d_model, d_ff)
        self.dropout = nn.Dropout(dropout)
        self.linear_2 = nn.Linear(d_ff, d_model)
        self.activation = activation
    def forward(self, x):
        x = self.dropout(self.activation(self.linear_1(x)))
        x = self.linear_2(x)
        return x

def attention(q, k, v, d_k, mask=None, dropout=None):
    scores = th.matmul(q, k.transpose(-2, -1)) /  math.sqrt(d_k)
    if mask is not None:
        mask = mask.unsqueeze(0)
        scores = scores.masked_fill(mask == 1, -1e9)
    scores = F.softmax(scores, dim=-1)
    if dropout is not None:
        scores = dropout(scores)
    output = th.matmul(scores, v)
    return output

class MultiHeadAttention(nn.Module):
    def __init__(self, heads, d_model, dropout = 0.1):
        super().__init__()
        self.d_model = d_model
        self.d_k = d_model // heads
        self.h = heads
        self.q_linear = nn.Linear(d_model, d_model)
        self.v_linear = nn.Linear(d_model, d_model)
        self.k_linear = nn.Linear(d_model, d_model)
        self.dropout = nn.Dropout(dropout)
        self.out = nn.Linear(d_model, d_model)
    
    def forward(self, q, k, v, mask=None):
        # perform linear operation and split into h heads
        k = self.k_linear(k).view(-1, self.h, self.d_k)
        q = self.q_linear(q).view(-1, self.h, self.d_k)
        v = self.v_linear(v).view(-1, self.h, self.d_k)
        # transpose to get dimensions bs * h * sl * d_model
        k = k.transpose(0,1)
        q = q.transpose(0,1)
        v = v.transpose(0,1)# calculate attention using function we will define next
        scores = attention(q, k, v, self.d_k, mask, self.dropout)
        # concatenate heads and put through final linear layer
        concat = scores.transpose(0,1).contiguous().view(-1, self.d_model)
        output = self.out(concat)
        return output

class EncoderLayer(nn.Module):
    def __init__(self, d_model, heads, dropout, activation):
        super().__init__()
        self.norm_1 = nn.InstanceNorm1d(d_model)
        self.norm_2 = nn.InstanceNorm1d(d_model)
        self.self_attn = MultiHeadAttention(heads, d_model)
        self.door_attn = MultiHeadAttention(heads, d_model)
        self.gen_attn = MultiHeadAttention(heads, d_model)
        self.ff = FeedForward(d_model, d_model*2, dropout, activation)
        self.dropout = nn.Dropout(dropout)
        
    def forward(self, x, door_mask, self_mask, gen_mask):
        x2 = self.norm_1(x)
        x = x2 + self.dropout(self.door_attn(x2,x2,x2,door_mask)) \
                + self.dropout(self.self_attn(x2, x2, x2, self_mask)) \
                + self.dropout(self.gen_attn(x2, x2, x2, gen_mask))
        x2 = self.norm_2(x)
        x = x + self.dropout(self.ff(x2))
        return x

class TransformerModel(nn.Module):
    def __init__(
        self,
        in_channels,
        model_channels,
        out_channels,
    ):
        super().__init__()
        self.in_channels = in_channels
        self.model_channels = model_channels
        self.out_channels = out_channels
        self.num_layers = 4
        self.activation = nn.ReLU()
        self.features_emb = nn.Linear(self.in_channels, self.model_channels)
        self.transformer_layers = nn.ModuleList([EncoderLayer(self.model_channels, 4, 0.1, self.activation) for _ in range(self.num_layers)])
        self.output_linear1 = nn.Linear(self.model_channels, self.model_channels)
        self.output_linear2 = nn.Linear(self.model_channels, self.model_channels//2)
        self.output_linear3 = nn.Linear(self.model_channels//2, self.out_channels)

    def forward(self, masks, features):
        features = th.from_numpy(features).float() 
        features_emb = self.features_emb(features)
        out = features_emb
        for layer in self.transformer_layers:
            out = layer(out, masks['door_mask'], masks['self_mask'], masks['gen_mask'])
        out_dec = self.output_linear1(out)
        out_dec = self.activation(out_dec)
        out_dec = self.output_linear2(out_dec)
        out_dec = self.output_linear3(out_dec)
        return out_dec
  
