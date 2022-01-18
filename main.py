from Crypto.Cipher import AES
from Crypto.Util.Padding import  pad

'''It must be 16, 24 or 32 bytes long(respectively for *AES - 128 *,*AES - 192 * or *AES - 256 *).'''

key = b'mysecretpassword'  # 16 byte keyt

cipher = AES.new(key,AES.MODE_CBC)


plaintext = b'this is my super secret message'
cipherText = cipher.encrypt(pad(plaintext,AES.block_size))




print("encrypted : ",cipherText)



print("  IV  :  ", cipher.iv)
