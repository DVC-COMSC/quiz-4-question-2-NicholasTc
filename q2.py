
# ******************************
# Make your Code
# ******************************
longest = ""
shortest = ""

counter = 0
while True:
    input_string = input()

    if input_string == "stop" or input_string == "":
        break
    
    if counter == 0:
        longest = input_string
        shortest = input_string

    # checks the length
    input_len = len(input_string)

    if input_len > len(longest):
        longest = input_string

    if input_len < len(shortest):
        shortest = input_string

    counter += 1

print(f"{longest} {shortest}")
# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
