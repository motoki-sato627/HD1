# preprocess_data


Code and instructions for converting msd dataset to house diffusion data format. 


 

Input Data
------
Data: [msd dataset](https://www.kaggle.com/datasets/caspervanengelenburg/modified-swiss-dwellings) 
<br/>
 
Requirtments
------
   
```
pip install argparse
pip install numpy
pip install matplotlib
pip install shapely
pip install descartes
git clone https://github.com/motoki-sato627/preprocess_data.git
cd preprocess_data

```

How to run
------
  
```python raster_to_json.py --path ~/Desktop/modified-swiss-dwellings-v1-train_50/graph_out_50```

Output data format
------

The data file (e.g., /sample_output/0.json).

```
ROOM_CLASS = {"living_room": 1, "kitchen": 2, "bedroom": 3, "bathroom": 4, "balcony": 5, "entrance": 6, "dining room": 7, "study room": 8,
              "storage": 10 , "front door": 15, "unknown": 16, "interior_door": 17}
              
              
# having room type in it
"room_type": [3, 4, 1, 3 ]

#bounding boxes per room        
"boxes: [[72.0, 161.0, 124.0, 220.0], [72.0, 130.0, 107.0, 157.0], [111.0, 28.0, 184.0, 203.0], [72.0, 87.0, 124.0, 126.0]] 

#first four entry are per list are rooms edges and 4th and 6th are showing what room type is on each side of edge 
"edges":[72.0, 161.0, 72.0, 220.0, 3, 0], ...,[107.0, 130.0, 72.0, 130.0, 4, 0], [148.0, 28.0, 148.0, 87.0, 1, 2]] 

#room indexes that are on each side of the edges
"ed_rm":[0], [0], [0], [0, 2], ..., [2], [2, 3], [2, 1], [2, 0], [2]] 
```
