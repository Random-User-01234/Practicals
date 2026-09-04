from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

key_pair = RSA.generate(1024)

pubkey = key_pair.publickey()
print(f"Public Key: (n = {hex(pubkey.n)}, e = {hex(pubkey.e)})")

pubkeyPEM = pubkey.export_key()
print(pubkeyPEM.decode('ascii'))

privkey = key_pair
print(f"Private key: (n = {hex(privkey.n)}, d = {hex(privkey.d)})")

privkeyPEM = privkey.export_key()
print(privkeyPEM.decode('ascii'))

msg = b'SDSM College'
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)

print("Encrypted: ", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(privkey)
decrypted = decryptor.decrypt(encrypted)

print("Decrypted: ", decrypted.decode('utf-8'))