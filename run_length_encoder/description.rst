==================
Run Length Encoder
==================

A function that will take a string, and return a run length encoded string, where a 'run' is an uninterrupted
sequence of the same character. This is the same as a 'segment' in the `sequence_and_counts` challenge.

In the output string the following rules are applied :

    - A run of length 1 is econded as just the character on it's own
    - A run of length 2 is encoded as two of the same characters
    - A run of length 3 and less than 10 is encoded as a single character, followed by a a single digits from 3 to 9
    - A run of length more than or equal to 10 are encoded as if they are one or more runs of length 9 and then a
        smaller run for the remainder

*Examples*

    - Input string  : aabbbbccd
    - Output string : aab4ccd

*Example*

    - Input string  : hhgggggiiippp
    - Output string : hhg5i3p3

*Example*
     - Input string  : aaaggggggggggggvvvvhhh
     - Output string : a3g9g3v4h3

Exceptions
----------
There are no exceptions expected to be raised from this function.
