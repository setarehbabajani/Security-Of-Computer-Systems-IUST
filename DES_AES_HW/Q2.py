from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# تولید کلید و داده ورودی
key = get_random_bytes(16)  # کلید 16 بایتی
data = 'It is a test message'.encode('utf-8')

# رمزنگاری
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))
iv = cipher.iv

# چاپ داده‌های رمزنگاری شده
print("key:", key.hex())
print("IV:", iv.hex())
print("cipher text:", ciphertext.hex())

# رمزگشایی
decipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = unpad(decipher.decrypt(ciphertext), AES.block_size)

# چاپ داده‌های رمزگشایی شده
print("plain text:", plaintext.decode('utf-8'))
