############### Blackjack Project #####################
import random
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(card, u_cards):
    """Deals cards"""
    u_cards.append(random.choice(card))
    return u_cards

def deal(card):
    """Deals the begining card"""
    u_cards = []
    i = 0
    while i < 2 :
        u_cards.append(random.choice(card))
        i+=1
    return u_cards

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

# random cards for user
user_cards = deal(cards)
print(user_cards)

# random cards for user
computer_cards = deal(cards)
print(computer_cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(card):
    score = sum(card)
    if score > 21:
        for n in card:
            if n == 11:
                card.remove(11)
                card.append(1)
                score = sum(card)
                return score
        return score
    elif score == 21 and score == 0 :
        return 0

    else:
        return score

user_score = calculate_score(user_cards)
print(user_score)
computer_score = calculate_score(computer_cards)
print(computer_score)
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game. done

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove(). done

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends. done

if computer_score == 0:
    end_game = True
    print("dealer wins")
elif user_score == 0:
    print("you win")
    end_game = True
else:
    end_game = False


#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended. done
def compare(score_1, score_2):
    """Compares the scores of two players and returns the winner"""
    if score_1 == 0 and score_2 == 0:
        end_game =  True
        return "It's a Draw!"
    elif score_1 == 0:
        end_game = True
        return  "Dealer Wins"
    elif score_2 == 0:
        end_game = True
        return "You win"
    elif score_1 > score_2 and score_1 < 21:
        end_game = True
        return "Dealer Wins"
    elif score_2 > score_1 and score_2 < 21:
        end_game = True
        return "You win"
    elif score_1 == score_2:
        end_game = True
        return "It's a Draw"
    elif score_1 > 21:
        end_game = True
        return "You win"
    elif score_2 > 21:
        end_game = True
        return "Dealer wins"
    else:
        end_game = True
        return "You Win"


while end_game == False:
    want_to_continue = str(input("Do you want to draw another card, Enter 'y' to continue or 'n' to end the game: "))
    if want_to_continue == 'y':
        deal_cards(cards, user_cards)
        print(user_cards)
        user_score = calculate_score(user_cards)
        print(user_score)
        end_game = False
        compare(computer_score, user_score)
        # if computer_score == 0:
        #     end_game = True
        #     print("dealer wins")
        # elif user_score == 0:
        #     print("you win")
        #     end_game = True
        # else:
        #     end_game = False
    else:
        while computer_score < 17:
            deal_cards(cards, computer_cards)
            print(computer_cards)
            calculate_score(computer_cards)
            print(computer_score)
            compare(computer_score, user_score)
            # end_game = True
        end_game = True
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends. done


#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17. done

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


