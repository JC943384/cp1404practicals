"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = get_income_input()
    months = get_all_month()

    for month in range(1, months + 1):
        income = get_imcome_input(month)
        upload_incomes(income, incomes)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total = calculate_total_income(income, total)
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


def calculate_total_income(income, total):
    total += income
    return total


def upload_incomes(income, incomes):
    incomes.append(income)


def get_income_input():
    return []


def get_imcome_input(month):
    return float(input(f"Enter income for month {month}:"))


def get_all_month():
    return int(input("How many months? "))


main()