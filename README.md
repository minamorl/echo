# Echo

Echo is an advanced Discord bot using gpt4all
## Getting Started
### Prerequisites

- A valid Discord account and server
- Python 3.10 or later installed on your system
- Poetry, a Python dependency management tool

## Installation

To set up Echo on your Discord server, follow these steps:

1. Clone this repository.

2. Install the necessary Python dependencies using Poetry. In your terminal, navigate to the project's root directory and run poetry install.

3. Create a .env file in your project root. This is where you'll store environment-specific variables, such as your Discord bot token. Your .env file might look something like this:

 `.env`
```sh
DISCORD_BOT_TOKEN=your-discord-token
```
Make sure to replace your-discord-token with your actual Discord bot token.

To start the bot, activate the poetry environment by typing poetry shell into the terminal, and then start the bot using the main python file (typically something like python main.py).

Remember to keep your .env file private and never commit it to your public repository, as it contains sensitive information.

## Contributing

Your contributions are always welcome! Please take a look at our contribution guidelines first.

## License

Echo is under the MIT license. See the LICENSE file for more details.
