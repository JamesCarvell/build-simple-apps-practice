from random import choice
from sys import exit
from time import sleep

faces = ["J", "Q", "K"]


def annoying(annoyed_string):
    for i in range(annoyance):
        print("...")
        sleep(1)
    print(annoyed_string)
    money = 0
    sleep(1)


def deal_card(hand):
    draw = choice(new_deck)
    new_deck.remove(draw)
    hand.append(draw)


def check_hand(cards):
    score = 0
    aces = 0
    for card in cards:
        if card[1] in faces:
            score += 10
        elif card[1] in "A":
            aces += 1
        else:
            score += int(card[1])

    if aces == 0:
        return score

    if aces > 1:
        score += aces - 1
        aces = 1
    
    if score > 10:
        return (score + 1)
    else:
        return (score + 11)


money = 0
annoyance = 0
while money == 0 and annoyance < 3:
    money_string = input(f"How much money, in dollars, did you bring today?\nLimit is $1000 and no cents please.\n> ")
    try:
        money = int(money_string)
    except:
        annoyance += 1
        annoying("We don't deal in cents here.")
        continue

    if money > 1000:
        annoyance += 1
        annoying("That's too much")
    else:
        print(f"${money}! Very good!")
        sleep(1)

if annoyance >= 3:
    print("Get out.")
    exit()

suits = ["hearts", "diamonds", "spades", "clubs"]
card_set = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(suit, value) for suit in suits for value in card_set]

while 10000 > money > 0:

    try:
        bet = int(input("How much do you want to bet?\n> "))
        if (bet > money):
            print(f"You can't bet that. You only have {money}")
            continue
        elif (bet < 1):
            print("You can't bet negative")
            continue
        else:
            print(f"Very good. ${bet} it is")
    except:
        continue

    money -= bet

    player_hand = []
    dealer_hand = []
    new_deck = deck[:]

    print("<Dealing...>")
    sleep(2)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)

    hit = "yes"
    while "no" not in hit:
        player_score = check_hand(player_hand)
        print(f"Your current player_hand: {player_hand}")
        print(f"Your current score: {player_score}")
        print(f"The dealer has a face down card and face up {dealer_hand[1]}")

        hit = input("Hit? yes/no:")
        if "yes" in hit:
            deal_card(player_hand)
        else:
            result = "Undefined"

        player_score = check_hand(player_hand)
        if player_score > 21:
            print(f"Your current player_hand: {player_hand}")
            result = "Went Bust"
            break

    dealer_score = check_hand(dealer_hand)
    if dealer_score < 17 and "Went Bust" not in result:
        while dealer_score < 17:
            deal_card(dealer_hand)
            dealer_score = check_hand(dealer_hand)
    
    if (dealer_score == player_score):
        result = "Tied"
        print(f"The dealer was dealt {dealer_hand} and you were dealt {player_hand}")
        print("You both scored 21 and tied")
    elif (dealer_score <= 21) and (dealer_score > player_score):
        result = "Lost"
        print(f"The dealer was dealt {dealer_hand} and you were dealt {player_hand}")
        print(f"The dealer scored {dealer_score}, beating your {player_score}")
    elif "Went Bust" in result:
        pass
    else:
        result = "Won"
        print(f"The dealer was dealt {dealer_hand} and you were dealt {player_hand}")
        print(f"You scored {player_score}, beating the dealer's {dealer_score}")

    print(f"You {result}.")
    if "Won" in result:
        money += (bet * 2)
    elif "Tied" in result:
        money += bet
    else:
        pass
    print(f"You now have ${money}")

    keep_playing = "yes"
    if 10000 > money > 0:
        keep_playing = input("Do you want to keep playing? yes/no:")
    if "no" in keep_playing:
        break

if money >= 10000:
    print(f"You're at ${money}. You've won enough for today. Please leave.")
elif money <= 0:
    print("I'm afraid you're out of money. Please leave.")
else:
    print(f"You're leaving with ${money}. Please come again!")