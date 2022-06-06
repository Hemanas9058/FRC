def choice_checker(question, options):

    valid = False
    while not valid:

            response = input(question).lower()

            for var_item in options:
                if response == var_item:
                    return response
                elif response == var_item[0]:
                    return var_item

            print("Please enter either yes or no...\n")

# Loops to make testing faster..

to_check = ["yes", "no"]

for item in range(0,6):
    want_help = choice_checker("Do you want to read the instructions? ", to_check)
    print("You said '{}'\n".format(want_help))