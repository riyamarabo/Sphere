"""
Program: Sphere.py
Author: Riyam arabo
Last Date Modified: 9/5/2018

The purpose of this program is to compute the diameter, circumference, surface area, and the volume of a sphere by inputting the radius from a user and outputting the results.
"""

while True:
    try:
        radius = float(input("Please enter radius: "))
        if radius > 0:
            diameter = radius * 2
            circumference = radius * 3.14 * 2
            surfaceArea = 4 * 3.14 * (radius ** 2)
            volume = (4 / 3) * 3.14 * (radius ** 3)
            print("diameter: ", diameter, "\ncircumference: ", circumference, "\nsurface area: ", surfaceArea, "\nvolume: ", volume)
            break
        else:
            print("Please enter a positive number")
    except ValueError:
        print("This was not a valid number; please try again.")




