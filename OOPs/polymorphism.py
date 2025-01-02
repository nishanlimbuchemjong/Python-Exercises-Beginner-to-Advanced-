# creating a class 'Calculate' with attributes length, breadth, and height
class Calculate:
    def calculation(self, length, breadth=None, height=None):
        if ((breadth is None) and (height is None)):
            return length**2
        elif (height is None):
            return length * breadth
        else:
            return length * breadth * height

# Create an object of the Calculate class
cal = Calculate()

# printing the result
print("\nExample of CompileTime Polymorphism (Method Overloading):")
print("Area of square:", cal.calculation(5))  
print("Area of rectangle:", cal.calculation(5, 10)) 
print("Volume of cuboid:", cal.calculation(5, 10, 15)) 
