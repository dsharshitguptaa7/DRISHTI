from brain import process_command

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    response = process_command(user)

    print("DRISHTI:", response)
