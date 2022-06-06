def yes_no(question):

    valid = False
    while not valid:

            response = input(question).lower()

            if response == "yes" or response == "y":
                return "yes"
            elif response == "no" or response == "n":
                return "no"
            else:
                print("Please enter yes / no")

# Loops to make testing faster..


for item in range(0,6):
    want_help = yes_no("Do you want to read the instructions? ")
    print("You said '{}'\n".format(want_help))