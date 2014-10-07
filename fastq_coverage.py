#!/usr/bin/env python

import sys
from os import listdir
from os.path import isfile, join
from collections import Counter

from src.fastq import read_fastq, get_seq_coverage, get_avg_seq_coverage

def main():
    #if len(sys.argv) < 2:
    #    print("Usage: fastq_coverage.py <file.fastq>")
    #    exit()

    male_path = "data/M"
    female_path = "data/F"

    male_files = [join(male_path, f) for f in listdir(male_path) if isfile(join(male_path, f))]
    female_files = [join(female_path, f) for f in listdir(female_path) if isfile(join(female_path, f))]

    # Calculate coverage
    male_coverage = Counter()
    for male_file in male_files:
        print("Processing "+male_file+" ...")
        with open(male_file, "r") as fastq_file:
            seqs = read_fastq(fastq_file)
            male_coverage += Counter(get_seq_coverage(seqs))
    female_coverage = Counter()
    for female_file in female_files:
        print("Processing "+female_file+" ...")
        with open(female_file, "r") as fastq_file:
            seqs = read_fastq(fastq_file)
            female_coverage += Counter(get_seq_coverage(seqs))

    # What seqs to keep?
    kept_male_seqs = []
    avg_male_coverage = get_avg_seq_coverage(male_coverage)
    for seq, count in male_coverage.items():
        if count >= avg_male_coverage/3 and count <= avg_male_coverage/2:
            kept_male_seqs.append(seq)
            print(seq)

#############################

if __name__ == "__main__":
    main()
