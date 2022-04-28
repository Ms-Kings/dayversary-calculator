from ast import Break
from datetime import date
from datetime import timedelta
from logging import exception

# Checks if the alphabetic part of the string spells "exit"
def is_exit(str):
    n = ""
    for x in str:
        if x.isalpha():
            n = n + x
    all_alpha = n.lower()
    if all_alpha == "exit":
        return True
    else:
        return False

# Returns only the numbers of a string
def get_onlynum(str):
    n = ""
    for x in str:
        if x.isnumeric():
            n = n + x
    return n

exit_loop = False
while not exit_loop:
    try:
        print("Type 'exit' whenever you're ready to leave.")
        x = input("When will I be 'X' days old?\nInsert 'X': ")
        
        if is_exit(x):
            exit_loop = True
            break
        
        # If there's a letter raise exception
        for i in x:
            if i.isalpha():
                raise Exception("That's not a number")

        x = int(get_onlynum(x))

        db = input("What your date of birth? (Use 'dd/mm/yyyy' format)\n")

        if is_exit(db):
            exit_loop = True
            break

        db = get_onlynum(db)

        d = int(db[0:2])
        m = int(db[2:4])
        y = int(db[4::])

        # Checks for valid dates
        if d > 31 or m > 12 or len(db) < 5:
            raise Exception("Invalid date.")

        bd = date(y,m,d)
        today = date.today()
        xdate = bd + timedelta(days = x)

        if xdate > today:
            print("You'll be %i days old in " %(x) + str(xdate))
        elif xdate == today:
            print("You're %i today!" %(x) )
        else:
            print("You were %i days old in " %(x) + str(xdate))
        
        input("Thanks for playing. Press 'enter' to go again.")
    except Exception as e:
        print(e)
        input("Invalid input. Press 'enter' to try again.")