class Cylender:
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def getArea(self):
        return 2*3.14*self.r*self.h+2*3.14*self.r*self.r
    def getPerameter(self):
        return 2*3.14*self.r

i=int(input("ENTER THE RADIUS:"))
j=int(input("ENTER THE HIGHT:"))
p1=Cylender(i,j)
print(p1.getArea())
print(p1.getPerameter())