# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.

# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.

# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

# 4) Adjust the logic to load the file content to work with pickled/ json data.

import pickle
import json

while True:
    user_choice = input('Pick 1 to add to a file, q to quit, rj to read json file, rb to read binary file: ')
    if user_choice == '1':
        user_input = [input('What is your input? ')]
        # with open ('assignment6.b', mode='wb') as f:
        #     f.write(pickle.dumps(user_input))
        with open ('assignment6.txt', mode='w') as f:
            f.write(json.dumps(user_input))
            f.write('\n')
    elif user_choice == 'rj':
        with open ('assignment6.txt', mode='r') as f:
            print(json.loads(f.readlines()[0]))
    elif user_choice == 'rb':
        with open ('assignment6.b', mode='rb') as f:
            print(pickle.loads(f.read()))
    elif user_choice == 'q':
        break

