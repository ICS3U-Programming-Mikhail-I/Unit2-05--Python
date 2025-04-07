# Copyright 2025 Mikhail Ibrahim
# Date: Mar 6, 2025
# Description: A Python program that calculates
# the area, perimeter, and circumference of a circle,
# based on user input for the radius.

import math

def main():
    # Prompt user for radius input
    radius = float(input("Enter the radius of the circle: "))

    # Calculate area, perimeter, and circumference using math.pi
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    circumference = 2 * math.pi * radius  # Circumference is same as perimeter

    # Display results rounded to 2 decimal places
    print(f"Area: {area:.2f} cm²")
    print(f"Perimeter: {perimeter:.2f} cm")
    print(f"Circumference: {circumference:.2f} cm")

# Call the main function
if __name__ == "__main__":
    main()
