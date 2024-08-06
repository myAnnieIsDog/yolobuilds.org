import argparse
import random
import time


def main():
    parse()

def parse():
    global_parser = argparse.ArgumentParser(
        prog="spd",
        description="Play 'Paper-Rock-Scissors' using a Command Line Interface.",
        # usage="",
        epilog="By Scott Paul Doolittle 2024",
    )
    subparsers = global_parser.add_subparsers(
        title="subcommands",
    )

    prs_parser = subparsers.add_parser(
        "prs", help="A class game of Paper Rock Scissors."
    )
    prs_parser.add_argument(dest="prs", help="A class game of Paper Rock Scissors.")
    prs_parser.set_defaults(func=prs)

    two_parser = subparsers.add_parser("two", help="The 'other' game.")
    two_parser.add_argument(dest="two", help="The 'other' game.")
    two_parser.set_defaults(func=two)

    args = global_parser.parse_args()

    print(args)


def prs(p1:dict):
    # p1 = parser.parse_args()
    ai = ai_choices()

    print(p1)
    print(ai)


    def ai_choices():
        ai = {}
        ai["go"] = choice()
        ai["juke"] = choice()
        ai["react"] = react(25)
        return ai



    def choice(self):
        return random.choice(["paper", "rock", "scissors"])

    def react(self, n):
        if n > random.randrange(1, 100):
            return True
        return False
    
    def win():
        a = random.choice(["YOU WIN!!!", "you lose :(", "You won, but I think you cheated.","I'm going to cry myself to sleep now. I quit."])
        return a

    def lose():
        a = random.choice(["better luck next time, my friend", "you lose :(", "Haha you lost you little bitch!",])
        return a
    
    def drama(p1:dict, ai:dict):
        # Adding drama...
        print("The computer is anticipating your every move...")
        time.sleep(1)

        if p1.juke:
            print(f"You start to make {p1.juke}...")
            time.sleep(1)

        print(f"The computer is starting to make {ai["juke"]}...")
        time.sleep(1)

        if p1.React:
            print(f"Yes, you react and change your move to {choice()}...")
        else:
            print(f"You stick with {p1.go}")
            time.sleep(1)

        if ai["react"]:
            print("The computer is changing to...")
            time.sleep(1)

            ai["go"] = choice()
            print(f"{str(ai["go"]).capitalize()}!!!")
        return "Paper Rock Scissors"


def two():
    return "Alternative"


if __name__ == "__main__":
    main()
