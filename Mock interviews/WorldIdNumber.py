# Make a "system" that holds IDs for every person in the world. People can request a specific ID or a new random one.
# Assume only one ID per person and there are 7 billion people on earth.

import random

all_ids = set()


def valid_id(id):
    if id < 0:
        return False
    if id < 7000000000:
        return True
    return False
    

def is_available(id):
    if valid_id(id):
        if id not in all_ids:
            return True
    return False

def request_id(id):
    if is_available(id):
        all_ids.add(id)
        return True
    else:
        return False

def request_random_id():
    new_id = random.randint(0,7000000000)
    while(not request_id(new_id)):
        new_id = random.randint(0,7000000000)
    return new_id