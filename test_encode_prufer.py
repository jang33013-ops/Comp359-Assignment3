from encode_pruferM4 import encode_prufer, decode_prufer, sort_edges

def runtest(tree_edges,n,expected_code=None):
    print("Original Tree")
    print(sort_edges(tree_edges))

    code=encode_prufer(tree_edges,n)
    print ("\nEncoded Prufer code.",code)

    if expected_code is not None:
        print("Expected Code:",expected_code)
        if code == expected_code:
            print("Test passed")
        else:
            print("Test Failed")
    decoded_tree = decode_prufer(code)
    print("\nDecoded Tree:")
    print(sort_edges(decoded_tree))
    
    if sort_edges(tree_edges)== sort_edges(decoded_tree):
        print("Both Test passed")
    else:
        print("Test Failed")
    print("\n" + "-" * 40 + "\n")

#Test 1 
tree1=[(1,2),(1,3),(3,4),(3,5)]
n1=5
expected_code1=[1,3,3]
runtest(tree1,n1,expected_code1)

#test 2
tree2=[(1,2),(2,3),(2,4),(4,5)]
n2=5
expected_code2=[2,2,4]
runtest(tree2,n2,expected_code2)

#test 3 
tree3=[(1,2),(1,4),(2,6),(6,3),(6,5)]
n3=6
runtest(tree3,n3)
