# SALARY CALCULATOR
def Gross_Salary():
    Basic_salary= int(input("ENTER BASIC SALARY: "))
    Hra = int(input("ENTER HRA: "))
    Allowance= int(input("ENTER ALLOWANCE: "))
    gross_salary = Basic_salary + Hra + Allowance
    return gross_salary

def net_profit():
    gross = Gross_Salary()

    deduction = int(input("Enter deduction: "))

    net = gross - deduction

    print("Net Salary:", net)


net_profit()

    