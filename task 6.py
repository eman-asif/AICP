# Constants
C_CEMENT = 'C'
G_GRAVEL = 'G'
S_SAND = 'S'
CEMENT_WEIGHT_MIN = 24.9
CEMENT_WEIGHT_MAX = 25.1
GRAVEL_SAND_WEIGHT_MIN = 49.9
GRAVEL_SAND_WEIGHT_MAX = 50.1
CEMENT_PRICE = 3
GRAVEL_SAND_PRICE = 2
SPECIAL_PACK_DISCOUNT_PRICE = 10

def check_single_sack(contents, weight):
    """
    Check the contents and weight of a single sack.
    """
    if contents not in [C_CEMENT, G_GRAVEL, S_SAND]:
        return "Rejected: Invalid contents"
    
    if contents == C_CEMENT and not (CEMENT_WEIGHT_MIN < weight < CEMENT_WEIGHT_MAX):
        return "Rejected: Invalid weight for cement"
    
    if contents in [G_GRAVEL, S_SAND] and not (GRAVEL_SAND_WEIGHT_MIN < weight < GRAVEL_SAND_WEIGHT_MAX):
        return "Rejected: Invalid weight for gravel or sand"

    return f"Accepted: Contents - {contents}, Weight - {weight} kg"

def check_customer_order(order):
    """
    Check a customer's order for delivery.
    """
    total_weight = 0
    rejected_sacks = 0

    for sack_type, sack_count in order.items():
        for _ in range(sack_count):
            contents = input(f"Enter contents for {sack_type} sack (C, G, or S): ").upper()
            weight = float(input(f"Enter weight for {sack_type} sack (in kilograms): "))

            result = check_single_sack(contents, weight)

            if result.startswith("Accepted"):
                total_weight += weight
            else:
                rejected_sacks += 1
                print(result)

    print(f"\nTotal Weight of the Order: {total_weight} kg")
    print(f"Number of Rejected Sacks: {rejected_sacks}")

    return total_weight

def calculate_order_price(total_weight, order):
    """
    Calculate the price for a customer's order.
    """
    regular_price = 0
    special_pack_count = min(order.get(C_CEMENT, 0), order.get(S_SAND, 0) // 2, order.get(G_GRAVEL, 0) // 2)

    # Calculate regular price
    for sack_type, sack_count in order.items():
        if sack_type == C_CEMENT:
            regular_price += sack_count * CEMENT_PRICE
        elif sack_type in [G_GRAVEL, S_SAND]:
            regular_price += sack_count * GRAVEL_SAND_PRICE

    # Calculate discount price if special packs are present
    discount_price = special_pack_count * SPECIAL_PACK_DISCOUNT_PRICE
    new_price = regular_price - discount_price

    print("\nOrder Summary:")
    print(f"Regular Price: ${regular_price}")
    if special_pack_count > 0:
        print(f"Discount Price (Special Packs): -${discount_price}")
        print(f"New Price: ${new_price}")
        print(f"Amount Saved: ${discount_price}")

def main():
    # Task 1 - Check the contents and weight of a single sack
    print("Task 1 - Check the contents and weight of a single sack")
    contents_input = input("Enter contents for a sack (C, G, or S): ").upper()
    weight_input = float(input("Enter weight for the sack (in kilograms): "))
    print(check_single_sack(contents_input, weight_input))

    # Task 2 - Check a customer's order for delivery
    print("\nTask 2 - Check a customer's order for delivery")
    order_input = {
        C_CEMENT: int(input("Enter number of cement sacks: ")),
        G_GRAVEL: int(input("Enter number of gravel sacks: ")),
        S_SAND: int(input("Enter number of sand sacks: "))
    }
    total_weight = check_customer_order(order_input)

    # Task 3 - Calculate the price for a customer's order
    print("\nTask 3 - Calculate the price for a customer's order")
    calculate_order_price(total_weight, order_input)
main()