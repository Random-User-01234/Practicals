import hashlib

text = input("Enter the text to encode: ")
result = hashlib.sha1(text.encode())


print("The Hexadecimal equivalent of SHA is: : ")
print(result.hexdigest())

