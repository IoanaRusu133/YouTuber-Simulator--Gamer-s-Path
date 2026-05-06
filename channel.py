import random as rd

class Channel:
    def __init__(self, name, subscribers, likes, views, money, games, pc):
        self.name = name
        self.subscribers = subscribers
        self.likes = likes
        self.views = views
        self.money = money
        self.games = games  
        self.pc = pc      

    def post_video(self, mini, maxi, bonus):
        s_base = rd.randint(mini, maxi)
        s = int(s_base * (1 + bonus) + (self.subscribers * 0.02))
        
        active_subs = self.subscribers * rd.uniform(0.2, 0.5)
        v_base = active_subs + (s * 2) + rd.randint(mini * 5, maxi * 5)
        v = int(v_base * (1 + bonus))
        
        l_base = v * rd.uniform(0.05, 0.1)
        l = int(l_base * (1 + bonus))

        self.subscribers += s
        self.likes += l
        self.views += v
    
        print(f"Your video gained: {s} subscribers, {l} likes and {v} views!")
        
        m = v / 100
        self.money += m
        print(f"+ {m:.2f}$")

    def add_money(self, money):
        self.money += money
        print(f"+ {money}$")