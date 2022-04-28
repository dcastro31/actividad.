# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:57:08 2022


"""

#Instructions Hamming
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    # calculates distance by counting 1 for every mis-match
    return sum(amino_code_a != amino_code_b
               for amino_code_a, amino_code_b
               in zip(strand_a, strand_b))