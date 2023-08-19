def fetch():
    file = open("ipl-data-2022.csv", "r")
    lines  = file.readlines()

    for line in lines:
        yield line


# If function , yields, it means we get generator in return

result = fetch()
print("result: ", result)

# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result," no more record"))

while True:
    data = next(result, "nothing")
    print(data)
    if data == "nothing":
        break