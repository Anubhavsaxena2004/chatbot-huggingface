# chat_memory.py
class ChatMemory:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.buffer = []

    def add_turn(self, user, bot):
        self.buffer.append((user, bot))
        # Maintain window size
        if len(self.buffer) > self.window_size:
            self.buffer = self.buffer[-self.window_size:]

    def get_context(self):
        context = ""
        for user, bot in self.buffer:
            context += f"User: {user}\nBot: {bot}\n"
        return context

    def clear(self):
        self.buffer.clear()