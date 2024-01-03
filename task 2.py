class ElectricMountainRailway:
    def __init__(self):
        # Initialize data structures
        self.available_seats = {9: 80, 10: 160, 11: 240, 12: 320, 13: 400, 14: 480, 15: 560, 16: 640}
        self.total_passengers = {up: 0 for up in range(9, 16, 2)}
        self.total_money = {up: 0 for up in range(9, 16, 2)}

    def start_of_day_display(self):
        print("Start of the Day Display:")
        for up in range(9, 16, 2):
            print(f"Train {up}: {self.available_seats[up]} seats available")

    def purchase_tickets(self, passengers, departure_time):
        if departure_time not in self.available_seats:
            print("Invalid departure time.")
            return

        available_seats = self.available_seats[departure_time]

        if passengers <= 0 or passengers > available_seats:
            print("Invalid number of passengers.")
            return

        # Calculate total price
        total_price = passengers * 25
        group_discount = (passengers // 10) * 25
        total_price -= group_discount

        # Update data structures
        self.available_seats[departure_time] -= passengers
        self.total_passengers[departure_time] += passengers
        self.total_money[departure_time] += total_price

        print(f"{passengers} tickets purchased for Train {departure_time}. Total Price: ${total_price}")

    def end_of_day_display(self):
        print("\nEnd of the Day Display:")
        for up in range(9, 16, 2):
            if self.available_seats[up] == 0:
                print(f"Train {up}: Closed")
            else:
                print(f"Train {up}: {self.available_seats[up]} seats available")

        total_passengers_day = sum(self.total_passengers.values())
        total_money_day = sum(self.total_money.values())
        print(f"\nTotal Passengers for the Day: {total_passengers_day}")
        print(f"Total Money Taken for the Day: ${total_money_day}")

        most_passengers_train = max(self.total_passengers, key=self.total_passengers.get)
        print(f"\nTrain {most_passengers_train} had the most passengers today.")

# Task 1 - Start of the day
railway = ElectricMountainRailway()
railway.start_of_day_display()

# Task 2 - Purchasing tickets
railway.purchase_tickets(15, 9)
railway.purchase_tickets(25, 11)
railway.purchase_tickets(30, 13)

# Task 3 - End of the day
railway.end_of_day_display()
