def caps_lock_on_or_off(s):
    if s.isupper():
        return s.lower()
    elif len(s) == 1:
        if s.islower():
            return s.upper()
    elif s[0].islower() and s[1:].isupper():
        return s[0].upper() + s[1:].lower()
    else:
        return s

if __name__ == "__main__":
    s = input()
    print(caps_lock_on_or_off(s))