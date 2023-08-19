#STRINGS ARE IMMUTABLE
names = "John , Jennie , Jim , Jack , Joe"
print("names:", names)
upper_case_names = names.upper()

print("names now:", names, id(names))
print("upper_case_names:",upper_case_names, id(upper_case_names))
print("upper_case_names check:", )
s1 = names.capitalize()
quote = " be exceptional have a good day"

s2 = quote.title
s3 = names.swapcase()
s4 = names.replace('J', 'KO')

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4;", s4)

# password = input("Enter the password")
# #rstrip(), lstrip()
# print("Password:", password.strip())

data = '0001100011'
print("data:", data.strip('0'))

number = 3.5600000
number = float(str(number).strip('0'))
print(number, type(number))

message = "No Internet Connectivity"
print(message)
print(message.center(120))
print(message.rjust(120))
print(message.ljust(120))

data = "545"
print(data.zfill(50))

quote = "search for the candles rather than cursing the darkness"
print(quote.find('sing'))
print(quote.find('the'))
print(quote.index('the'))
print(quote.rindex('the'))

idx1 = quote.index('candle')
print(idx1)
idx2 = idx1 + len('candle')-1
print(idx2)
