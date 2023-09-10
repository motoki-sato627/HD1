import math
import networkx as nx

def rotate_point_around_center(a, b, angle):
    # 座標 a から中心座標 b を引く
    translated_a = (a[0] - b[0], a[1] - b[1])

    # 回転行列を作成
    cos_theta = math.cos(angle)
    sin_theta = math.sin(angle)
    rotated_x = cos_theta * translated_a[0] - sin_theta * translated_a[1]
    rotated_y = sin_theta * translated_a[0] + cos_theta * translated_a[1]

    # 回転後の座標に中心座標 b を再度加える
    rotated_a = (rotated_x + b[0], rotated_y + b[1])

    return rotated_a

def rotation(G):
    n=G.number_of_nodes()
    geo = nx.get_node_attributes(G, "geometry")
    n1=geo[0][0]
    n2=geo[0][1]
    angle=math.atan2(n1[1] - n2[1], n1[0] - n2[0])

    for i in range(n):
        fixed_geo=[]
        for g in geo[i]:
            g=rotate_point_around_center(g, n2, -angle)
            fixed_geo.append(g)
        G.nodes[i]['geometry'] = fixed_geo
    return G

def pixel_coors(G):
    n=G.number_of_nodes()
    geo = nx.get_node_attributes(G, "geometry")
    min_x=100000
    max_x=-100000
    min_y=100000
    max_y=-100000
    for i in range(n):
        for g in geo[i]:
            min_x=min(g[0], min_x)
            max_x=max(g[0], max_x)
            min_y=min(g[1], min_y)
            max_y=max(g[1], max_y)

    X=max_x-min_x
    Y=max_y-min_y
    r=0.125
    min_x-=r*X
    max_x+=r*X
    min_y-=r*Y
    max_y+=r*Y
    X=max_x-min_x
    Y=max_y-min_y
    D=max(X,Y)

    dx=(D-X)/2
    dy=(D-Y)/2
    
    for i in range(n):
        fixed_geo=[]
        for g in geo[i]:
            x=int(255*(g[0]+dx-min_x)/D)
            y=int(255*(g[1]+dy-min_y)/D)
            #x,yを(-1,1)にする
            x=(x-128)/128
            y=(y-128)/128
            fixed_geo.append((x, y))
            
        G.nodes[i]['geometry'] = fixed_geo
    return G

def preprocess(G):
  G=rotation(G)
  G=pixel_coors(G)
  return G
