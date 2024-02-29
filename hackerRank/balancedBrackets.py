# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-five

def isBalanced(s):
    
    def is_opening(char):
        if char == '[' or char == '(' or char == '{':
            return True
        else:
            return False
    
    def matching_opening(char):
        if char == ']':
            return '['
        if char == ')':
            return '('
        if char == '}':
            return '{'
    
    opening_stack = []
    string_list = list(s)
    if not string_list:
        return "NO"
    for char in string_list:
        if is_opening(char):
            opening_stack.append(char)
        else:
            try:
                popped_char = opening_stack.pop()
                if popped_char != matching_opening(char):
                    return "NO"
            except:
                return "NO"
    if not opening_stack:
        return "YES"
    else:
        return "NO"