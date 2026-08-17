import csv
import json
import re
from collections import Counter
from pathlib import Path


# ============================================================
# Helper function
# ============================================================

def read_text(source):
    """
    Accept either:
    - a filename/path
    - a normal string

    If source exists as a file, read the file.
    Otherwise treat source as text.
    """
    path = Path(source)

    if path.is_file():
        return path.read_text(encoding="utf-8")

    return source


# ============================================================
# EXERCISES: LEVEL 1
# ============================================================


# ------------------------------------------------------------
# 1. Count number of lines and words in a text file
# ------------------------------------------------------------

def count_lines_and_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)

    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)

    return line_count, word_count


speech_files = [
    "day19/data/obama_speech.txt",
    "day19/data/michelle_obama_speech.txt",
    "day19/data/donald_speech.txt",
    "day19/data/melina_trump_speech.txt",
]

for speech in speech_files:
    lines, words = count_lines_and_words(speech)

    print(f"{speech}:")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print()


# ------------------------------------------------------------
# 2. Most spoken languages
# ------------------------------------------------------------

def most_spoken_languages(filename, number):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    languages = []

    for country in countries:
        languages.extend(country["languages"])

    language_counts = Counter(languages)

    result = [
        (count, language)
        for language, count in language_counts.most_common(number)
    ]

    return result


print("10 most spoken languages:")
print(
    most_spoken_languages(
        filename="day19/data/countries_data.json",
        number=10
    )
)

print()

print("3 most spoken languages:")
print(
    most_spoken_languages(
        filename="day19/data/countries_data.json",
        number=3
    )
)


# ------------------------------------------------------------
# 3. Most populated countries
# ------------------------------------------------------------

def most_populated_countries(filename, number):
    with open(filename, "r", encoding="utf-8") as file:
        countries = json.load(file)

    sorted_countries = sorted(
        countries,
        key=lambda country: country["population"],
        reverse=True
    )

    result = []

    for country in sorted_countries[:number]:
        result.append({
            "country": country["name"],
            "population": country["population"]
        })

    return result


print("\n10 most populated countries:")

for country in most_populated_countries(
    "day19/data/countries_data.json",
    10
):
    print(country)


print("\n3 most populated countries:")

for country in most_populated_countries(
    "day19/data/countries_data.json",
    3
):
    print(country)


# ============================================================
# EXERCISES: LEVEL 2
# ============================================================


# ------------------------------------------------------------
# 1. Extract incoming email addresses
# ------------------------------------------------------------

def extract_incoming_emails(filename):
    emails = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:

            # In mailbox files, incoming messages normally
            # contain lines such as:
            #
            # From example@email.com ...
            #
            if line.startswith("From "):
                match = re.search(
                    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}",
                    line
                )

                if match:
                    emails.append(match.group())

    return emails


incoming_emails = extract_incoming_emails(
    "day19/data/email_exchange_big.txt"
)

print("\nIncoming emails:")
print(incoming_emails)

print("Number of incoming emails:", len(incoming_emails))


# ------------------------------------------------------------
# 2. Find most common words
# ------------------------------------------------------------

def find_most_common_words(source, number):
    text = read_text(source)

    # Finds words while allowing apostrophes such as:
    # don't, we're, it's
    words = re.findall(
        r"\b[A-Za-z]+(?:'[A-Za-z]+)?\b",
        text
    )

    # Convert everything to lowercase so:
    # The, THE and the are counted together
    words = [word.lower() for word in words]

    word_counts = Counter(words)

    return [
        (count, word)
        for word, count in word_counts.most_common(number)
    ]


# Example:
# print(find_most_common_words("day19/data/sample.txt", 10))


# ------------------------------------------------------------
# 3. Most frequent words in speeches
# ------------------------------------------------------------

print("\nObama - 10 most common words:")
print(
    find_most_common_words(
        ".day19/data/obama_speech.txt",
        10
    )
)

print("\nMichelle Obama - 10 most common words:")
print(
    find_most_common_words(
        "day19/data/michelle_obama_speech.txt",
        10
    )
)

print("\nDonald Trump - 10 most common words:")
print(
    find_most_common_words(
        "day19/data/donald_speech.txt",
        10
    )
)

print("\nMelina Trump - 10 most common words:")
print(
    find_most_common_words(
        "day19/data/melina_trump_speech.txt",
        10
    )
)


# ------------------------------------------------------------
# 4. Text similarity
# ------------------------------------------------------------

def clean_text(source):
    text = read_text(source)

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation/numbers
    text = re.sub(r"[^a-z\s']", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def load_stop_words(filename="day19/data/stop_words.py"):
    """
    Handles the stop_words.py file from the 30 Days of Python
    exercise without importing it.
    """

    text = Path(filename).read_text(encoding="utf-8")

    # Extract quoted words
    words = re.findall(
        r"""['"]([^'"]+)['"]""",
        text
    )

    return set(word.lower() for word in words)


def remove_support_words(text, stop_words):
    words = text.split()

    filtered_words = [
        word
        for word in words
        if word not in stop_words
    ]

    return filtered_words


def check_text_similarity(
    source1,
    source2,
    stop_words_file="day19/data/stop_words.py"
):
    text1 = clean_text(source1)
    text2 = clean_text(source2)

    stop_words = load_stop_words(stop_words_file)

    words1 = set(
        remove_support_words(text1, stop_words)
    )

    words2 = set(
        remove_support_words(text2, stop_words)
    )

    # Jaccard similarity:
    #
    # common words / all unique words

    intersection = words1.intersection(words2)
    union = words1.union(words2)

    if not union:
        return 0

    similarity = len(intersection) / len(union)

    return similarity * 100


similarity = check_text_similarity(
    "day19/data/michelle_obama_speech.txt",
    "day19/data/melina_trump_speech.txt"
)

print(
    f"\nMichelle/Melina speech similarity: "
    f"{similarity:.2f}%"
)


# ------------------------------------------------------------
# 5. Ten most repeated words in Romeo and Juliet
# ------------------------------------------------------------

romeo_words = find_most_common_words(
    "day19/data/romeo_and_juliet.txt",
    10
)

print("\n10 most common words in Romeo and Juliet:")

for count, word in romeo_words:
    print(count, word)


# ------------------------------------------------------------
# 6. Hacker News CSV
# ------------------------------------------------------------

def analyze_hacker_news(filename):
    python_count = 0
    javascript_count = 0
    java_count = 0

    with open(
        filename,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        for line in file:

            # Python, python, PYTHON, etc.
            if re.search(
                r"\bpython\b",
                line,
                re.IGNORECASE
            ):
                python_count += 1

            # JavaScript, javascript, Javascript, etc.
            if re.search(
                r"\bjavascript\b",
                line,
                re.IGNORECASE
            ):
                javascript_count += 1

            # Java but NOT JavaScript
            #
            # \bjava\b prevents "javascript"
            # from matching anyway, but this explicitly
            # follows the exercise requirement.
            if (
                re.search(
                    r"\bjava\b",
                    line,
                    re.IGNORECASE
                )
                and not re.search(
                    r"\bjavascript\b",
                    line,
                    re.IGNORECASE
                )
            ):
                java_count += 1

    return {
        "Python": python_count,
        "JavaScript": javascript_count,
        "Java": java_count
    }


hn_results = analyze_hacker_news(
    "day19/data/hacker_news.csv"
)

print("\nHacker News results:")

print(
    "Lines containing Python:",
    hn_results["Python"]
)

print(
    "Lines containing JavaScript:",
    hn_results["JavaScript"]
)

print(
    "Lines containing Java but not JavaScript:",
    hn_results["Java"]
)