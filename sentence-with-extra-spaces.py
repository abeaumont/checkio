#! /usr/bin/env python
#
# Copyright 2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
Given string is a sentence, and words should be separated by only one space
character. Remove all extra spaces.

Input data: A sentence in the string variable.

Output data: A sentence without extra spaces.

Example:
    checkio('I  like   python') == "I like python"
"""

def checkio(l):
    return ''.join([l[i] for i in range(len(l)) if l[i:i+2] != '  '])

if __name__ == '__main__':
    assert checkio('I  like   python') == "I like python", 'Example'
