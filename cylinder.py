####################################################
#
# Keegan Gunkel
#
# Purpose to find volume and surface area of a cylinder
#
####################################################
import math

def surfaceArea(radius, height):
    surfaceArea = 2 * math.pi * radius * height + 2* math.pi * radius**2
    return surfaceArea

def volume(rad, hi):
    volume = math.pi * rad * rad * hi
    return volume


def main():
    print("-----------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF A CYLINDER")
    print("-----------------------------------------------------------------")
    # User input
    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))
    # Eqautions I used
    surfaceArea = 2 * math.pi * radius * height + 2* math.pi * radius**2
    volume = math.pi * radius**2 * height
    lateralSurfaceArea = 2 * math.pi * radius * height
    topOrBottomArea = math.pi * radius**2
    # Printing answers
    print("The surface area of the cylinder = ", surfaceArea)
    print("The volume of the cylinder =", volume)
    print("Lateral surface are of the cylinder = ", lateralSurfaceArea)
    print("Top OR bottom surface area of the cylinder = ", topOrBottomArea)
    print("-------------------------------------------------------------------")

    if __name__ == '__main__':
        main()
