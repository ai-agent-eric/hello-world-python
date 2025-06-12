# Hello World Python

A multi-language Hello World application written in Python with personalized time-based greetings.

## Features

- **Multi-language support**: English, Spanish, French, German, Italian, Portuguese, Japanese, and Chinese
- **Time-based greetings**: Different greetings based on the current time of day
- **Personalized messages**: Support for custom names
- **System language detection**: Automatically detects your system language
- **Command-line language selection**: Override system language with `--lang` option

## Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
No additional installation required - uses only Python standard library.

### Usage
```bash
# Basic usage (uses system language)
python main.py

# Personalized greeting (uses system language)
python main.py Alice
python main.py John Doe

# Specify language with --lang or -l
python main.py --lang es
python main.py --lang fr Alice
python main.py -l de John Doe

# Supported language codes: en, es, fr, de, it, pt, ja, zh
```

## Language Support

The application automatically detects your system language and provides appropriate greetings. Supported languages:

- **English (en)**: Hello, World! / Good morning, etc.
- **Spanish (es)**: ¡Hola, Mundo! / Buenos días, etc.
- **French (fr)**: Bonjour, le Monde! / Bonjour, etc.
- **German (de)**: Hallo, Welt! / Guten Morgen, etc.
- **Italian (it)**: Ciao, Mondo! / Buongiorno, etc.
- **Portuguese (pt)**: Olá, Mundo! / Bom dia, etc.
- **Japanese (ja)**: こんにちは、世界！ / おはようございます, etc.
- **Chinese (zh)**: 你好，世界！ / 早上好, etc.

Time-based greetings change throughout the day:
- Morning (5:00-11:59): Good morning / Buenos días / Bonjour, etc.
- Afternoon (12:00-16:59): Good afternoon / Buenas tardes / Bon après-midi, etc.
- Evening (17:00-20:59): Good evening / Buenas tardes / Bonsoir, etc.
- Night (21:00-4:59): Good night / Buenas noches / Bonne nuit, etc.

## Development

### Setup
1. Clone the repository
2. Run the application: `python main.py`

### Testing
Run the application to verify it prints "Hello, World!"

## License

MIT License - see LICENSE file for details