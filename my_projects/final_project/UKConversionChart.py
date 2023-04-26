"""UK Conversion Tool for your Average American"""

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def pounds_to_USD(pounds):
    USD = pounds * 1.25
    return USD

def cm_to_inches(cm):
    inches = cm * 0.393701
    return inches

def kgs_to_lbs(kgs):
    lbs = kgs * 2.2
    return lbs

def liters_to_gallons(liters):
    gallons = liters * 0.264172
    return gallons

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

def USD_to_pounds(USD):
    pounds = USD / 1.25
    return pounds

def inches_to_cm(inches):
    cm = inches / 0.393701
    return cm

def lbs_to_kgs(lbs):
    kgs = lbs / 2.2
    return kgs

def gallons_to_liters(gallons):
    liters = gallons / 0.264172
    return liters

def main():
    option = 0
    print("\nOi Bruv, make your bleedin choice, innit?: \n")
    while True:
        print("1. Celsius to Fahrenheit")
        print("2. Pound Sterling to USD")
        print("3. Cm to Inches")
        print("4. Kgs to lbs")
        print("5. Liters to Gallons")
        print("6. Fahrenheit to Celsius")
        print("7. USD to Pound Sterling")
        print("8. Inches to Cm")
        print("9. lbs to Kgs")
        print("10. Gallons to Liters")
        print("11. Exit the conversion")
        option = int(input("> (1/2/3/4/5/6/7/8/9/10/11): "))

        if option == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"\n{celsius} Celsius is equal to {fahrenheit} Fahrenheit.\n")
        elif option == 2:
            pounds = float(input("Enter amount in Pound Sterling: "))
            USD = pounds_to_USD(pounds)
            print(f"\n{pounds} Pound Sterling is equal to {USD} USD.\n")
        elif option == 3:
            cm = float(input("Enter length in cm: "))
            inches = cm_to_inches(cm)
            print(f"\n{cm} cm is equal to {inches} inches.\n")
        elif option == 4:
            kgs = float(input("Enter weight in kgs: "))
            lbs = kgs_to_lbs(kgs)
            print(f"\n{kgs} kgs is equal to {lbs} lbs.\n")
        elif option == 5:
            liters = float(input("Enter volume in liters: "))
            gallons = liters_to_gallons(liters)
            print(f"\n{liters} liters is equal to {gallons} gallons.\n")
        elif option == 6:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"\n{fahrenheit} Fahrenheit is equal to {celsius} Celsius.\n")
        elif option == 7:
            USD = float(input("Enter amount in USD: "))
            pounds = USD_to_pounds(USD)
            print(f"\n{USD} USD is equal to {pounds} pounds.\n")
        elif option == 8:
            inches = float(input("Enter length in inches: "))
            cm = inches_to_cm(inches)
            print(f"\n{inches} inches is equal to {cm} cm.\n")
        elif option == 9:
            lbs = float(input("Enter weight in lbs: "))
            kgs = lbs_to_kgs(lbs)
            print(f"\n{lbs} lbs is equal to {kgs} kgs.\n")
        elif option == 10:
            gallons = float(input("Enter volume in gallons: "))
            liters = gallons_to_liters(gallons)
            print(f"\n{gallons} gallons is equal to {liters} liters.\n")
        elif option == 11:
            break
        else:
            print("\nAin't a choice, mate. Try again.\n")
    print("\nCheers Guvna\n")

if __name__ == '__main__':
    main()
