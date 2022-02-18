#Peedu Erik Pajo
#Ülesanne 7
#16.02.2022

#3
import math



def kuup(a):
    v = a**3
    return v
def kera(r):
    v = (4*math.pi*r**3)/3
    return v
def koonus(r,h):
    v = round(1/3*math.pi*r**2*h,2)
    return v
def silinder(r,h):
    v = round(math.pi*r**2*h,2)
    return v
    
loop = 1
while loop ==1:
    kujund = int(input("Vali kujund:\n 1 Kuup \n 2 Kera \n 3 Koonus \n 4 Silinder \n 5 lahku \n"))

    if kujund == 1:
        a = int(input("Sisesta kuubi külg: "))
        v = kuup(a)
        print("Kuubi ruumala on: ",v)
        
    elif kujund == 2:
        r = int(input("Sisesta kera raadius: "))
        v = kera(r)
        print("Kera ruumala on:", v)
        
    elif kujund == 3:
        r = int(input("Sisesta koonuse raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        v = koonus(r,h)
        print("Koonuse ruumala on: ",v)
    elif kujund == 4:
        r = int(input("Sisesta silindri raadius: "))
        h = int(input("Sisesta silindri kõrgus: "))
        v = silinder(r,h)
        print("Silindri ruumala on: ",v)
    else:
        print("lahku")
        loop = 0

    

          
#2

nimi = input("Sisesta oma nimi: ")
keel = input("Sisesta keel est,deu,eng: ")

def tsau():
    if keel == "est":
        print("Tere,",nimi)
    elif keel == "eng":
        print("Hello,",nimi)
    elif keel == "deu":
        print("Hallo,",nimi)
    
tsau()    
        
#1


nimi = input("Sisesta oma nimi ")

def minu_kontakt():
    print("Tere,",nimi)

minu_kontakt()