import hashlib

result = hashlib.md5(b'PersonA')
result1 = hashlib.md5(b'PersonB')

print("The byte equivalent of hash (PersonA): ", end="")
print(result.digest())

print("The byte equivalent of hash (PersonB): ", end="")
print(result1.digest())
