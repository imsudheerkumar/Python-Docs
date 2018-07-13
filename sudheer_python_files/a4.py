class customer():
    def __init__(self,name,number,network):
        self.name=name
        self.number=number
        self.network=network
        return
    def name(self):
        print("the name is ",self.name)
    def number(self):
        return self.number
    def network(self):
        return self.network

c=customer("sudheer","82032165","airtel")

c.name()


