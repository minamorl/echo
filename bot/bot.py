from discord import Client
from helpers.gpt4all_helper import GPT4AllHelper

class MyClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpt_helper = GPT4AllHelper("ggml-gpt4all-l13b-snoozy")
        self.messages = [{"role": "user", "content": "You are a discord bot"}]

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('/chatgpt'):
            user_message = message.content[9:]
            result = self.gpt_helper.chat_completion(user_message)
            await message.channel.send(result)
