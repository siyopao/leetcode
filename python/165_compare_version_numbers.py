"""
165. Compare Version Numbers
Medium

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each
revision consists of digits and may contain leading zeros. Every revision
contains at least one character. Revisions are 0-indexed from left to right,
with the leftmost revision being revision 0, the next revision being revision
1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order.
Revisions are compared using their integer value ignoring any leading zeros.
This means that revisions 1 and 001 are considered equal. If a version number
does not specify a revision at an index, then treat the revision as 0. For
example, version 1.0 is less than version 1.1 because their revision 0s are
the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:
- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0.
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(c) for c in version1.split(".")]
        v2 = [int(c) for c in version2.split(".")]

        lenv1 = len(v1)
        lenv2 = len(v2)
        l = max(lenv1, lenv2)

        v1 = v1 + [0] * (l - lenv1)
        v2 = v2 + [0] * (l - lenv2)

        for i in range(l):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1

        return 0
