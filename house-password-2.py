#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
Help Nikola to develop a password security check module for Sofia. Password
is considered to be strong enough if its length is more than or equal 10
symbols and it has at least one digit, one upper and one lower case letters.

Input data: String which is a password.

Output data: True if the password is safe.
"""

from functools import partial
from operator import lt


def checkio(data):
    'Return True if password strong and False if not'
    checks = [str.isdigit, str.islower, str.isupper]
    return len(data) >= 10 and all(map(lambda fn: any(map(fn, data)), checks))

if __name__ == '__main__':
    assert checkio('A1213pokl') is False, 'First'
    assert checkio('bAse730onE4') is True, 'Second'
    assert checkio('asasasasasasasaas') is False, 'Third'
    assert checkio('QWERTYqwerty') is False, 'Fourth'
    assert checkio('123456123456') is False, 'Fifth'
    assert checkio('QwErTy911poqqqq') is True, 'Sixth'
    print 'All ok'
