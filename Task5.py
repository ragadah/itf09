dict1 = {"Name": "Raghad", "Age": 20}
dict2 = {"City": "Gaza", "Gender": "Female"}

concatenated_dict = {}
for key, value in dict1.items():
    concatenated_dict[key] = value

for key, value in dict2.items():
    concatenated_dict[key] = value

print("Concatenated Dict 3:", concatenated_dict)