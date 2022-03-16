# Peedu Erik Pajo
#Kontrolltöö
#16.03.2022

#info
summa = 0
summa1 = 0
keskmine = 0
keskmine1 = 0
suur = 0
suur1 = 0
raham=[2340,2570,1960,2900,2850,2570]
rahan=[2060,2250,2370,2340,2120]

#faili avamine
with open("palk.txt", "r")as fail:
#Summa saamine, keskmise arvutamine ja maksimaalse arvu leidmine
    for i in fail:
        rida = i.split(" ")
        if rida[2] == "m":
            summa += int(rida[3])
            keskmine = summa/6
            
        elif rida[2] == "n":
            summa1 += int(rida[3])
            keskmine1 = summa1/len(rida[3])
           
            
        
#Keskmiste välja andmine        
print ("Meeste keskmine palk on: ",keskmine,"€.")            
print ("Naiste keskmine palk on: ",keskmine1,"€.")

#Meeste ja naiste palga vahe leidmine
vahe=keskmine-keskmine1
print("Meeste palk on ",vahe,"€ võrra suurem.")

#Kellel on max palk
print ("Naiste suurim palk on: ",max(rahan),"€.")
print ("Meeste suurim palk on: ",max(raham),"€.")

#Keskmiste palkade võrdlemine
if keskmine1 < keskmine:
    print("See on naiste soo järgi diskrimineerimine.")
else:
    if keskmine1 == keskmine:
        print("See oleks aus mõlema jaoks.")


#Tekst läheb faili, aga see rikub koodi ära ja peale seda enam ei tööta.
"""
with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0 :
        file_object.write("\n")
    file_object.write("Seal Firmas toimub nasite vastu diskrimineerimine")
 """

            



