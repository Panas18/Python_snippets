# The function is expected to return an integer.
# The function accepts an integer as parameter.

def logic(my_input):
    # Write your code here and remove pass statement
    # You can create other functions and call from here
    # Don't print anything. Just return the intended output
    sums = 0
    lists = [int(num) for num in str(my_input)]
    power = len(lists)
    last_power = lists[0]
    for i, num in enumerate(lists):
        if i == power - 1:
            power = last_power
        sums += pow(num, power)

    return sums


# Do not edit below
# Get the input
my_input = int(input())

# Print output returned from the logic function
print(logic(my_input))
