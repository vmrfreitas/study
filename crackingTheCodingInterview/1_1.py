
input_string = "Maria"

def is_unique():
    set_string = set(input_string) # a set does not allow repeated elements
    if len(set_string) == len(input_string):
        print(input_string + " is a unique string")
    else:
        print(input_string + " is not a unique string")

is_unique()