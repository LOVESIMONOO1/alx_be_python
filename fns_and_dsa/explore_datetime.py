from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    # Prompt the user for the number of days
    days = int(input("Enter the number of days to add: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=days)
    # Format and print the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future Date:", formatted_future_date)

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
