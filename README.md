## Blackjack Test

### Scenarios

Given I play a game of blackjack\
When I am dealt my opening hand\
Then I have two cards

Given I have a valid hand of cards\
When I choose to ‘hit’\
Then I receive another card\
And my score is updated

Given I have a valid hand of cards\
When I choose to ‘stand’\
Then I receive no further cards\
And my score is evaluated

Given my score is updated or evaluated\
When it is 21 or less\
Then I have a valid hand

Given my score is updated\
When it is 22 or more\
Then I am ‘bust’ and do not have a valid hand

Given I have a king and an ace\
When my score is evaluated\
Then my score is 21

Given I have a king, a queen, and an ace\
When my score is evaluated\
Then my score is 21

Given that I have a nine, an ace, and another ace\
When my score is evaluated\
Then my score is 21
