#!/usr/bin/env python
# encoding: utf-8
"""
busfintools.py

Created by Softwell on 2013-12-07.
Copyright (c) 2013 Softwell Pty Ltd. All rights reserved.
"""

from datetime import datetime
import math


def pv(rate=None, nper=None, pmt=None, fv=0.0, beg=False,rounded=2):
    """
    Description:
    Present value of an annuity pmt.
    
    Usage:
    presentvalue = pv(rate=None, nper=None, pmt=None, fv=0.0, beg=False,rounded=2)
    
    Parameters:
    * rate = interest rate compounded once per period, expressed as a decimal eg .05 for 5%
    * nper = number of periods.
    * pmt = payment each period paid either at the beginning (beg=True) 
      or at the end (beg=False) of each period
    * fv = future value
    * beg = True if the payment was made at the start of the period, False if at the end of a period
    * rounded = Number of decimal places to round, default=2
    """
    beg = 1 if beg else 0
    if rate==0:
        pv  = (-1* fv) - (pmt * nper)
    else:            
        pv = (-1*fv / (1 + rate)**nper) - (pmt*(1 + rate*beg)/rate*((1 + rate)**nper - 1) / (1 + rate)**nper)
    return round(pv,rounded)

def npv(rate=None,pmts=None, beg=False,rounded=2):
    """
    * rate = interest rate compounded once per period, expressed as a decimal eg .05 for 5%
    * a list of payments the number of elements equating to the nperiods.
      The convention is a payment is a negative value, and income is a positive value
    """
    pv = 0
    for per, pmt in enumerate(pmts):
        pv +=  (pmt*-1)/(1+rate)**(per+1)
    return round(pv,rounded)


def fv(rate=None, nper=None, pmt=None, pv=0.0, beg=True, rounded=2):
    """
    Description:
    Future value of an annuity pmt.
    
    Usage:
    futurevalue = fv(rate=None, nper=None, pmt=None, pv=0.0, beg=True,rounded=2)
    
    Parameters:
    * rate = interest rate compounded once per period, expressed as a decimal eg .05 for 5%
    * nper = number of periods.
    * pmt = payment each period paid either at the beginning (beg=True) 
      or at the end (beg=False) of each period
    * pv = present value
    * beg = True if the payment was made at the start of the period, False if at the end of a period
    * rounded = Number of decimal places to round, default=2
    """
    beg = 1 if beg else 0

    if rate==0:
        fv  = (-1* pv) - (pmt * nper)
    else:
        fv = ((pv*(1+rate)**nper)/-1) + ((pmt*(1 + rate*beg)/rate*((1 + rate)**nper - 1)) /-1)        
    return round(fv,rounded)


def pmt(rate=None, nper=None, pv=None, fv=0, beg=False,rounded=2):
    """
    Compute the payment against loan principal plus interest.

    Given:
     * a present value, `pv` (e.g., an amount borrowed)
     * a future value, `fv` (e.g., 0) NOT WORKING
     * an interest `rate` compounded once per period, of which
       there are
     * `nper` total
     * and (optional) specification of whether payment is made
       at the beginning (`when` = {'begin', 1}) or the end
       (`when` = {'end', 0}) of each period

    Return:
       the (fixed) periodic payment.

    Parameters
    ----------
    rate : Rate of interest (per period)
    nper : Number of compounding periods
    pv : Present value
    fv : Future value (default = 0)
    beg : True or False When payments are due ('begin' (True) or 'end' (False))
    """
    # formula that I could not get to work
    #=====================================
    # fv +
    # pv*(1 + rate)**nper +
    # pmt*(1 + rate*beg)/rate*((1 + rate)**nper - 1) == 0
    
    
    if rate==0:
        pmt = ((-1*fv)/nper)-(pv/nper)
    else:
        # The formula is M = P * ( J / (1 - (1 + J)^ -N)).
        # M: monthly payment
        # P: principal or amount of loan
        # J: monthly interest; annual interest divided by 100, then divided by 12.
        # N: number of months of amortization, determined by length in years of loan.
        pmt = (pv * (rate/(1-(1 + rate)**-nper)/(1 + rate*beg)) * -1)
    return round(pmt,rounded)

def nper(rate=None, pmt=None, pv=None, fv=0.0, beg=True):
    """
    The number of periods ``nper`` is computed by solving the equation::
     fv + pv*(1+rate)**nper + pmt*(1+rate*when)/rate*((1+rate)**nper-1) = 0
    but if ``rate = 0`` then::
     fv + pv + pmt*nper = 0
    """
    if rate==0:
        pass
        #fv + pv + pmt*nper = 0
        
    else:
        pass
        #fv + pv*(1+rate)**nper + pmt*(1+rate*beg)/rate*((1+rate)**nper-1)==0
        
        # ignore below for the moment . . please solve the above 2 equations for nper using natural logs (log)
        #        Log(M) - Log(M - PR/12)
        #N = ---------------------------------
        #                  Log(1 + R/12)
    

def calculatedaysbetween2dates(fromdate,todate):
    from_dt_obj = datetime.strptime(fromdate, "%Y-%m-%d")
    to_dt_obj = datetime.strptime(todate, "%Y-%m-%d")
    delta = from_dt_obj - to_dt_obj
    return delta.days

def printf(a, b):

    print '%s  %0.2f ==> %0.2f' %(a==b, a, b)
if __name__ == '__main__':
    
    printf(fv(rate=.05, nper=5, pmt=-1000, beg=False),5525.63)
    printf(fv(rate=.05, nper=5, pmt=-1000, beg=True), 5801.91)
    printf(fv(rate=.05/12, nper=10*12, pmt=-100, beg=False,pv=12000), -4235.89)
    printf(fv(rate=.05/12, nper=10*12, pmt=-100, beg=True,pv=12000), -4171.19)

    printf(pv(rate=.05, nper=5, pmt=-1000, beg=False), 4329.48)
    printf(pv(rate=.05, nper=5, pmt=-1000, beg=True),  4545.95)
    printf(pv(rate=.05/12, nper=120, pmt=-100, beg=False),  9428.14)
    printf(pv(rate=.05/12, nper=120, pmt=-100, beg=True),  9467.42)

    printf(pv(rate=.05/12, nper=10*12, pmt=-100, beg=False,fv=15692.93) , -100)
    printf(pv(rate=.04/12, nper=10*12, pmt=-100, beg=False,fv=15692.93) , -649.27)
    printf(pv(rate=.03/12, nper=10*12, pmt=-100, beg=False,fv=15692.93) , -1273.79)
    printf(pv(rate=.0/12, nper=10*12, pmt=-100, beg=False,fv=15692.93) , -3692.93)
    printf(npv(rate=.05/12,pmts=[-100]*120), 9428.14)

    printf(calculatedaysbetween2dates('2008-08-18','2008-09-26'), -39)
    printf(pmt(rate=.075/12, nper=15*12, pv=20000, beg=False) , -185.40)
    printf(pmt(rate=.075/12, nper=15*12, pv=20000, beg=True) , -184.25)
    