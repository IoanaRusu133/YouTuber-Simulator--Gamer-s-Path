import channel as ch
import scraping as sp
import random as rd

class Game:
    def __init__(self, title):
        self.title = title
        self.status = "Not owned"
        self.price = sp.games_dict[self.title][0]

    def buy_game(self, channel):
        if self.status == "Owned":
            print(f"You already own {self.title}!")
            return

        if channel.money >= self.price:
            channel.money -= self.price
            self.status = "Owned"
            channel.games.append(self) 
            print(f"You just bought {self.title} for {self.price}$! Have fun playing!")
        else:
            print(f"Insufficient funds! You need {self.price}$, but you only have {channel.money:.2f}$.")