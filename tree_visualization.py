#Create one combined image containing up to 100 generated trees.

import json
import math
import os
import matplotlib.pyplot as plt
import networkx as nx

N_VERTICES = 7
MAX_TREES = 100
INPUT_FILE = "accepted_trees.json"
OUTPUT_FOLDER = "results"
OUTPUT_IMAGE = "all_trees_n7_maxdeg3.png"
COLORS = ["red", "blue", "green", "orange", "purple", "cyan", "magenta"] #Node labels are represented by colours to keep nodes small/legible.
NODE_COLOR_MAP = {i + 1: COLORS[i] for i in range(N_VERTICES)}

def load_graphs(path):
    with open(path, "r", encoding="utf-8") as f:
        accepted = json.load(f)
    graph_list = []
    for edges in accepted:
        graph = nx.Graph()
        graph.add_edges_from(edges)
        graph_list.append(graph)
    return graph_list
    
def draw_combined_image(graphs, output_path, max_trees=100):
    selected_graphs = graphs[:max_trees]
    count = len(selected_graphs)
    if count == 0:
        raise ValueError("No trees available to draw.")
    cols = math.ceil(math.sqrt(count))
    rows = math.ceil(count / cols)
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 2.4, rows * 2.4))      # layout keeps every miniature tree readable.
    if hasattr(axes, "flatten"):              # Normalize axes to a flat list for uniform handling.
        axes_list = list(axes.flatten())
    else:
        axes_list = [axes]
    for i, graph in enumerate(selected_graphs):
        ax = axes_list[i]
        pos = nx.spring_layout(graph, seed=42)
        nx.draw(
            graph,
            pos,
            with_labels=False,
            node_color=[NODE_COLOR_MAP[node] for node in graph.nodes()],
            node_size=120,
            edge_color="black",
            width=1.2,
            ax=ax,
        )
        ax.set_title(f"Tree {i + 1}", fontsize=8)
        ax.set_axis_off()
    for j in range(count, len(axes_list)):             # Hide extra subplot boxes when count is not a perfect square.
        axes_list[j].set_axis_off()
    fig.suptitle(
        f"Labeled trees (n=7, max degree ≤ 3) showing {count} trees",
        fontsize=14,
        y=0.995,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.98])
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
    
def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    graphs = load_graphs(INPUT_FILE)
    output_path = os.path.join(OUTPUT_FOLDER, OUTPUT_IMAGE)
    draw_combined_image(graphs, output_path, max_trees=MAX_TREES)
    print(f"Loaded {len(graphs)} trees from {INPUT_FILE}")
    print(f"Saved combined image: {output_path}")
