inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snow(inches_of_snow):
    total_inches = 0
    for day,inches in inches_of_snow.items():
        total_inches += inches
    print("Total snowfall inches: ", total_inches)
    today = input("Enter today's snowfall: ")
    total_inches += int(today)
    print("Total snowfall inches: ", total_inches)


print_total_snow(inches_snow)