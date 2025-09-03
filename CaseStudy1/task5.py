l = [3,6,4,3,73,8,3,1,68,5,4,4,6,8,3,5,74,7,45,63,6,3,4574,5,35,34,4,2]

def div(full_list):
    listx = []
    listy = []
    for x in full_list:
        if x % 2 == 0:
            listx.append(x)
        else:
            listy.append(x)
    return listx, listy

evenlist, oddlist = div(l)
print(evenlist)
print(oddlist)
