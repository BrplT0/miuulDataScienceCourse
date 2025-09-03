students = ["ali","veli","ayşe","talat","zeynep","ece"]
müh_fak = students[0:3]
tıp_fak = students[3:]

for index, student in enumerate(müh_fak):
    print(f"Mühendislik Fakültesi {index+1}. öğrenci: {student}")

for index, student in enumerate(tıp_fak):
    print(f"Tıp Fakültesi {index+1}. öğrenci: {student}")