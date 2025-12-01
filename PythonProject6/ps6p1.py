# Jeremy Lance
# Functions Problem 1

def compute_total(qty, price):
    total = qty * price
    if total > 10000:
        total *= 0.90
    return total

def main():
    extended_sum = 0
    response = input("Do you want to enter an item? (Yes/No): ")

    while response.lower() == "yes":
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        total = compute_total(qty, price)

        print(f"\nQuantity: {qty}")
        print(f"Price: ${price:,.2f}")
        print(f"Total: ${total:,.2f}\n")

        extended_sum += total

        response = input("Do you want to enter another item? (Yes/No): ")

    print(f"\nExtended price sum of all totals: ${extended_sum:,.2f}")

main()
