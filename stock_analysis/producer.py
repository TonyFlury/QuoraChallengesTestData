#!/usr/bin/env python
# coding=utf-8
"""
    QuoraChallengesTestData.producer.py :

"""
import random
from datetime import date, timedelta
import json

def date_range(start_date:date, end_date:date, include_weekends = False):
    days:timedelta = end_date - start_date

    for daycount in range(0,days.days +1):
        td = timedelta(days=daycount)
        d = start_date + td
        if d.isoweekday() >= 6 and not include_weekends:
            continue

        # Number of days until end_date
        to_end = end_date - d

        yield daycount, to_end.days, start_date+td

latest = date.fromisoformat('2020-03-05')

test_data = []

for test_id in range(1,2001):

    # Generate test date for this test case

    intervals = random.choices([(90,60,30),(60,30),(30,)],cum_weights=[80,95,100],k=1)[0]

    gap = random.randint(3,27)

    start_price = random.randint(25,230)

    start_date = latest - timedelta(days=(max(intervals) + gap))

    prices = []
    dated_prices = {}

    # Generate a random set of prices over the required interval
    for daynum, to_date, this_date in date_range(start_date, latest, include_weekends=False):

        if daynum == 0:
            price = start_price
        else:
            price_delta = random.uniform(-5.0,5.0)
            price += float(price_delta)*price/100
        prices.append((this_date.isoformat(), round(price)))

        for i in intervals:
            if to_date >= i:
                dated_prices[i] = round(price)
                break

    end_price = round(price)

    # Calculate gain/loss
    for interval, dated_price in dated_prices.items():
       dated_prices[interval] = end_price - dated_prices[interval]

    ret = [dated_prices.get(i, None) for i in (30,60,90)]
    test_data.append(
        {
            'test_id':f'{test_id:04}',
            'arguments':f'{prices!r}',
            'return':f'{ret!r}'
        }
    )

with open('testdata.json','w') as tdf:
    json.dump(obj=test_data, fp=tdf)