####################################################
#
# Keegan Gunkel
#
# Purpose to find volume and surface area of a sphere
#
####################################################
import math

#Method to find surface area
def surfaceArea(radius):
    surfaceArea = 4 * math.pi * radius**2
    return surfaceArea

# Method to find volume
def volume(radius):
    volume = 4/3 *math.pi * radius**3
    return volume

def main():
    print("----------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A SHPHERE")
    print("----------------------------------------------------------------")
    # User input
    radius = eval(input("Please enter the radius: "))
    # Equations I used
    surfaceArea = 4 * math.pi * radius**2
    volume = 4/3 *math.pi * radius**3
    # Prints answer
    print("The surface area of the sphere = ", surfaceArea)
    print("The volume of a sphere = ", volume)

if __name__ == '__main__':
    main()
