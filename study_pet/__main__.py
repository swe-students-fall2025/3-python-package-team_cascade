from . import start_session, end_session, get_status, reset_pet
from .data_manager import load_state, save_state
from .pet import rename_pet, feed_pet, check_daily_mood_decay
import argparse
import study_pet.tracker as tracker


def main():
    parser = argparse.ArgumentParser(description="� StudyPet")
    parser.add_argument(
        "command",
        nargs="?",
        default="menu",
        help="Available commands: start, end, status, feed, rename, menu",
    )
    parser.add_argument(
        "arg",
        nargs="?",
        default=None,
        help="Optional argument for feed (food name) or rename (new name)",
    )
    args = parser.parse_args()

    check_daily_mood_decay()

    if args.command == "start":
        start_session()
    elif args.command == "end":
        end_session()
    elif args.command == "status":
        print(get_status())
    elif args.command == "feed":
        feed_pet(args.arg)
    elif args.command == "rename":
        rename_pet(args.arg)
    elif args.command == "menu":
        main_menu()
    else:
        print("Unknown command. Use: start | end | status | feed [food] | rename [name] | menu")


def actions_menu():
    """Submenu for all pet-related actions."""
    while True:
        print("\n🐍 Actions Menu:")
        print("1. Feed your ball python")
        print("2. Back")

        choice = input("\nSelect an option (1–2): ").strip()

        if choice == "1":
            feed_pet()
        elif choice == "2":
            break
        else:
            print("Invalid option. Try again.")


def settings_menu():
    """Submenu for settings and info."""
    while True:
        print("\n⚙️ Settings Menu:")
        print("1. Check ball python status")
        print("2. Rename your ball python")
        print("3. Reset all data")
        print("4. Back")

        choice = input("\nSelect an option (1–4): ").strip()

        if choice == "1":
            print(get_status())
        elif choice == "2":
            rename_pet()
        elif choice == "3":
            confirm = input(
                "This will reset all progress. Type 'byebye' to confirm "
            ).lower()
            if confirm == "byebye":
                reset_pet()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")


def main_menu():
    """Main entry menu."""
    while True:
        print("\n� Welcome to SsstudyPet 🐍\n")
        print("1. Start studying ")
        print("2. End session")
        print("3. Actions")
        print("4. Settings")
        print("5. Close Menu (return to terminal)")
        print("6. Exit (Close StudyPet to terminal)")

        choice = input("\nSelect an option (1–6): ").strip()
        if choice == "1":
            start_session()
        elif choice == "2":
            end_session()
        elif choice == "3":
            actions_menu()
        elif choice == "4":
            settings_menu()
        elif choice == "5":
            tracker.manual_close = True
            break
        elif choice == "6":
            tracker.manual_close = False
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
