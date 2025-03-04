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

DECKS = 1

def main():
    count = 0
    user_input = True
    nb_cards = 0
    while user_input:
        card = input('CARD >> ')
        card = card.upper()
        count += BASIC_HI_LO[CARD_NAME[card]]
        nb_cards = nb_cards + 1
        print('COUNT: {}'.format(count))
        print('NB CARDS: {}'.format(nb_cards))

if __name__ == '__main__':
    main()