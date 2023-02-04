from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_OAEP
#Public Key Cryptography Standards
#Optimal-Asymmetric-Encryption-padding
key=RSA.generate(2048)
public_key=key.publickey().exportKey()
private_key =key.exportKey()
print(public_key)
print(private_key)
pk_file=open('pk.pem','w')
pk_file.write(public_key.decode('ascii'))
pk_file.close()
prk_file=open('prk.pem','w')
prk_file.write(private_key.decode('ascii'))
