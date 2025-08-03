# Check that datetime module is imported using 'from datetime'
from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    """Displays the current date and time in a formatted string."""
    # Save the current date and time
    current_date = datetime.now()

    # Format the current date and time as 'YYYY-MM-DD HH:MM:SS'
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print(f"Current date and time: {formatted_date}")
    return formatted_date

# Part 2: Calculate a future date
def calculate_future_date(days_to_add):
    """Calculates the future date by adding the specified number of days."""
    # Save the current date
    current_date = datetime.now().date()

    # Add the specified number of days to the current date using timedelta
    future_date = current_date + timedelta(days=days_to_add)

    # Format the future date as 'YYYY-MM-DD'
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")
    return formatted_future_date

# Main function to run the script
def main():
    """Main function to display current date and time, and calculate a future date."""
    # Check if display_current_datetime is implemented
    if not callable(display_current_datetime):
        raise NameError("display_current_datetime function is not defined or callable")

    # Check if calculate_future_date is implemented
    if not callable(calculate_future_date):
        raise NameError("calculate_future_date function is not defined or callable")
    
    # Display current date and time
    display_current_datetime()

    # Prompt user for number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Calculate and display the future date
    calculate_future_date(days_to_add)

# Run the main function
if __name__ == "__main__":
    main()