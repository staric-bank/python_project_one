# Python Project
# Command Line Checkbook Application
with open('checkbook_register.txt') as f:
    file_contents = f.read()
current_balance = 0.00


print(' ~~~ Welcome to your terminal checkbook! ~~~ ')

def user_options():
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
            print('Invalid choice')
            continue

        if  prompt in prompts:
            prompts[prompt]()
        else:
            print('Invalid choice: {}'.format(prompt))

def realtime_balance():
    global current_balance
    print('Your current balance is ${}'.format(current_balance))

def debit_balance():
    amount = float(input('How much is the debit: $'))
    global current_balance
    current_balance = current_balance - amount
    updated_balance()
    user_options()

def credit_balance():
    amount = float(input('How much is the credit: $'))
    global current_balance
    current_balance = current_balance + amount
    updated_balance()
    user_options()  

def updated_balance():
    with open('checkbook_register.txt', 'a+') as f:
        f.write('+'+ str(current_balance) + '\n')


user_options()

