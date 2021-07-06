class Sphere:
    def __init__(self,r):
        self.r=r
    def getArea(self):
        return 4*3.14*self.r*self.r
    def getPerameter(self):
        return 1.33*3.14*self.r*self.r*self.r

i=int(input("ENTER THE RADIUS:"))
p1=Sphere(i)
print(p1.getArea())
print(p1.getPerameter())