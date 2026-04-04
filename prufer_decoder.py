# prufer_decoder.py

def decode_prufer(code):
    """
    Decode a Prüfer code into a labeled tree represented as a list of edges.
    
    Parameters:
    code (list of int): The Prüfer sequence
    
    Returns:
    edges (list of tuple): List of edges (u, v) representing the tree
    """
    n = len(code) + 2  
    degree = [1] * n    
    
    for node in code:
        degree[node - 1] += 1  
    
    edges = []
    ptr = 0  
    
    while degree[ptr] != 1:
        ptr += 1
    leaf = ptr
    
    for node in code:
        edges.append((leaf + 1, node))  
        
        degree[leaf] -= 1
        degree[node - 1] -= 1
        
        if degree[node - 1] == 1 and node - 1 < ptr:
            leaf = node - 1
        else:
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr
    
    u = [i + 1 for i, deg in enumerate(degree) if deg == 1]
    edges.append((u[0], u[1]))
    
    return edges


def print_step_by_step(code):
    """
    Print step-by-step decoding process of the Prüfer code.
    """
    print(f"Decoding Prüfer code: {code}")
    n = len(code) + 2
    degree = [1] * n
    for node in code:
        degree[node - 1] += 1
    
    ptr = 0
    while degree[ptr] != 1:
        ptr += 1
    leaf = ptr
    
    remaining_code = code.copy()
    step = 1
    
    while remaining_code:
        node = remaining_code.pop(0)
        print(f"\nStep {step}:")
        print(f"  Smallest leaf not in remaining code: {leaf + 1}")
        print(f"  Connect leaf {leaf + 1} to node {node}")
        
        degree[leaf] -= 1
        degree[node - 1] -= 1
        
        print(f"  Updated degrees: {degree}")
        
        if degree[node - 1] == 1 and node - 1 < ptr:
            leaf = node - 1
        else:
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr
        
        print(f"  Next leaf to connect: {leaf + 1 if leaf < n else 'None'}")
        step += 1
    
    u = [i + 1 for i, deg in enumerate(degree) if deg == 1]
    print(f"\nFinal step:")
    print(f"  Connect remaining leaves {u[0]} and {u[1]}")
    print(f"Decoded edges: {[(u[0], u[1])]}")
