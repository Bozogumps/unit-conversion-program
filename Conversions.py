# PROG 1003 - Fall 2026
# HW3 - Conversions
# By Alex Daniels

def volume_to_gallons(value, unit):
    if unit == 11:
        return value / 128
    elif unit == 12:
        return value
    elif unit == 13:
        return value / 3.78541
    elif unit == 14:
        return value * 31.5
    elif unit == 15:
        return value * 7.48052
    elif unit == 16:
        return value / 768
    elif unit == 17:
        return value * 252

def length_to_inches(value, unit):
    if unit == 21:
        return value
    elif unit == 22:
        return value * 12
    elif unit == 23: 
        return value / 0.0254
    elif unit == 24:
        return value / 0.0254 * 1000
    elif unit == 25:
        return value * 4
    elif unit == 26:
        return value * 7920
    elif unit == 27:
        return value * 198

def gallons_to_ounces(gallons):
    return gallons * 128

def gallons_to_liters(gallons):
    return gallons * 3.78541

def gallons_to_barrels(gallons):
    return gallons / 31.5

def gallons_to_cubic_feet(gallons):
    return gallons / 7.48052

def gallons_to_teaspoons(gallons):
    return gallons * 768

def gallons_to_tuns(gallons):
    return gallons / 252

def inches_to_feet(inches):
    return inches / 12

def inches_to_meters(inches):
    return inches * 0.0254 

def inches_to_kilometers(inches):
    return inches * 0.0254 / 1000

def inches_to_hands(inches):
    return inches / 4

def inches_to_furlongs(inches):
    return inches / 7920

def inches_to_rods(inches):
    return inches / 198

print("HW3 - Conversions")
print("Solution by Alex Daniels")
print()

while True:
    print("What are the units of the initial value?")
    print()
    print("Volume Measures\t\tLength Measures")
    print("11 - US Ounces\t\t21 - Inches")
    print("12 - US Gallons\t\t22 - US Feet")
    print("13 - Liters\t\t23 - Meters")
    print("14 - Fluid Barrels\t24 - Kilometers")
    print("15 - Cubic Feet\t\t25 - Hands")
    print("16 - Teaspoons\t\t26 - Furlongs")
    print("17 - Tuns\t\t\t27 - Rods")

    while True:
        try:
            choice = int(input("Choose a set of units by its number: "))

            if 11 <= choice <= 17 or 21 <= choice <= 27:
                break
            print("Invalid choice. Please enter a number from 11-17 or 21-27.")

        except ValueError:
            print("Invalid choice. Please enter a number from 11-17 or 21-27.")

    while True:
        try:
            value = float(input("How many units to convert? (positive, non-zero): "))

            if 0 < value < 1000:
                break
            print("Invalid value. Please enter a number greater than 0 and less than 1000.")

        except ValueError:
            print("Invalid value. Please enter a number greater than 0 and less than 1000.")

    if 11 <= choice <= 17:
        gallons = volume_to_gallons(value, choice)

        ounces = gallons_to_ounces(gallons)
        liters = gallons_to_liters(gallons)
        barrels = gallons_to_barrels(gallons)
        cubic_feet = gallons_to_cubic_feet(gallons)
        teaspoons = gallons_to_teaspoons(gallons)
        tuns = gallons_to_tuns(gallons)

        if choice == 11:
            print(f"{value:,.4f} US Ounces is equivalent to:")
        elif choice == 12:
            print(f"{value:,.4f} US Gallons is equivalent to:")
        elif choice == 13:
            print(f"{value:,.4f} Liters is equivalent to:")
        elif choice == 14:
            print(f"{value:,.4f} Fluid Barrels is equivalent to:")
        elif choice == 15:
            print(f"{value:,.4f} Cubic Feet is equivalent to:")
        elif choice == 16:
            print(f"{value:,.4f} Teaspoons is equivalent to:")
        elif choice == 17:
            print(f"{value:,.4f} Tuns is equivalent to:")

        if choice != 11:
            print(f"{ounces:,.4f} US Ounces")

        if choice != 12:
            print(f"{gallons:,.4f} US Gallons")

        if choice != 13:
            print(f"{liters:,.4f} Liters")

        if choice != 14:
            print(f"{barrels:,.4f} Fluid Barrels")

        if choice != 15:
            print(f"{cubic_feet:,.4f} Cubic Feet")

        if choice != 16:
            print(f"{teaspoons:,.4f} Teaspoons")

        if choice != 17:
            print(f"{tuns:,.4f} Tuns")

    else:
        inches = length_to_inches(value, choice)

        feet = inches_to_feet(inches)
        meters = inches_to_meters(inches)
        kilometers = inches_to_kilometers(inches)
        hands = inches_to_hands(inches)
        furlongs = inches_to_furlongs(inches)
        rods = inches_to_rods(inches)

        if choice == 21:
            print(f"{value:,.4f} Inches is equivalent to:")
        elif choice == 22:
            print(f"{value:,.4f} US Feet is equivalent to:")
        elif choice == 23:
            print(f"{value:,.4f} Meters is equivalent to:")
        elif choice == 24:
            print(f"{value:,.4f} Kilometers is equivalent to:")
        elif choice == 25:
            print(f"{value:,.4f} Hands is equivalent to:")
        elif choice == 26:
            print(f"{value:,.4f} Furlongs is equivalent to:")
        elif choice == 27:
            print(f"{value:,.4f} Rods is equivalent to:")

        if choice != 21:
            print(f"{inches:,.4f} Inches")

        if choice != 22:
            print(f"{feet:,.4f} US Feet")

        if choice != 23:
            print(f"{meters:,.4f} Meters")

        if choice != 24:
            print(f"{kilometers:,.4f} Kilometers")

        if choice != 25:
            print(f"{hands:,.4f} Hands")

        if choice != 26:
            print(f"{furlongs:,.4f} Furlongs")

        if choice != 27:
            print(f"{rods:,.4f} Rods")

    print()

    again = input("Do another conversion? (Y/N): ").strip().upper()

    while again != "Y" and again != "N":
        print("Invalid choice. Please enter Y or N.")
        again = input("Do another conversion? (Y/N): ").strip().upper()

    if again == "N":
        break

print("HW3 Complete")
















