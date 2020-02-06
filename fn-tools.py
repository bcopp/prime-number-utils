from inspect import *
import itertools as itt
import functools as ftt
import more_itertools as mitt
import pprint
import time

pp = pprint.PrettyPrinter(indent=4)
def p(l):
  pp.pprint(l)

# Time decorator
def timeit(f):
  """ Simple decorator for timing functions"""

  def timed(*args, **kw):
      ts = time.time()
      result = f(*args, **kw)
      te = time.time()

      print('func:%r args:[%r, %r] took: %2.4f sec' % \
        (f.__name__, args, kw, te-ts))
      return result

  return timed

def all(f, iterable) -> bool:
  """ If all the conditions are True then return True, otherwise return False at the first failiure"""
  for e in iterable:
    if not f(e):
      return False
  return True
def any(f, iterable) -> bool:
  """ If any of the conditions are True then return True immedietly, otherwise False after iterating each item"""
  for e in iterable:
    if f(e):
      return True
  return False

# Infinte iterators
def count(start=0, step=1):
  """ An infinite iterator, it generate the next number in the series based on the step """
  n = start
  while True:
    yield n
    n += step

def primes_gen() -> int:
  """ A prime number generator. Each next() will return the next prime in the series """
  prev_primes = []
  # populate primes up to this number
  for n in count(start=2):
    if all(lambda e: n % e != 0, prev_primes):
      prev_primes.append(n)
      yield n

def is_prime(num:int) -> bool:
  """Returns whether or not a number is a prime"""
  primes = itt.takewhile(lambda p: p <= num/2, primes_gen())
  return all(lambda i: num%i != 0, primes)

def primes_to(num:int) -> list:
  """ Returns a list up prime numbers up from 0 to the argument number"""
  if num < 0:
    return None
  if num in [0,1]:
    return [num]

  prev_primes = []
  for n in range(2,num+1):
    if all(lambda e: n % e != 0, prev_primes):
      prev_primes.append(n)
  return prev_primes

def factors_of(ns: list) -> dict:
  """
  Finds the prime factors of each number within a list.
  Returns a dict containg each number and its prime factors, {number1:[prime_factor1...] ...}.
  """
  ps = {i:[] for i in ns} # Hash of all the primes in an iterable
  max_num = max(ns)
  print("Generating list of needed primes...")
  p_list = list(itt.takewhile(lambda p: p <= (max_num/2)+1, primes_gen())) # Primes up to half of the highest number
  for n_orig in ns:
    n = n_orig
    pi = 0
    while n != 1 and pi < len(p_list):
      p_cur = p_list[pi]
      if n % p_cur == 0:
        n /= p_cur
        ps[n_orig].append(p_cur)
        pi = -1
      pi += 1
    # If a prime number then append
    if len(ps[n_orig]) == 0:
      ps[n_orig].append(n_orig)
  return ps

# Receives a list of nums
# Returns lcm
@timeit
def lcm_list_multiples(iterable: list) -> int:
  """(SLOW) Finds the Least Common Multiple of two or more numbers using List Multiples"""
  if len(iterable) == 0:
    return [0]
  elif len(iterable) == 1:
    return [iterable[0]]
  it = sorted(iterable, reverse=True) #Sort lcm high to low
  if any(lambda n: n <= 0, reversed(iterable)):
    raise Exception("LCF OF ZERO EXCEPTION")

  gens = [(n, count(n,n)) for n in it]
  ns = {n:[] for n in it}

  while True:
    for i, (n, gen) in enumerate(gens):
      n_list = ns[n]
      n1 = next(gen)
      n_list.append(n1)
      # Check for matches on newly generated num, use non-inclusive iterable
      if _lcm_list_multiples_drill(n1, ns, list(filter(lambda it_n: n != it_n, it))):
        return n1

def _lcm_list_multiples_drill(val, ns, its):
  n_list = ns[its[0]]
  if len(its) == 1:
    if val in n_list:
      return True
    return False

  for n in n_list:
      if lcm_drill(n, ns, its[1:]):
        if val == n:
          return True
  return False
      
@timeit
def lcm(ns: list) -> int:
  """Finds the Least Common Multiple of two or more numbers using Prime Factorization"""
  fs = factors_of(ns)
  factors_all = list(fs.values())
  factors_count = {k:0 for k in set(mitt.collapse(factors_all))}

  for fl in factors_all:
    m_count = {}
    for f in fl:
      if m_count.get(f) != None:
        m_count[f] +=1
      else:
        m_count[f] = 1
    # Compare with main
    for mk in m_count.keys():
      if m_count[mk] > factors_count[mk]:
        factors_count[mk] = m_count[mk]

  acc = 1
  for k, v in factors_count.items():
    acc *= k**v
  return acc


  
def test():
  print("\nPrimes until 50")
  print(primes_to(50))

  print("\nBuild and run prime generator 5 times")
  p = primes_gen()
  l = []
  for _ in range(5):
    print(next(p))

  print("\nIs 17 a prime?")
  print(is_prime(17))
  print("\nFind factors of [10, 18, 1000]")
  print(factors_of([10,18,1000]))
  print("\nFind Least Common Multiple of [10, 18, 1000]")
  print(lcm([19999,18]))
  print("\nFind Least Common Multiple of [10,18,25,85,90191, 912]")
  print(lcm([10,18,25,85,90191, 67001]))
test()
