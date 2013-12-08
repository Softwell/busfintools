#!/usr/bin/env python
# encoding: utf-8
"""
busfintools.py

Created by Softwell on 2013-12-07.
Copyright (c) 2013 Softwell Pty Ltd. All rights reserved.
"""


# Present value of a cash flow
def pv(cash_flow, period, cost_of_capital):
    """
    Input: cash_flow, year, cost_of_capital
    Output: present value of cash_flow
    """
    return cash_flow / (1.0 + cost_of_capital) ** period


if __name__ == '__main__':
    x= pv(100,2,.03)
    print x
    print round(x,2)

