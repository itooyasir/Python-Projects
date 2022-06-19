# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 10:44:58 2022

@author: Yasir Itoo
"""

from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)