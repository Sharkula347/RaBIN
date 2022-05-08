'''Приложение'''
from RaBIN import *

mes=input()
immit=input()
btxt=bytearray(mes,'UTF-8')
bimmit=bytearray(immit,'UTF-8')
k=genkeys(512)

try:
    enc=encrypt(k[0],btxt+bimmit)
except:
    print('Ошибка при шифровании!')

try:
    decr=decrypt(k[1],enc)
except:
    print('Ошибка при расшифровании! Неверный файл, фраза-пароль или ключ.')
#print(enc)
print(decr)

for i in decr:
    decrypted=i[-len(bimmit):]
    if decrypted==bimmit:
        decrypted=i[:-len(bimmit)]

print(decrypted)


