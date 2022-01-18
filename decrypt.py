from Crypto.Cipher import AES
from Crypto.Util.Padding import  unpad

key = b'mysecretpassword'  # 16 byte key - same key to decrpt

IV = b"\xa8#\xbf'\xebT\x07\xa9\xfaH\xabs#\xb2\xf1["  # iv gen when encrypted
encText = b"\x1b`\xec\xea\x8f;\xec\xdd\xe1\xc8\x91|*\xce1\xfeK\xb0\xc6\xd1\x17'\xd1S\xeb\xdb\xe6\x9d\x83\xd3Q\xf0"

cipher = AES.new(key,AES.MODE_CBC,IV)

plaintext = unpad(cipher.decrypt(encText),AES.block_size)
print(plaintext)
print(plaintext.decode())