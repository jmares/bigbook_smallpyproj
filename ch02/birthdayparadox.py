"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random

def get_birthdays(number_of_birthdays):
    """Returns a list of random data objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation
        start_of_year = datetime.date(2021, 1, 1)

        # Get random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0,364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """Returns the date object of a birthday that occurs more than once in the list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique

    # Compare each birthday to every other birthday
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1 :]):
            if birthday_a == birthday_b:
                return birthday_a  # Return the matching birthday


# Display the intro
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

# Set up a table of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate (max 100)?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print()

# Generate and display birthdays
print(f'Here are {num_bdays} birthdays: ')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma before each birthday after the first birthday
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print()
print()

# Determine if there are two birthdays that match
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100.000 simulations
print(f'Generating {num_bdays} random birthdays 100.000 times ...')
input('Press enter to begin ...')
print('Let\'s run another 100,000 simulations.')
sim_match = 0    # How many simulations had matching birthdays
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run ...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100.000 simulations run')

# Display simulation results
probability = round(sim_match / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {num_bdays} people, there was a')
print(f'matching birthday in that group {sim_match} times. This means')
print(f'that {num_bdays} people have a {probability}% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')



