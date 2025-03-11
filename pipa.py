import hashlib
import string
import time
import itertools
password = 'Varvar'  
res = hashlib.md5(password.encode())  
print(res.hexdigest())

target_hash = "ae72f935bdf3dcb7104ca078f8fc4f85"
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