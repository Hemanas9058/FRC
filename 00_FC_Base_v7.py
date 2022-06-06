# import libraries
import pandas
import math


# *** Functions go here ***

# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list,
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be "
                              "blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
                                 "The amount must be a whole number "
                                 "more than zero",
                                 int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return""


# work out profit goal and total sales required
def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal..
        response = not_blank("What is your profit goal (eg $500 or 50%) ",
                             "Please enter a profit goal")

        # check if first character is $..
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = string_check("Do you mean ${:.2f}. ie {:.2f} dollars? , y / n".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = string_check("Do you mean {}%? , y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function
def round_up(amount, round_to):
            return int(math.ceil(amount / round_to)) * round_to


# checks specifically for yes / no - change error message if generalising
def string_check(question, options):

    is_valid = ""

    valid = False
    while not valid:

        choice = input(question)

        for var_list in options:

            # if the snack is in one of the lists, return the full name
            if choice in var_list:

                # Get full name of snack and put it
                # in title case so it looks nice when outputted
                chosen = var_list[0]
                is_valid = "yes"
                break

            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

                # if choice is not OK, repeat question
        if is_valid == "yes":
            return chosen

        else:
            print("Please enter yes / no")
            print()
            # return "invalid choice"


def instructions(options):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = string_check("Would you like to read the instructions?", options)

    if show_help == "yes":
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


# *** Main Routine goes here ***

# valid options for yes / no questions
yes_no_list = [
    ["yes", "y"],
    ["no", "n"]
]

# Ask if instructions are needed
instructions(yes_no_list)
print()

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank")

how_many = num_check("How many items will you be producing? ",
                     "The number of items must be whole "
                     "number more than zero", int)

print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = string_check("Do you have fixed costs (y / n)? ", yes_no_list)

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = ""

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding
round_to = num_check("Round to nearest...? $", "Can't be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many
print("Selling Price: ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)

# ***Printing Area***

print()
print("**** Fund Raising - {} ****".format(product_name))
print()
expense_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes":
    # expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub)
    expense_print("Fixed", fixed_frame, fixed_sub)

print()
print("****** Total Costs: ${:.2f} **********".format(all_costs))
print()

print()
print("**** Profit & Sales Targets ****")
print("Profit Target: ${:.2f}".format(profit_target))
print("Total Sales: ${:.2f}".format(all_costs, profit_target))

print()
print("**** Pricing ****")
print("Minimum Price: ${:.2f}".format(selling_price))
print("Recommended Price: ${:.2f}".format(recommended_price))