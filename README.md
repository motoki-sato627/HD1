# HouseDiffusion

## Installation
**1. Clone our repo and install the requirements:**

```
git clone https://github.com/motoki-sato627/HD.git
cd HD
pip install -r requirements.txt
pip install -e .
mkdir processed_rplan
```
**2. Download the dataset and create the datasets directory**

```
house_diffusion
├── datasets
│   ├── rplan
|   |   └── 0.json
|   |   └── 1.json
|   |   └── ...
|   └── list.txt
└── guided_diffusion
└── scripts
└── ...
```

## Running the code

**1. Training**

You can run a single experiment using the following command:
```
python train.py 
```
**2. Sampling**
To sample floorplans, you can run the following command from inside of the `scripts` directory. To provide different visualizations, please see the `save_samples` function from `scripts/image_sample.py`

```
python sample.py
```
