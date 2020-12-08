with open("Report_Repair.dat") as expenseData:
    expenses = expenseData.read().split('\n')

for expense in expenses:
    for secExpense in expenses[expenses.index(expense)+1::]:
        if(int(expense)+int(secExpense)==2020):
            print('Found it! Expense1: {} Expense2: {} Product {}'.format(expense, secExpense, int(expense)*int(secExpense)))

for expense in expenses:
    for secExpense in expenses[expenses.index(expense)+1::]:
        for thirExpense in expenses[expenses.index(secExpense)+1::]:
            if(int(expense)+int(secExpense)+int(thirExpense)==2020):
                print('Found it! Expense1: {} Expense2: {} Expense3: {} Product {}'.format(expense, secExpense, thirExpense, int(expense)*int(secExpense)*int(thirExpense)))