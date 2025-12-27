#--------- string lenggth----------
# def string_length(s):
#     count = 0
#     for _ in s:
#         count += 1
#     return count

# n = "python"
# r = string_length(n)
# print(r)


# -----------count-------------
# def char_count(s, target):
#     count = 0
#     for ch in s:
#         if ch == target:
#             count += 1
#     return count

# t = "python"
# r = char_count(t, "h")
# print(r)


# -----reverse string--------
# def reverse_string(s):
#     rev = ""
#     length = 0
#     for _ in s:
#         length += 1

#     for i in range(length - 1, -1, -1):
#         rev = rev + s[i]

#     return rev


# t = "python"
# print(reverse_string(t))


# ---palindrome--
# def palindrome(s):
#     l = 0
#     for _ in s:
#         l += 1

#     for i in range(l):
#         if s[i] != s[l - 1 - i]:
#             return False
#     return True
# t = input("Enter string or number: ")
# if palindrome(t):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# ----convert charater in upper case to lower case ------------
# def to_lower(ch):
#     if ch >= 'A' and ch <= 'Z':
#         ch = chr(ord(ch) + 32)
#     return ch
# c = input("Enter character: ")
# print(to_lower(c))


# ----------convert character lower case to upperv case-----

# def to_upper(ch):
#     if ch >= 'a' and ch <= 'z':
#         ch = chr(ord(ch) - 32)
#     return ch

# c = input("Enter char: ")
# print(to_upper(c))


# removing space 
# def remove_space(s):
#     r = ""
#     for ch in s:
#         if ord(ch) != 32:
#             r = r + ch
#     return r
# n = input("Enter")
# print(remove_space(n))


# ------count_word---
# t = input("Enter string: ")
# count = 0
# in_word = False

# for ch in t:
#     if not in_word:
#         count += 1
#         in_word = True
#     if ch == " ":
#         in_word = False

# print(count)


# ----------------Reaplace character-------------------
# def replace_char(s, old, new):
#     result = ""
#     for ch in s:
#         if ch == old:
#             result = result + new
#         else:
#             result = result + ch
#     return result


# text = input("Enter string: ")
# old_char = input("Enter character to replace: ")
# new_char = input("Enter new character: ")

# print(replace_char(text, old_char, new_char))

