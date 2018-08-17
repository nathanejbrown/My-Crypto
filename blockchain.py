# Initializing our blockchain list
genesis_block = {
        'previous_hash': '', 
        'index': 0, 
        'transactions': []
        }
blockchain = [genesis_block]
open_transactions = []
owner = 'Nathan'

def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):

    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block = {
        'previous_hash': 'xyz', 
        'index': len(blockchain), 
        'transactions': open_transactions
        }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Enter the recipient\'s name: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)

def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else: 
            is_valid = False
            break
    return is_valid

while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        print('Invalid choice')
    if not verify_chain():
        print('Invalid blockchain')
        break

print('Done')
