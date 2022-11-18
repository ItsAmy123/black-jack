import random
import numpy as np
from sys import exit

#card pool
cards_to_points = {
    "♠A": 1, "♠2": 2, "♠3": 3, "♠4": 4, "♠5": 5, "♠6": 6, "♠7": 7, "♠8": 8, "♠9": 9, "♠10": 10, "♠J": 10, "♠Q": 10, "♠K": 10,
    "♥A": 1, "♥2": 2, "♥3": 3, "♥4": 4, "♥5": 5, "♥6": 6, "♥7": 7, "♥8": 8, "♥9": 9, "♥10": 10, "♥J": 10, "♥Q": 10, "♥K": 10,
    "♣A": 1, "♣2": 2, "♣3": 3, "♣4": 4, "♣5": 5, "♣6": 6, "♣7": 7, "♣8": 8, "♣9": 9, "♣10": 10, "♣J": 10, "♣Q": 10, "♣K": 10,
    "♦A": 1, "♦2": 2, "♦3": 3, "♦4": 4, "♦5": 5, "♦6": 6, "♦7": 7, "♦8": 8, "♦9": 9, "♦10": 10, "♦J": 10, "♦Q": 10, "♦K": 10
}

poker_num = 1
face_card = list(cards_to_points.keys())
poker_list = poker_num * face_card #52cards

# round
game_round = 1

# Ace list
aces = ["♠A", "♥A", "♣A", "♦A"]

# score
total_score = np.array([0, 0])


#Use shuffle to set the random playing mechanism
def random_cards(random_card_list):
    random.shuffle(random_card_list)
    
#Get first 2 cards
def get_first_two_cards(input_hand_list):
    return [input_hand_list.pop(random.randint(0, len(input_hand_list)-1)),
            input_hand_list.pop(random.randint(0, len(input_hand_list)-1))]
#Hit
def add_one_poker(input_hand_list):
    return input_hand_list.pop(random.randint(0, len(input_hand_list)-1))


#score count
def score_count(hand_card):
    score = 0
    for i in hand_card:
        score += cards_to_points.get(i)

    # ace is 1 or 11
    for i in hand_card:
        if i in aces:
            if score + 10 <= 21:
                score = score + 10
            else:
                break

    return score


def win_lose(p_score, b_score):
    if p_score > 21 and b_score > 21:
        print("Draw")
        return np.array([0, 0])
    elif p_score <= 21 and b_score > 21:
        print("You Win")
        return np.array([1, 0])
    elif p_score > 21 and b_score <= 21:
        print("You Lose")
        return np.array([0, 1])
    else:
        if p_score > b_score:
            print("You Win")
            return np.array([1, 0])
        elif p_score == b_score:
            print("Draw")
            return np.array([0, 0])
        else:
            print("You Lose")
            return np.array([0, 1])


#hit
def add_card():
    continue_add_card = input("Hit？(Y/N):")
    if continue_add_card.upper() == "Y":
        return True
    elif continue_add_card.upper() == "N":
        return False
    else:
        print("Please enter'Y'or'N'")
        add_card()


#continute next round
def continue_next_round (p_total, b_total):
    next_round = input("Do you want to continue to the next round?(Y/N)>>>>>>:")
    if next_round.upper() == "Y":
        if len(poker_list) < 20:
            print("There are {} cards left, so the game is over!".format(len(poker_list)))
            print("The final score is：")
            print("Player VS.Dealer ==> {}:{}".format(p_total, b_total))
            if p_total> b_total:
                print("Yeah！！！You WIN～～～～")
            elif p_total < b_total:
                print("Dealer win the game～")
            else:
                print("Draw")

            exit(1)
        else:
            return True
    elif next_round.upper() == "N":
        print("The game is OVER")
        print("")
        print("The final score is：")
        print("Player: {} VS. Dealer: {}".format(p_total, b_total))
        if p_total > b_total:
            print("Yeah！！！You WIN～～～～")
        elif p_total < b_total:
            print("Yeah！！！You WIN～～～～")
        else:
            print("Draw")
        exit(1)
    else:
        print("Please enter the valid string")
        continue_next_round()



#cards and score
def every_round(input_hand_list):
    # Initialize player and computer hands
    player_hand_poker = []
    banker_hand_poker = []

    # Initialize 2 cards
    player_init_poker = get_first_two_cards(input_hand_list)
    banker_init_poker = get_first_two_cards(input_hand_list)

    print("Player's hands are：{} and {}".format(player_init_poker[0], player_init_poker[1]))
    print("Dealer's hands are：{} and ？".format(banker_init_poker[0]))

    # blackjack?
    p_score = score_count(player_init_poker)
    b_score = score_count(banker_init_poker)

    # add hands
    player_hand_poker.extend(player_init_poker)
    banker_hand_poker.extend(banker_init_poker)

    if p_score == 21 or b_score == 21:
        print("The card face is 21")
        return win_lose(p_score, b_score)
    else:
        # Player
        while True:
            if_add_card = add_card()
            if if_add_card == True:
                new_card = add_one_poker(input_hand_list)
                player_hand_poker.append(new_card)
                p_score = score_count(player_hand_poker)

                print("Player's hand：{}".format(player_hand_poker))

                if p_score > 21:
                    print("BUST！")
                    print("Dealer's hand：{}".format(banker_hand_poker))
                    return np.array([0, 1])
                else:
                    continue
            else:
                print("Stop adding card")
                # Computer/Dealer
                while p_score > b_score:
                    new_card = add_one_poker(input_hand_list)
                    banker_hand_poker.append(new_card)
                    b_score = score_count(banker_hand_poker)
                print("Dealer's hand:{}".format(banker_hand_poker))
                return win_lose(p_score, b_score)


        
#format of the game
print("Welcome to BlackJack!")
print("-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-")

input("Press'Enter'to start your game!")

        
while True:
    game_rule = input("Would you like to read the game rule (Y/N): ")
    if game_rule.upper() == "Y":
        print(" ")
        print("The game rule： ")
        print("1. The purpose of BlackJack is to reach to 21 points, or the player's score higher than dealer's but not exceeding 21")
        print("2. The score of 10, J, Q, K are 10 points，A is 1 or 11 points，and the cards 2 to 9 have same score as their card face.")
        print("3. When the game start, Each of the player and dealer will have 2 cards. They need to add 2 cards together,")
        print("   and decide wether they want to Hit or stop taking card.")
        print("4. In the round, who reach the 21 points frist or one person's score higher than another and close to 21 points that person")
        print("   win. If one person's score higher than 21 points,then he/she loses; another person's need to smaller than 21 points.")
        print(" ")
    elif game_rule.upper() == "N":
        print(" ")
    else:
        print("Please enter the valid string")
        continue
    
    # current round
    print("-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-{} ROUND-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-".format(game_round))

    # shuffle
    random_cards(poker_list)

    # record current score
    current_score = every_round(poker_list)

    total_score = np.add(total_score, current_score)

    # report the score
    print("-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-♠-♥-♦-♣-")
    print("The current score is-->Player：Dealer ==> {}:{}".format(total_score[0], total_score[1]))

    game_round = game_round + 1

    continue_next_round(total_score[0], total_score[1])
    print("")
