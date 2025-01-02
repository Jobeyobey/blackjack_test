## Blackjack Tech Test - Starter Code

This code is offered as a potential starting point for completing the BBC Software Engineering Graduate Scheme tech test.
You do **not** have to use this starter code.

### Getting started

-   Ensure you can run the provided code.
    -   If you have Python 3 installed:
        -   Open a terminal window and navigate to the folder containing this `README.md`.
        -   Type `python3 blackjack.py`
        -   Look for a welcome message in the console.
    -   If that doesn't work, check your setup and download Python 3 if needed:
        -   https://wiki.python.org/moin/BeginnersGuide/Download
-   Ensure you can run the unit tests.
    -   From the same terminal window, type `python3 -m unittest discover test`.
    -   Python should find and run the one provided failing test, with the message `AssertionError: 0 != 52`

### Adding to the starter code

-   A great place to start is by making the provided unit test pass.
    -   The provided Deck class has an empty array, `self.cards`.
    -   The test will pass if `self.cards` on line 3 of `deck.py` contains 52 things.
    -   once this test passes, extend the test or add more tests.
    -   e.g. the first test only ensures a Deck has 52 of _something_- what else might you want to test?
-   A TDD (test-driven development) approach can be useful:
    -   write a failing test that describes what you want your code to do
        -   e.g. 'a deck should have 4 aces'
    -   modify the code that you're testing so that the test passes
        -   e.g. the deck actually _has_ 4 aces!
    -   each of the scenarios in the brief can be turned into a single test
-   You can add more test files:
    -   keep them in the `test/` directory
    -   make sure they have filenames beginning with `test`
    -   make sure test methods within those files also begin with `test`
-   You can add more source files:
    -   keep them in the `src/` directory
-   You can use any approach you want
    -   The provided code hints at an object-oriented approach (since we have a Deck class)
    -   if you wanted to extend this approach, you might want to create classes for Hand, Card, Dealer, etc.

### Disregarding the starter code

-   As stated above you, can use any language or framework you prefer to solve this challenge.
-   If you prefer not to use the starter code, let us know in your submission how to run it.

### Completing the task

-   Remember, the task is to write code that accurately scores a hand of blackjack, _not_ to make a whole game
-   This means you _don't_ need to have a running program to complete this test
    -   You can just prove your code works with unit tests
    -   You _don't_ need to add anything to `blackjack.py` to do this.
-   You can _choose_ to make a running program that demonstrates that your code works
    -   If you want to do this, you can extend the `play` method of `blackjack.py`
    -   This method is the entry point when you do `python3 blackjack.py`.

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
