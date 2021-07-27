from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import sys
import base64

with open('rsa_key.pub', 'rb') as f:
  public_key = RSA.import_key(f.read())
 
message = sys.stdin.read()

cipher_rsa = PKCS1_OAEP.new(public_key)
ciphertext = cipher_rsa.encrypt(message.encode())
print(base64.b64encode(ciphertext).decode())
