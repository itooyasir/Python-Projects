# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:25:42 2022

@author: Yasir Itoo
"""

# group all the words which are anagrams of each other

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))