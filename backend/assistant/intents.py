from commands import COMMANDS


def detect_intent(user_input):

    text = user_input.lower()

    for intent, phrases in COMMANDS.items():

        for phrase in phrases:

            if phrase in text:
                return intent

    return "unknown"