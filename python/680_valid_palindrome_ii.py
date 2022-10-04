"""
680. Valid Palindrome II
Easy

Given a string s, return true if the s can be palindrome after deleting at
most one character from it.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        return helper(s, 1)


def helper(s: str, remaining: int) -> bool:
    l = len(s)
    if l == 0 or l == 1:
        return True

    if s[0] == s[l - 1]:
        return helper(s[1:-1], remaining)

    if remaining > 0:
        return helper(s[0:-1], 0) or helper(s[1:], 0)

    return False