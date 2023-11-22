#my_set = {0,1,2,3,4,5,6,7,8}
#my_set.add(9)
#my_set.remove(8)
#print("Set after adding nine:", my_set)
#print("Set after removing eight:", my_set)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1.union(set2)
print("Union of set1 and set2", union_set)

intersection_set = set1.intersection(set2)
print("intersection of set1 and set2", intersection_set)

difference_set = set2.difference(set1)
print("difference of set1 and set2", difference_set)