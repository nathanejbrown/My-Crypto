# Initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """

    Arguments: 
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction(default [1]).
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)


add_value(get_transaction_value())

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        break
    else: 
        print('Invalid choice')

print('Done')
