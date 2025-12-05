# https://leetcode.com/explore/interview/card/amazon/84/recursion/521/
# its kinda sad how long I got stuck on this one.
# I tried recursively from the start but the return values were hard to manage.
# Now I gotta do some more backtracking practice lol

def letterCombinations(digits: str):
    letters = [[],['a','b','c'],['d', 'e', 'f'],['g', 'h', 'i'],['j', 'k', 'l'],['m', 'n', 'o'],['p', 'q', 'r', 's'],['t', 'u', 'v'],['w', 'x', 'y', 'z']]
    combinations = []

    def get_combinations(index, combination):
        if(index == len(digits)):
            combinations.append(combination)
            return

        for letter in letters[int(digits[index])-1]:
            get_combinations(index+1, combination + letter)

    get_combinations(0,"")
   
    print(combinations)

letterCombinations("23")

# Below is more of me talking to Copilot, lol

# What is the time complexity of this solution?
# O(4^n) where n is the length of the digits string, since the maximum number of letters
# per digit is 4 (for digits 7 and 9).
# The space complexity is also O(4^n) to store all the combinations in the combinations list.

# is there a more efficient way to do this?
# Not really, since we need to generate all possible combinations,
# we can't do better than O(4^n) in terms of time complexity.

# so are all permutation problems O(k^n) where k is the number of choices per position and n is the length of the string?
# Yes, in general, permutation problems have a time complexity of O(k^n) where k is the number of choices per position and n is the length of the string.
# However, the actual time complexity can vary depending on the specific problem and constraints.
