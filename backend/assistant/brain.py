from intents import detect_intent
from vision import run_vision

def process_command(command):

    intent = detect_intent(command)

    if intent == "vision":
        return run_vision()

    elif intent == "read":
        return "Launching OCR module"

    elif intent == "currency":
        return "Launching currency module"

    elif intent == "shopping":
        return "Launching shopping module"

    return "Sorry, I did not understand."