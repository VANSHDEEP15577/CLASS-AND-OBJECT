class Cone:
    def __init__(self,r,s):
        self.r=r
        self.s=s
    def getArea(self):
        return 3.14*self.r*self.s
    def getPerameter(self):
        return 0.33*3.14*self.r*self.r*self.s

i=int(input("ENTER THE RADIUS:"))
j=int(input("ENTER THE SIDE:"))
p1=Cone(i,j)
print(p1.getArea())
print(p1.getPerameter())