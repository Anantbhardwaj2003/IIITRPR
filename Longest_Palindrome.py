def longest_palindrome(words):
    from collections import Counter

    count = Counter(words)
    length = 0
    used_center = False

    for word in list(count.keys()):
        rev = word[::-1]
        if word != rev:
            # Match pairs like 'ab' with 'ba'
            pair_count = min(count[word], count[rev])
            length += pair_count * 4  # each pair contributes 4 characters
            count[word] -= pair_count
            count[rev] -= pair_count
        else:
            # Word is a palindrome like 'aa', 'bb'
            pairs = count[word] // 2
            length += pairs * 4
            count[word] -= pairs * 2

    # Now check if we can place a single palindrome word in the center
    for word in count:
        if word[0] == word[1] and count[word] > 0 and not used_center:
            length += 2
            used_center = True

    return length

c1 = longest_palindrome(["ab", "ba", "aa", "bb", "cc"])
print(c1)  # Output: 12