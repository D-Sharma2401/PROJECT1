# for each or enhanced for loop

data = list(range(10,101,10))
print(data)
"""for idx in range(len(data)):
    print(data[idx])"""
data = set(data)

#element can be any name of your choice
# enhaced for loop will work for list, tuple , set

for element in data:
    print(element)

student = {
    "rollno":10,
    "name":"fionna",
    "age":21
}
print("dictionary keys only...")

items = student.items()
for items in items:
    #print(item)
    print(items[0],items[1])

keys = student.keys()
for key in keys:
    print(key)

print("dictionary keys and values only...")
for key in student:
    print(key, student[key])