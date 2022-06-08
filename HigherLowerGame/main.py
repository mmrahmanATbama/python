# add to git
import random
from art import logo
from art import vs
from game_data import data


current_score = 0


def increase_current_score():
    global current_score
    current_score += 1
    return current_score


def result(ind_a, ind_b, ans):
    a_follower_count = data[ind_a]['follower_count']
    b_follower_count = data[ind_b]['follower_count']
    print(logo)
    if ans == 'A' and a_follower_count > b_follower_count:
        increase_current_score()
        print(f"You're right. Current score: {current_score}")
        return ind_b
    elif ans == 'B' and b_follower_count > a_follower_count:
        increase_current_score()
        print(f"You're right. Current score: {current_score}")
        return ind_b
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        return -1


def get_user_choice(ind_a, ind_b):
    print(f"Compare A: {data[ind_a]['name']}, {data[ind_a]['description']}, {data[ind_a]['country']}")
    print(vs)
    print(f"Against B: {data[ind_b]['name']}, {data[ind_b]['description']}, {data[ind_b]['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    return answer


def play():
    print(logo)
    index_a = 0
    index_b = 0

    while index_a == index_b:
        index_a = random.randint(0, len(data) - 1)
        index_b = random.randint(0, len(data) - 1)

    answer = get_user_choice(index_a, index_b)
    game_play = result(index_a, index_b, answer)

    while game_play != -1:
        index_a = game_play
        index_b = random.randint(0, len(data) - 1)
        answer = get_user_choice(index_a, index_b)
        game_play = result(index_a, index_b, answer)


play()
