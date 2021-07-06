class Trapezoid:
    def __init__(self,h,b1,b2):
        self.h=h
        self.b1=b1
        self.b2=b2
    def getArea(self):
        return self.h*self.b1+self.b2/2
    def getPerameter(self):
        return self.h*self.b1+self.b2/2

i=int(input("ENTER THE HIGHT:"))
j=int(input("ENTER THE BASE NO. 1:"))
k=int(input("ENTER THE BASE NO. 2:"))
p1=Trapezoid(i,j,k)
print(p1.getArea())
print(p1.getPerameter())