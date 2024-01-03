
# Constants
BASIC_COMPONENTS_PRICE = 200.00
DISCOUNT_PERCENT_1_ITEM = 5
DISCOUNT_PERCENT_2_OR_MORE_ITEMS = 10

# Arrays to store item information
item_codes = ['A1', 'A2', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'E1', 'E2', 'E3', 'F1', 'F2', 'G1', 'G2']
descriptions = ['Compact Case', 'Tower Case', '8 GB RAM', '16 GB RAM', '32 GB RAM', '1 TB HDD', '2 TB HDD', '4 TB HDD',
                '240 GB SSD', '480 GB SSD', '1 TB HDD', '2 TB HDD', '4 TB HDD', 'DVD/Blu-Ray Player', 'DVD/Blu-Ray Re-writer',
                'Standard OS', 'Professional OS']
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Function to display items and get user choice
def get_user_choice(category):
    print(f"\n{category} Items:")
    for i in range(len(item_codes)):
        if item_codes[i].startswith(category):
            print(f"{item_codes[i]} - {descriptions[i]} - ${prices[i]}")
    choice = input(f"Select {category} item code: ").upper()
    while choice not in item_codes or not choice.startswith(category):
        print("Invalid item code. Please try again.")
        choice = input(f"Select {category} item code: ").upper()
    return choice

# Function to calculate and display the total price
def calculate_and_display_price(chosen_items):
    total_price = BASIC_COMPONENTS_PRICE
    for item in chosen_items:
        index = item_codes.index(item)
        total_price += prices[index]
    
    print("\nChosen Items:")
    for item in chosen_items:
        index = item_codes.index(item)
        print(f"{item} - {descriptions[index]} - ${prices[index]}")
    
    print(f"\nTotal Price: ${total_price:.2f}")
    return total_price

# Task 1 - Setting up the system and ordering main items
print("Task 1 - Setting up the system and ordering main items")
case_choice = get_user_choice('A')
ram_choice = get_user_choice('B')
hdd_choice = get_user_choice('C')

main_items = [case_choice, ram_choice, hdd_choice]
total_price = calculate_and_display_price(main_items)

# Task 2 - Ordering additional items
print("\nTask 2 - Ordering additional items")
additional_items = []
add_more = input("Do you want to purchase additional items? (Y/N): ").upper()
while add_more == 'Y':
    category_choice = input("Enter the category code (D, E, F, or G): ").upper()
    additional_choice = get_user_choice(category_choice)
    additional_items.append(additional_choice)
    add_more = input("Do you want to add more items? (Y/N): ").upper()

total_price = calculate_and_display_price(main_items + additional_items)

# Task 3 - Offering discounts
print("\nTask 3 - Offering discounts")
if len(additional_items) == 1:
    discount_amount = total_price * (DISCOUNT_PERCENT_1_ITEM / 100)
    total_price -= discount_amount
    print(f"\nYou saved ${discount_amount:.2f} with a {DISCOUNT_PERCENT_1_ITEM}% discount!")
elif len(additional_items) >= 2:
    discount_amount = total_price * (DISCOUNT_PERCENT_2_OR_MORE_ITEMS / 100)
    total_price -= discount_amount
    print(f"\nYou saved ${discount_amount:.2f} with a {DISCOUNT_PERCENT_2_OR_MORE_ITEMS}% discount!")

print(f"\nNew Total Price after Discount: ${total_price:.2f}")
