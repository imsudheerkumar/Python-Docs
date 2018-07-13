class student:
    raise_ammount=25
    def __init__(self,name,age):
        self.name=name
        self.age=age
        return
    def fullname(self):
        print("the full name is :",self.name)
        return
    def age(self):
        print("the age of the person is :",+str(self.age))
        return

c=student('sudheer',22)
print(c.fullname())
print(c.raise_ammount())
