# * unpacks the items in a list into a tuple. ** unpacks items and turns them into a dictionary

def unlimited_arguments(*args, **keyword_args):
    print(keyword_args)
    for argument in keyword_args:
        print(argument)

unlimited_arguments(1,2,3,4, name='Nathan', age=26)