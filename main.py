from bot.bot import MyClient
from dotenv import load_dotenv
import discord
import os

def main():
    load_dotenv()
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(os.getenv('DISCORD_BOT_TOKEN'))

if __name__ == "__main__":
    main()
