#Peedu Erik Pajo
#Harjutus 06
#15.02.2022


ERE=0
KES=0
erakond=[]

with open('s6pru_l6ustaraamatus.txt','r') as fail:
    for i in fail:
        rida = i.split(" ")
        print(f"{rida[0]:11} {rida[1]:11}{rida[2]:11}{rida[3]:11}")
        if rida [2] == "RE":
            ERE += 1
        elif rida [2] == "KE":
            KES += 1
        if rida [2]  not in erakond:
            erakond.append(rida [2])

print("Reformikad ",ERE)
print("Kesk: ",KES)
print("Erakondi on: ",len(erakond))            
        
        
      