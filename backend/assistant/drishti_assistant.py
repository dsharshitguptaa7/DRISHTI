from brain import process_command
from voice_input import listen
while True:

    user = listen()

    if user.lower() == "exit":
        break

    response = process_command(user)

    print("DRISHTI:", response)
