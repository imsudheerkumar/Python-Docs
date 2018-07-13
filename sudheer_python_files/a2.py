import time
class sphere():
    def __init__(self,radius):
        self.radius=radius
        return
    def area(self):
        return 4*3.14*self.radius
class prism():
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
        return
    def surface_area(self):
        return 2*(self.length*self.height)+2*(self.length*self.width)+2*(self.width*self.height)

    def volume(self):
        return self.length*self.width*self.height



class triangle():
    def __init__(self,breadth,height):
        self.breadth=breadth
        self.height=height
        return
    def area(self):
        return 0.5 *(self.breadth*self.height)

###SPHERE##
print("-------------SPHERE--------------")
x=int(input("enter radius of sphere :"))
obj1=sphere(x)
print("the area of sphere is : ",obj1.area())
time.sleep(2)

##PRISM####
print("-------------PRISM--------------")
y1=int(input("enter length of prism :"))
y2=int(input("enter width of prism :"))
y3=int(input("enter height of prism :"))
obj2=prism(y1,y2,y3)
print("the surface area of prism is : ",obj2.surface_area())
time.sleep(2)
##TRIANGLE##
print("-------------TRIANGLE--------------")
z2=int(input("enter breadth of triangle :"))
z3=int(input("enter height of triangle :"))
obj4=triangle(z2,z3)
print("The area of triangle is : ",obj4.area())



        
