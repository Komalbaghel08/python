# angram checker
def angram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)
print(angram("listen", "silent"))  # True
print(angram("hello", "world"))  # False

