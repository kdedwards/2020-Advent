with open("Report_Repair.dat") as expenseData:
    expenseLines = expenseData.read().split('\n')

# Comprehension to convert all of the strings read in from the file to ints
expenses = [int(expenseLine) for expenseLine in expenseLines]

for expense in expenses:
    for secExpense in expenses[expenses.index(expense) + 1::]:
        if(expense + secExpense == 2020):
            print('Found it! Expense1: {} Expense2: {} Product {}'.format(expense, secExpense, expense * secExpense))

for expense in expenses:
    for secExpense in expenses[expenses.index(expense) + 1::]:
        for thirExpense in expenses[expenses.index(secExpense) + 1::]:
            if(expense + secExpense + thirExpense == 2020):
                print('Found it! Expense1: {} Expense2: {} Expense3: {} Product {}'.format(expense, secExpense, thirExpense, expense * secExpense * thirExpense))
