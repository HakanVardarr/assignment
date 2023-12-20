import random


def play():
    # 0 as
    dealer_cards = [deal(), deal()]
    player_cards = [deal(), deal()]

    while True:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        if 11 in player_cards and player_score != 21:
            print(
                f"Your cards value: {calculate_score(player_cards)}/{calculate_score(player_cards) - 10}"
            )
        else:
            print(f"Your cards value: {calculate_score(player_cards)}")

        print(f"Dealer's first card: {dealer_cards[0]}")
        print("---------------------------")

        if player_score == 21 or player_score > 21 or dealer_score == 21:
            break
        print("Do you want to hit or stand?")

        while True:
            user_input = input().lower()
            print("---------------------------")
            if user_input in ["hit", "stand"]:
                break
            else:
                print("Invalid input. Please type 'hit' or 'stand'")

        if user_input == "stand":
            break
        else:
            player_cards.append(deal())

    while dealer_score != 21 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = calculate_score(dealer_cards)

    print(
        f"\nDealer's hand: {dealer_cards}(Score: {dealer_score})\nYour hand: {player_cards}(Score: {player_score})\n"
    )

    if player_score == dealer_score:
        print("Draw!")
    elif dealer_score == 21:
        print("Dealer has Blackjack. You lost! :(")
    elif player_score == 21:
        print("You got BLACKJACKK!!!!!!! You won.")
    elif player_score > 21:
        print("You busted. You lost.")
    elif dealer_score > 21:
        print("Dealer busted. You won.")
    elif player_score > dealer_score:
        print("You won.")
    else:
        print("You lost.")


def deal():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)


def check_blackjack(cards: list) -> bool:
    if sum(cards) == 21:
        return True
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return check_blackjack(cards)
    return False


def calculate_score(cards: list) -> int:
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
