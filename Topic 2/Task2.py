import time

# 1. Brute Force Method - O(n^2)
def longest_substring_brute(s):
    n = len(s)
    max_len = 0
    max_sub = ""
    for i in range(n):
        seen = set()
        current = ""
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            current += s[j]
        if len(current) > max_len:
            max_len = len(current)
            max_sub = current
    return max_sub, max_len

# 2. Sliding Window Method - O(n)
def longest_substring_sliding_window(s):
    seen = {}
    start = 0
    max_len = 0
    max_sub = ""
    
    for end in range(len(s)):
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        seen[s[end]] = end
        if (end - start + 1) > max_len:
            max_len = end - start + 1
            max_sub = s[start:end+1]
    return max_sub, max_len

# 3. Test Cases
test_cases = [
    "abcabcbb",     # Expected: "abc", 3
    "bbbbb",        # Expected: "b", 1
    "pwwkew",       # Expected: "wke", 3
    "",             # Expected: "", 0
    "abcdefg",      # Expected: "abcdefg", 7
    "abba",         # Expected: "ab", 2
    "dvdf"          # Expected: "vdf", 3
]

# 4. Execution Time Comparison
print("\nExecution Time Comparison:\n")
for s in test_cases:
    print(f"Input string: {s}")
    
    # Brute Force
    start = time.time()
    sub_b, len_b = longest_substring_brute(s)
    time_b = time.time() - start
    print(f"  Brute Force -> Substring: '{sub_b}', Length: {len_b}, Time: {time_b:.6f}s")
    
    # Sliding Window
    start = time.time()
    sub_s, len_s = longest_substring_sliding_window(s)
    time_s = time.time() - start
    print(f"  Sliding Win -> Substring: '{sub_s}', Length: {len_s}, Time: {time_s:.6f}s\n")
