
"""
Password Strength Checker (single-file)
Enhancements / Creativity:
 - Personalized greeting (asks for user's name)
 - Friendly final salutation
 - Brute-force crack time estimator (human-readable + scientific notation for huge values)
 - Clear comments and safe handling when word files are missing
"""

import math

# ---------------- Constants ----------------
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}|;:\"',.<>?/`~")

# ---------------- Utility functions ----------------
def word_in_file(word, filename, case_sensitive=False):
    """
    Check if word exists in a file (each line contains a single entry).
    - case_sensitive=False performs a case-insensitive match.
    - Returns True if found, False otherwise.
    - If file is missing, prints a warning and returns False.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line_word = line.strip()
                if not case_sensitive:
                    if word.lower() == line_word.lower():
                        return True
                else:
                    if word == line_word:
                        return True
    except FileNotFoundError:
        print(f"⚠️ Warning: {filename} not found. Skipping check.")
    return False


def word_has_character(word, character_list):
    """Return True if any character in `word` appears in `character_list`."""
    for ch in word:
        if ch in character_list:
            return True
    return False


def word_complexity(word):
    """
    Return a complexity score 0..4:
     - 1 point for containing lowercase
     - 1 point for containing uppercase
     - 1 point for containing digit
     - 1 point for containing special char
    """
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# ---------------- Core logic ----------------
def password_strength(password, min_length=10, strong_length=16):
    """
    Evaluate password and return strength 0..5:
     - 0 if dictionary word (case-insensitive) OR top password (case-sensitive)
     - 1 if too short (len < min_length)
     - 5 if long (len >= strong_length)
     - otherwise: base 1 + complexity (complexity 0..4) -> result 1..5
    Also prints the exact reason message (per spec).
    """
    # 1. Dictionary check (case-insensitive)
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Top passwords check (case-sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Very long -> strong
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. Complexity scoring
    complexity = word_complexity(password)  # 0..4
    # (Note: complexity==0 could happen for empty or non-matching chars)
    strength = 1 + complexity  # 1..5
    # Print complexity only when not failing earlier (optional detail)
    print(f"Password complexity: {complexity}/4")
    return strength

# ---------------- Creative feature: Crack time ----------------
def estimate_crack_time(password, guesses_per_second=1_000_000_000):
    """
    Estimate brute-force crack time for the given password.
    Uses math.log10 to avoid overflow for very large values.
    Returns a nicely formatted string (seconds/minutes/hours/days/years or scientific notation).
    - guesses_per_second default: 1 billion guesses/sec (adjustable)
    """
    # compute charset size from character classes used
    charset_size = 0
    if word_has_character(password, LOWER):
        charset_size += 26
    if word_has_character(password, UPPER):
        charset_size += 26
    if word_has_character(password, DIGITS):
        charset_size += 10
    if word_has_character(password, SPECIAL):
        charset_size += len(SPECIAL)

    if charset_size == 0 or len(password) == 0:
        return "⏱️ Crack time estimate: less than 1 second (no valid charset or empty password)."

    # log10 of total guesses = len(password) * log10(charset_size)
    log10_guesses = len(password) * math.log10(charset_size)
    # log10 seconds = log10_guesses - log10(guesses_per_second)
    log10_seconds = log10_guesses - math.log10(guesses_per_second)

    # helper to convert log10_seconds to units
    def fmt_seconds_from_log10(l10s):
        """Return friendly string based on log10(seconds)."""
        # seconds thresholds (log10)
        log10_minute = math.log10(60)          # ~1.78
        log10_hour = math.log10(3600)          # ~3.56
        log10_day = math.log10(86400)          # ~4.94
        log10_year = math.log10(31_536_000)    # ~7.5 (seconds/year)
        # small values -> compute exact seconds
        if l10s < log10_minute:
            seconds = 10 ** l10s
            return f"⏱️ Crack time estimate: {seconds:.2f} seconds"
        if l10s < log10_hour:
            minutes = (10 ** l10s) / 60
            return f"⏱️ Crack time estimate: {minutes:.2f} minutes"
        if l10s < log10_day:
            hours = (10 ** l10s) / 3600
            return f"⏱️ Crack time estimate: {hours:.2f} hours"
        if l10s < log10_year:
            days = (10 ** l10s) / 86400
            return f"⏱️ Crack time estimate: {days:.2f} days"
        # years: may still be huge — produce either numeric or scientific shorthand
        log10_years = l10s - log10_year
        # if small enough (<6 => <1,000,000 years) show numeric
        if log10_years < 6:
            years = 10 ** log10_years
            return f"⏱️ Crack time estimate: {years:.2f} years"
        # otherwise use scientific notation: mantissa e exponent
        exponent = int(math.floor(log10_years))
        mantissa = 10 ** (log10_years - exponent)
        return f"⏱️ Crack time estimate: {mantissa:.2f}e{exponent} years (approx.)"

    return fmt_seconds_from_log10(log10_seconds)

# ---------------- Main program ----------------
def main():
    """Main interactive loop with user greeting and farewell."""
    print("🔐 Password Strength Checker")
    username = input("Hello — please enter your name: ").strip().title()
    if username == "":
        username = "User"
    print(f"\n👋 Welcome, {username}! Let's test how strong your passwords are.")
    print("Type 'q' to quit at any prompt.\n")

    while True:
        pwd = input("🔑 Enter a password to test: ")
        if pwd.lower() == "q":
            print(f"\n👋 Goodbye, {username}! Stay safe online. 🔒")
            break

        strength = password_strength(pwd)
        print(f"⭐ Final password strength score: {strength}/5")
        print(estimate_crack_time(pwd))
        print("-" * 56)

# ---------------- Entry point ----------------
if __name__ == "__main__":
    main()

