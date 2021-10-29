# -*- coding: utf-8 -*-
"""344. Reverse String

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_O2jTS98mmGwWxGZ5czYTxeeMQNr0xDn
"""

class Solution:
    def reverseString(self, a: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Two pointer Approach
        # TC=O(n/2)=O(n)
        
        s=0
        e=len(a)-1
        while s<e:
            a[s],a[e]=a[e],a[s]
            s,e=s+1,e-1
            
        
        '''
        # One liner
        for i in range(len(a)//2): a[i], a[-i-1] = a[-i-1], a[i]
        '''
        
        '''
        # Pythonic Solution
        a[:]=a[::-1]
    
        '''