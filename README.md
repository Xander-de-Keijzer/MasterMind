## MasterMind
#### AI Project HU
___
> How to play

The game is played with 6 colors and guess contains 4 colors.
Before the game starts a random secret is chosen made of 4 colors.
A game is played by making guesses until the colors of the guess match the secret code. A maximum of 10 guesses can be made before the game is 'lost'.
Each guess will result in an answer that consists of any amount of white and black colors, each white color represents a guessed color that is in the secret but not in the right position and each black color represents a guessed color in the right position.

- **Run Game.py**
- Choose **Play** or **Watch**
- Play:
  - The game will choose a random secret
  - The user can make a maximum of 10 guesses to find the secret
  - Every guess will result in 0 to 4 black and white answer colors given by the game
  - The user has to figure out the secret using the information from each answer
- Watch:
  - The user will choose a random secret
  - An AI will make a maximum of 10 guesses to find the secret
  - The game will generate the 0 to 4 black and white answer colors
  - The AI will try to figure out what the secret is