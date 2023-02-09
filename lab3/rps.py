import random

class Rps:
    choices = ("rock", "paper", "scissors")
    inferior_choice_of = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    def __init__(self, player1: "RpsPlayer", player2: "RpsPlayer") -> None:
        self.player1 = player1
        self.player2 = player2

    def print_choices(self) -> None:
        print(f"{self.player1.name} chose {self.player1.choice}")
        print(f"{self.player2.name} chose {self.player2.choice}")

    def get_winner(self):
        if self.player2.choice == self.inferior_choice_of[self.player1.choice]:
            return self.player1
        elif self.player1.choice == self.inferior_choice_of[self.player2.choice]:
            return self.player2
        else:
            return None

class RpsPlayer:
    def __init__(self, name, choice) -> None:
        self.name = name
        self.choice = choice

    @property
    def choice(self):
        return self._choice

    @choice.setter
    def choice(self, choice):
        if choice not in Rps.choices:
            raise ValueError("Invalid choice")
        self._choice = choice

    def get_new_choice(self):
        while True:
            try:
                self.choice = input("Enter choice (rock|paper|scissors): ")
            except ValueError:
                continue
            else:
                break

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        player = cls(name, "rock") # initialize with temp choice
        player.get_new_choice()

        return player


def main():
    user = RpsPlayer.get()
    while True:
        bot = RpsPlayer("Bot", random.choice(Rps.choices)) # spawn bot

        #Instantiate game
        rps = Rps(user, bot)
        rps.print_choices()

        # Evaluate winner of game
        winner = rps.get_winner()
        if winner == None:
            print("* Tie game *")
        else:
            print(f"* {winner.name} won! *")

        print("")

        user.get_new_choice()

if __name__ == "__main__":
  main()
