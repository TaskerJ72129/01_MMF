def yes_no(question):

    error = "Please answer yes / no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)


# Main routine

for item in range(0, 6):
    want_snacks = yes_no("Do you want snacks? ")
    print("Answer OK, you said:", want_snacks)
    print()