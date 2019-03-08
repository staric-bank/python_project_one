# Python Project
# Command Line Checkbook Application

current_balance = 0.00



print(' ~~~ Welcome to your terminal checkbook! ~~~ ')

def user_options():
    print('\nWhat would you like to do? Please select an option')

    prompt = int(input('''\n1) view current balance\n'''+'''2) record a debit (withdrawl)\n'''+'''3) record a credit (deposit)\n'''+'''4) exit\n'''))
    print('Your choice: {}'.format(prompt))

    # if prompt==1:
    #     user=current_balance()
    # elif prompt==2:
    #     user=debit_balance()
    # elif prompt==3:
    #     user=credit_balance()
    # elif prompt==4:
    #     user=exit()
    # else:
    #     print('Invalid choice: {}'.format(prompt))
    #     user_options()


def debit_balance(amount):
    amount = float(input('How much is the debit: $'))
    current_balance -= amount
    print("Your new account balance is %.2f" % current_balance)
    user_options()

def credit_balance(amount):
    amount = float(input('How much is the credit: $'))
user_options()
# print('Thanks, have a great day!')