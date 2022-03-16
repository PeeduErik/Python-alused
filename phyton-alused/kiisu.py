#info
m=0
n=0
raham=0
rahan=0
summa = 0
summa1 = 0
sugu=[]


#faili avamine
with open("palk.txt", "r")as fail:
#
    for i in fail:
        rida = i.split(" ")
        if rida [2] == "m":
            raham += int(rida[3])
            summa +=sum(rida[3])
            keskmine = summa/len(rida[3])
        elif rida [2] == "n":
            rahan += int(rida[3])
            summa1 +=int(rida[3])
            keskmine1 = summa1/len(rida[3])
 #Keskmiste palkade leidmine   
    '''
    for i in fail:
        rida = i.split(" ")
        if rida [2] == "m":
            summa = sum(raham)
            keskmine = summa/len(raham)
        elif rida [2] == "n":
            summa1 = sum(rahan)
            keskmine1 = summa1/len(rahan)
'''


#Keskmiste palkade printimine
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

