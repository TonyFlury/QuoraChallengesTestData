#!/usr/bin/env python
# coding=utf-8
"""
    QuoraChallengesTestData.producer.py :

"""
import random
from datetime import date, timedelta
from collections import defaultdict
import json

def date_range(start_date:date, end_date:date, include_weekends = False, exclude=None):
    """Generator to generate valid dates between start date and end date
        generates a 2-Tuple :
            * Integer number of days until the end date
            * The generated date

        Parameters

            :param start_date: datetime.date - the start of the range
            :param end_date: datetime.date - the end date of the range
            :param include weekends: Boolean - whether saturday or sunday should be excluded.
            :param exclude: set of integers - the set of day numbers to be excluded - Monday is 1
        """
    if exclude is None:
        exclude = set()

    if not include_weekends:
        exclude |= {6,7}

    days:timedelta = end_date - start_date

    for daycount in range(0,days.days +1):
        td = timedelta(days=daycount)
        d = start_date + td
        if d.isoweekday() in exclude:
            continue

        # Number of days until end_date
        to_end = end_date - d

        yield to_end.days, start_date+td

latest = date.fromisoformat('2020-05-01')

test_data = []

for test_id in range(1,2000):

    # Generate test date for this test case

    intervals = random.choices([(90,60,30),(60,30),(30,)],cum_weights=[80,95,100],k=1)[0]

    gap = random.randint(3,27)

    interval_start_price = random.randint(100, 250)

    start_date = latest - timedelta(days=(max(intervals) + gap))

    prices = []
    period_start_price = {}
    period_growth_days = defaultdict(int)
    period_gain = {}

    # Generate a random set of prices over the required interval
    for daynum, (days_to_end, this_date) in enumerate(date_range(start_date, latest, include_weekends=False)):

        if daynum == 0:
            price = interval_start_price
            price_delta = 0
        else:
            # Use a guassian distribution to calculate new price
            price_delta = round(random.gauss(mu=0.0001, sigma=price*0.03))
            price += price_delta
        prices.append((this_date.isoformat(), round(price)))

        for i in intervals:
            if days_to_end >= i:
                period_start_price[i] = round(price)
                break
            if days_to_end < i and price_delta > 0:
                period_growth_days[i] += 1

    end_price = round(price)

    return_value = []

    # Calculate the 2-tuple for each interval
    for interval in  (30, 60, 90):
        start = period_start_price.get(interval,None)
        if start is None:
            return_value.append((None,None))
            continue

        return_value.append((round(100*(end_price-start)/start,1), period_growth_days[interval]))

    return_value = tuple(return_value)

#    return_value = tuple((start := period_start_price.get(i,end_price), end_price,
#                            round(100*(end_price - start)/start,1), period_gain.get(i, None), period_growth_days.get(i, None)) for i in (30, 60, 90))

    test_data.append(
        {
            'test_id':f'{test_id:04}',
            'arguments':f'{prices!r}',
            'return':f'{return_value!r}'
        }
    )

with open('testdata.json','w') as tdf:
    json.dump(obj=test_data, fp=tdf)