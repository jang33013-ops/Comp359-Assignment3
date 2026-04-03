"""
Prüfer Code Decoding — Member 3
Reconstructs a labeled tree from a Prüfer sequence.

Algorithm:
  Given a Prüfer sequence of length n-2, the tree has n vertices labelled 1..n.
  Repeat n-2 times:
    1. Find the smallest label NOT in the remaining code (this is a leaf).
    2. Connect that leaf to the first element of the remaining code.
    3. Remove the leaf from the available set and remove the first element of the code.
  The last two remaining labels form the final edge.
"""


def decode_prufer(code):
   
    if len(code) == 0:
        raise ValueError("Prüfer code must be non-empty (encodes a tree on at least 3 vertices).")

    n = len(code) + 2
    labels = list(range(1, n + 1))

    for val in code:
        if val < 1 or val > n:
            raise ValueError(f"Label {val} is out of range for a tree on {n} vertices (1..{n}).")

    edges = []
    remaining_code = list(code)
    available = set(labels)

    for _ in range(n - 2):
        code_set = set(remaining_code)
        leaf = min(v for v in available if v not in code_set)
        neighbor = remaining_code[0]
        edge = (min(leaf, neighbor), max(leaf, neighbor))
        edges.append(edge)
        available.remove(leaf)
        remaining_code.pop(0)

    u, v = sorted(available)
    edges.append((u, v))

    return edges


def decode_prufer_verbose(code):
    """
    Same algorithm as decode_prufer(), but prints each step for teaching purposes.
    """
    if len(code) == 0:
        raise ValueError("Prüfer code must be non-empty.")

    n = len(code) + 2
    labels = list(range(1, n + 1))

    print(f"Prüfer code : {code}")
    print(f"Vertices    : {labels}  (n = {n})")
    print("-" * 50)

    edges = []
    remaining_code = list(code)
    available = set(labels)

    for step in range(1, n - 1):
        code_set = set(remaining_code)
        leaf = min(v for v in available if v not in code_set)
        neighbor = remaining_code[0]
        edge = (min(leaf, neighbor), max(leaf, neighbor))
        edges.append(edge)

        print(f"Step {step}:")
        print(f"  Remaining code : {remaining_code}")
        print(f"  Available      : {sorted(available)}")
        print(f"  Leaf (smallest not in code): {leaf}")
        print(f"  Connect {leaf} — {neighbor}  →  edge {edge}")

        available.remove(leaf)
        remaining_code.pop(0)

    u, v = sorted(available)
    final_edge = (u, v)
    edges.append(final_edge)
    print(f"Final step:")
    print(f"  Remaining vertices: {sorted(available)}")
    print(f"  Connect {u} — {v}  →  edge {final_edge}")
    print("-" * 50)
    print(f"Edge list: {edges}")
    return edges


if __name__ == "__main__":
    examples = [[1, 1], [2, 3], [1, 1, 3]]
    for code in examples:
        print()
        decode_prufer_verbose(code)
        print()
