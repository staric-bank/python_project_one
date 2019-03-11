# Python Project
# Command Line Checkbook Application

with open('checkbook_register.txt') as f:
    statement_balance = f.readlines()
    pass

current_balance = float(statement_balance[-1].replace('+','').replace('-',''))

print(' ~~~ Welcome to your terminal checkbook! ~~~ ')

def user_options():
    print('\n**************************************************')
    print('\nWhat would you like to do? Please select an option')

    prompts = {
    1: realtime_balance,
    2: debit_balance,
    3: credit_balance,
    4: exit
    }

    while(True):
        try:
            prompt = int(input('''\n1) View Current Balance\n'''+'''2) Record a Debit (Withdrawl)\n'''+'''3) Record a Credit (Deposit)\n'''+'''4) Exit\n'''))
            print('Your choice: {}'.format(prompt))
        except ValueError:
            print('Invalid choice, Please enter another option')
            continue

        if  prompt in prompts:
            prompts[prompt]()

def realtime_balance():
    global current_balance
    print('Your current balance is $%.2f' % current_balance)
    user_options()

def debit_balance():
    while(True):
        try:
            amount = float(input('How much is the debit: $').replace('$',''))
            break
        except ValueError:
            print('Please enter an exact amount')
            continue

    global current_balance
    current_balance = current_balance - amount
    updated_balance()
    user_options()

def credit_balance():
    while(True):
        try:
            amount = float(input('How much is the credit: $'))
            break
        except ValueError:
            print('Please enter an exact amount')
            continue 

    global current_balance
    current_balance = current_balance + amount
    updated_balance()
    user_options()  

def updated_balance():
    with open('checkbook_register.txt', 'a+') as f:
        f.write('+'+ str(current_balance) + '\n')

user_options()