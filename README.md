# MyPetBot

MyPetBot is a Telegram bot that allows users to take care of a virtual pet. The bot is written in Python using the aiogram library for Telegram Bot API.

## About the Project

The project is structured around three main files:

- `main.py`: This is the main script that handles the bot's interactions with the user. It uses the aiogram library to listen for and respond to user messages. It also maintains a dictionary of Pet and Player objects for each user.

- `pet.py`: This file defines the Pet class. Each Pet object has properties for hunger, dirtiness, boredom, and sleepiness, which are all initially set to 0. The Pet class also includes methods for feeding, bathing, playing with, and putting the pet to sleep, as well as a method to update the pet's status.

- `player.py`: This file defines the Player class. Each Player object has an id, a score, and a game_started flag. The Player class also includes methods for starting the game and updating the player's score.

## How It Works

When a user starts a conversation with the bot, a new Pet and Player object are created for that user. The user can then interact with their pet by sending commands to feed, bathe, play with, or put their pet to sleep. The bot responds to these commands by calling the appropriate method on the user's Pet object and sending a message back to the user.

The bot also periodically sends notifications to the user with the current status of their pet. The status includes the pet's health, hunger, dirtiness, boredom, and sleepiness levels.

## How to Run the Project

1. Install the required Python packages by running `pip install -r requirements.txt`.
2. Set your Telegram Bot API token in the `config.py` file.
3. Run the `main.py` script to start the bot.
