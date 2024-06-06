# Jodd - A Discord Bot

Jodd is a versatile Discord bot built using Python and the discord.py library. It offers a variety of commands, including fun activities, utilities, and information retrieval from different APIs.

## Features

- **Ping**: Check the bot's latency.
- **Bot Invite**: Get an invite link to add Jodd to your server.
- **Joke**: Fetch and display a random joke.
- **Bitcoin**: Display the current price of Bitcoin.
- **Ask**: Get responses to your questions.
- **Meme**: Fetch and display random memes from Reddit.
- **Clear**: Delete a specified number of messages in a channel.
- **Server Info**: Display information about the server.
- **Submit**: Submit answers and have them displayed by the bot.
- **Test**: Test button functionality in Discord.

## Installation

### Prerequisites

- Python 3.6+
- discord.py library
- aiohttp library

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Macret16/jodd-discord-bot.git
    cd jodd-discord-bot
    ```

2. **Install required libraries**:
    ```sh
    pip install discord.py aiohttp requests
    ```

3. **Update config file**:
    - Update the file `config.py` in the project directory.
    - Replace the placeholders with your actual values:
    ```python
    prefix = '!'  # or any other prefix you want
    token = 'YOUR_DISCORD_BOT_TOKEN'
    ownerid = 'YOUR_DISCORD_USER_ID'
    link = 'YOUR_BOT_INVITE_LINK'
    ```

4. **Run the bot**:
    ```sh
    python bot.py
    ```

## Usage

Once the bot is running, you can use the following commands in your Discord server:

- `!ping`: Shows the current ping of Jodd.
- `!botinvite`: Sends an invite link to your DMs to invite Jodd to another server.
- `!joke`: Displays a random joke.
- `!bitcoin`: Shows the current Bitcoin price.
- `!ask`: Responds to your questions with a random answer.
- `!meme`: Fetches and displays a random meme from Reddit.
- `!clear <amount>`: Deletes the specified number of messages in the channel (requires `manage_messages` permission).
- `!server`: Displays information about the server.
- `!submit <answers>`: Submits and displays your answers.
- `!test`: Sends a test button (currently not fully implemented).

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


Discord Bot Made By - Karan Jaswani
