def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def invalid_input():
    print("Invalid input! Please choose a valid option.")

def quit_program():
    print("Exiting the temperature converter. Goodbye!")
    quit()

options = {
    '1': lambda temperature: print(f"{temperature}°C is equal to {celsius_to_fahrenheit(temperature)}°F"),
    '2': lambda temperature: print(f"{temperature}°C is equal to {celsius_to_kelvin(temperature)} K"),
    '3': lambda temperature: print(f"{temperature}°F is equal to {fahrenheit_to_celsius(temperature)}°C"),
    '4': lambda temperature: print(f"{temperature}°F is equal to {fahrenheit_to_kelvin(temperature)} K"),
    '5': lambda temperature: print(f"{temperature} K is equal to {kelvin_to_celsius(temperature)}°C"),
    '6': lambda temperature: print(f"{temperature} K is equal to {kelvin_to_fahrenheit(temperature)}°F"),
    '7': quit_program
}

while True:
    print("\nChoose an option:")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Celsius to Kelvin")
    print("3. Convert Fahrenheit to Celsius")
    print("4. Convert Fahrenheit to Kelvin")
    print("5. Convert Kelvin to Celsius")
    print("6. Convert Kelvin to Fahrenheit")
    print("7. Quit")
    
    choice = input("\nEnter your choice (1/2/3/4/5/6/7): ")

    selected_option = options.get(choice, invalid_input)
    
    try:
        if choice == '7':
            selected_option()
        else:
            temperature = float(input("Enter temperature value: "))
            selected_option(temperature)
    except ValueError:
        print("Invalid input! Please enter a valid temperature value.")
