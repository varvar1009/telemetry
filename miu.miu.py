encrypter_message= b'\x08r\x9b*\xeee\x96a\xafdY\x05F\t:\x95:I.\xabU\xa6S\x8a\xbaw\xf8V\x16sa\xbe'
super_secret_key = 1234654# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')

aesCipher = Cipher(algorithms.AES(key), modes.ECB(), 
backend=default_backend()) 
aesEncryptor = aesCipher.encryptor() 
aesDecryptor = aesCipher.decryptor()

print(aesDecryptor.update(encrypter_message))

rock= b'maks durak'
polk=aesEncryptor.update (klop)
print(polk)
k=b'\xdc\x9fw^\xfd\xb8\x83\x11a`\x84\t9\xa0\xef\xa8'
print(aesDecryptor.update(k))
super_secret_key = 12345# здесь должен быть числовой ключ
key = super_secret_key.to_bytes(16, 'big')
encrypter_message = b'maks durak'
print(encrypter_message)
print(aesDecryptor.update(encrypter_message))

password = 'Varvar'  
res = hashlib.md5(password.encode())  
print(res.hexdigest())

target_hash = "b0357b632ffd56428171695e240acafe"
alphabet = string.ascii_letters
start_time = time.time()

for combination in itertools.product(alphabet, repeat=5):
    password = ''.join(combination)  
    test_hash = hashlib.md5(password.encode()).hexdigest() 
    
    if test_hash == target_hash:
        print(f"Пароль найден: {password}")
        break

finish_time = time.time()
print(f"Время подбора: {finish_time - start_time:.6f} сек")