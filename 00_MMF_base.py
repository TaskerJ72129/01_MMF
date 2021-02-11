# import statements


# functions go here

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

# ----- Main Routine -----

# dictionaries / lists

# used program before?

# loop
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # tells user how many seats left
    if count < 4:
        print("You have {} seats "
              "left".format(MAX_TICKETS - count))

    # warns user only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    # Get details...

    # Get name (no blank)
    name = not_blank("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(count, MAX_TICKETS - count))
    # Get name (no blank)
    name = not_blank("Name: ")

    # age (12-130)


    # price


    # loop snack