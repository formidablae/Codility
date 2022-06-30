# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    possible_passwords = S.split(' ')
    max_length = -1
    for password in possible_passwords:
        if len(password) > max_length and is_valid_password(password):
            max_length = len(password)
    return max_length

def is_valid_password(password):
    """
    it has to contain only alphanumerical characters (a-z, A-Z, 0-9);
    there should be an even number of letters;
    there should be an odd number of digits.
    """
    if len(password) % 2 == 0:
        return False
    letters = 0
    digits = 0
    for c in password:
        if not c.isalnum():
            return False
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            digits += 1
    return letters % 2 == 0 and digits % 2 == 1
