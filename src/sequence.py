#!/usr/bin/env python

import sys

class Sequence:

    def __init__(self, header="", bases="", scores=None, locus="", sample=""):
        self.header = header
        self.bases = bases
        if not scores:
            scores = []

    def __str__(self):
        result = "Header: " + self.header + "\n"
        result += "Bases: " + self.bases + "\n"
        return result
