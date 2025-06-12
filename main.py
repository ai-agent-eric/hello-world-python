#!/usr/bin/env python3
"""
Enhanced Hello World application in Python with personalized greetings and multi-language support.
"""

import sys
import locale
from datetime import datetime


TRANSLATIONS = {
    "en": {
        "hello_world": "Hello, World!",
        "good_morning": "Good morning",
        "good_afternoon": "Good afternoon", 
        "good_evening": "Good evening",
        "good_night": "Good night"
    },
    "es": {
        "hello_world": "¡Hola, Mundo!",
        "good_morning": "Buenos días",
        "good_afternoon": "Buenas tardes",
        "good_evening": "Buenas tardes",
        "good_night": "Buenas noches"
    },
    "fr": {
        "hello_world": "Bonjour, le Monde!",
        "good_morning": "Bonjour",
        "good_afternoon": "Bon après-midi",
        "good_evening": "Bonsoir",
        "good_night": "Bonne nuit"
    },
    "de": {
        "hello_world": "Hallo, Welt!",
        "good_morning": "Guten Morgen",
        "good_afternoon": "Guten Tag",
        "good_evening": "Guten Abend",
        "good_night": "Gute Nacht"
    },
    "it": {
        "hello_world": "Ciao, Mondo!",
        "good_morning": "Buongiorno",
        "good_afternoon": "Buon pomeriggio",
        "good_evening": "Buonasera",
        "good_night": "Buonanotte"
    },
    "pt": {
        "hello_world": "Olá, Mundo!",
        "good_morning": "Bom dia",
        "good_afternoon": "Boa tarde",
        "good_evening": "Boa tarde",
        "good_night": "Boa noite"
    },
    "ja": {
        "hello_world": "こんにちは、世界！",
        "good_morning": "おはようございます",
        "good_afternoon": "こんにちは",
        "good_evening": "こんばんは",
        "good_night": "おやすみなさい"
    },
    "zh": {
        "hello_world": "你好，世界！",
        "good_morning": "早上好",
        "good_afternoon": "下午好",
        "good_evening": "晚上好",
        "good_night": "晚安"
    }
}


def get_system_language():
    """Detect the system's default language."""
    try:
        # Try modern approach first
        lang_code = locale.getlocale()[0]
        if not lang_code:
            # Fallback to environment variables
            import os
            lang_code = os.environ.get('LANG', '')
        
        if lang_code:
            # Extract language code (before underscore or period)
            lang = lang_code.split('_')[0].split('.')[0].lower()
            return lang if lang else "en"
    except:
        pass
    return "en"


def get_greeting(language="en"):
    """Get a time-appropriate greeting in the specified language."""
    hour = datetime.now().hour
    translations = TRANSLATIONS.get(language, TRANSLATIONS["en"])
    
    if 5 <= hour < 12:
        return translations["good_morning"]
    elif 12 <= hour < 17:
        return translations["good_afternoon"]
    elif 17 <= hour < 21:
        return translations["good_evening"]
    else:
        return translations["good_night"]


def parse_arguments():
    """Parse command line arguments to extract name and language."""
    args = sys.argv[1:]
    language = None
    name_parts = []
    
    i = 0
    while i < len(args):
        if args[i] in ("--lang", "-l"):
            if i + 1 < len(args) and not args[i + 1].startswith('-'):
                language = args[i + 1]
                i += 2
            else:
                # Skip malformed language option
                i += 1
        else:
            name_parts.append(args[i])
            i += 1
    
    name = " ".join(name_parts) if name_parts else None
    return name, language


def main():
    """Main function that prints a personalized greeting."""
    name, specified_language = parse_arguments()
    
    # Determine language: specified > system default > English
    language = specified_language or get_system_language()
    if language not in TRANSLATIONS:
        language = "en"
    
    translations = TRANSLATIONS[language]
    
    if name:
        greeting = get_greeting(language)
        print(f"{greeting}, {name}!")
    else:
        print(translations["hello_world"])


if __name__ == "__main__":
    main()