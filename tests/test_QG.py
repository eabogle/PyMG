import sys
import os

# Add repo root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyMG.QG import QG

def test_qg_data_loading():
    graph_name = "G14" 
    qg = QG(graph_name=graph_name, base_path="../graph_data/")
    
    qg.load_data()
    
    # Simple print checks
    print("Edge to Node:")
    print(qg.edge_to_node.head())

    print("\nEdge Lengths:")
    print(qg.edge_lengths.head())

    print("\nNode Coordinates:")
    print(qg.node_to_coor.head())

    print("\nNode to Edge:")
    print(qg.node_to_edge.head())

    # Optional assertions (checking individually)
    assert qg.edge_to_node is not None and not qg.edge_to_node.empty, "edge_to_node failed to load"
    assert qg.edge_lengths is not None and not qg.edge_lengths.empty, "edge_lengths failed to load"
    assert qg.node_to_coor is not None and not qg.node_to_coor.empty, "node_to_coor failed to load"
    assert qg.node_to_edge is not None and not qg.node_to_edge.empty, "node_to_edge failed to load"

    print("\nAll data loaded successfully!")

if __name__ == "__main__":
    test_qg_data_loading()
