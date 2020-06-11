#! python 3
import hashlib
import base64

for word in open('file'): #filepath to wordlist.txt here
    username = "username" #insert username here
    word = word.rstrip("\n") #remove trailing newline
    word_ascii = word.encode("ascii") #transform string to bytes
    crypt_password = username + hashlib.md5(word_ascii).hexdigest() #hash word_ascii with md5 algorithm, then transform it to string in hex, and combine it with username.
    b64_cookie = base64.b64encode(crypt_password.encode("ascii")) #convert crypt_password to bytes then encode in Base64
    print(b64_cookie)