#!/usr/bin/env python3
"""
Enhanced Hello World application in Python with personalized greetings.
"""

import sys
from datetime import datetime


def get_greeting():
    """Get a time-appropriate greeting."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


def main():
    """Main function that prints a personalized greeting."""
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
        greeting = get_greeting()
        print(f"{greeting}, {name}!")
    else:
        print("Hello, World!")


if __name__ == "__main__":
    main()