############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
# import only system from os
from os import system, name


def draw_cards(is_first_draw):
    """
    randomly picks two cards from deck, if first draw, returns list of two cards
    else return a random card
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if is_first_draw:
        return random.sample(cards, 2)
    else:
        return random.choice(cards)

def handle_ace_card(card_list):
    """ ace card is either 1 or 11, depending on player lose"""
    index = card_list.index(11)
    card_list[index] = 1
    return card_list

def game_winner(score_record):
    player_score = score_record["player"]
    computer_score = score_record["computer"]
    if player_score > 21:
        print("You lose")
        return
    if computer_score > 21:
        if player_score > 21:
            print("You lose")
        else:
            print("Opponent went over. You win :)")
    elif computer_score == player_score and computer_score <= 21 and player_score <= 21:
        print("Draw")
    elif computer_score < player_score:
        print("You win. :)")
    else:
        print("You lose")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def continue_game_play():
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == 'y':
        clear()
        print(logo)
        return True
    else:
        quit()


def players_turn_to_play(pl_card, comp_cards):
    local_ans = 'y'
    while local_ans != 'n':
        pl_card.append(draw_cards(is_first_draw=False))
        pl_total = sum(pl_card)
        game_score = {
            "player": pl_total,
            "computer": sum(comp_cards),
        }
        if pl_total > 21:
            if 11 in pl_card :
                pl_card = handle_ace_card(pl_card)
                pl_total = sum(pl_card)
                if sum(pl_card) > 21:
                    return game_score
            else:
                break
        print(f"Your current cards: {pl_card} , current score: {pl_total}")
        print(f"Computer's first card: {comp_cards[0]}")
        local_ans = input("Type 'y' to get another card, type 'n' to pass: ")

    return game_score

# Fix logic
def computer_turn_to_play(game_score,computers_cards):
    # user "Stand" or said no to more cards. Now computer picks
    comp_total = game_score["computer"]
    # fix logic here.
    while comp_total < 17:
        computers_cards.append(draw_cards(is_first_draw=False))
        comp_total = sum(computers_cards)

    while comp_total <= game_score["player"] and not comp_total >= 21:
        computers_cards.append(draw_cards(is_first_draw=False))
        comp_total = sum(computers_cards)
        if comp_total > 21:
            if 11 in computers_cards:
                computers_cards = handle_ace_card(computers_cards)
                comp_total = sum(computers_cards)
                if comp_total > 21:
                    return game_score
            else:
                break

    game_score["computer"] = comp_total
    return game_score

def final_hand(pl_card, comp_card):
    print(f"Your final hand: {pl_card}, final score: {sum(pl_card)}")
    print(f"Computer final hand: {comp_card}, final score: {sum(comp_card)}")
# -------------------------------------------------------------------------------------------

while continue_game_play():
    # Declare variables
    players_card = draw_cards(is_first_draw=True)
    players_total = sum(players_card)
    computers_card = draw_cards(is_first_draw=True)
    computers_total = sum(computers_card)
    score_card = {
        "player": players_total,
        "computer": computers_total,
    }
    print(f"Your current cards: {players_card} , current score: {players_total}")
    print(f"Computer's first card: {computers_card[0]}")
    ans = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if ans == 'y':
        score_card = players_turn_to_play(players_card, computers_card)

    if score_card["player"] < 22:
        score_card = computer_turn_to_play(score_card, computers_card)

    final_hand(players_card, computers_card)
    game_winner(score_card)

