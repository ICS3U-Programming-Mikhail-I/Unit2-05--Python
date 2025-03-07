#!/usr/bin/env python3
# Author: Mikhail Ibrahim
# Date: Mar 6, 2025
# Description: A Python program that calculates the area and perimeter of a circle based on user input for the radius.

import math


# Function to calculate area
def calculate_area(radius):
    """Function to calculate the area of a circle based on the given radius."""
    return math.pi * radius**2


# Function to calculate perimeter
def calculate_perimeter(radius):
    """Function to calculate the perimeter of a circle based on the given radius."""
    return 2 * math.pi * radius


def main():
    """Main function to get user input for radius and display the area and perimeter."""
    try:
        # Prompt the user to enter the radius of the circle
        radius = float(input("Enter the radius of the circle in centimeters: "))

        # Calculate the area and perimeter of the circle
        area = calculate_area(radius)
        perimeter = calculate_perimeter(radius)

        # Display the results with two decimal places
        print(f"\nArea of the circle: {area:.2f} cm²")
        print(f"Perimeter of the circle: {perimeter:.2f} cm")

    except ValueError:
        # Handle invalid input if the user does not enter a number
        print("Invalid input! Please enter a numeric value.")


# Check if this script is being run directly (not imported) and call the main function
if __name__ == "__main__":
    main()
