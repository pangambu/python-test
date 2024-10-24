import csv
names = []

#opening and reading a txt file
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names, reverse=True):
    print(f"Hello, {name}")



#opening and reading a csv file

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
    
    
print()


#sorting the csv file
namesToSort = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        namesToSort.append({"name": row["name"], "home": row["home"]})
        
        



for student in sorted(namesToSort, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")
