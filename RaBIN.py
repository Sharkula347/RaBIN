'''
   Программная реализация алгоритма Рабина.
   Автор: Казарян Максим
   Россия, Ростовская обл., г.Ростов-на-Дону, ФГБОУ ВО ДГТУ, фак.ИИВТ, гр. ВКБ43.
'''
from random import randint as rnd
from sympy import isprime as isp

PROGRESS = [0,None]

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')
    
def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')

def genkeys(length=256):
    global PROGRESS
    '''genkeys(Длина ключа в битах) - Генерирует ключи для криптосистемы Рабина'''
    n1 = rnd(2**(length-1),2**length-1)
    n2 = rnd(2**(length-1),2**length-1)
    PROGRESS[0]=0
    PROGRESS[1]='genk'
    while n1 % 4 !=3 or n2 % 4 !=3 :
        
        if n1 % 4 !=3:
            n1+=1
        else:
            PROGRESS[0] = 25
        if n2 % 4 !=3:
            n2+=1

    PROGRESS[0] = 50
    
    while not(isp(n1) and isp(n2)):
        
        if not isp(n1):
            n1+=4
        else:
            PROGRESS[0] = 75
        if not isp(n2):
            n2+=4

    PROGRESS[0] = 100
    
    return (n1*n2,(n1,n2)) #Возвращаем публичный ключ и закрытые ключи

def encrypt(open_key,mes):
    return int_to_bytes(pow(int_from_bytes(mes),2,open_key))

def decrypt(cls_keys,mes):
    PROGRESS[0]=0
    PROGRESS[1]='decr'
    mes = int_from_bytes(mes)
    p=cls_keys[0]
    q=cls_keys[1]
    a1=pow(mes,(p+1)//4,p)
    a2=-a1 % p
    b1=pow(mes,(q+1)//4,q)
    b2=-b1 % q

    variants=((a1,b1),(a1,b2),(a2,b1),(a2,b2))
    M = p * q
    r=[]
    for varis in variants:
        r.append((varis[0]*pow(q,-1,p)*q+varis[1]*pow(p,-1,q)*p) % M)
        PROGRESS[0]+=int(100/len(variants))
    return ([int_to_bytes(i) for i in r])

