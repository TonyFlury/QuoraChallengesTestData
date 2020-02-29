================
Stock Analysis 1
================

A function that will take one positional parameter :
   - prices: a list of 2-tuples (date:string, price:integer) - in chronological order (earliest first).

The function will return a 3-tuple giving the 30 day, 60 day and 90 day price change.

The Dates are given in the format 'yyyy-mm-dd'

These date intervals are always calculated with reference to the date of the last entry - that is the 'last date'

For example to calculate the 30 day price change, you need to find the 'last date', and then find the latest date
in the sequence that is at least 30 days before the 'last date' - i.e. the difference between the date for the entry
and the 'last date' >= 30. The increase or decrease is simply the difference between the two prices.

Example
-------
    This is an example of the prices list that could be passed to the function.

::

    prices = [  ('2020-01-01', 228), ('2020-01-02', 236), ('2020-01-03', 233),
                ('2020-01-06', 241), ('2020-01-07', 249), ('2020-01-08', 248),
                ---
                ---
                ('2020-02-03', 258), ('2020-02-04', 256), ('2020-02-05', 252),
                ('2020-02-06', 240), ('2020-02-07', 234), ('2020-02-10', 232),
                ---
                ---
                ('2020-02-28', 321), ('2020-03-02', 330), ('2020-03-03', 324),
                ('2020-03-04', 334), ('2020-03-05', 331)]

The 'last date' here is 2020-03-05, and 60 days before this is 2020-01-05; since this date doesn't exist in the
prices data, you have to use the latest date before that - which is 2020-01-03.

The price on '2020-01-03' was 223, and the price on '2020-03-05' is 331 - therefore the 60 day change is 331-223 = 98.
Similarly 30 days before the 'last date' is '2020-02-04', and the price then is 256, and the change is 331-256 = 75
Since data does not exist in this data set more than 64 from the 'last_date', the 90 date change is reported as None.

From this data set the return from the function should be (75, 98, None).

Exceptions
----------
    The function should raise the ValueError exception if any of the dates are not valid.

Hints
-----
    The main purpose of this challenge is to use the datetime library - specifically the datetime.date and the
    timedelta classes; life is simply too short to write your own date and time handling functions.

    It should be noted that this form of date formatting is called the ISO format, and it is one of the standard ways
    to transmit date information.
