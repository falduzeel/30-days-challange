def convert_temp():
    print("--- Simple Temperature Converter ---")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Kelvin or Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
    else:
        print("Invalid choice! Please select 1 or 2.")

convert_temp()