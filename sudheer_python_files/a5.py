class dog:
    def __init__(self,name):
        self.name=name

    def add_trick(self,trick):
        self.trick=trick
    
 

d=dog('figo')
e=dog('buddy')

d.add_trick('roll over')
e.add_trick('play dead')
print(d.name)
print(__str__(d.add_trick))

