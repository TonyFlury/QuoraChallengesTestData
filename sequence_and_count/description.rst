===================
Sequence and Counts
===================

A function that will take a string (as a positional argument), and return a list of lists describing each segment
within the string. Each inner lists has two elements - a single character, and a count.

A segment is defined as uninterrupted sequence of the same character, so for example

*Example*
 - Input string : abbccbbba
 - Segments : a, bb, cc, bbb, a
 - Expected return : [['a',1],['b',2],['c',2],['b',3],['a',1]]

*Example*
 - Input string : abca
 - Segments : a, b, c, a
 - Expected return : [['a',1],['b',1],['c',1],['a',1]]

Exceptions
----------
There are no exceptions expected to be raised from this function.