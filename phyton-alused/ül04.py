#Peedu Erik Pajo
#Ülesanne 4
#03.02.2022

#matemaatika

a = int(input("sisesta 1 arv: "))
b = int(input("sisesta teine arv: "))
tehe = int(input("vali tehe:\n 1) liitmine \n 2) lahutamine \n 3) korrutamine \n 4) jagamine \n "))
if tehe == 1:
    v = a + b
elif tehe == 2:
    v = a-b
elif tehe == 3:
    v = a*b
elif tehe == 4:
    v = a/b


    
    


#ruut kontroll

a = int(input("sisesta ruudu 1 külg: "))
b = int(input("sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruuduga")
else:
    print("Tegemist on ristkülikuga")