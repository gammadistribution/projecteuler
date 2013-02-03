#!/usr/bin/python


"""
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(n, seq=None):
    """
    The variable n is a positive integer and seq is an accumulator to collect
    the elements of the Collatz sequence. 

    The sequence is generated by the following rules if n is even return n / 2
    else if n is odd besides 1, return 3n + 1.  Continue until one is produced.  
    """

    assert n == int(n), "Input is not an integer."
    assert n > 0, "Input is not a positive integer."

    if not seq:
        seq = []
    
    seq.append(n)
    
    if n % 2 == 0:
        return collatz(n / 2, seq)
    
    elif n != 1:
        return collatz(3 * n + 1, seq)
    
    else:
        return tuple(seq)


def main():
    
    LIMIT = 1000000

    # The length of collatz(1) is 1.
    max_length = 1 
    greatest_chain_producer = 1 

    for n in range(1, LIMIT):
        seq = collatz(n)
        length = len(seq)
        if length > max_length:
            max_length = length 
            greatest_chain_producer = n
    
    print "answer", greatest_chain_producer, collatz(greatest_chain_producer)

if __name__ == "__main__":
    main()
