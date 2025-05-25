# Write a function in which we have 0-indexed array of strings and character x, return an array of indices representing the words that contain the character x.
def find_words_with_character(words, x):
    indices = []
    for i, word in enumerate(words):
        if x in word:
            indices.append(i)
    return indices

c1 = find_words_with_character(["apple", "banana", "cherry", "date"], 'a')
print(c1)  # Output: [0, 1, 3]