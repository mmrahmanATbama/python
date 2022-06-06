# show Higher Lower art
# Compare A: Biilie Ellish, a Musician, from United States.

# Show Vs. logo
# Against B: Shawn Mendes, a Musician, from Canada.
# Who has more followers? Type 'A' or 'B':
# Get Answer:
# Logo
# if Correct You're right! Current score: 1  Repeat
# else: Sorry, that's wrong. Final score:


import random

from art import logo
from art import vs
from game_data import data

# Get a random data from a list of dictionaries. Call it Compare A:
# Get a random data from a list of dictionaries, Call it Against B:
# Ensure A and B are not identical.
# get input from user.
# Compare and give answer.

def get_user_input():
    print(logo)
    index_A = 0
    index_B = 0

    while index_A == index_B:
        index_A = random.randint(0, len(data) - 1)
        index_B = random.randint(0, len(data) - 1)

# {
#     'name': 'Ariana Grande',
#     'follower_count': 183,
#     'description': 'Musician and actress',
#     'country': 'United States'
# },
    A_follower = data[index_A]['follower_count']
    B_follower = data[index_B]['follower_count']
    index_A = 0
    print(f"Compare A: {data[index_A]['name']}, {data[index_A]['description']}, {data[index_A]['country']}")
    print(vs)
    print(f"Against B: {data[index_A]['name']}, {data[index_A]['description']}, {data[index_A]['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()



#print(vs)
get_user_input()