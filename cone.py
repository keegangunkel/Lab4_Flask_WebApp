####################################################
#
# Keegan Gunkel
#
# Purpose to find volume and surface area of a cone
#
####################################################
import math

#Method to find surface area
def surfaceArea(radius, height):
    surfaceArea = math.pi * radius * (radius + math.sqrt (height**2 + radius**2))
    return surfaceArea

# Method to find volume

def volume(radius, height):
    volume = math.pi * radius**2 * height/3
    return volume

def main():
    print("-------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CONE")
    print("-------------------------------------------------------------")
    # User input
    radius= eval(input("Please enter the radius of a cone: "))
    height= eval(input("Please enter the height of a cone: "))
    print()
    # Eqautions to figure out problem
    surfaceArea = math.pi * radius * (radius + math.sqrt (height**2 + radius**2))
    volume = math.pi * radius**2 * height/3
    lateralSurfaceArea = math.pi * radius * math.sqrt (height**2 + radius**2)
    sideSlantLength = math.sqrt (radius**2 + height**2) 
    # Printing answers and rounding them
    print("Length of side (slant) of the cone = ", sideSlantLength)
    print("The surface Area of the cone = ", surfaceArea)
    print("The volume of the cone = ", volume)
    print("Lateral surface area of the cube = ", lateralSurfaceArea)

    if __name__ == '__main__':
        main()