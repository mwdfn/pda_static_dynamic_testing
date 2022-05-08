### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# The card class has not been imported, so no '.value' is defined.

  def check_for_ace(self, card): # self is not needed as a parameter
    if card.value = 1: # this should be == 'equal to'
      return True
    else # a semicolon is missing here (it should appear after 'else')
      return False


  dif highest_card(self, card1 card2): # 'dif' should be 'def', and a comma is missing after 'card1' argument. Self is not needed as a parameter.
  if card1.value > card2.value: # if statement is not indented (so not in the function). '.value' is not defined if Card class is not imported.
    return card # this should be card1
  else:
    return card2


def cards_total(self, cards): # this whole function should be indented, so it is inside the CardGame class. Self is not needed as a parameter.
  total # total variable has no assigned value 
  for card in cards:
    total += card.value
    return "You have a total of" + total # interger cannot be concatenated with string. The variable should be interpolated into the string instead.
  
```
