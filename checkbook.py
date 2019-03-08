# Python Project
# Command Line Checkbook Application

current_balance = 0.00

print(' ~~~ Welcome to your terminal checkbook! ~~~ ')

def user_options():
    print('\nWhat would you like to do? Please select an option')

    prompt = int(input('''\n1) view current balance\n'''+'''2) record a debit (withdrawl)\n'''+'''3) record a credit (deposit)\n'''+'''4) exit\n'''))
    print('Your choice: {}'.format(prompt))

    if prompt==1:
        print('Your current balance is $%.2f' % current_balance)
        user_options()
    elif prompt==2:
        user=debit_balance()
    elif prompt==3:
        user=credit_balance()
    elif prompt==4:
        print('\nThanks, have a great day!')
    else:
        print('Invalid choice: {}'.format(prompt))
        user_options()

def debit_balance():
    amount = float(input('How much is the debit: $'))
    global current_balance
    current_balance = current_balance - amount
    # print('\nYour current balance is $%.2f' % current_balance)
    user_options()

def credit_balance():
    amount = float(input('How much is the credit: $'))
    global current_balance
    current_balance = current_balance + amount
    # print('\nYour current balansce is $%.2f' % current_balance)
    user_options()

user_options()