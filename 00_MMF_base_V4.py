# import statements
import pandas, re


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

# Gets snacks
def get_snack():
    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with valid options for each snack
    # <full name, letter code (a - e), and possible abbreviations etc>
    valid_snacks = [
        ["Bpopcorn", "popcorn", "p", "corn", "a"],
        ["Em&Ms", "M&m's", "m&m's", "mms", "m", "b"],
        ["Dpita chips", "pita chips", "chips", "pc", "pita", "c"],
        ["Cwater", "water", "w", "d"],
        ["Forange Juice", "orange juice", "oj", "o", "juice", "e"]
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)
        '''print("Snack Choice: ", snack_choice)'''

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        # add snack AND amount to list...

        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_row)


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
MAX_TICKETS = 3

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# snack lists
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# store surcharge multiplier
surcharge_multi_list = []
# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Aticket': all_tickets,
    'Bpopcorn': popcorn,
    'Cwater': water,
    'Dpita Chips': pita_chips,
    'Em&Ms': mms,
    'Forange Juice': orange_juice,
    'GSurcharge_Multiplier' : surcharge_multi_list
}

# cost of each snack
price_dict = {
    'Bpopcorn': 2.5,
    'Cwater': 2,
    'Dpita Chips': 4.5,
    'Em&Ms': 3,
    'Forange Juice': 3.25
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
    # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # If they say yes, ask what snacks they want (and add to snack list)
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    # Get payment method (ie: work out if surcharge is needed)
    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit)? ").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_multi_list.append(surcharge_multiplier)

# End of tickets loop / snacks / payment loop

# print details
# Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket
movie_frame["Sub Total"] = \
    movie_frame['Aticket'] + \
    movie_frame['Bpopcorn']*price_dict['Bpopcorn'] + \
    movie_frame['Cwater']*price_dict['Cwater'] + \
    movie_frame['Dpita Chips']*price_dict['Dpita Chips'] + \
    movie_frame['Em&Ms']*price_dict['Em&Ms'] + \
    movie_frame['Forange Juice']*price_dict['Forange Juice']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["GSurcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

# Shorten column names
movie_frame = movie_frame.rename(columns={'Aticket' : 'Ticket', 'Forange Juice': 'OJ',
'Dpita Chips': 'Chips', 'Bpopcorn' : 'Popcorn', 'Cwater' : 'Water', 'Em&Ms': 'M&Ms',
                                          'GSurcharge_Multiplier' : 'SM'})

# Set up columns to be printed
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp
pandas.set_option('precision', 2)

print_all = input("Print all columns?? (y) for yes ")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total', 'Surcharge', 'Total']])

print()

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