# Jeremy Lance
# Functions Problem 4

def compute_pay(code, hours):

    if code.upper() == "L":
        rate = 25
    elif code.upper() == "A":
        rate = 30
    elif code.upper() == "J":
        rate = 50
    else:
        rate = 0

    if hours > 40:
        overtime_hours = hours - 40
        gross = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross = hours * rate

    return rate, gross

def main():
    total_gross = 0
    response = input("Do you want to enter an employee? (Yes/No): ")

    while response.lower() == "yes":
        last_name = input("Enter employee last name: ")
        job_code = input("Enter job code (L, A, J): ")
        hours = float(input("Enter hours worked: "))
        rate, gross = compute_pay(job_code, hours)
        total_gross += gross

        print(f"\nEmployee: {last_name}")
        print(f"Hours Worked: {hours}")
        print(f"Pay Rate: ${rate:.2f}")
        print(f"Gross Pay: ${gross:,.2f}\n")

        response = input("Do you want to enter another employee? (Yes/No): ")

    print(f"\nTotal gross pay for all employees: ${total_gross:,.2f}")

main()
