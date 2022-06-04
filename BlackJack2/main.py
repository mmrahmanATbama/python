# Used nested Dictionary for this one. 

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
# from art import logo
from os import system, name


def print_player(games_play):
    print(
        f"Your current cards: {games_play['player']['player_card']} , current score: {games_play['player']['player_total']}")
    print(f"Computer's first card: {games_play['dealer']['dealer_card'][0]}")


def total_score(games_play):
    game_play['player']['player_total'] = sum(game_play['player']['player_card'])
    game_play['dealer']['dealer_total'] = sum(game_play['dealer']['dealer_card'])
    return games_play


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


def game_winner(games_play):
    games_play = total_score(games_play)
    player_score = game_play['player']['player_total']
    computer_score = game_play['dealer']['dealer_total']
    if player_score > 21:
        print("**************")
        print("You lose")
    elif computer_score > 21:
        if player_score > 21:
            print("**************")
            print("You lose")
        else:
            print("**************")
            print("Opponent went over. You win :)")
    elif computer_score == player_score and computer_score <= 21 and player_score <= 21:
        print("**************")
        print("Draw")
    elif computer_score < player_score:
        print("**************")
        print("You win. :)")
    else:
        print("**************")
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
        #        print(logo)
        return True
    else:
        quit()


def players_turn_to_play(games_play):
    games_play = total_score(games_play)
    local_ans = 'y'
    while local_ans != 'n':
        games_play['player']['player_card'].append(draw_cards(is_first_draw=False))
        games_play['player']['player_total'] = sum(game_play['player']['player_card'])
        games_play = total_score(games_play)

        if games_play['player']['player_total'] > 21:
            if 11 in games_play['player']['player_card']:
                games_play['player']['player_card'] = handle_ace_card(games_play['player']['player_card'])
                games_play['player']['player_total'] = sum(game_play['player']['player_card'])
                if games_play['player']['player_total'] > 21:
                    print_player(games_play)
                    return games_play
            else:
                break

        if games_play['player']['player_total'] == 21:
            break
        print_player(games_play)
        local_ans = input("Type 'y' to get another card, type 'n' to pass: ")

    return games_play


def computer_turn_to_play(games_play):
    # if computer total is less than 17 (16 or less) computer must pick a card
    # if computer have an ace, than it can be 1 or 11, whichever one gives dealer a chance to win
    # if computer is less then 21 or computer is less then the player, computer will pick a card (again whichever wins)
    games_play = total_score(games_play)
    while games_play['dealer']['dealer_total'] < 17:
        games_play['dealer']['dealer_card'].append(draw_cards(is_first_draw=False))
        games_play = total_score(games_play)
        if 11 in games_play['dealer']['dealer_card']:
            games_play['dealer']['dealer_card'] = handle_ace_card(games_play['dealer']['dealer_card'])
            games_play['dealer']['dealer_total'] = sum(game_play['dealer']['dealer_card'])
        if games_play['dealer']['dealer_total'] > 21:
            return games_play
        if games_play['dealer']['dealer_total'] == 21 or games_play['dealer']['dealer_total'] == games_play['player'][
            'player_total']:
            # dealer has the best possible hand.
            return games_play
    # at this point, the dealer is > 17 and < 21 (however winning is still not certain, since the player may have 19 and dealer has 18)
    while games_play['dealer']['dealer_total'] < games_play['player']['player_total'] and games_play['dealer'][
        'dealer_total'] < 21:
        games_play['dealer']['dealer_card'].append(draw_cards(is_first_draw=False))
        games_play = total_score(games_play)
        if 11 in games_play['dealer']['dealer_card']:
            games_play['dealer']['dealer_card'] = handle_ace_card(games_play['dealer']['dealer_card'])
            games_play['dealer']['dealer_total'] = sum(game_play['dealer']['dealer_card'])
        if games_play['dealer']['dealer_total'] == 21 or games_play['dealer']['dealer_total'] == games_play['player'][
            'player_total']:
            # dealer has the best possible hand.
            return games_play
    # edge case
    return games_play


def final_hand(games_play):
    total_score(games_play)
    print(
        f"Your final hand: {games_play['player']['player_card']}, final score: {games_play['player']['player_total']}")
    print(
        f"Computer final hand: {games_play['dealer']['dealer_card']}, final score: {games_play['dealer']['dealer_total']}")
    # -------------------------------------------------------------------------------------------


while continue_game_play():
    # First draw, both player and dealer gets two cards, players cards are visible, only one card from dealer is visible
    game_play = {
        "player": {
            "player_card": draw_cards(is_first_draw=True),
            "player_total": 0,
        },
        "dealer": {
            "dealer_card": draw_cards(is_first_draw=True),
            "dealer_total": 0,
        },
    }

    game_play = total_score(game_play)
    print_player(game_play)

    ans = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if ans == 'y':
        game_play = players_turn_to_play(game_play)
        game_play = total_score(game_play)

    if game_play['player']['player_total'] < 22:
        game_play = computer_turn_to_play(game_play)

    final_hand(game_play)
    game_winner(game_play)
