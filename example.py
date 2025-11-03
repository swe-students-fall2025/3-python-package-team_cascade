"""
example.py - Complete demonstration of SsstudyPet

This example program demonstrates all the functions available in the
SsstudyPet package. It shows how to:
- Start and end study sessions with task tracking
- Feed your ball python
- Rename your ball python
- Set morphs (color patterns)
- Check status and access saved data
"""

from study_pet.tracker import start_session, end_session
from study_pet.pet import feed_pet, rename_pet, set_morph, get_status
from study_pet.data_manager import load_state


def main():
    print("=" * 60)
    print("🐍 Welcome to SsstudyPet Example Program 🐍")
    print("=" * 60)
    print("\nThis program demonstrates all SsstudyPet functions.\n")

    # Start a study session
    print("📚 STARTING A STUDY SESSION")
    print("-" * 60)
    start_session()  # Will prompt for task count
    
    print("\n✏️  Imagine you're studying now...")
    print("    (In real use, you'd close the terminal and study!)")
    input("\n    Press Enter to end your study session...")

    # End the session and earn rewards
    print("\n🎉 ENDING STUDY SESSION")
    print("-" * 60)
    end_session()  # Will prompt for completed tasks

    # Check your ball python's status
    print("\n📊 CHECKING YOUR BALL PYTHON'S STATUS")
    print("-" * 60)
    print(get_status())

    # Rename your python
    print("\n✏️  RENAMING YOUR BALL PYTHON")
    print("-" * 60)
    new_name = input("What would you like to name your ball python? (or press Enter for 'Monty'): ").strip()
    if not new_name:
        new_name = "Monty"
    rename_pet(new_name)
    print(f"\n🐍 Your ball python is now named {new_name}!")

    # Set a morph (color pattern)
    print("\n🎨 SETTING A MORPH (COLOR PATTERN)")
    print("-" * 60)
    print("Available morphs:")
    print("  1. Banana    2. Pastel    3. Pied      4. Clown")
    print("  5. Mojave    6. Cinnamon  7. Albino    8. Blue Eyed Leucistic")
    print("  9. GHI      10. Spider")
    
    morph_choice = input("\nEnter a morph name (or press Enter for 'Banana'): ").strip()
    if not morph_choice:
        morph_choice = "Banana"
    set_morph(morph_choice)
    print(f"\n✨ Your python is now a beautiful {morph_choice} morph!")

    # Check status again to see the changes
    print("\n📊 UPDATED STATUS")
    print("-" * 60)
    print(get_status())

    # Feed your python
    print("\n🍽️  FEEDING YOUR BALL PYTHON")
    print("-" * 60)
    print("Available prey:")
    print("  - cricket (30 coins, +5 mood)")
    print("  - mouse   (50 coins, +10 mood)")
    print("  - rat     (80 coins, +15 mood)")
    print("  - quail   (130 coins, +25 mood)")
    print("  - rabbit  (150 coins, +30 mood)")
    
    # Check current coins
    state = load_state()
    print(f"\nYou currently have {state['coins']} coins.")
    
    prey_choice = input("\nWhat would you like to feed your python? (or press Enter for 'mouse'): ").strip().lower()
    if not prey_choice:
        prey_choice = "mouse"
    
    feed_pet(prey_choice)
    print(f"\n🐭 Fed your python a {prey_choice}!")

    # Show final status
    print("\n📊 FINAL STATUS")
    print("-" * 60)
    print(get_status())

    # Access and display raw data
    print("\n📈 RAW DATA")
    print("-" * 60)
    state = load_state()
    print(f"💰 Total coins: {state['coins']}")
    print(f"⏱️  Total study time: {state['total_minutes']} minutes")
    print(f"📅 Current streak: {state['streak']} days")
    print(f"🎯 Level: {state['level']}")
    print(f"😊 Mood: {state['mood']}")
    print(f"🎨 Morph: {state['morph']}")
    print(f"📝 Session tasks planned: {state['session_tasks_planned']}")
    print(f"✅ Session tasks completed: {state['session_tasks_completed']}")

    print("\n" + "=" * 60)
    print("🎉 Example program complete!")
    print("=" * 60)
    print("\nTo use SsstudyPet normally, run: study-pet menu")
    print("or use individual commands like: study-pet start, study-pet status, etc.")


if __name__ == "__main__":
    main()
