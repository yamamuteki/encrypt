from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import base64

with open('rsa_key', 'rb') as f:
    private_key = RSA.import_key(f.read())

ciphertext = base64.b64decode(sys.stdin.read())

decipher_rsa = PKCS1_OAEP.new(private_key)
msg = decipher_rsa.decrypt(ciphertext).decode("utf-8")
print(msg)