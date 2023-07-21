from collections import Counter

def find_repeated_words(string):
    # Remove punctuation and convert the string to lowercase
    string = string.lower().replace(",", "").replace(".", "")

    # Split the string into individual words
    words = string.split()

    # Count the occurrence of each word
    word_counts = Counter(words)

    # Find the repeated words
    repeated_words = [word for word, count in word_counts.items() if count > 1]

    return repeated_words

# Example usage:
input_string = "The quick brown fox jumps over the lazy dog. The dog jumps over the fence."
repeated_words = find_repeated_words(input_string)
print(repeated_words)
