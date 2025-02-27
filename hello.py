from angle_methods import dms_to_decimal, decimal_to_dms, degrees_to_radians, radians_to_degrees

def main():
    while True:
        print("Angle Calculator")
        print("1. Subtract Angles")
        print("2. Add Angles")
        
        choice = input("Select an option (1 or 2) or 'exit' to quit: ")
        if choice.lower() == 'exit':
            break
        if choice == '1':
            # Logic for subtracting angles
            angle1 = float(input("Enter first angle in DMS (ddd.mmss): "))
            angle2 = float(input("Enter second angle in DMS (ddd.mmss): "))
            decimal_angle1 = dms_to_decimal(angle1)
            decimal_angle2 = dms_to_decimal(angle2)
            result = decimal_angle1 - decimal_angle2
            print(f"Result of subtraction: {result:.4f} degrees")
        elif choice == '2':
            # Logic for adding angles
            angle1 = float(input("Enter first angle in DMS (ddd.mmss): "))
            angle2 = float(input("Enter second angle in DMS (ddd.mmss): "))
            decimal_angle1 = dms_to_decimal(angle1)
            decimal_angle2 = dms_to_decimal(angle2)
            result = decimal_angle1 + decimal_angle2
            print(f"Result of addition: {result:.4f} degrees")
        else:
            print("Invalid choice. Please select 1, 2, or 'exit'.")

if __name__ == "__main__":
    main()
