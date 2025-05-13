def are_anagrams(str1, str2):
    # If lengths of the two strings are not the same, they can't be anagrams
    if len(str1) != len(str2):
        return False

    # Create hash tables (dictionaries) to store frequency of characters
    frequency_map = {}

    # Count the frequency of each character in the first string
    for char in str1:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1

    # Decrease the frequency based on the second string
    for char in str2:
        if char in frequency_map:
            frequency_map[char] -= 1
        else:
            # If the character is not in the frequency map, they can't be anagrams
            return False

    # If all frequencies are zero, then the strings are anagrams
    for count in frequency_map.values():
        if count != 0:
            return False

    return True

# Test cases
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
print(are_anagrams("aabbcc", "abcabc"))  # Output: True
print(are_anagrams("python", "typhon"))  # Output: True
print(are_anagrams("race", "care"))      # Output: True
print(are_anagrams("abcdef", "abcfed"))  # Output: True
