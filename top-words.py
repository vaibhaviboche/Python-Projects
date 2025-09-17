import re
from collections import Counter

def get_words(paragraph):
    # Normalize: lowercase and remove punctuation
    cleaned = re.sub(r'[.,!]', '', paragraph.lower())
    words = cleaned.split()

    # Count word frequencies
    freq = Counter(words)

    # Get top 3 most common words
    top_three = [word for word, _ in freq.most_common(3)]
    return top_three

# Use print() to display the results
print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
# Output: ["coding", "python", "in"]

print(get_words("I like coding. I like testing. I love debugging!"))
# Output: ["i", "like", "coding"]

print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))
# Output: ["debug", "test", "deploy"]
