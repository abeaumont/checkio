#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

def checkio(arr):
    'convert all elements in arr in one row'
    
    def flatten(flattened, tree):
        for item in tree:
            if isinstance(item, list):
                flatten(flattened, item)
            else:
                flattened.append(item)
        
    flattened = []
    flatten(flattened, arr)
    return flattened

if __name__ == '__main__':
    assert checkio([1,2,3]) == [1,2,3], 'First'
    assert checkio([1,[2,2,2],4]) == [1,2,2,2,4], 'Second'
    assert checkio([[[2]],[4,[5,6,[6],6,6,6],7]])\
                              == [2,4,5,6,6,6,6,6,7], 'Third'
    print ('All ok')
