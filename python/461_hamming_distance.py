"""
# 461. Hamming Distance

Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return format(x ^ y, "b").count("1")
