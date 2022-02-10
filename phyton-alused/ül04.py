#Peedu Erik Pajo
#Ülesanne 4
#03.02.2022

#Ruutude ja kuupide tabel  
print("   Arv | Ruut | Kuup")
for d in range(1,11):
    print(f" {d:6}|{d*d:6}|{d*d*d:6}")

#Pank

raha = 10000
intress = 0.05
aastad = 5
konto = 0

konto += raha
for i in range(aastad):
    kasum = intress*konto
    print(konto,kasum,kasum+konto)
    konto += kasum



#arvamismäng

nr = 9
loop = 1
kordade_arv = 0
 
print('Arva ära number 1-50')
 
while loop == 1:
    arva = int(input('Sisesta täisarv: '))
    
    if arva == nr:
        kordade_arv += 1
        print('Tubli tegid pakkumisi: ',kordade_arv)
        loop = 0
    elif arva < nr:
        kordade_arv += 1
        print('Sinu arv on liiga väike')
    else:
        kordade_arv += 1
        print('Sinu arv on liiga suur')
        
#viisik

for i in range (1, 101):
    if i % 5 == 0:
        print(i)



#pisike korrutus tabel

number = 5

for i in range(1,11):
    print (number ,'x', i, '=', number*i)


#paaris ja paaritu

number= input("Sisesta number: ")
if int(number) %2 == 0:
    print("{0} on paaris".format(number))
else:
    print("{0} on paaritu".format(number))


#loto

import random
print(random.randrange(0,99999))


#tärn

for i in range(0,5):           
    for j in range(0,5):       
        print('* ', end='')
    print()



for i in range(1,6):
    print("* "*i)
    
for m in range(5,0, -1):           
    for n in range(0,m):       
        print('* ', end='')
    print()

    

#jalgpall

sugu = input("Sisesta sugu: ")
if sugu == "mees":
    vanus = int(input("Sisesta vanus: "))
    if vanus >= 16 and vanus <=18:
         print("Sobid meeskonda")
    
    
#müük

hind = int(input("Sisesta toote hind: "))
if hind <= 10:
    ale = 0.1
else:
    ale = 0.2
tootehind = hind-(hind*ale)

print("Tootehind on:",tootehind)

     
#juubel

aasta = input("Sisesta sünniaeg kujul dd.mm.yyyy:")
d,m,y = aasta.split(".")
aasta1 = 2022
aasta2 = aasta1 - int(y)
if aasta2%5==0:
    print("sul on juubel")
else:
    print("sul pole juubel")


#matemaatika

a = int(input("Siesta arv1: "))
b = int(input("Sisesta arv2: "))
tehe = input("Vali tehe:\n + Liitmine \n - Lahutamine \n * Korrutamine \n / Jagamine \n")


if tehe=="+":
    v = a + b
elif tehe=="-":
    v = a - b
elif tehe=="*":
    v = a * b
elif tehe==":":
    v = a / b

else:
    vastus
print(f"{a}{tehe}{b}={v}")


#ruut kontroll

a = int(input("sisesta ruudu 1 külg: "))
b = int(input("sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruuduga")
else:
    print("Tegemist on ristkülikuga")