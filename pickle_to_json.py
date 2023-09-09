import os
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from descartes.patch import PolygonPatch

def main():
    args = parse_args()
    pre_line=args.path 
    for i in range(50):
        num=str(i)
        line=pre_line+"/"+num+".pickle"
