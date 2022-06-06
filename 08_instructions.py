# functions go here

def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

            # if choice is not OK, repeat question
    if is_valid == "yes":
        return chosen

    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions?")
        show_help = string_check(show_help, options)


    if show_help == "Yes":
        print()
        print("**** Fund Raising Calculator Instructions ****")
        print()
        print("In order to use this program you will be asked to input")
        print("the name of your product, variable costs, fixed costs, and your profit goal")
        print("after inputting all of the data the program will output a list")
        print("with all the input data as well as the total costs and")
        print("recommended price for your product to reach your profit goal.")
        print()
        print("The data can also be found in the text file titled with the")
        print("same name as your product.")

    return ""

# Main Routine goes here

# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# Ask if instructions are needed
instructions(yes_no)
print()