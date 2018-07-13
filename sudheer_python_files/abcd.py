class parent:
    def __init__(self,a):
        self.a=a
        return

class child(parent):
    def __init__(self,a,b):
            parent __init__(self,a)
        self.b=b
        return
def access():
        print("a value:",self.a)
        print("b value",self.b)
        
c=child(10,20)
c.access()
