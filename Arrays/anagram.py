def check_anagram(s, t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False


print(check_anagram("hello", "elloh"))
