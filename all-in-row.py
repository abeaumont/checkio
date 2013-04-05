#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
There is a list that contains one or more lists inside. Put all values in one
list.

Input data: Multiple list.

Output data: Single list.
"""

checkio = lambda a: type(a) == list and sum([checkio(i) for i in a], []) or [a]

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print ('All ok')
