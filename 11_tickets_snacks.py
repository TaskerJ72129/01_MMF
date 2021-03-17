import pandas

# Initialise snack lists

all_names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']
all_tickets = [7.5, 10.5, 10.5, 10.5, 6.5]

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'aTicket': all_tickets,
    'bPopcorn': popcorn,
    'cWater': water,
    'dPita Chips': pita_chips,
    'eM&Ms': mms,
    'fOrange Juice': orange_juice,
}

# cost of each snack
price_dict = {
    'bPopcorn': 2.5,
    'cWater': 2,
    'dPita Chips': 4.5,
    'eM&Ms': 3,
    'fOrange Juice': 3.25,
}

test_data = [
    [[2, 'bPopcorn'], [1, 'dPita Chips'], [1, 'fOrange Juice']],
    [[]],
    [[1, 'cWater']],
    [[1, 'bPopcorn'], [1, 'fOrange Juice']],
    [[1, 'eM&Ms'], [1, 'dPita Chips'], [3, 'fOrange Juice']]
]

count = 0
for client_order in test_data:

    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)

    # get order (hard coded for easy testing)
    snack_order = test_data[count]
    count += 1

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

print()

# Create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total' fill it price for snacks and ticket

movie_frame["Sub Total"] = \
    movie_frame['aTicket'] + \
    movie_frame['bPopcorn']*price_dict['bPopcorn'] + \
    movie_frame['cWater']*price_dict['cWater'] + \
    movie_frame['dPita Chips']*price_dict['dPita Chips'] + \
    movie_frame['eM&Ms']*price_dict['eM&Ms'] + \
    movie_frame['fOrange Juice']*price_dict['fOrange Juice']

# Shorten column names
movie_frame = movie_frame.rename(columns={'aTicket' : 'Ticket', 'fOrange Juice': 'OJ',
'dPita Chips': 'Chips', 'bPopcorn' : 'Popcorn', 'cWater' : 'Water', 'eM&Ms': 'M&Ms'})

print(movie_frame)
