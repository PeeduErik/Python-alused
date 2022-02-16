#Peedu Erik Pajo
#Ülesanne 05
#10.02.2022

#tärnid

import random
tärnid=[]

for i in range(5):
    tärnid.append(random.randint(1,10))
for n in range (len(tärnid)):
                  print("*"*tärnid[n])


#vanused

import random

vanused=[]

for i in range(5):
      vanused.append(random.randint(1,99))
   
print("kõikide vanuste summa",sum(vanused))
print("kõige noorem",min(vanused))
print("kõige vanem",max(vanused))

#duplikaadid

nimed = ['Juhan','Kati','Mario','Mario','Mati','Mati']
puhastatud = list(set(nimed))
for n in range(len(nimed)):
    print(n+1, nimed[n])
#õpilased

opilased = ['Juhan','Kati','Maarja','Mario','Mati']
for i in range(len(opilased)):
    print (f"{i+1}. {opilased[i]}")
valik = int(input("Sisesta number: "))
del opilased[valik-1]

uus_nimi = input("Sisesta uus või muudetud nimi: ")
opilased.insert(valik-1,uus_nimi)

print("Nimi muudetud")
print(opilased)


#nimede lisamine loendisse

nimed = []
for i in range(5):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)
nimed.sort()

for j in range (len(nimed)):
    print(nimed[j])