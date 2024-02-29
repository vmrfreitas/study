# https://www.youtube.com/watch?v=wOI6P9-QRNQ


# made this right after she explained the problem
piggy_bank_list = [1,2,3]

def break_two(desired_amount):

    piggy_bank_dict = set(piggy_bank_list)
    for piggy_amount in piggy_bank_list:
        second_piggy_amount = desired_amount - piggy_amount
        if second_piggy_amount in piggy_bank_dict:
            return (piggy_amount, second_piggy_amount)


# got his bug of repeating the same piggy bank as well

piggy_bank_list = [1,2,3]

def break_two(desired_amount):

    piggy_bank_dict = set(piggy_bank_list)
    for piggy_amount in piggy_bank_list:
        second_piggy_amount = desired_amount - piggy_amount
        if second_piggy_amount in piggy_bank_dict and second_piggy_amount != piggy_amount:
            return (piggy_amount, second_piggy_amount)

# from her definition of the problem, returning only one pair is fine, I found a pair that works, not sure if the wanted solution is all possible pairs tho