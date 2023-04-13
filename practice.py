import random

def magic_8_ball():
    responses = ["um, prolly not.", "I mean, maybe I dunno.", "Definitely not.",
                 "Not very confident in that.", "Absolutely not.", "That's it! Me. You. Parking Lot. Now!",
                 "Most improbable.", "Outlook bad.", "Nope.",
                 "Reply hazy, just give up.", "You are you?.", "Hutch said no, you're hopeless.",
                 "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
                 "My reply is no.", "My sources say no.", "Outlook not so good.",
                 "Very doubtful."]
    print("Welcome to the Magic 8 Ball! Ask your question:")
    question = input("> ")
    print("Processing...")
    answer = random.choice(responses)
    print(answer)

magic_8_ball()

