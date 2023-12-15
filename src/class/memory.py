# Creation date: 30-03-2020
# Created by Hasan Kayan

class chat_memory:
    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.memory = {}

    def get(self, key):
        return self.memory.get(key)

    def set(self, key, value):
        self.memory[key] = value
        return True

    def delete(self, key):
        if key in self.memory:
            del self.memory[key]
            return True
        else:
            return False

    def clear(self):
        self.memory = {}
        return True

    def get_all(self):
        return self.memory

    def get_keys(self):
        return self.memory.keys()

    def get_values(self):
        return self.memory.values()

    def get_items(self):
        return self.memory.items()

    def get_length(self):
        return len(self.memory)

    def get_chat_id(self):
        return self.chat_id

    def get_memory(self):
        return self.memory

    def set_memory(self, memory):
        self.memory = memory
        return True

    