#Peedu Erik Pajo
#Tunnitöö 2
#02.03.2022


#2.6
import random
l = 14
v = int(input("Mitut õuna soovivad pöialpoisid?: "))
for i in range(v):
    o = random.randint(1,2)
    print(o)
    l = l - o
print ("lumivalgekesele jäi: ",(l))        

#2.5


arv = int(input("Sisetage täisarv: "))

nisuterad = 1

i = 1
while i <= arv:
    nisuterad *= 2
    i += 1
    
print(f"Niusteri {arv} ruudu eest:{nisuterad}")


#2.4

import random
taringud = int(input("Sisestage täringute arv: "))
for i in range(taringud):
    print(random.randint(1,6))

#2.2

ringid = int(input("Mitu ringi läbisid?: "))
porgandid = 0
ring = 1
while ring <= ringid:
    if i%2==0:
        porgandid+=1
    ring += 1
print(f"Porgandite koguarv on: {porgandid} ")

#2.1

aratus = int(input("Mitu korda peaks äratus helisema?: "))
for i in range(aratus):
    print("Tõuse ja sära!")