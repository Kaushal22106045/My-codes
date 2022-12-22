Gross_income =int(input("Enter Gross income: "))
Num_dep =int(input("Enter number of dependents: "))
std_ded = 10000 #standard deduction
dep_ded = 3000 #dependent deduction

Taxable_income = Gross_income - std_ded - Num_dep*dep_ded
if (Taxable_income <=0):
    print("Congratulations you don't have to pay any tax!!")
else:
    print("Your tax to be paid is ", Taxable_income/5)