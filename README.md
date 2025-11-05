[![CI](https://github.com/swe-students-fall2025/3-python-package-team_cascade/actions/workflows/ci.yml/badge.svg?branch=pipfile-experiment)](https://github.com/swe-students-fall2025/3-python-package-team_cascade/actions/workflows/ci.yml)

# 🐍 SsstudyPet

**SsstudyPet** is a Python package that provides an interactive command-line application to gamify your study sessions by letting you raise and care for a virtual ball python. The more you study, the more your snake grows! Track your study time, earn coins, feed your python, and watch it level up as you build consistent study habits.

## Features

- **📚 Study Session Tracking**: Start and end study sessions with automatic time tracking
- **✅ Task-Based Rewards**: Set tasks at the start of each session and earn 75 coins per completed task
- **� Virtual Ball Python**: Your snake levels up based on total study hours (1 level per 5 hours)
- **� Mood System**: Keep your python happy by logging in regularly and feeding it
- **💰 Earn Coins**: Complete tasks to earn coins that can be used to purchase food for your python
- **🐭 Feed Your Python**: Choose from various prey (mouse, rat, quail, rabbit, cricket) to boost mood
- **📈 Progress Tracking**: Monitor your study streaks, total study time, and python status
- **🔄 Auto-save**: Sessions automatically save on exit or interruption
- **🎮 Interactive Menu**: Easy-to-use CLI menu for all features

## Team Members

- [Catherine Yu](https://github.com/catherineyu2014)
- [Leo Fu](https://github.com/LeoFYH)
- [JunHao Chen](https://github.com/JunHaoChen16)
- [Majo Salgado](https://github.com/mariajsalgadoq)
- [Zeba Shafi](https://github.com/Zeba-Shafi)

## Installation

Install from PyPI:

```bash
pip install study-pet
```

Or install from source:

```bash
git clone https://github.com/swe-students-fall2025/3-python-package-team_cascade.git
cd team_cascade
pipenv install --dev
```

## Using SsstudyPet in Your Code

You can import and use SsstudyPet's functions in your own Python programs. Here's documentation for all available functions:

### Study Session Management

```python
from study_pet.tracker import start_session, end_session

# Start a study session with task planning
start_session()
# Prompts: "How many tasks do you plan to complete this session?"
# Sets session_tasks_planned and records start time

# End a study session with task completion
end_session()
# Prompts: "How many tasks did you complete this session?"
# Rewards 75 coins per completed task
# Updates total study time and saves progress
```

### Pet Care Functions

```python
from study_pet.pet import feed_pet, rename_pet, set_morph

# Feed your ball python (costs coins, boosts mood)
feed_pet("mouse")   # Costs 50 coins, +10 mood
feed_pet("rat")     # Costs 80 coins, +15 mood
feed_pet("quail")   # Costs 130 coins, +25 mood
feed_pet("rabbit")  # Costs 150 coins, +30 mood
feed_pet("cricket") # Costs 30 coins, +5 mood

# Rename your ball python
rename_pet("Slithers")

# Set your ball python's morph (color pattern)
set_morph("Banana")           # Choose from 10 preset morphs
set_morph("Custom Morph Name") # Or create your own custom morph
# Available presets: Banana, Pastel, Pied, Clown, Mojave, 
# Cinnamon, Albino, Blue Eyed Leucistic, GHI, Spider

# Get an encouraging phrase from your pet
encouragement = get_encouragement()
print(encouragement)  # Outputs: 🐍 Guido says: "Sssstay focused!"

# Get your ball python's current status
status = get_status()
print(status)  # Returns formatted status string
```

### Status and Data Functions

```python
from study_pet.pet import get_status
from study_pet.data_manager import load_state, save_state, reset_data

# Get your ball python's current status
status = get_status()
print(status)  # Returns formatted status string with all pet info

# Load current saved data
state = load_state()
print(f"Level: {state['level']}")
print(f"Coins: {state['coins']}")
print(f"Morph: {state['morph']}")

# Manually save data (normally done automatically)
save_state(state)

# Reset all data (use with caution!)
reset_data()
```

### Example Program

See our complete example program that demonstrates all functions: [example.py](https://github.com/swe-students-fall2025/3-python-package-team_cascade/blob/main/example.py)

```python
# example.py - Complete demonstration of SsstudyPet
from study_pet.tracker import start_session, end_session
from study_pet.pet import feed_pet, rename_pet, set_morph, get_status
from study_pet.data_manager import load_state

# Start a study session
print("Starting study session...")
start_session()  # Will prompt for task count

# Do some studying... (simulated)
print("\n📚 Studying...\n")

# End the session and earn rewards
end_session()  # Will prompt for completed tasks

# Check your ball python's status
print("\n" + get_status())

# Name your python
rename_pet("Monty")
print("\n🐍 Your ball python is now named Monty!")

# Set a morph
set_morph("Banana")
print("\n✨ Your python is now a beautiful Banana morph!")

# Feed your python
feed_pet("mouse")
print("\n🐭 Fed your python a mouse!")

# Check final status
print("\n" + get_status())

# Access raw data
state = load_state()
print(f"\n💰 Total coins: {state['coins']}")
print(f"⏱️  Total study time: {state['total_minutes']} minutes")
```

## Contributing to SsstudyPet

Want to help make SsstudyPet better? Here's how to set up your development environment:

### Prerequisites

- Python 3.10 or higher (Python 3.13 recommended)
- pipenv for dependency management

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/swe-students-fall2025/3-python-package-team_cascade.git
   cd 3-python-package-team_cascade-4
   ```

2. **Install pipenv** (if not already installed)
   ```bash
   pip install pipenv
   ```

3. **Set up the virtual environment and install dependencies**
   ```bash
   # Install all dependencies including dev dependencies
   pipenv install --dev
   
   # This installs:
   # - pytest (for testing)
   # - build (for building the package)
   # - twine (for publishing to PyPI)
   ```

4. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

5. **Run the tests**
   ```bash
   # Run all tests
   pytest tests/ -v
   
   # Run tests with coverage
   pytest tests/ --cov=study_pet --cov-report=html
   
   # Run specific test file
   pytest tests/test_actions.py -v
   ```

6. **Build the package**
   ```bash
   # Build distribution files
   python -m build
   
   # This creates dist/ directory with:
   # - .tar.gz (source distribution)
   # - .whl (wheel distribution)
   ```

7. **Test the package locally**
   ```bash
   # Install in editable mode for development
   pip install -e .
   
   # Run the CLI
   study-pet menu
   ```

### Development Workflow

1. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test thoroughly:
   ```bash
   pytest tests/ -v
   ```

3. Commit your changes:
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

4. Push to GitHub and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Wait for CI tests to pass (GitHub Actions automatically runs tests)

### Project Structure

```
study_pet/
├── __init__.py           # Package initialization
├── __main__.py           # CLI entry point
├── data_manager.py       # Data persistence functions
├── tracker.py            # Study session tracking
└── pet/
    ├── __init__.py       # Pet module exports
    ├── core.py           # Pet status and leveling
    └── actions.py        # Pet interaction functions
tests/
├── test_actions.py       # Tests for pet actions
├── test_core.py          # Tests for pet core functions
├── test_data_manager.py  # Tests for data management
├── test_tracker.py       # Tests for session tracking
├── test_main.py          # Tests for CLI commands
└── test_morph.py         # Tests for morph system
```

### Running Specific Tests

```bash
# Test specific functionality
pytest tests/test_morph.py::test_set_morph_valid -v
pytest tests/test_tracker.py -v
pytest tests/test_actions.py::test_feed_pet -v

# Test with output
pytest tests/ -v -s

# Generate coverage report
pytest tests/ --cov=study_pet --cov-report=term-missing
```

## PyPI Package

This package is available on PyPI: [study-pet](https://test.pypi.org/project/study-pet/0.1.0/))
