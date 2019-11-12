"""Produce the test data for the sequence_counter"""

import string
import random
import json

cases = []

def runs():
    letters = random.sample(string.ascii_lowercase, k = random.randint(3,6))
    last_c = None
    for _ in range(random.randint(5,40)):
        c = random.choice(letters)
        if c == last_c:
            continue
        yield c, random.randint(1,15)
        last_c = c

for index in range(1,2001):
    # Choose a random set of letters

    inp = []
    out = []
    for char, length in runs():
        inp.append(char*length)
        m,r = divmod(length,9)
        out.append( (char+'9')*m + (char*r if r < 3 else char+str(r)))

    args = ''.join(inp)
    rets = ''.join(out)
    cases.append({'id':f'{index:04}', 'arguments':f'{args!r}','return':f'{rets!r}'})

cases.append({'id':'2001', 'arguments':'""', 'return':'""' })

with open('testdata.json', 'w') as json_fp:
    json.dump(obj=cases, fp=json_fp)