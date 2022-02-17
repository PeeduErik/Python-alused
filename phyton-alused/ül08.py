#Peedu Erik Pajo
#ül 8
#17.02.2022

class Auto:
    automark = "Ford"
    aasta = 1969
    mudel = "Mustang 69"
    hind = 50000
    läbisõit = "100000km"
    
    
    
    def lisaautomark(self,x):
        self.automark = x
        
    def lisaaasta(self,x):
        self.aasta = x
        
    def lisahind(self,x):
        self.hind = x
    
    def lisamudel(self,x):
        self.mudel = x
    
    def lisaläbisõit(self,x):
        self.läbisõit = x
      def kuva(self):
        print("automark: {} \n Aasta: {} \n Hind: {}€ \n Mudel: {} \n Läbisõit"(self.Automark, self.Aasta, self.Hind, self.Läbisõit, self.mudel))
        

uusObjekt = Auto()
uusObjekt.lisaautomark("Ford")
uusObjekt.lisaaasta(1969)
uusObjekt.lisahind(50000)
uusObjekt.lisamudel("Mustang 69")
uusObjekt.lisaläbisõit("100000km")
uusObjekt.kuva()
