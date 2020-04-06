#!/usr/bin/env python
# coding=utf-8
"""
    QuoraChallengesTestData.exemplar.py : Count uninterrupted sequences

Summary :
    Count the number of uninterrupted sequences within the string
    
DO NOT PUBLISH !!!!
"""

def sequence_and_counts(in_string):
    count = 0
    lastc = ''
    for c in in_string:
        if c == lastc:
            count += 1
        else:
            if lastc:
                yield lastc, count
            count = 1
            lastc = c
    else:
        yield lastc, count

def rle(in_string):
    out = ''
    for char, length in sequence_and_counts(in_string):
        mul, rem = divmod(length,9)
        if mul == 0 and rem < 3:
            out += char*rem
        elif mul == 0 and rem >= 3:
            out += char+str(rem)
        else:
            out += (char + '9') * mul
            if rem >= 3:
                out += char + str(rem)
            else:
                out += char * rem
    return ''.join(out)