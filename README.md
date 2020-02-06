# Prime Number Utilities
Several utilities related to generating, testing, and using prime numbers (such as finding the Least Common Factor for a given set of integers)

### lcm(ns: list) -> int:
Finds the Least Common Multiple of two or more numbers using Prime Factorization

### lcm_list_multiples(iterable: list) -> int:
(SLOW) Finds the Least Common Multiple of two or more numbers using List Multiples
 
### factors_of(ns: list) -> dict:
Finds the prime factors of each number within a list.
Returns a dict containg each number and its prime factors, {number1:[prime_factor1...] ...}.
  
### primes_to(num: int) -> list:
Returns a list up prime numbers up from 0 to the argument number
  
### def primes_gen() -> int:
A prime number generator. Each next() will return the next prime in the series
 
### is_prime(num: int) -> bool:
Returns whether or not a number is a prime
 
### def count(start=0, step=1):
An infinite iterator, it generate the next number in the series based on the step
 
### all(f, iterable) -> bool:
If all the conditions are True then return True, otherwise return False at the first failiure

### any(f, iterable) -> bool:
If any of the conditions are True then return True immedietly, otherwise False after iterating each item
