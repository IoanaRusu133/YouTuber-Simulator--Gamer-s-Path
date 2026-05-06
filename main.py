import scraping as sp
import game as gm
import pc as cp
import channel as ch
import gameplay as gmp

def choose(x, current_username):
    global username
    if x == "1":
        return gmp.start(current_username)
    elif x == "2":
        new_username = input("New username: @")
        username = new_username
        return gmp.start(username)
    else:
        while x not in ["1", "2"]:
            x = input("Choose between 1 and 2: ")
        return choose(x, current_username)

print("--- Create a channel! ---")
name = input("Name: ")
username = input("@")
print(f"Ready, @{username}?\n 1 - Yes\n 2 - I wanna change my username")
choice = input("Pick a choice: ")

final_channel = choose(choice, username)

print(f"""
---------------------------------------
Let's see how far you made it...
@{username}, you have:
{final_channel.subscribers} subscribers,
{final_channel.money:.2f} money,
{final_channel.likes} likes,
{final_channel.views} views,
{len(final_channel.games)} games owned.
---------------------------------------
""")

if gmp.achievement3 == 1:
    print("ACHIEVEMENT UNLOCKED: GAMING GOD")
elif gmp.achievement2 == 1:
    print("ACHIEVEMENT UNLOCKED: INTERNATIONAL LEGEND")
elif gmp.achievement1 == 1:
    print("ACHIEVEMENT UNLOCKED: NATIONAL LEGEND")

print("\nThanks for playing!")