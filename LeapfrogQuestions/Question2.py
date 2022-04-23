# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # Don't print anything. Just return the intended output
    # You can create other functions and call from here
    result = []
    for i, num in enumerate(my_input):
        try:
            if (i+1) % 2 != 0:
                if num > my_input[i+1]:
                    result.append(num)
                elif num == my_input[i+1]:
                    pass
                else:
                    result.append(my_input[i+1])
            else:
                pass
        except IndexError:
            result.append(num)
    if not result:
        result = "total carnage"

    result = ''.join(str(i) for i in result) 
    return result


# Do not edit below

# Get the input
my_input = input()

# Print output returned from the logic function
print(logic(my_input))
