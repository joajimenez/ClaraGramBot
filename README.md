# Telegram Bot - Clarabot

This is a Python Telegram bot named Clarabot. Clarabot is a fun and interactive bot that can perform various tasks, including answering yes or no questions, sharing cat and dog images, providing random messages, and even suggesting a beer for you. Additionally, it can respond to the command 'sentido_de_la_vida' with a humorous error code.

## Prerequisites

Before using Clarabot, you need to set up a few things:

1. Create a `.env` file to store your Telegram API token. The file should contain the following line:
   ```
   TELEGRAM_API_TOKEN=your_bot_token_here
   ```

2. Install the required Python libraries. You can do this by running:
   ```
   pip install python-telegram-bot
   ```

3. Make sure you have the `decider`, `cat`, `dog`, and `beers` modules in your project directory, providing the required functions as shown in the script.

## Getting Started

To use Clarabot, follow these steps:

1. Start a chat with Clarabot on Telegram.

2. Send one of the following commands to Clarabot:

   - `/start`: Start a conversation with Clarabot.

   - `/yesno`: Get a yes or no answer from Clarabot.

   - `/clara_klk`: Get a random message from Clarabot.

   - `/misu`: Receive a cute cat picture from Clarabot.

   - `/firulais`: Receive an adorable dog picture from Clarabot.

   - `/sentido_de_la_vida`: Request the meaning of life (humorously answered with "Error code: 42").

   - `/cerveza`: Get a beer recommendation from Clarabot.

## Features

### 1. Start Command
- `/start`: Initiates a conversation with Clarabot. It responds with a greeting message.

### 2. Yes or No Command
- `/yesno`: Clarabot answers yes or no questions with a random animation.

### 3. Random Message Command
- `/clara_klk`: Clarabot shares a random message from its collection.

### 4. Cat Picture Command
- `/misu`: Clarabot sends a cute cat picture.

### 5. Dog Picture Command
- `/firulais`: Clarabot shares an adorable dog picture.

### 6. Meaning of Life Command
- `/sentido_de_la_vida`: Clarabot humorously responds with "Error code: 42" to the meaning of life query.

### 7. Beer Recommendation Command
- `/cerveza`: Clarabot recommends a beer along with its image, name, description, and food pairing.

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to modify and extend the bot according to your needs.

## Acknowledgments

This Telegram bot was created using the [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/) library. Special thanks to the authors and contributors of the library.

## Author

[Joan Jimenez](https://joanjimenez.me/)

If you have any questions or suggestions for Clarabot, feel free to reach out. Enjoy using Clarabot!
