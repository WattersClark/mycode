"""UK Conversion Tool for your Average American"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def pound_to_dollar(pound):
    dollar = pound * 1.25
    return dollar

def cm_to_inches(cm):
    inches = cm * 0.393701
    return inches

def main():
    option = 0
    print("Oy Bruv, make your choice: ")
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Pound Sterling to USD")
        print("3. Cm to Inches")
        print("4. Exit the conversion")
        option = int(input("> (1/2/3/4): "))

        if option == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius} Celsius is equal to {fahrenheit} Fahrenheit.\n")
        elif option == 2:
            pound = float(input("Enter amount in Pound Sterling: "))
            dollar = pound_to_dollar(pound)
            print(f"\n{pound} Pound Sterling is equal to {dollar} USD.\n")
        elif option == 3:
            cm = float(input("Enter length in cm: "))
            inches = cm_to_inches(cm)
            print(f"\n{cm} cm is equal to {inches} inches.\n")
        elif option == 4:
            break
        else:
            print("That is not a choice.")
    print("Cheers")

if __name__ == '__main__':
    main()

