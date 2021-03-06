import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

"""
    First pass, runtime: 1.120605230331421 seconds
"""
# for i in range(len(names_1)-1):
#     if names_1[i] in names_2:
#         duplicates.append(names_1[i])

"""
Using BST, runtime: 0.10721707344055176 seconds
"""
# Create a BST with names_2
bst = BinarySearchTree(names_2[0])
for i in range(1, len(names_2)):
    bst.insert(names_2[i])
# Loop through names_1 and call bst.contans()

for name in names_1:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
