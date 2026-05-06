# 🎮 YouTuber Simulator: Gamer's Path

A strategic career simulation game built in **Python** for the **Cisco Academy: Python 101** course.

## 📝 Description
**YouTuber Simulator: Gamer's Path** puts you in the shoes of an aspiring content creator. Your goal? Navigate the complex world of gaming trends, manage your finances, and upgrade your setup to reach the ultimate status: **Gaming God**. 

The game combines real-world data with survival mechanics, where one viral hit can make you, and one "cancel" event can break you.

---

## ✨ Key Features

*   **📈 Real-Time Market Scraping:** Uses web scraping to fetch the most popular games and current prices directly from **Steam**.
*   **💻 Hardware Progression:** Earn revenue to upgrade your PC components. Better gear reduces editing time and boosts video quality.
*   **🎭 Random Event System:** 
    *   **Success:** Viral hits, shoutouts, and collaborations.
    *   **Drama:** Hate waves and the dreaded **CANCEL** events that can ruin your reputation.
*   **⏳ Realistic Workflow:** Integrated `time` module mechanics simulate the grind of filming, editing, and uploading.
*   **🏗️ OOP Architecture:** Robust Object-Oriented Programming structure to manage the Channel, PC, and Inventory.

---

## 🏆 Milestones & Achievements

Track your progress through the official Creator Awards:
*   **Silver Button:** 10,000 Subscribers
*   **Gold Button:** 100,000 Subscribers
*   **Diamond Button:** 1,000,000 Subscribers
*   **Ultimate Rank:** 👑 **Gaming God**

---

## 🛠️ Technical Stack

*   **Python 3.x**
*   `requests` & `BeautifulSoup`: For live data scraping.
*   `random`: For the unpredictable nature of the internet.
*   `time`: For process simulation.

---

## 💻 Code Example (Logic Snippet)
```python
# Example of the event engine logic
import random

def check_career_status(subscribers):
    # print("Calculating growth...") # From previous exercise: Basic subscriber logic
    if random.random() < 0.05:
        return "CANCELED" # The career-ruining event
    return "STABLE"
