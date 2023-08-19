numbers = list(range(10, 101, 10))
print("1. numbers:", numbers)
print("Type of numbers:", type(numbers))

numbers.append(30)
numbers.append(77)
numbers.append(95)

print("2. numbers:", numbers)
print("sum:", sum(numbers))
print("min:", min(numbers))
print("max:", max(numbers))
print("length:", len(numbers))

reverse_numbers = list(reversed(numbers))
print("reverse_numbers: ", reverse_numbers)

print("Index of 50 is:", numbers.index(50))
print("count of 30 is :", numbers.count(30))

data = [70, 30, 50, 90, 20]
print("data is:", data)
data.sort()
print("data in sorted arrangment is:", data)
names = ["john", "anna", "sia", "angel", "kim"]
names.sort()
print("names:", names)
print("min:", min(names))
print("max:", max(names))

names.remove("sia")
data.remove(30)

print(names)
print(data)

data = [10, 20, 30, 40, 50]
"""data.pop(0)
data.clear()
print(data)"""

data.insert(2, 77)
data.insert(len(data) ,99)
print(data)