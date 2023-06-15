from gpt4all import GPT4All

class GPT4AllHelper:
    def __init__(self, model_name):
        self.gpt = GPT4All(model_name)
        self.messages = [{"role": "user", "content": "You are a discord bot"}]

    def chat_completion(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        result = self.gpt.chat_completion(self.messages)
        assistant_message = result['choices'][0]['message']['content']
        self.messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message
