from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
import os
class E_file:
    def __init__(self,key):
        self.key=key
        self.Counter = Counter.new(128)
        self.block_size =AES.block_size
    def encryption(self,file_name):
        c = AES.new(self.key,AES.MODE_CTR,counter=self.Counter)
        with open(file_name,"r+b") as fn:
            plaintext =fn.read(self.block_size)
            while plaintext:
                fn.seek(-len(plaintext),1)
                fn.write(c.encrypt(plaintext))
                plaintext =fn.read(self.block_size)
        fn.close()
        dd=file_name.strip(file_name.split('/')[-1])
        os.chdir(dd)
        os.rename(file_name,file_name.split('/')[-1]+'.en.mrx')
        #os.rename(direction,direction+".en.mrx")
        return [key]
    def decryption(self,file_name):
            d = AES.new(self.key,AES.MODE_CTR,counter=self.Counter)
            with open(file_name,'r+b')  as fe:
                plaintext =fe.read(self.block_size)
                while plaintext:
                    fe.seek(-len(plaintext),1)
                    fe.write(d.decrypt(plaintext))
                    plaintext =fe.read(self.block_size)
            fe.close()
            
print("This is a key:")           
direction =r'C:/Users/C850/Desktop/python/123.mp4'
key = Random.new().read(16)
c = E_file(key)
e =c.encryption(direction)
print('[+] Your file was encrytped...')
print("{Done}",direction.split('/')[-1])
ansower =input("Do you to reverce your file:[Y/N]:")
if(ansower=='y'):
    os.rename(direction+'.en.mrx',direction.strip('.en.mrx'))
    c.decryption(direction)
    print('[-] Your file is reverce>>',direction.split('/')[-1])



