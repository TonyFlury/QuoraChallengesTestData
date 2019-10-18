#!/usr/bin/env python
# coding=utf-8
"""
    QuoraChallengesTestData.exemplar.py : Count uninterrupted sequences

Summary :
    Count the number of uninterrupted sequences within the string
    
DO NOT PUBLISH !!!!
"""

def sequence_and_counts(in_string):
    sc = []
    count = 0
    lastc = None
    for c in in_string:
        if c == lastc:
            count += 1
        else:
            if lastc:
                sc.append([lastc,count])
            count = 1
            lastc = c
    else:
        sc.append([lastc, count])
    return sc