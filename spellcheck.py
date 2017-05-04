#!/usr/bin/env python
import math
import random
import string

from bloomfil import BloomFilter


def fp_prob(num_hash_funcs, num_items, bit_vec_length):
    probability_of_success = math.e**(
        (-num_hash_funcs * float(num_items)) / bit_vec_length)
    return (1.0 - probability_of_success)**num_hash_funcs


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


if __name__ == '__main__':

    bloomfil = BloomFilter(1024000, 5)

    lines = open("./wordlist.txt").read().splitlines()
    for line in lines:
        bloomfil.add(line)
    #result = raw_input("Which word you want to search: ")
    prob_fp = fp_prob(5, len(lines), 1024000)
    print "Probability of False Positives: {}".format(prob_fp)
    random_word = random_char(5)
    print "Randomly generated word is {}".format(random_word)
    print "{} Spelling is {} correct".format(random_word, bloomfil.lookup(random_word))
    # print "{} Spelling is {} correct".format(result,bloomfil.lookup(result))
