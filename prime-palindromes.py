#! /usr/bin/env python
#
# Copyright 2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
An integer is said to be a palindrome if it is equal to its reverse in a string
form. For example, 79197 and 324423 are palindromes. In this task you will be
given an integer N. You must find the smallest integer M >= N such that M is a
prime number and M is a palindrome.

Input: An integer.

Output: A prime palindrome. An integer.
"""


def checkio(n):
    s = str(n)
    return not any([n % i == 0 for i in range(2, n >> 1)]) and s == s[::-1] \
        and n or checkio(n + 1)

if __name__ == '__main__':
    assert checkio(31) == 101, 'First example'
    assert checkio(130) == 131, 'Second example'
    assert checkio(131) == 131, 'Third example'
