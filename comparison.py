# Compare the number of the labeled trees vs unlabeled trees 


def labeled_tree_count(n):
    # we are using Cayley's formula which is n**(n-2)
    if n == 1:
        return 1
    return n**(n-2)

# dictionary for the unlabeled tree counts from n = 1 to 7
unlabeled_counts = {
    1:1,
    2:1,
    3:1,
    4:2,
    5:3,
    6:6,
    7:11
}

print("Comparison of Labeled vs Unlabeled trees")
print("_" * 50)
print(f"{'n': <5}{'Labeled': <12}{'Unlabeled': <12}")
print("_" * 50)

for n in range(1,8):
    labeled = labeled_tree_count(n)
    unlabeled = unlabeled_counts[n]
    print(f"{n: <5}{labeled : <12}{unlabeled : <12}")


print("Labeled trees count different vertex names separately")
print("Unlabeled trees only count the different shapes")