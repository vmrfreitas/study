# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-five
# check if for every opening there's a closing, for example: [({})] is balanced, but [({}] is not
def isBalanced(s):
    
    def is_opening(char):
        if char == '[' or char == '(' or char == '{':
            return True
        else:
            return False
    
    # checks if the closing matches the opening parameter char 
    def matching_opening(char):
        if char == ']':
            return '['
        if char == ')':
            return '('
        if char == '}':
            return '{'
    
    opening_stack = []
    string_list = list(s)

    # empty string
    if not string_list:
        return "NO"
    
    for char in string_list:
        # appending opening char to the opening_stack
        if is_opening(char):
            opening_stack.append(char)
        else:
            try:
                # whenever we find a closing char we pop the stack and check if the corresponding opening is the last one on the stack
                # since it will always work -> {([]{})} just think lol
                popped_char = opening_stack.pop()
                if popped_char != matching_opening(char):
                    return "NO"
            # exception means we tried to pop extra
            except:
                return "NO"
    # empty stack means we closed them all, so it is balanced
    if not opening_stack:
        return "YES"
    else:
        return "NO"