class Rect:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def area(self):
        ar=self.l *self.b
        return ar

    def perimeter(self):
        p=2 * (self.l+self.b)
        return p

x1=int(input("enter length of 1st rectamgle:"))
y1=int(input("enterr breadth of 1st rectangle:"))
r1=Rect(x1,y1)
print("area of rectangle 1:",r1.area())
print("perimeter of rectangle 1:",r1.perimeter())

x2=int(input("n\nenter length of 2nd rectangle:"))
y2=int(input("enter breadth of 2nd recdtangle:"))
r2=Rect(x2,y2)
print("area of rectangle 2:",r2.area())
print("perimeter of rectangle 2:",r2.perimeter())

if r1.area()==r2.area():
    print("\nareas of both rectangles are equal.")
else:
    print("\nareas of both rectangles are not equal.")
    
