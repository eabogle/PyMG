import pandas as pd
import numpy as np

class QG:
    def __init__(self, graph_name: str):
        self.graph_name = graph_name
        
        # Data containers
        self.edge_to_node = None       
        self.edge_lengths = None      
        self.node_coor = None   
        self.node_to_edge = None       
        self.discr_points = None 
        
        
