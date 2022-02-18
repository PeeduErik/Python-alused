#Peedu Erik Pajo
#ül 8
#17.02.2022

class Auto:
    automark = 0
    aasta = 0
    mudel = 0
    hind = 0
    läbisõit = 0
    
    
    def lisaautomark(self,x):
        self.automark = x
        
    def lisamudel(self,x):
        self.mudel = x
        
        
    def lisahind(self,x):
        self.hind = x
    
    def lisaaasta(self,x):
        self.aasta = x
    
    def lisaläbisõit(self,x):
        self.läbisõit = x
    def kuva(self):
         print(f"{self.automark} {self.mudel} {self.hind} {self.aasta} {self.läbisõit}")
       
        

uusObjekt = Auto()
uusObjekt.lisaautomark("Ford")
uusObjekt.lisamudel("Mustang 69")
uusObjekt.lisahind(50000)
uusObjekt.lisaaasta(1969)
uusObjekt.lisaläbisõit("100000km")
uusObjekt.kuva()