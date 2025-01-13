# Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the conversion factor directly."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def get_temperature_input():
    """Prompt the user for temperature and unit, and return them."""
    temperature = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    return temperature, unit

def main():
    temperature, unit = get_temperature_input()

    try:
        temperature = float(temperature)

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        elif unit == 'C':
            # Remove the word Celsius from the conversion function call
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
