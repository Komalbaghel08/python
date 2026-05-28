# Anagram checker
def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Sort the characters of both words and compare
    return sorted(word1) == sorted(word2)
# Example usage
word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
    


    