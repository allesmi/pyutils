#!/usr/bin/env python3

def get_pairs(seq):
	return get_n_tuples(seq, 2)

def get_triples(seq):
	return get_n_tuples(seq, 3)

def get_n_tuples(seq, n):
	assert len(seq) % n == 0, "Length of {} is not a multiple of {}".format(seq, n)
	return list(zip(*[iter(seq)]*n))