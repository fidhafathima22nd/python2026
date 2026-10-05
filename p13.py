list1=[8,6,7,4,5]
list2=[5,4,3,1]
#a.check if the lists have the same length
if len(list1)==len(list2):
   print("a.the lists have the same length")
else:
    print("a.the lists have differentlengths.")
#b.check if the lists have the same sum
print(f"b. sum of list1:{sum(list1)} &sum of list2:{sum(list2)}")
if sum(list1) == sum(list2):
    print("the lists sum to the same value.")
else:
    print("the lists do not sum to the same value.")
#c.check if there are any commom values in both lists
common_values = set(list1) &set(list2)
if common_values:
    print(f"c.common values in both lists:{common_values}")
else:
    print("c.there are no common values in both lists.")
