class A:
    def guru(self,model,year):
        self.model=model
        self.year=year
        print("2016 galaxy")
        print(self.model,self.year)
        return
    def guru_latest(self,newmodel,year):
        self.newmodel=newmodel
        self.year=year
        print("launced in 1995")
        print(self.newmodel,self.year)
        return
class B(A):
    def galaxy(self,modelname,year):
        self.modelname=modelname
        self.year=year
        print("2017 galaxy")
        print(self.modelname,self.year)
        return
    def guru_latest2(self,newmodel,year):
        self.newmodel=newmodel
        self.year=year
        print("launched in 1997")
        print(self.newmodel,self.year)
        return
class C(B):
    def galaxy1(self,modelname,year):
        self.modelname=modelname
        self.year=year
        print("2018 new galaxy")
        print(self.modelname,self.year)
        return
    def guru_latest1(self,newmodel,year):
        self.newmodel=newmodel
        self.year=year
        print("launched in 1998")
        print(self.newmodel,self.year)
        return

c=C()
c.galaxy("j7-->2018 EDITION",2018)
