#Peedu Erik Pajo
#Ülesanne 3
#03.02.2022

#palindroom

palin = input("Sisesta palindroom: ")
print([::-1])

#Tundide ajad

start = input("Algus: ")
lopp = input("lõpp: ")
#tükeldus
hh1,mm1 = start.split(":")
hh2,mm2 = lopp.split(":")

#minutiteks teiseldamine
minutid = int(hh1)*60+int(mm1)
minutid2 = int(hh2)*60+int(mm2)
#ajavahe
ajavahe = abs(minutid-minutid2)
#teisendamine
hh = ajavahe // 60 #täisarv
mm = ajavahe % 60 #jääk

print(f"Õpilase päeva pikkus on {hh}:{mm}")

#Email

email = input("Sisesta email: ")
print('@' in email)

#Vandumine

vanne = input("Ära kurat ütle: ")
vanne = vanne.lower().replace("kurat","Lilleke")
print(vanne)

#Korralik kasutajanimi

nimi = input("Sisesta nimi: ")
nimi = nimi.strip().capitalize()
print("Tere "+nimi+"!")