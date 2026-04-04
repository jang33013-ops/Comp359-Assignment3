# Member 4; Prufer code Encoding 
#1. Take a labelled tree a sinout 
#2. Convert it into its prufer code 
#3. Check correctness by decoding it back 
# Tree format; [(1,2),(1,4),(2,6),(6,3)]
def encode_prufer( tree_edges,n):
    adjacency ={}                         # creating adjacency list
    for i in range(1,n+1):
        adjacency [i]= []
    #fill this list using the edge list 
    for edge in tree_edges:
        a = edge[0]
        b = edge[1]
        adjacency[a].append(b)
        adjacency[b].append(a)
    prufer_code=[]
    for step in range (n-2):
        leaves=[]                                    # finding leaves with one neighbor 
        for vertex in adjacency:
            if len(adjacency[vertex])==1:
                leaves.append(vertex)
        smallest_leaf=min(leaves)                    # pick the smallest leaf
        neighbor=adjacency [smallest_leaf][0]         # leaf with just one neighbor 
        prufer_code.append(neighbor)                 # adding neighbor to prufer code
        adjacency[neighbor].remove(smallest_leaf)    # remove leaf from neighbor adjacency list 
        adjacency [smallest_leaf]=[]                 # removing all the connection form leaf
    return prufer_code
# starting decoding 
def decode_prufer(code):
    n=len(code)+2
    degree={}
    for i in range(1,n+1):                           # each vertex start with degree 1 
        degree[i]=1
    for value in code:                               # increase degree based on code
        degree[value] +=1
    edges=[]
    for value in code:                               # build tree from the code
        smallest_leaf=None
        for i in range (1,n+1):                      # finding smallest vertex with deg 1
            if degree[i]==1:
                smallest_leaf=i
                break
        edges.append((smallest_leaf,value))
        degree [smallest_leaf] -=1
        degree [value] -=1
    remaining=[]
    for i in range (1,n+1):
        if degree[i]==1:
            remaining.append(i)
    edges.append((remaining[0],remaining[1]))
    return edges


def sort_edges(edges):      
    sorted_list=[]
    for edge in edges:              
        a=edge[0]
        b=edge[1]
        if a<b:
            sorted_list.append((a,b))         # making comparison easier; (5,1) changes to (1,5)
        else:
            sorted_list.append((b,a))
    sorted_list.sort()
    return sorted_list

def test_encode_and_decode (tree_edges,n):
    print("original tree:")
    print(sort_edges(tree_edges))

    code=encode_prufer(tree_edges,n)
    print("\nencoded_tree")
    print(code)

    decoded_tree=decode_prufer(code)
    print("\ndecoded_tree")
    print(sort_edges(decoded_tree))

    if sort_edges(tree_edges)==sort_edges(decoded_tree):
        print("\nResults after Encoding and Decoding matches.")
    else:
        print("\nResults: TREES DO NOT MATCH")







