# Jeremy Lance
# Functions Problem 3

def compute_trip(miles, gallons):
    mpg = miles / gallons
    gas_cost = gallons * 3.00
    return mpg, gas_cost

def main():
    trip_count = 0
    total_miles = 0
    total_gas_cost = 0

    response = input("Do you want to enter a trip? (Yes/No): ")

    while response.lower() == "yes":
        city = input("Enter destination city: ")
        miles = float(input("Enter miles traveled: "))
        gallons = float(input("Enter gallons used: "))

        mpg, gas_cost = compute_trip(miles, gallons)

        trip_count += 1
        total_miles += miles
        total_gas_cost += gas_cost

        print(f"\nDestination: {city}")
        print(f"Miles: {miles:,.2f}")
        print(f"MPG: {mpg:.2f}")
        print(f"Gas Cost: ${gas_cost:,.2f}\n")

        response = input("Do you want to enter another trip? (Yes/No): ")

    print("\n----- Trip Summary -----")
    print(f"Number of trips: {trip_count}")
    print(f"Total miles traveled: {total_miles:,.2f}")
    print(f"Total gas cost: ${total_gas_cost:,.2f}")

main()
