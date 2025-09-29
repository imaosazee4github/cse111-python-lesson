import math
from datetime import date

# Get the current date
current_date = date.today()

# Prompt the user for tire information
width_of_tire = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_of_wheel = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume using the formula
volume = (math.pi * width_of_tire**2 * aspect_ratio * (width_of_tire * aspect_ratio + 2540 * diameter_of_wheel)) / 10000000000

# Display the result
print(f"Current date: {current_date}")
print(f"Width of the tire: {width_of_tire}")
print(f"Aspect ratio of the tire: {aspect_ratio}")
print(f"Diameter of the wheel: {diameter_of_wheel}")
print(f"The approximate volume is {volume:.2f} liters")

# Dictionary of example prices for specific tire sizes

tire_prices = {
    (185, 50, 14): 85000,
    (205, 60, 15): 95000,
    (225, 55, 17): 120000,
    (245, 45, 18): 150000,
}

# Check if entered tire size matches one in the dictionary
tire_key = (width_of_tire, aspect_ratio, diameter_of_wheel)
price = tire_prices.get(tire_key)

if price:
    print(f"Tires with size {width_of_tire}/{aspect_ratio}R{diameter_of_wheel} cost ₦{price:,}")
else:
    print("Sorry, no price available for this tire size.")

# Ask if user wants to buy tires
phone_number = ""
buy_choice = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy_choice == "yes":
    phone_number = input("Please enter your phone number: ").strip()

# Append the results to a text file
with open("volumes.txt", "a") as file:
    file.write(f"{current_date}, {width_of_tire}, {aspect_ratio}, {diameter_of_wheel}, {volume:.2f}")
    if phone_number:
        file.write(f", {phone_number}")
    file.write("\n")