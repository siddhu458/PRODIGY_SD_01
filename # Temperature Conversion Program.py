# Temperature Conversion Program

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def main():
    try:
        temperature = float(input("Enter the temperature value: "))
        original_unit = input("Enter the original unit (Celsius, Fahrenheit, or Kelvin): ").lower()

        if original_unit == "celsius":
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
        elif original_unit == "fahrenheit":
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
        elif original_unit == "kelvin":
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
        else:
            print("Invalid input. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")
            return

        print(f"{temperature} {original_unit.capitalize()} is equivalent to:")
        print(f"{fahrenheit:.2f} Fahrenheit")
        print(f"{kelvin:.2f} Kelvin")

    except ValueError:
        print("Invalid input. Please enter a valid numeric temperature value.")

if __name__ == "__main__":
    main()
