# member6_visualization.py

import networkx as nx
import matplotlib.pyplot as plt
import json
import os
# accepted = list of edge lists returned by Member 5's generate_trees()
# accepted, stopped_early, total_checked = generate_trees(n=7, max_degree=3, stop_at=100)

# Load accepted trees
with open("accepted_trees.json", "r") as f:
    accepted = json.load(f)

print(f"Loaded {len(accepted)} accepted trees")
graph_list = []
for edges in accepted:
    G = nx.Graph()
    G.add_edges_from(edges)
    graph_list.append(G)


n = 7  # number of vertices
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']
node_color_map = {i+1: colors[i] for i in range(n)}

output_folder = "results"
os.makedirs(output_folder, exist_ok=True)

max_images = 100

for i, G in enumerate(graph_list):
    if i >= max_images:
        break

    # fixed layout for consistency
    pos = nx.spring_layout(G, seed=42)  # stable positions

    # draw tree
    nx.draw(
        G,
        pos,
        with_labels=False,  # hide numeric labels
        node_color=[node_color_map[node] for node in G.nodes()],
        node_size=500,
        edge_color='black',
        width=2
    )

    # save the image
    plt.savefig(f"{output_folder}/tree_{i+1}.png", dpi=300)
    plt.close()

print(f"Saved {min(len(graph_list), max_images)} tree images successfully!")