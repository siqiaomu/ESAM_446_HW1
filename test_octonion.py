# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:23:00 2022

@author: QQ
"""

from extended_numbers import O

O1 = O([0, -1, 2, -3, 4, -5, 6, -7])
O2 = O([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8])

O_prod = O1.mul(O2)

print(O_prod)