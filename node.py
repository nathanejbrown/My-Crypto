class Node:
    def __init__(self):
        self.blockchain = []

    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient\'s name: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount


    def get_user_choice(self):
        user_input = input('Your choice: ')
        return user_input

    def print_blockchain_elements(self):
        for block in self.blockchain:
            print('Outputting block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True

        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                if add_transaction(recipient, amount=amount):
                    print('Added transaction')
                else:
                    print('Transaction failed')
                print(open_transactions)
            elif user_choice == '2':
                if mine_block():
                    open_transactions = []
                    save_data()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                verifier = Verification(open_transactions, get_balance)
                if verifier.verify_transactions():
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else:
                print('Invalid choice')
            verifier = Verification()
            if not verifier.verify_chain(blockchain):
                self.print_blockchain_elements()
                print('Invalid blockchain')
                break
            print(blockchain)
            print('Balance of {}: {:6.2f}'.format('Nathan', get_balance('Nathan')))
        else:
            print('User left!')

        print('Done')