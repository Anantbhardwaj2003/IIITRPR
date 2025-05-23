# Write a function that takes two strings s and t, and returns the minimum window substring of s that contains all the characters of t. If there is no such substring, return an empty string.
def min_window_substring(s, t):
    if not s or not t:
        return ""

    from collections import Counter

    t_count = Counter(t)
    required = len(t_count)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    min_length = float("inf")
    min_window = (0, 0)

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = (left, right)

            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1

        right += 1

    return s[min_window[0]:min_window[1] + 1] if min_length != float("inf") else ""

c1 = min_window_substring("ADOBECODEBANC", "ABC")
print(c1)  # Output: "BANC"