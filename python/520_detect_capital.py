"""
520. Detect Capital
Easy

We define the usage of capitals in a word to be right when one of the
following cases holds:

- All letters in this word are capitals, like "USA".
- All letters in this word are not capitals, like "leetcode".
- Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower() or word == word.title():
            return True

        return False