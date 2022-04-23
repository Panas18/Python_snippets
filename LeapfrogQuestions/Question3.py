# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
    vowels = ['a', 'e', 'i', 'o','u']
    result = ''
    for vowel in vowels:
        count = 1
        for char in my_input.lower():
            if char == vowel:
                count +=2
        output = f"{count}{vowel}"
        if count != 0:
            result = result+output
    return result 

# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))

