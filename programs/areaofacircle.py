# # calculating the area of a circle
#using a class

class circlearea:
    pi = 3.142
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):                         #method to calculate the area
        result = circlearea.pi * self.radius * self.radius
        return result


radius_input = int(input("enter the radius of the circle: "))

calculation1 = circlearea(radius_input)

print(calculation1.area())

#using a function

# def areaofcircle(radius):
#     pi = 3.142
#     result = 3.142 * radius * radius
#     return result

# radius_input = int(input("enter the radius of the circle: "))

# print(areaofcircle(radius_input))
   
    
    