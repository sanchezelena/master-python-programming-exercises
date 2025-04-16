# Your code here
def remove_duplicate_words(text):
    words = set(text.split())
    return " ".join(sorted(words))

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))