# Jeremy Lance
# Functions Problem 5

def compute_tuition(credit_hours, district_code):
    if district_code.upper() == "I":
        tuition = credit_hours * 250
    else:
        tuition = credit_hours * 550
    return tuition

def main():
    total_tuition = 0
    response = input("Do you want to enter a student? (Yes/No): ")

    while response.lower() == "yes":
        last_name = input("Enter student last name: ")
        credits = int(input("Enter credit hours: "))
        district = input("Enter district code (I or O): ")

        tuition = compute_tuition(credits, district)
        total_tuition += tuition

        print(f"\nStudent: {last_name}")
        print(f"Tuition Owed: ${tuition:,.2f}\n")

        response = input("Do you want to enter another student? (Yes/No): ")

    print(f"\nTotal tuition owed for all students: ${total_tuition:,.2f}")

main()
