#Peedu erik Pajo
#Tunnitöö 1
#02.03.2022


#1.4


inimesed = int(input("Sisestage reisijate arv: "))
buss = int(input("Sisestage bussi kohtade arv: "))
viimases = inimesed % buss
if viimases ==0:
    bussid = inimesed // buss
    viimases = buss
else:
    bussid=inimesed//buss+1
print(f"Busse vaja:{bussid}\nViimases bussis inimesi:{viimases}")




#1.3

def pilved(a):
    if a > 6:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
        
a = int(input("Sisestage aluse kõrgus: "))

pilved(a)




#1.2


def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = " Aasta liblikas on: "
    lause = str(aasta)+lause_keskosa+liblikas
    print(lause)
liblikas()


#1.1


def maailm():
    print("Tere, maailm!")
    
maailm()
