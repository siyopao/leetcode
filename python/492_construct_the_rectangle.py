"""
492. Construct the Rectangle
Easy

A web developer needs to know how to design a web page's size. So, given a
specific rectangular web page’s area, your job by now is to design a
rectangular web page, whose length L and width W satisfy the following
requirements:

1. The area of the rectangular web page you designed must equal to the given
  target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.

Return an array [L, W] where L and W are the length and width of the web page
you designed in sequence.
"""

import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(math.floor(math.sqrt(area)), 0, -1):
            l = area // w
            if l * w == area:
                return [l, w]
