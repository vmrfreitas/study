input_string = "string legal maneira radicau  "

def urlify():
    url_string = ""
    for i in range(len(input_string)):
        if input_string[i] == " ":
            url_string += "%20"
        else:
            url_string += input_string[i]
    input_string = url_string

urlify()
print(input_string)

## not sure about creating two strings tho...
## will check the solution

# ok so you have two iterables, both going backwards through the string 
# one starts at the end of the text, before the trailing spaces, and goes character by character checking for spaces
# the other starts at the end of the string, goes character by character but when a space is found it jumps 3 characters and writes the %20


# takes less space but same time complexity