dictr = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

print(dictr.keys())
print(dictr.values())

dictr["Daisy"] = ["England", 13]
print(dictr)
dictr["Ahmet"] = ["Turkey", 24]
print(dictr)
dictr.pop("Antonio")
print(dictr)