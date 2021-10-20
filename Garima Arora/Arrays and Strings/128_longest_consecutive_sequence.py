# -*- coding: utf-8 -*-
"""128. Longest Consecutive Sequence

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_O2jTS98mmGwWxGZ5czYTxeeMQNr0xDn
"""

class Solution:
    def longestConsecutive(self, a: List[int]) -> int:
        a=set(a)
        maxl=0
        for x in a:
            if x-1 not in a:
                y=x+1
                while y in a:
                    y+=1
                maxl=max(maxl,y-x)
        return maxl