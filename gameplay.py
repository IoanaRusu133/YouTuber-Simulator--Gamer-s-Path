import scraping as sp
import game as gm
import pc as cp
import channel as ch
import random
import time

permanent_bonus = 0.0
temporary_bonus = 0.0
posted_videos = [] 
sample = []        
event_triggered = 0
take_break = 0

youtubers = [
    "MrBeeston", "PewDewPie", "Logan Powl", "Jake Pawl", 
    "James Charlies", "MarkyPlyer", "JackSepticEyee", 
    "SSSniperWulfy", "Vlad Campeanu", "Iraphaell", 
    "MaxInfinity", "Noaptea Devreme", "Bodrin Cradea", 
    "IHATEBLUE", "AlexVortexRO", "MaraDaily", 
    "NoScopeNicu", "ShadowDani", "TurboTeo", 
    "RaduReacts", "BlazeNova", "EchoStorm", 
    "ViralViper", "NeonRift", "QuantumKai", 
    "SkylineJade", "HexaHunter", "NovaPulse", 
    "CrimsonByte", "GlitchMaverick", "FrostyZen", 
    "PixelPhantom", "SolarFlareX", "CyberNinja", "AlphaOrbit"
]
def trending():
    global sample
    print("Trending this week:\n")
    sample = random.sample(list(sp.games_dict.items()), 5)
    for item in sample:
        print(f"- {item[0]}")

def day_choice(day,week):
    choice = int(input(f"""Day {day}, Week {week}:
                    1 -> Post video.
                    2 -> See stats.
                    3 -> View your games.
                    4 -> View your PC.
                    5 -> Shop
                    6 -> Check week's trending
                    7 -> Go to sleep (next day)."""))
    return choice

def buy_game(choice, your_channel):
    titles = list(sp.games_dict.keys())

    while choice != 0:
        if 1 <= choice <= len(titles):
            title = titles[choice - 1]
        
            owned_titles = [g.title for g in your_channel.games]
            if title in owned_titles:
                print(f"You already own {title}!")
            else:
                obj = gm.Game(title)
                obj.buy_game(your_channel)
        else:
            print("Invalid selection!")

        choice = int(input("\nWhat else would you like to buy? (Write 0 to go back to shop menu): "))

    print("Returning to main shop...")

def buy_component(choice, your_channel):
    global permanent_bonus
    obj = your_channel.pc

    if choice == 1:

        if obj.component['GPU'] == 4:
            print("Can't upgrade anymore!")
        else:
            permanent_bonus += 0.2
            price = 40 * obj.component['GPU']
            obj.upgrade(your_channel, price, "GPU", 0.2)
    
    elif choice == 2:

        if obj.component['CPU'] == 4:
            print("Can't upgrade anymore!")
        else:
            permanent_bonus += 0.15
            price = 30 * obj.component['CPU']
            obj.upgrade(your_channel, price, "CPU", 0.15)
    
    elif choice == 3:

        if obj.component['RAM'] == 4:
            print("Can't upgrade anymore!")
        else:
            permanent_bonus += 0.1
            price = 20 * obj.component['RAM']
            obj.upgrade(your_channel, price, "RAM", 0.1)
    
    elif choice == 4:

        if obj.component['microphone'] == 4:
            print("Can't upgrade anymore!")
        else:
            permanent_bonus += 0.05
            price = 10 * obj.component['microphone']
            obj.upgrade(your_channel, price, "microphone", 0.05)
    
    shop(your_channel)

def shop(your_channel):
    n = int(input("What are you interested in buying?\n1 - Games\n2 - Upgrade PC"))
    
    if n == 1:
        shop_games = {}
        titles = list(sp.games_dict.keys())
        owned_titles = [g.title for g in your_channel.games]
        for x in range(1,21):
            title = titles[x-1]
            if title not in owned_titles:
                shop_games[x] = title
        print("Choose a game:")
        for x in sorted(shop_games.keys()): 
            game_name = shop_games[x]
            price = sp.games_dict[game_name][0]
            print(f"{x} - {game_name} ({price}$)")
            
        print(f"Money: {your_channel.money:.2f}$")
        
        choice = int(input("What game would you like to buy? Write 0 if you wanna go back to main shop."))
        
        if choice == 0:
            shop(your_channel)
        else:
            buy_game(choice, your_channel)
    
    elif n == 2:
        gpu_lvl = your_channel.pc.component['GPU']
        cpu_lvl = your_channel.pc.component['CPU']
        ram_lvl = your_channel.pc.component['RAM']
        mic_lvl = your_channel.pc.component['microphone']

        print(f"""Your PC:
        GPU: {gpu_lvl if gpu_lvl < 4 else 'MAX'} {f'-> {40 * gpu_lvl}$, +0.2 BONUS' if gpu_lvl < 4 else ''}
        CPU: {cpu_lvl if cpu_lvl < 4 else 'MAX'} {f'-> {30 * cpu_lvl}$, +0.15 BONUS' if cpu_lvl < 4 else ''}
        RAM: {ram_lvl if ram_lvl < 4 else 'MAX'} {f'-> {20 * ram_lvl}$, +0.1 BONUS' if ram_lvl < 4 else ''}
        Microphone: {mic_lvl if mic_lvl < 4 else 'MAX'} {f'-> {10 * mic_lvl}$, +0.05 BONUS' if mic_lvl < 4 else ''}""")        
        choice = int(input("Which one do you want to upgrade?\n1 - GPU\n2 - CPU\n3 - RAM\n4 - Microphone")) 
        while choice > 4:
            print("Invalid choice!")
            choice = int(input("Which one do you want to upgrade?\n1 - GPU\n2 - CPU\n3 - RAM\n4 - Microphone")) 
        else:
            buy_component(choice, your_channel)

def same_video_event():
    global temporary_bonus
    temporary_bonus -= random.uniform(0.01, 0.1)

def popular_video(week):
    global temporary_bonus
    temporary_bonus += 0.3

def collab_event():
    global temporary_bonus
    n = int(input("Do you accept?\n1 - Yes\n2 - No"))
    if n == 1:
        l = [1,2,3]
        random_choice = random.choice(l)
        if random_choice == 1:
            print("People hated it. -0.05 on all stats for this video")
            temporary_bonus -= 0.05
        else:
            print("People liked it! +0.05 on all stats for this video!")
            temporary_bonus +=0.05
    else:
        print("You declined the collaboration.")

def cancel_event(your_channel):
    global take_break, temporary_bonus
    n = int(input("What do you do?\n1 - Apologize sincerely\n2 - Fake apology\n3 - Deny everything!"))
    l = [1,2,3]
    random_choice = random.choice(l)

    if n == 1:
        if random_choice == 1:
            print("They didn't believe it, but let it slide. -0.15 on all stats for this video")
            temporary_bonus -= 0.15
        else:
            print("They seem to understand and support you. -0.05 on all stats for this video.")
            temporary_bonus -= 0.05
    elif n == 2:
        if random_choice == 1:
            print("They didn't buy it and now some hate you. half of them unsubscribed and I suggest you take a break for a while...")
            your_channel.subscribers = int(your_channel.subscribers // 2)
            take_break = 1
        else:
            print("They seem to believe you... Mostly... -0.25 on all stats for this video.")
            temporary_bonus -= 0.25
    else:
        print("They didn't buy it and now some hate you. half of them unsubscribed and I suggest you take a break for a while...")
        your_channel.subscribers = int(your_channel.subscribers // 2)
        take_break = 1

def partner_event():
    global temporary_bonus
    l = [1,2,3]
    random_choice = random.choice(l)
    if random_choice == 1:
        print("They are on their side. They think you're an a**hole. - 0.15 on all stats.")
        temporary_bonus -= 0.15
    elif random_choice == 2:
        print("They don't care.")
    else:
        print("They pity and support you! + 0.15 on all stats for this video.")
        temporary_bonus += 0.15

def check_event(week, your_channel):
    global event_triggered, temporary_bonus
    random_chance = random.randint(1, 100)
    if random_chance <= 40:
        if week == 1:
            if random_chance <= 20:
                print("Massive hate!\nBOOOO! People hate you! -0.5 on all stats for this video")
                temporary_bonus -= 0.5  
            else:
                print("Future star!\nPeople love you. But will they always? +0.5 on all stats for this video")
                temporary_bonus += 0.5  
        elif week == 2:
            if random_chance <= 15:
                print("'Why is this guy still trying?'\nPeople don't really like you... - 0.25 on all stats for this video.")
                temporary_bonus -= 0.25
            elif random_chance <= 30:
                print("'Remember me when you're famous!'\nYour fanbase is getting strong! +0.5 on all stats for this video")
                temporary_bonus += 0.5
            else:
                print("A bigger youtuber talked about you on their Twitch livestream!\n+0.1 on all stats for this video")
                temporary_bonus += 0.1
        else:
            if random_chance <= 10:
                print("You've been cancelled :(")
                cancel_event(your_channel)
            elif random_chance <= 20:
                print("A bigger youtuber talked about you on their Twitch livestream!\n+0.1 on all stats for this video")
                temporary_bonus += 0.1
            elif random_chance <= 30:
                youtuber = random.choice(youtubers)
                print(f"{youtuber} wants to collaborate!")
                collab_event()            
            else:
                print("Your partner broke up with you. Share it with the subscribers?")
                partner_event()
        event_triggered = 1

def post_video(day,week, your_channel):
    global temporary_bonus, sample, event_triggered
    
    dict_your_games = {}
    for i in range(1, len(your_games) + 1):
        dict_your_games[i] = your_games[i - 1].title

    print(f"Your games: {dict_your_games}")
    n = int(input("What do you want to post?"))
    if n in dict_your_games:
        chosen_game = dict_your_games[n]
        print(f"You want to post {chosen_game}.")
        if len(posted_videos) > 0:
            if posted_videos[-1] == chosen_game:
                print("People will get bored seeing the same game...")
                same_video_event()
        posted_videos.append(chosen_game)

        trending = [item[0] for item in sample]
        if chosen_game in trending:
            popular_video(week)
    
        print("Recording...")
        time.sleep(random.randint(3,7))
        print("Editing...")
        time.sleep(random.randint(3,7))
        print("Posting...")
        time.sleep(random.randint(1,5))
        print("Posted!")

        if event_triggered == 0:
            check_event(week, your_channel)

        bonus = permanent_bonus + temporary_bonus
        your_channel.post_video(1, (week*day) * 100,bonus)
    
        temporary_bonus = 0
    
    else:
        print("Invalid choice.")
        post_video(day, week, your_channel)

def check_subscribers(username, your_channel):
    global achievement1, achievement2, achievement3, permanent_bonus

    if your_channel.subscribers >= 1000000 and achievement3 == 0:
        
        print(f"""New email!
              Hello, @{username}! Team YouTube here! We reached for you to congratulate on gaining the supercalifragilisticexpialidoucious sum of {your_channel.subscribers} subscribers!
              In the following days you will be delivered the Diamond Button (don't sell it, please. It's not real diamond)! Congratulations!!!!
              +0.3 BONUS on all videos from this point!""")
        achievement3 = 1
        permanent_bonus += 0.3
        print(f"""New email!
              OMMGGGGG @{username}!!!! NOT EVEN I MADE IT!!!!!!!!!!!!! JEALOUS FR!!!!! 
              Signed, Vikt0r""")

    elif your_channel.subscribers >= 100000 and achievement2 == 0:
        print(f"""New email!
              Hello, @{username}! Team YouTube here! We reached for you to congratulate on gaining the sum of {your_channel.subscribers} subscribers!
              In the following days you will be delivered the Gold Button (don't sell it, please. It's not real gold)! Congratulations!!!!
              +0.2 BONUS on all videos from this point!""")
        achievement2 = 1
        permanent_bonus += 0.2
        print(f"""New email!
              Hiii, @{username}! You did it! Congrats!!!!!!!!!! Should I be afraid you're gonna take my "YouTube king" title?? haha jk
              Signed, Vikt0r""")
    
    elif your_channel.subscribers >= 10000 and achievement1 == 0:
        
        print(f"""New email!
              Hello, @{username}! Team YouTube here! We reached for you to congratulate on gaining the sum of {your_channel.subscribers} subscribers!
              In the following days you will be delivered the Silver Button! Congratulations!!!!
              +0.1 BONUS on all videos from this point!""")
        achievement1 = 1
        ok1 = 0
        permanent_bonus += 0.1
        print(f"""New email!
              Hello, @{username}! I was so happy to see you reached the first milestone in your gaming career!
              Oh, I remember the time when I reached my first 10k... Back when Minecraft was still popular ig. Anyway, keep it up!!!
              Signed, Vikt0r!""")
        
def start(username):
    global take_break, your_games, posted_videos, event_triggered, sample, achievement1, achievement2, achievement3
    achievement3 = 0
    achievement2 = 0
    achievement1 = 0

    week = 1

    first_game = random.choice(list(sp.games_dict.keys()))
    first_game_obj = gm.Game(first_game)
    first_game_obj.status = "Owned"
    your_games = [first_game_obj]
    your_pc = cp.PC()
    your_channel = ch.Channel(username, 0, 0, 0, 0, your_games, your_pc)

    while week != 5:

        print(f"Week {week}")
        posted_videos = []
        event_triggered = 0
        trending()

        for day in range(1,6):

            if week == 1 and day == 2:
                print(f"""New email!
                      Hello, {username}! I am glad to see another YouTuber that enjoys having people watch them play games... Lovely.
                      My name is Victor (or you might know me as Vikt0r, my YouTuber username) and I have been posting on YouTube for a few years now, so I know my way around.
                      I see your first video wasn't really... succesfull. Well, that's normal! Here are some tips and tricks that might help you!
                      - Follow the trends! People like to watch games that are popular. Follow weekly trends and you will become the next one!
                      - Don't exaggerate! We don't enjoy watching the same thing over and over again. Try to be diverse with your videos.
                      - Keep up with the technology! Your subscribers will not appreciate a laggy video or a microphone that makes you seem like you're in a cave.
                      - BE CAREFUL WITH WHAT YOU SAY! If it's on the Internet, it stays there! Always choose your words carefully.
                      I think that's all... I can't wait to watch more of your videos :)
                      PS. I sent a little welcome gift on PayPal. Use it wisely!
                      PPS. I also told my subscribers about you so a few might come check your channel.
                      + 50$
                      """)
                your_channel.add_money(50)
                gift_subs = random.randint(1,50)
                print(f"+{gift_subs} new subscribers!")
                your_channel.subscribers += gift_subs

            check_subscribers(username, your_channel)

            day_over = False

            while not day_over:

                choice = day_choice(day, week)

                if choice == 1:

                    post_video(day,week, your_channel)
                    print("Going to sleep...")
                    day_over = True

                elif choice == 2:

                    print(f"""Subscribers: {your_channel.subscribers}
                          Views: {your_channel.views}
                          Likes: {your_channel.likes}
                          Money: {your_channel.money}$""")

                elif choice == 3:

                    titles = [g.title for g in your_channel.games]
                    print(f"Your games: {titles}")

                elif choice == 4:

                    gpu = your_channel.pc.component["GPU"]
                    cpu = your_channel.pc.component["CPU"]
                    ram = your_channel.pc.component["RAM"]
                    mic = your_channel.pc.component["microphone"]

                    print(f"GPU: {gpu if gpu < 4 else 'MAX'}")
                    print(f"CPU: {cpu if cpu < 4 else 'MAX'}")
                    print(f"RAM: {ram if ram < 4 else 'MAX'}")
                    print(f"Mic: {mic if mic < 4 else 'MAX'}")

                elif choice == 5:

                    shop(your_channel)

                elif choice == 6:

                    for item in sample:
                        print(f"- {item[0]}")

                elif choice == 7:

                    print("Going to sleep...")
                    day_over = True

                else:

                    print("Invalid choice!")

            if take_break == 1:
                take_break = 0 
                break
       

        week += 1

    return your_channel