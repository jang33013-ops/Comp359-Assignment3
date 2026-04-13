#Generates all labeled trees on n vertices using Prüfer sequences,

import itertools
from decode_prufer import decode_prufer
import json
def get_max_degree(edges, n):      #filters to max degree <= 3, and stops if results exceed 100 graphs.
   
    degree = {v: 0 for v in range(1, n + 1)}
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
    return max(degree.values())
def generate_trees(n, max_degree=3, stop_at=100):   #Stops early if the accepted list would exceed stop_at trees.
    if n < 2:
        raise ValueError("n must be at least 2.")

    if n == 2:
        return [[(1, 2)]], False, 1
    accepted = []
    stopped_early = False
    total_checked = 0
    for code in itertools.product(range(1, n + 1), repeat=n - 2):
        total_checked += 1
        edges = decode_prufer(list(code))

        if get_max_degree(edges, n) <= max_degree:
            accepted.append(edges)

            if len(accepted) >= stop_at:
                stopped_early = True
                break
    return accepted, stopped_early, total_checked
if __name__ == "__main__":                                                               # Main required case: n=7, max degree 3, stop at 100
    accepted, stopped_early, total_checked = generate_trees(n=7, max_degree=3, stop_at=100)
    print(f"n=7 | checked: {total_checked} | accepted: {len(accepted)} | stopped early: {stopped_early}")
    for i, edges in enumerate(accepted, 1):
        print(f"  Tree {i:3d}: {edges}")
    with open("accepted_trees.json", "w") as f:  # save the tress in a file 
        json.dump(accepted, f)
    print(f"Accepted {len(accepted)} trees saved to accepted_trees.json")
