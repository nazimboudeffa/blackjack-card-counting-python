CARD_NAME = {
    'A': "Ace",
    '2': "Two",
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
    '10': "Ten",
    'J': "Jack",
    'Q': "Queen",
    'K': "King",
    }

BASIC_OMEGA_II = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 2, "Seven": 1, "Eight": 0, "Nine": -1, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
BASIC_HI_LO = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_HI_OPT_I = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
BASIC_KO = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_RED_SEVEN = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_ZEN_COUNT = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 2, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
BASIC_HALVES = {"Ace": 0.5, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0.5, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_REKO = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_KISS_II = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_CANFIELD_MASTER = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_SILVER_FOX = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_FELTENBERGER = {"Ace": 1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_HI_OPT_II = {"Ace": 0, "Two": 1, "Three": 1, "Four": 2, "Five": 2, "Six": 1, "Seven": 1, "Eight": 0, "Nine": 0, "Ten": -2, "Jack": -2, "Queen": -2, "King": -2}
BASIC_WONG_HALVES = {"Ace": 0.5, "Two": 1, "Three": 1.5, "Four": 1, "Five": 1, "Six": 1, "Seven": 0.5, "Eight": 0, "Nine": -0.5, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_REVERSES = {"Ace": -1, "Two": -1, "Three": -1, "Four": -2, "Five": -2, "Six": -2, "Seven": -1, "Eight": 0, "Nine": 0, "Ten": 1, "Jack": 1, "Queen": 1, "King": 1}
BASIC_ACE_FIVE = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}
BASIC_COUNT = {"Ace": -1, "Two": 1, "Three": 1, "Four": 1, "Five": 1, "Six": 1, "Seven": 0, "Eight": 0, "Nine": 0, "Ten": -1, "Jack": -1, "Queen": -1, "King": -1}

DECKS = [[]]

#black spades S (♠), red hearts H (♥), black diamonds D (♦), and red clubs C (♣)
CARDS = {(figure, color) for figure in CARD_NAME.keys() for color in ['H', 'D', 'C', 'S']}

def main():
    count = 0
    user_input = True
    nb_cards_played = 0
    while user_input:
        
        figure = input('FIGURE: 2...9, 10, J, Q, K >> ')
        figure = figure.upper()
        color = input('COLOR: S=♠, H=♥, D=♦, C=♣ >> ')
        card = (figure, color.upper())
        print('COUNT: {}'.format(count))

        count += BASIC_HI_LO[CARD_NAME[figure]]

        # Check if card is in any of the decks
        card_exists = any(card in deck for deck in DECKS)

        if not card_exists:
            DECKS[-1].append(card)
            for deck in DECKS:
                print(deck)
        else:
            print('CARD ALREADY USED')

        nb_cards_played += 1
        print('NUMBER OF CARDS PLAYED: {}'.format(nb_cards_played))

        if nb_cards_played > 52:
            DECKS.append([])  # Add a new sublist for the new deck
            nb_cards_played = 0  # Reset the card count for the new deck
            print('NEW DECK CREATED')
            print('DECKS: {}'.format(len(DECKS)))

        # Calculate and print the true count
        true_count = count / len(DECKS)
        print('TRUE COUNT: {:.2f}'.format(true_count))

if __name__ == '__main__':
    main()