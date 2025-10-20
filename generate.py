#!/usr/bin/env python3
# password_generator.py
import secrets
import string
import argparse

def generate(length=16, numbers=True, symbols=True, upper=True, lower=True):
    alphabet = ""
    if lower: alphabet += string.ascii_lowercase
    if upper: alphabet += string.ascii_uppercase
    if numbers: alphabet += string.digits
    if symbols: alphabet += string.punctuation
    if not alphabet:
        raise ValueError("No character sets selected.")
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Strong password generator")
    parser.add_argument("-l","--length", type=int, default=16)
    parser.add_argument("--no-symbols", action="store_true")
    parser.add_argument("--no-numbers", action="store_true")
    parser.add_argument("--no-upper", action="store_true")
    parser.add_argument("--no-lower", action="store_true")
    args = parser.parse_args()
    pwd = generate(
        length=args.length,
        numbers=not args.no_numbers,
        symbols=not args.no_symbols,
        upper=not args.no_upper,
        lower=not args.no_lower
    )
    print(pwd)

if __name__ == "__main__":
    main()
