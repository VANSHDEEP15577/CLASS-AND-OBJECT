class Cube:
    def __init__(self,s):
        self.s=s
    def getArea(self):
        return 6*self.s*self.s
    def getPerameter(self):
        return 12*self.s

i=int(input("ENTER THE SIDE:"))
p1=Cube(i)
print(p1.getArea())
print(p1.getPerameter())