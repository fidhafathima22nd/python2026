class Rectangle:
    def __init__(self, l, b):
        # Constructor to initialize rectangle dimensions
        self.__length = l
        self.__breadth = b

    def getDimensions(self):
        # Return the dimensions of the rectangle
        return self.__length, self.__breadth

    def getArea(self):
        # Calculate and return the area
        return self.__length * self.__breadth

    def __lt__(self, other):
        # Overload the '<' operator
        return self.getArea() < other.getArea()


# Get dimensions of the first rectangle
length1 = int(input("Enter the 1st rectangle length: "))
breadth1 = int(input("Enter the 1st rectangle breadth: "))

ar1 = Rectangle(length1, breadth1)

# Get dimensions of the second rectangle
length2 = int(input("Enter the 2nd rectangle length: "))
breadth2 = int(input("Enter the 2nd rectangle breadth: "))

ar2 = Rectangle(length2, breadth2)

# Display areas
print(f"Area of 1st rectangle = {ar1.getArea()}")
print(f"Area of 2nd rectangle = {ar2.getArea()}")

# Compare rectangle areas
if ar1 < ar2:
    print("1st rectangle is smaller")
elif ar2 < ar1:
    print("2nd rectangle is smaller")
else:
    print("Both rectangles have equal area")
