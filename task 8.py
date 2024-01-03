# Constants
NUM_BOATS = 10
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_TIME = 10
CLOSING_TIME = 17

# Boat class to store information for each boat
class Boat:
    def __init__(self, boat_number):
        self.boat_number = boat_number
        self.money_taken = 0
        self.total_hours_hired = 0
        self.currently_hired = False
        self.return_time = 0

    def hire_boat(self, hours):
        if not self.currently_hired:
            self.currently_hired = True
            self.return_time = OPENING_TIME + hours
            self.total_hours_hired += hours
            return True
        return False

    def return_boat(self):
        if self.currently_hired:
            self.currently_hired = False
            return True
        return False

# Function to calculate the money taken in a day for one boat
def calculate_money_for_one_boat(boat):
    print(f"\nBoat {boat.boat_number}:")
    while True:
        try:
            hire_hours = float(input("Enter the number of hours to hire the boat (0.5 or 1.0): "))
            if hire_hours not in [0.5, 1.0]:
                print("Invalid input. Please enter 0.5 or 1.0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if OPENING_TIME <= boat.return_time <= CLOSING_TIME:
        print("Boat already hired until", boat.return_time, "Please choose a different boat or try later.")
        return

    if boat.hire_boat(hire_hours):
        cost = hire_hours * HALF_HOUR_RATE if hire_hours == 0.5 else hire_hours * HOURLY_RATE
        boat.money_taken += cost
        print(f"Boat hired for {hire_hours} hours. Money taken: ${cost:.2f}")
    else:
        print("Boat not available at the moment. Please choose a different boat or try later.")

# Function to find the next boat available
def find_next_available_boat(boats):
    current_time = int(input("Enter the current time (in 24-hour format): "))
    available_boats = [boat for boat in boats if boat.return_time < current_time]
    
    if available_boats:
        print("Available boats:", [boat.boat_number for boat in available_boats])
    else:
        next_available_time = min(boats, key=lambda x: x.return_time).return_time
        print("No boats available. Next available time:", next_available_time)

# Function to calculate the money taken for all the boats at the end of the day
def calculate_money_for_all_boats(boats):
    total_money = sum(boat.money_taken for boat in boats)
    total_hours = sum(boat.total_hours_hired for boat in boats)
    unused_boats = [boat for boat in boats if not boat.currently_hired]
    most_used_boat = max(boats, key=lambda x: x.total_hours_hired)

    print("\nEnd of Day Report:")
    print(f"Total Money Taken: ${total_money:.2f}")
    print(f"Total Number of Hours Boats Were Hired: {total_hours} hours")
    print(f"Number of Boats Not Used Today: {len(unused_boats)}")
    print(f"Boat {most_used_boat.boat_number} was used the most with {most_used_boat.total_hours_hired} hours.")

if __name__ == "__main__":
    # Task 1 - Calculate the money taken in a day for one boat
    print("Task 1 - Calculate the money taken in a day for one boat")
    boats = [Boat(i + 1) for i in range(NUM_BOATS)]
    calculate_money_for_one_boat(boats[0])

    # Task 2 - Find the next boat available
    print("\nTask 2 - Find the next boat available")
    find_next_available_boat(boats)

    # Task 3 - Calculate the money taken for all the boats at the end of the day
    print("\nTask 3 - Calculate the money taken for all the boats at the end of the day")
    for boat in boats[1:]:
        calculate_money_for_one_boat(boat)

    calculate_money_for_all_boats(boats)
