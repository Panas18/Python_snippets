def logic(my_input):
    happy = 0
    for i, digit in enumerate(my_input):
        if i == 0:
            if digit == my_input[i+1]:
                happy+=1
        elif i == len(my_input):
            if digit == my_input[i-1]:
                happy+=1
                break
        else:
            before = my_input[i-1]
            after = my_input[i+1]
            if digit == 1:
                if before != 0 or after != 0:
                    happy+=1
            else:
                if digit == 0:
                    if before == 0 or after == 0:
                        happy += 1
    return happy





my_input = "010101"

print(logic(my_input))
