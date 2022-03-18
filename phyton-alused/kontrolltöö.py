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

#faili avamine
with open("palk.txt", "r")as fail:
#Summa saamine, keskmise arvutamine ja maksimaalse arvu leidmine
    for i in fail:
        rida = i.split(" ")
        if rida[2] == "m":
            summa += int(rida[3])
            keskmine = summa/6
            maks = max(rida[3])
        elif rida[2] == "n":
            summa1 += int(rida[3])
            keskmine1 = summa1/len(rida[3])
            maks1 = max(rida[3])
            
        
#Keskmiste välja andmine        
print ("Meeste keskmine palk on: ",keskmine,"€.")            
print ("Naiste keskmine palk on: ",keskmine1,"€.")

#Meeste ja naiste palga vahe leidmine
vahe=keskmine-keskmine1
print("Meeste palk on ",vahe,"€ võrra suurem.")

#Kellel on max palk

print ("Naiste suurim palk on: ",maks,"€.")
print ("Meeste suurim palk on: ",maks1,"€.")

#Keskmiste palkade võrdlemine
if keskmine1 < keskmine:
    print("See on naiste soo järgi diskrimineerimine.")
    
elif keskmine < keskmine1:
    print("See on meeste soo järgi diskrimineerimine.")
    
else:
    if keskmine1 == keskmine:
       print("Seal firmas ei diskrimineerita.")


#Tekst läheb faili, aga see rikub koodi ära ja peale seda enam ei tööta.

with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if keskmine1 < keskmine:
        file_object.write("\n")
        file_object.write("Seal Firmas toimub naiste vastu diskrimineerimine")
    

with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if keskmine < keskmine1:
        file_object.write("\n")
        file_object.write("Seal Firmas toimub meeste vastu diskrimineerimine")
    
with open("palk.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if keskmine == keskmine1:
        file_object.write("\n")
        file_object.write("Seal Firmas ei toimu diskrimineerimist")


