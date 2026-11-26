class Time:
    def __init__(self):
        # Constructor to initialize time details
        self.__hours = int(input("Enter the hours (0-23): "))
        self.__minutes = int(input("Enter the minutes: "))
        self.__seconds = int(input("Enter the seconds: "))

    def __add__(self, other):
        # Overload '+' operator to add two Time objects

        # Calculate total seconds
        total_seconds = (
            (self.__hours + other.__hours) * 3600
            + (self.__minutes + other.__minutes) * 60
            + self.__seconds + other.__seconds
        )

        # Calculate hours, minutes and seconds
        hours = (total_seconds // 3600) % 24
        minutes = (total_seconds // 60) % 60
        seconds = total_seconds % 60

        # Return result in 24-hour format
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# Enter details for Time 1
print("Enter details for Time 1:")
t1 = Time()

# Enter details for Time 2
print("\nEnter details for Time 2:")
t2 = Time()

# Add two Time objects
result = t1 + t2

# Display the result
print("Sum of the two times:", result)
