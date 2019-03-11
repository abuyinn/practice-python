import sys

s = input("Give a string:")

def isPalindrome(word):
    for i in range(len(word)):
        if word[i] != word[-(i+1)]:
            return False
    return True

if isPalindrome(s):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

# Easier:
print("It is a palindrome.") if s == s[::-1] else print("It is not a palindrome.")

