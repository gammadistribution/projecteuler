#!/usr/bin/python


"""
This is a utility designed to facilitate the use of operations and algorithims
related to the ring of integers.  
"""


import math


def factor(n):
    """
    The variable n is a positive integer.

    This function returns a list of 2-tuples containing the prime factorization
    of n where the first element of the tuple is the prime factor and the 
    second element is the power to which the factor occurs.  

    For example, If n = p_0 ^ a_0  *  ...  *  p_k ^ a_k, then 
    factor(n) returns the following list, [(p_0, a_0), ..., (p_k, a_k)].
    
    A more specific example would be the following: If n = 12, then factor(n)
    returns the following list [(2, 2), (3, 1)].
    """

    assert n == int(n), "Input is not an integer."
    assert n > 1, "Input is not greater than 1."

    original = n
    integer = 2
    factors = []

    while original > 1:
        power = 0 
        while original % integer == 0:
            power += 1
            original /= integer
        
        if n % integer == 0:
            factors.append((integer, power))

        integer += 1

    return factors


def fib(n):
    """
    The variable n is a positive integer.  

    This function returns a list of all Fibonacci numbers not exceeding n.  
    A Fibonacci number is a number that is a member of the Fibonacci sequence. 
    The Fibonacci sequence, referred to as f_n, is defined for all natural
    numbers as f_0 = 0, f_1 = 1, whose n-th term in the sequence is defined by
    f_n = f_n-1 + f_n-2.  

    For example, fib(6) would return the following list [0, 1, 1, 2, 3, 5].
    """
    
    assert n == int(n), "Input is not an integer."
    assert n > 0, "Input is not a positive integer."

    # Initialize the accumulator with the first two elements of the sequence.
    fibonacci = [0, 1]
    
    # The first two elements of the sequence, a and b, are 1 and 0, 
    # respectively.
    a, b = 1, 0

    while a + b < n: 
        fibonacci.append(a + b)
        a, b = a + b, a
    
    return fibonacci

        
def gcd(a, b):
    """
    The variables a and b are positive integers.  

    This function returns the greatest common divisor (gcd) between the two 
    integers a and b.  The function makes use of the Euclidean Division 
    algorithim through recursion to calculate the gcd.
    """
    
    assert a == int(a), "{} is not an integer.".format(a)
    assert a > 0, "{} is not a positive integer.".format(a)
    assert b == int(b), "{} is not an integer.".format(b)
    assert b > 0, "{} is not a positive integer.".format(b)
    
    # Henceforth, the integer a will be referred to as the larger of the two 
    # inputs.
    if b > a:
        a, b = b, a
    
    remainder = a % b
    
    if remainder:
        return gcd(b, remainder)
    
    else:
        return b


def gcd_multiple(factors, straw=None):
    """
    The variable factors is a list of positive integers. 

    This function finds the greatest common divisor among all elements of the
    list factors.  It does this through recursively calling the binary 
    function gcd().
    """

    stack = factors.pop()

    if not factors:
        return gcd(stack, straw)

    else:
        return gcd_multiple(factors, gcd(stack, straw))


def lcm(a, b):
    """
    The variables a and b are positive integers.

    This function finds the least common multiple (lcm) of the two integers 
    given as input.  It makes use of the gcd function defined earlier and the
    equation lcm(a, b) = abs(a * b)/gcd(a, b)
    """

    return abs(a * b) / gcd(a, b)


def lcm_multiple(factors, straw=1):
    """
    The variable factors is a list of positive integers. 

    This function finds the least common multiple among all elements of the
    list factors.  It does this through recursively calling the binary 
    function lcm().
    """

    stack = factors.pop()

    if not factors:
        return lcm(stack, straw)

    else:
        return lcm_multiple(factors, lcm(stack, straw))


def palindrome(n):
    """
    The variable n is a positive integer.

    This function will return True if n is a palindrome and False otherwise.
    """
    
    assert n == int(n), "Input is not an integer."
    assert n > 0, "Input is not a positive integer."

    representation = str(n)
    
    if representation == representation[::-1]:
        return True

    else:
        return False
    

def primality(n):
    """
    The variable n is an integer.
 
    This function returns True if n is prime and False otherwise.  It does this
    by checking if n is divisible by any number less than or equal to the
    square root of n.  If it is divisible by any such number, the function
    returns False as n has a factor different from 1 and itself.  
    """
 
    assert int(n) == n, "Input is not an integer."
 
    counter = 2
    prime = True

    if n < 2:
        prime = False

    elif n != 2:
        while counter <= math.sqrt(n):
            if n % counter == 0:
                prime = False
                break
            counter += 1
 
    return prime


def primes(n):
    """
    The variable n is a positive integer.
 
    This function returns a list named sequence of the first n prime numbers.
    It does this by checking all integers until the length of sequence is n.
    If the result of primality(integer) is True, then integer is appended to
    sequence.
    """
 
    assert int(n) == n, "Input is not an integer."
    assert n > 0, "Input is not a positive integer."
   
    sequence = []
    integer = 2
   
    while len(sequence) < n:
       
        if primality(integer):
            sequence.append(integer)
           
        integer += 1
       
    return sequence


def prime_factors(n):
    """
    The variable n is a positive integer greater than 1.

    This functions returns a list of the prime factors of n by returning only
    the first element of each tuple in the list returned by factor(n).

    For example, if the prime factorization of 
    n = p_0 ^ a_0  *  ...  * p_k ^ a_k, then factor(n) would return the list
    [(p_0, a_0), ..., (p_k, a_k)] and prime_factors(n) would return the list
    [p_0, ..., p_k].

    A more specific example would be the following: If n = 12, then factor(n)
    would return [(2, 2), (3, 1)] and prime_factors(n) would return [2, 3].
    """
    return [prime for prime, power in factor(n)]
