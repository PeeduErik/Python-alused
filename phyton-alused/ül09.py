#Peedu Erik Pajo
#Ülesanne 09
#28.02.2022

#kuupäev
import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_ALL, 'ET')

kuup = datetime.datetime.now()

print(kuup.strftime("%d.%B.%Y"))

#isikukood

ik = "50428140877"

aasta = int(ik[1]+ik[2])+2000
kuu = int(ik[3]+ik[4])
päev = int(ik[5]+ik[6])
print(aasta,kuu,päev)



                   