#Peedu Erik Pajo
#Tunnitöö3
#02.03.2022

#3.4

f = input("Sisestage failinimi: ")
f = open(f, encoding="UTF-8")

for i in f:
    print(i)
    


#3.3
f = open("konto.txt", encoding="UTF-8")
for rida in f:
    if float(rida) > 0:
        print(rida,end="")


#3.2
porgand = 0
ringid = int(input("sisestage ringide arv: "))

for i in range(1,ringid+1):
    if i%2==0:
    
        porgand += i
print(f"Porgandite koguarv on:{porgand}")


#3.1
f = open ("rebased.txt", encoding="UTF-8")
vastuvoetud = []
for rida in f:
    vastuvoetud.append(int(rida))
    
aasta = input("Palun sisetage, aasta andmeid vajate: ")
print(f"{aasta}. oli vastuvõetud {vastuvoetud[int(aasta[3])-1]}")