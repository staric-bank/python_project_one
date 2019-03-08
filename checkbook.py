# Python Project
# Command Line Checkbook Application

checkbook_register = open('checkbook_register.txt','r')

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
            print('Invalid choice, Please enter another option')
            continue

        if  prompt in prompts:
            prompts[prompt]()
        else:
            print('Invalid choice: {}'.format(prompt))

def realtime_balance():
    global current_balance
    print('Your current balance is ${}'.format(current_balance))
    user_options()

def debit_balance():
    amount = float(input('How much is the debit: $').replace('$',''))
    global current_balance
    current_balance = current_balance - amount
    user_options()

def credit_balance():
    amount = float(input('How much is the credit: $'))
    global current_balance
    current_balance = current_balance + amount
    user_options()  

user_options()