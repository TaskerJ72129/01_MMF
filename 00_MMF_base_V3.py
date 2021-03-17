# import statements
import re
import pandas


# functions go here

# String check
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set in_valid to no
        else:
            is_valid = "no"

    # if the snacks is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option\n")
        return "invalid choice"

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry - this can't be blank, "
                  "please enter your name.")


# checks for an integer between two values
def int_check(question):

    error = "Please enter a whole number"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response < 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)


# checks number of tickets left and warns user if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats "
              "left".format(ticket_limit - tickets_sold))

    # warns user only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    return ""


# Gets ticket price based on age
def get_ticket_price():

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price
# ----- Main Routine -----

# dictionaries / lists

#  list for valid yes / no responses
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]
# used program before?

# loop
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []


# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
}

# Ask user if they have used program before & show instructions

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check numbers of ticket limit has not been exceeded
    check_tickets(ticket_count, MAX_TICKETS)

    # Get details for each ticket

    # Get name (no blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    ticket_price = get_ticket_price()
    # if age is invalid, restart loop (and get name again
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # Get payment method (ie: work out if surcharge is needed)
    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit)? ").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge = 0

# End of tickets loop / snacks / payment loop

# print details
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))





    # price


    # loop snack