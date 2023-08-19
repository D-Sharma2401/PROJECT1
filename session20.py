#Encrypting data
import hashlib
password = input("Enter your password: ")
#encode password to UTF-8
password = password.encode('utf-8')
#Generate the secure SHA 256 Hash
password = hashlib.sha256(password).hexdigest()
print(password)