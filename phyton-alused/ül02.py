#Peedu Erik Pajo
#Harjutus 02
#01.02.2022


#kolmnurga ümbermõõt
a,b,c = 15,16,18
p=a+b+c
print("Kolmnurga übermõõt on:",p)


#toote hind

hind = 36.75
ale = 0.4
kogus =3
summa = (hind-(hind*ale))*3
print("Kolme toote summa:",summa, "€")
#kütusekulu
'''
liitirid =int(input("tangiti:"))
kilomeetrid =int(input("läbiti: km"))
'''




#arvusüsteemid
arv =int(input("sisesta täisarv kümnendsüsteemis:"))
print("kahendsüsteemis on",bin(arv))
print("kuuteistkümnendsüsteemis on",hex(arv))

#ajateisendus
minutid =int(input("sisesta minutid: "))
arv1 = minutid//60
arv2 = minutid % 60
print("tunde on",arv1 )



import math
#kolmnurga hüpotenuus
a = 16
b = 9
valem = (a*a+b*b)
c = round(math.sqrt(valem),2)
print("hüpotenuus on:", c)

#rulluisutaja

kiirus = 29.9
aeg = 24
kaugus =round(((kiirus/60)*aeg),2)
print("24 Min jõuab:",kaugus,) 
#pitsa

hind = 12.90
sobrad = 3
jootraha = 0.1
summa = (hind*jootraha+hind/sobrad)
print("Iga üks maksab:",summa, "€")
    