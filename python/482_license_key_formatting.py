"""
482. License Key Formatting
Easy

You are given a license key represented as a string s that consists of only
alphanumeric characters and dashes. The string is separated into n + 1 groups
by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k
characters, except for the first group, which could be shorter than k but
still must contain at least one character. Furthermore, there must be a dash
inserted between two groups, and you should convert all lowercase letters to
uppercase.

Return the reformatted license key.
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        t = s.replace("-", "").upper()[::-1]
        return "-".join(t[i : i + k] for i in range(0, len(t), k))[::-1]
