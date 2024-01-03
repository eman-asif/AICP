# Constants
NUM_CHARITIES = 3

# Function to set up the donation system
def setup_donation_system():
    charities = []
    for i in range(NUM_CHARITIES):
        charity_name = input(f"Enter the name of Charity {i + 1}: ")
        charities.append(charity_name)
    
    return charities

# Function to record and total each donation
def record_and_total_donation(charities, totals):
    while True:
        print("\nCharities:")
        for i, charity in enumerate(charities):
            print(f"{i + 1}. {charity}")

        choice = input("Enter the number of the chosen charity (1, 2, or 3), or -1 to show totals: ")

        if choice == "-1":
            show_totals(charities, totals)
            break

        try:
            choice = int(choice)
            if 1 <= choice <= NUM_CHARITIES:
                bill_amount = float(input("Enter the customer's shopping bill amount: "))
                donation = bill_amount * 0.01
                totals[choice - 1] += donation
                print(f"Donation of ${donation:.2f} recorded for {charities[choice - 1]}")
            else:
                print("Invalid choice. Please enter 1, 2, 3, or -1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to show the totals so far
def show_totals(charities, totals):
    sorted_totals = sorted(zip(charities, totals), key=lambda x: x[1], reverse=True)
    
    print("\nTotals So Far:")
    for charity, total in sorted_totals:
        print(f"{charity}: ${total:.2f}")
    
    grand_total = sum(totals)
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

def main():
    # Task 1 - Set up the donation system
    print("Task 1 - Set up the donation system")
    charity_names = setup_donation_system()
    donation_totals = [0] * NUM_CHARITIES

    # Task 2 - Record and total each donation
    print("\nTask 2 - Record and total each donation")
    record_and_total_donation(charity_names, donation_totals)

    # Task 3 - Show the totals so far
    print("\nTask 3 - Show the totals so far")
    show_totals(charity_names, donation_totals)
main()