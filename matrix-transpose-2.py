#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
Your task is to return a transposed matrix based on input.

Click on the following link for the further infoabout matrix transpose
operation: http://en.wikipedia.org/wiki/Transpose

Input: matrix A

Output: transposed matrix tA
"""

def checkio(matr):
    'return a transposed matrix'
    l = len(matr[0])
    return map(lambda i: sum(matr, [])[i::l], range(l))
    
if __name__ == '__main__':
    assert checkio([[1,2],
             [1,2]]) ==  [[1, 1],
                          [2, 2]], 'First'
    assert checkio([[1,0,3,4,0],
                    [2,0,4,5,6],
                    [3,4,9,0,6]]) == [[1, 2, 3],
                                      [0, 0, 4],
                                      [3, 4, 9],
                                      [4, 5, 0],
                                      [0, 6, 6]],'Second'
    print 'All ok'
