import math
import datetime

def calculate_tire_volume(width, aspect_ratio, wheel_diameter):
    # Convert wheel diameter from inches to millimeters
    wheel_diameter_mm = wheel_diameter * 25.4
    
    # Calculate volume using the provided formula
    volume = (math.pi * width**2 * aspect_ratio * width * aspect_ratio + 2540 * wheel_diameter_mm) / 10000000000
    
    return volume

def append_to_file(current_date, width, aspect_ratio, wheel_diameter, volume):
    # Open the file in append mode
    with open("volumes.txt", "a") as file:
        # Append the values to the file
        file.write("{}, {:.2f}, {:.2f}, {:.2f}, {:.2f}\n".format(current_date, width, aspect_ratio, wheel_diameter, volume))

def main():
    # Input
    width = float(input("Enter the width of the tire in millimeters: "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
    wheel_diameter = float(input("Enter the diameter of the wheel in inches: "))
    
    # Calculate tire volume
    volume = calculate_tire_volume(width, aspect_ratio, wheel_diameter)
    
    # Get the current date
    current_date = datetime.date.today()
    
    # Append the values to the file
    append_to_file(current_date, width, aspect_ratio, wheel_diameter, volume)
    
    # Display result
    print("The volume of space inside the tire is approximately {:.2f} liters.".format(volume))

if __name__ == "__main__":
    main()
