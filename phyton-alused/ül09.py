#Peedu Erik Pajo
#Ülesanne 09
#28.02.2022



import datetime
from datetime import timedelta
import locale
#Tänane kuupäev

aeg = datetime.datetime.today()   
kuupaev = aeg.strftime("%d.%B.%Y")
kuupaeva = aeg.strftime("%d.%m.%Y") 
print("Tänane kuupäev on:", kuupaev)


#Eesti kuupäev

locale.setlocale(locale.LC_ALL, 'ET')

kuup = datetime.datetime.now()

print("Tänane kuupäev on:",kuup.strftime("%d.%B.%Y"))

#isikukood

ik = "50428140877"

aasta = int(ik[1]+ik[2])+2000
kuu = int(ik[3]+ik[4])
päev = int(ik[5]+ik[6])
print(aasta,kuu,päev)

praegu = datetime.date.today().year
vanus = praegu - aasta
print("Su vanus: ",vanus)


