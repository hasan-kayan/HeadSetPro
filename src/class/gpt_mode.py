class gpt_mode:
    def __init__(self, mode, mode_name, mode_description, system_message):
        self.mode = mode
        self.mode_name = mode_name
        self.mode_description = mode_description
        self.system_message = system_message

    def get_mode(self):
        return self.mode

    def get_mode_name(self):
        return self.mode_name

    def get_mode_description(self):
        return self.mode_description

    def set_mode(self, mode):
        self.mode = mode

    def set_mode_name(self, mode_name):
        self.mode_name = mode_name

    def set_mode_description(self, mode_description):
        self.mode_description = mode_description

    def __str__(self):
        return "mode: " + str(self.mode) + ", mode_name: " + str(self.mode_name) + ", mode_description: " + str(self.mode_description)

    def __repr__(self):
        return "mode: " + str(self.mode) + ", mode_name: " + str(self.mode_name) + ", mode_description: " + str(self.mode_description)

    def __eq__(self, other):
        if isinstance(other, gpt_mode):
            return self.mode == other.mode and self.mode_name == other.mode_name and self.mode_description == other.mode_description
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def get_system_message(self):
        return self.system_message