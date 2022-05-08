## Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.
from src.card import *

class CardGame:

  def check_for_ace(card): 
    if card.value == 1:
      return True
    else:
      return False


  def highest_card(card1, card2):
    if card1 > card2:
      return card1 
    else:
      return card2

  cards = [1, 2, 3, 4]
  def cards_total(cards):
    total = 0
    for card in cards:
      total += card
    return (f"You have a total of {total}")


