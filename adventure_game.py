import time
import random


def print_pause(message):
    print(message)
    time.sleep(1)


def intro():
    print_pause("You wake up in the middle of the woods.")
    print_pause("There is an old men with you, he says:")
    print_pause("'Hello stranger, my name is Aaron, the wizard.'")
    print_pause("'I brought you here because I have something to offer you.'")
    print_pause("'I have with me two flowers.")
    print_pause("'The yellow flower will give you what you want "
                "the most in the world.'")
    print_pause("'The blue flower will give you what you need the most.'")
    print_pause("He opens his both hands, there is one flower in each hand.")


def flower_choice(items):
    print_pause("You understand that now is your time to choose.")
    flower = input("What is your choice:\n"
                   "1. Yellow\n"
                   "2. Blue\n"
                   "3. You run away from him.\n")
    if flower == '1':
        yellow_flower(items)
    elif flower == '2':
        blue_flower(items)
    elif flower == '3':
        run_away(items)
    else:
        print_pause("The man stares at you without saying any words.")
        print_pause("He probably did not understand your decision.")
        print_pause("After a while, he ask you again, "
                    "which flower would you like to pick.")
        flower_choice(items)


def yellow_flower(items):
    most_wanted = ['a big ice-cream', 'a pile of money',
                   'a 100% working, no errors, program']
    print_pause("'Well stranger, that is a good choice.'")
    print_pause("'To get what you want the most in the world all "
                "you need to do is to think on it while you hold "
                "tight the flower.'")
    print_pause("You then squeeze the flower thinking of"
                " what you want the most.")
    wanted_thing = random.choice(most_wanted)
    print_pause(f"Suddenly, {wanted_thing}"
                f" appears in front of you! UHU!")
    items.append("yellow flower")
    items.append(wanted_thing)
    gate(items)


def blue_flower(items):
    print_pause("In the moment you touch the blue flower, it starts to glow!")
    print_pause("You can feel the flower getting heavier.")
    print_pause("The flower is now a key!")
    print_pause("The man asks you if you would like to keep with your key,"
                " or have the opportunity the choose again.")
    key(items)


def key(items):
    message = input("What would you like to do?\n"
                    "1. Keep the key\n"
                    "2. Change your choice."
                    "\n")
    if message == '1':
        items.append('key')
        gate(items)
    elif message == '2':
        flower_choice(items)
    else:
        print_pause("Sorry, I don't understand you!")
        key(items)


def run_away(items):
    enemies = ['birds, foxes, and rabbits', 'trolls', 'angry fairies']
    enemy = random.choice(enemies)
    print_pause("You start to run, and you can see "
                "and hear that someone is following you.")
    print_pause(f"You look back and {enemy} "
                f"are all running after you!")
    if 'a big ice-cream' in items:
        print_pause("You remember of your ice-cream!")
        print_pause("You throw some ice-cream on them! "
                    "Now, you have more time to think!")
        items.remove('a big ice-cream')
        gate(items)
    elif 'a pile of money' in items:
        print_pause("You cannot believe in what your eyes are seeing!")
        print_pause("You try to throw some money in the air to distract them!")
        print_pause("It is working! But it will not work for long.")
        items.remove('a pile of money')
        gate(items)
    elif 'a 100% working, no errors, program' in items:
        print_pause("Oh no! First the wizard now you are being chased!")
        print_pause("You just want to go back home!")
        print_pause("Nothing that you have will help you now.")
        print_pause(f"You got caught by {enemy}! Better luck next time!")
        play_again()
    else:
        gate(items)


def gate(items):
    print_pause("You look around and see something distant"
                " it seems to be a gate! It is your way out!")
    print_pause("You run to the gate and try to open it,"
                " but the door seems to be locked!")
    if "key" in items:
        print_pause("But wait! You have a key!")
        final_chapter()
    else:
        print_pause("Then the old men appears, like magic, in front of you.")
        print_pause("'Hey stranger, you did\'t think it would be that easy,"
                    " did you?'")
        if "yellow flower" in items:
            print_pause("To get what you need you will have to "
                        "give me back my yellow flower!")
            exchange_flower(items)
        else:
            print_pause("'To leave the forest you need to make your choice "
                        "wisely.'")
            flower_choice(items)


def exchange_flower(items):
    print_pause("Now you understand! It is a trap!")
    print_pause("Unless you give up of the yellow flower "
                "you will stay in the forest forever!")
    message = input("What now?! Will you give the yellow flower "
                    "back to the man? Please say 'yes' or 'no'?\n").lower()
    if message == 'no':
        print_pause("You decided to keep what you wanted the most!")
        print_pause("Now you will be trapped in the woods forever!")
        play_again()
    elif message == 'yes':
        print_pause("'Very good, I'm happy to take my yellow flower back.'")
        print_pause("The old man then open his hands. "
                    "And you see the two flowers again.")
        items.remove("yellow flower")
        flower_choice(items)
    else:
        print_pause("Sorry, I don't understand. Let's try again.")
        exchange_flower(items)


def final_chapter():
    print_pause("In the moment you insert the key in the gate,"
                " all your world starts to spin!")
    print_pause("You are dizzy and you feel like floating!")
    print_pause("You faint.")
    print_pause("When you wake up you are in your bed. "
                "It is 7am. Your alarm is ringing.")
    print_pause("Congrats! You just escaped the magic woods!")
    play_again()


def play_game():
    items = []
    intro()
    flower_choice(items)


def play_again():
    message = input("Would you like to play again? "
                    "Please say 'yes' or 'no'?\n").lower()
    if message == 'no':
        print("See you then!")
    elif message == 'yes':
        print("Let's play!")
        play_game()
    else:
        play_again()


if __name__ == "__main__":
    play_game()
