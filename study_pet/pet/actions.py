"""
Pet interaction features (rename, feed, talk, etc.)
"""

from datetime import datetime, timedelta
import time
from ..data_manager import load_state, save_state
import random


def rename_pet(new_name: str = None):
    """
    Renames the pet and saves to state.
    If no new_name is passed, will ask user input interactively.
    """
    state = load_state()
    old_name = state.get("name", "Unnamed")

    if not new_name:
        print(f"\nCurrent name: {old_name}")
        new_name = input("Enter new name for your pet: ").strip()

    if not new_name:
        print("Name cannot be empty.")
        return

    state["name"] = new_name
    save_state(state)
    print(f"Pet name changed to '{new_name}'!\n")


def feed_pet(food_name: str = None):
    """
    Feed your pet with food purchased using money.
    Each food has different cost and mood increase.
    
    Args:
        food_name: Optional food name (apple, cake, coffee, carrot, sushi).
                  If not provided, will show interactive menu.
    """
    state = load_state()
    name = state.get("name", "Guido")
    money = state.get("money", 0)
    mood = state.get("mood", 100)

    foods = {
        "apple": {"cost": 80, "mood": 10, "emoji": "🍎", "msg": "Crunchy and sweet!"},
        "cake": {
            "cost": 150,
            "mood": 20,
            "emoji": "🍰",
            "msg": "So yummy! Sugar rush!",
        },
        "coffee": {"cost": 50, "mood": 5, "emoji": "☕", "msg": "Ahh... more energy!"},
        "carrot": {"cost": 65, "mood": 8, "emoji": "🥕", "msg": "Healthy choice!"},
        "sushi": {
            "cost": 130,
            "mood": 15,
            "emoji": "🍣",
            "msg": "Delicious! I feel fancy!",
        },
        "custom": {"cost": 80, "mood": 10, "emoji": "🍽️", "msg": "Yum! That was tasty!"},
    }
    
    # If food_name is provided, use it directly
    if food_name:
        food_name = food_name.lower().strip()
        if food_name not in foods:
            print(f"Invalid food name: {food_name}")
            print(f"Available foods: {', '.join([f for f in foods.keys() if f != 'custom'])}")
            return
        
        selected = food_name
        food = foods[selected]
        display_name = selected
        
        # check balance
        if money < food["cost"]:
            print(f"Not enough coins! {food['cost']} needed, but you have {money}.")
            return

        # apply effects
        money -= food["cost"]
        new_mood = min(100, mood + food["mood"])
        state["money"] = money
        state["mood"] = new_mood
        state["last_feed_date"] = datetime.now().strftime("%Y-%m-%d")
        save_state(state)

        print(f"\n{food['emoji']} You fed {name} a {display_name}!")
        print(food["msg"])
        print(f" Mood increased to {new_mood}/100.")
        print(f" Remaining balance: {money} coins.\n")
        return
    
    # Interactive menu mode (original behavior)
    print(f"\n{name}'s current mood: {mood}/100 😊")
    print(f"Current balance: {money} coins 💰")
    print("Choose something to feed your pet:")
    print("1. Apple 🍎 (Cost: 80 | +10 mood)")
    print("2. Cake 🍰 (Cost: 150 | +20 mood)")
    print("3. Coffee ☕ (Cost: 50 | +5 mood)")
    print("4. Carrot 🥕 (Cost: 65 | +8 mood)")
    print("5. Sushi 🍣 (Cost: 130 | +15 mood)")
    print("6. Custom food ✏️ (Cost: 80 | +10 mood)")
    print("7. Return")
    choice = input("Select (1–7): ").strip()

    mapping = {
        "1": "apple",
        "2": "cake",
        "3": "coffee",
        "4": "carrot",
        "5": "sushi",
        "6": "custom",
    }
    if choice == "7":
        return
    if choice not in mapping:
        print(" Invalid choice.")
        return

    selected = mapping[choice]
    food = foods[selected]

    # handle custom name
    if selected == "custom":
        custom_name = input("Enter your custom food name: ").strip() or "mystery meal"
        food["msg"] = f"{name} happily ate your {custom_name}!"
        display_name = custom_name
    else:
        display_name = selected

    # check balance
    if money < food["cost"]:
        print(f"Not enough coins! {food['cost']} needed, but you have {money}.")
        return

    # apply effects
    money -= food["cost"]
    new_mood = min(100, mood + food["mood"])
    state["money"] = money
    state["mood"] = new_mood
    state["last_feed_date"] = datetime.now().strftime("%Y-%m-%d")
    save_state(state)

    print(f"\n{food['emoji']} You fed {name} a {display_name}!")
    print(food["msg"])
    print(f" Mood increased to {new_mood}/100.")
    print(f" Remaining balance: {money} coins.\n")
