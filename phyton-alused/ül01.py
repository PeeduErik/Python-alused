#Harjutus 01
#Peedu Erik Pajo
#31.01.22


# konn
print("\"Cabernet Sauvignon\" või 'Cabernet Sauvignon'?")
print("  @..@")
print(" (----)")
print("( \__/ )")
print('^^ "" ^^')
# pindala
a = int(input("Sisesta ruudu külje pikkus: "))
p = a * a
print("Vastus: ruudu pindala on",p,"cm^2")


# vanuste vahe
nimi = input("lisa oma nimi: ")
print("Tere!", nimi+"!") #pluss ei lisa tühikut
vanus = int(input("Lisa oma vanus: "))
vanuste_vahe = 17-vanus
print("Meie vanuste vahe on:",vanuste_vahe,"aastat")


# Ümbermõõt
a = 12
b = 16
s=a*b
p = 2*(a+b)
print("Pindala",s,"ruutmeetrit")
print("Ümbermõõt",p,"meetrit")


# print
print("tere maailm") #sõne #string
print(2000) #int /täisarv
print(2.29) #float /komaarv
print('Ütle "Tere Maailm"') 
print("Ütle \"Tere Maailm\"") #escape string
print(type(2000)) #näitab andme tüüpi
