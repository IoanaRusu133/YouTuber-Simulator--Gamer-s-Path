import channel as ch

class PC:
    def __init__(self):
        self.component = {
            "GPU" : 1,
            "CPU" : 1,
            "RAM" : 1,
            "microphone" : 1
        }

    def upgrade(self, channel, price, name, bonus):

        if self.component[name] >= 4:
            print(f"Your {name} is already at MAX level!")
            return

        if channel.money >= price:
            self.component[name] += 1
            channel.money -= price
            level = self.component[name]
            print(f"You upgraded your {name} to level {level if level < 4 else 'MAX'}!")
            print(f"+ {bonus} stats for future videos!")
        else:
            print(f"Insufficient funds! You need {price}$, but you only have {channel.money:.2f}$.")