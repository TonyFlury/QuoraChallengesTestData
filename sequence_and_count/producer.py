"""Produce the test data for the sequence_counter"""

import string
import random
import json

cases = []

for index in range(1,2001):
    # Choose a random set of letters
    letters = random.sample(string.ascii_lowercase, k = random.randint(3,6))

    last_c = None
    res = []
    for _ in range(random.randint(5,40)):
        c = random.choice(letters)
        if c == last_c:
            continue
        res.append([c,random.randint(1,10)])
        last_c = c

    inp = ''.join(l*k for l,k in res)

    cases.append({'id':f'{index:04}', 'arguments':f'{inp!r}','return':f'{res!r}'})

cases.append({'id':'2001', 'arguments':'""', 'return':repr([[None,0]]) })

with open('testdata.json', 'w') as json_fp:
    json.dump(obj=cases, fp=json_fp)