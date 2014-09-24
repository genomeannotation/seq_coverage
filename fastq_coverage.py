#!/usr/bin/env python

import sys

from src.fastq import read_fastq

def main():
    if len(sys.argv) < 2:
        print("Usage: fastq_coverage.py <file.fastq>")
    
    fastq_path = sys.argv[1]

    with open(fastq_path, "r") as fastq_file:
        seqs = read_fastq(fastq_file)

        coverage = {}
        for seq in seqs:
            if seq.bases in coverage:
                coverage[seq.bases] += 1
            else:
                coverage[seq.bases] = 1
        
        for seq, count in coverage.items():
            print(seq+"\t"+str(count))

#############################

if __name__ == "__main__":
    main()
