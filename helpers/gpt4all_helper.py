import asyncio
import concurrent.futures
from gpt4all import GPT4All

class GPT4AllHelper:
    def __init__(self, model_name):
        self.gpt = GPT4All(model_name)
        self.messages = []
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    async def chat_completion(self, user_message):
        # Check if the user_message is the reset command
        if user_message.strip() == '/chatgpt reset':
            self.messages = []
            return "Conversation reset."

        self.messages.append({"role": "user", "content": user_message})
        
        # Run the blocking operation in a separate thread
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            self.executor,
            self.gpt.chat_completion,
            self.messages
        )

        assistant_message = result['choices'][0]['message']['content']
        self.messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message