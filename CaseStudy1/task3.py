lst = ["D","A","T","A","S","C","I","E","N","C","E"]

print(len(lst))
print(lst[0], lst[10])
lst2 = lst[0:4]
print(lst2)
lst.pop(8)
print(lst)
lst.append("<3")
lst.insert(8, "N")
print(lst)