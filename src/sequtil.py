#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def score_as_int(char, offset=33):
    return ord(char) - offset

def score_as_char(num, offset=33):
    return chr(num + offset)
