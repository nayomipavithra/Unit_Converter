# Simple Unit Converter (Length)

def show_menu():
    print("\n------ Unit Converter ------")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Centimeter to Meter")
    print("4. Meter to Centimeter")
    print("5. Exit")

def meter_to_km(m):
    return m / 1000

def km_to_meter(km):
    return km * 1000

def cm_to_meter(cm):
    return cm / 100

def meter_to_cm(m):
    return m * 100

while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        value = float(input("Enter meters: "))
        print("Kilometers:", meter_to_km(value))

    elif choice == "2":
        value = float(input("Enter kilometers: "))
        print("Meters:", km_to_meter(value))

    elif choice == "3":
        value = float(input("Enter centimeters: "))
        print("Meters:", cm_to_meter(value))

    elif choice == "4":
        value = float(input("Enter meters: "))
        print("Centimeters:", meter_to_cm(value))

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again!")
