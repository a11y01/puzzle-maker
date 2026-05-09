import random
import requests

REAL_PHRASE = "apple river candle orbit silver maple engine"
OUTPUT_FILE = "phrases.txt"

WORDLIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

print("Downloading dictionary...")

words = requests.get(WORDLIST_URL).text.splitlines()

words = [
    w.lower()
    for w in words
    if w.isalpha() and 4 <= len(w) <= 8
]

print(f"Loaded {len(words):,} words")

# Build structured pools (THIS is what creates controlled difficulty)
pools = {
    1: random.sample(words, 300),
    2: random.sample(words, 300),
    3: random.sample(words, 300),
    4: random.sample(words, 300),
    5: random.sample(words, 300),
    6: random.sample(words, 300),
    7: random.sample(words, 300),
}

phrases = set()

# generate decoys using structure
for _ in range(500000):  # decoys only
    phrase = " ".join(
        random.choice(pools[i]) for i in range(1, 8)
    )
    phrases.add(phrase)

# insert real solution
phrases.add(REAL_PHRASE)

phrases = list(phrases)
random.shuffle(phrases)

with open(OUTPUT_FILE, "w") as f:
    for p in phrases:
        f.write(p + "\n")

print(f"Generated {len(phrases):,} phrases")
print("Real phrase inserted")
