#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
Teach Sofia how to use an ATM. The ATM on their home island can only dispense
$5 bills which means that the machine will not dispense any amount of money
that is not divisible by $5. In addition to that, the fee for each withdrawal
is $0.5 + 1% of the amount of cash withdrawn. The robots cannot withdraw any
amount above the card's balance. After each transaction, the bank rounds down
the balance to the closest whole value (57.9 = 57, 61.1 = 61).

Input: A list of integers: the first one denotes the robot's account balance,
and the second is a list of the monetary amounts that the robot wants to
withdraw.

Output: The account balance after all operations (integer).
"""


from math import ceil
from functools import reduce


def checkio(data):
    return reduce(lambda a, b, d={}: d.__setitem__(0, (ceil(b * 1.01 + .5))) or
                  a - (not b % 5 and d[0] <= a and d[0] or 0), *reversed(data))

if __name__ == '__main__':
    assert checkio([120, [10, 20, 30]]) == 57, 'First'
    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio([120, [200, 10]]) == 109, 'Second'
    #with one incorrect amount
    assert checkio([120, [3, 10]]) == 109, 'Third'
    assert checkio([120, [200, 119]]) == 120, 'Fourth'
    assert checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56, \
        "It's mixed all base tests"
    print('All Ok')
