from mycroft import MycroftSkill, intent_file_handler


class Pizza(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pizza.intent')
    def handle_pizza(self, message):
        self.speak_dialog('pizza')


def create_skill():
    return Pizza()

