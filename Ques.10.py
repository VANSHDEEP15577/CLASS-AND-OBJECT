class Triangle:
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
    def getArea(self):
        return self.b*self.h/2
    def getPerimeter(self):
        return self.l+self.b+self.h

i=int(input("ENTER THE LENGTH:"))
j=int(input("ENTER THE BREADTH:"))
k=int(input("ENTER THE HIGHT:"))
p1=Triangle(i,j,k)
print(p1.getArea())
print(p1.getPerimeter())