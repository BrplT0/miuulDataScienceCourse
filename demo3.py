int_list = [2,124,32,2346,3,3,523,646,7548,65,7346,6,347,456,435,46,57,345,346,7457,6]
int_dict = {}

for i in int_list:
    if i % 2 == 1:
        continue
    else:
        ik = i**2
        int_dict[i] = ik

print(int_dict)