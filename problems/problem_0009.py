#!/usr/bin/python


"""
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def pythagorean_triplets(legs_total):
    """
    The variable legs_total is an integer representing the sum total of the
    lengths of a triangle.
 
    The function finds all Pythagorean triplets where the lengths of the legs
    of a triangle equal legs_total.  The function will then return a list
    of all such triplets.
    """
 
    assert legs_total == int(legs_total), "Input is not an integer"
    assert legs_total > 0, "Input is not a positive integer."
   
    triplets = []
 
    for a in range(1, legs_total + 1):
 
        for b in range(a + 1, legs_total + 1):
            c = legs_total - (a + b)
 
            if c > 0 and a ** 2 + b ** 2 == c ** 2:
               
                if tuple(sorted((a,b,c))) in triplets:
                    pass
 
                else:
                    triplets.append((a, b, c))
 
    return triplets


def main():
    
    triplet = pythagorean_triplets(1000)[0]
    a, b, c = triplet
    answer = a * b * c
    print answer
    

if __name__ == "__main__":
    main()
