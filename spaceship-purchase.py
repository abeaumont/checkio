#! /usr/bin/env python
#
# Copyright 2012-2013 Alfredo Beaumont <alfredo.beaumont@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the LICENSE file for more details.

"""
Write a program that, depending on Sofia and the old man's initial bargaining
sums--the steps by which they will increase or decrease the price during their
negotiations, will calculate which price they will agree upon. If Sofia's offer
is lower than or equal to the old man's offer, she will accept the old man's
price (and vice versa).

Sofi makes her proposition first. She never proposes an amount higher than what
is proposed to her. On the other hand, the old man never proposes an amount
lower than what is proposed to him.

Input data: Contains four integer numbers: Sofia's initial offer, Sofia's raise
to his offer, the initial counteroffer from the old man, and the old man's
reduction in his offer;

Output data: The amount of money that Sofia will pay for the spaceship.
"""

from math import ceil


def checkio(offers):
    return (lambda a, x, b, y: a + x * ceil(float(b - a) / (x + y)))(*offers)

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print('All is ok')
