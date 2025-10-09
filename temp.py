# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
word = input("Please input a word: ")
is_P = True

for x in word:
    if x == word[-1]:
        is_P = True
        print(word, "is a palindrome")
    else:
        is_P = False
        print(word, "is not a palindrome")
    