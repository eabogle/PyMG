import os
import pandas as pd
import numpy as np

class QG:
    def __init__(self, graph_name: str, base_path: str = "../graph_data/"):
        self.graph_name = graph_name
        self.data_path = os.path.join(base_path, graph_name)

        # Data containers
        self.edge_to_node = None       
        self.edge_lengths = None      
        self.node_to_coor = None   
        self.node_to_edge = None       
        self.discr_points = None 
        
        
    def load_data(self):
        """
        Load the graph data from the specified path.
        """
        try:
            self.edge_to_node = pd.read_csv(os.path.join(self.data_path, "edge_to_node.csv"), header=None)
            self.edge_lengths = pd.read_csv(os.path.join(self.data_path, "edge_lengths.csv"), header=None)
            self.node_to_coor = pd.read_csv(os.path.join(self.data_path, "node_to_coor.csv"), header=None)
            self.node_to_edge = pd.read_csv(os.path.join(self.data_path, "node_to_edge.csv"), header=None)
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")