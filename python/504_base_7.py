"""
504. Base 7
Easy

Given an integer num, return a string of its base 7 representation.
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        res = []
        while num != 0:
            res.append(str(num % 7))
            num = num // 7

        return sign + "".join(res)[::-1]
