# generatordemo.py
# Lesson: how generators improve on the patterns from listcompdemo.py
#
# A LIST COMPREHENSION builds the whole list in memory immediately (eager).
# A GENERATOR EXPRESSION produces one value at a time, only when asked (lazy).
#
# The syntax difference is tiny:  [ ]  becomes  ( )
# The behavior difference is big: no intermediate lists, constant memory.


import sys


# ---------------------------------------------------------------------------
# 1. WARM-UP: same example as listcompdemo.py
# ---------------------------------------------------------------------------

tal = [3, 6, 9, 12, 15]


def two_or_three(t):
    if t % 2 == 0:
        return t * 2
    else:
        return t * 3


# List comprehension: computes ALL values right now and stores them.
nya_tal_list = [two_or_three(t) for t in tal]
print("NU") # denna rad kkommer att köras när hela listan är klar

# Generator expression: computes NOTHING yet. It just remembers the recipe.
nya_tal_gen = (two_or_three(t) for t in tal)
for t in nya_tal_gen:
    print(t)  # denna rad körs först när vi kommer hit, en i taget

print("List version :", nya_tal_list)
print("Gen version  :", nya_tal_gen)  # not the numbers! just a generator object

# Consume the generator to get the same numbers out:
print("From generator:", [t for t in nya_tal_gen])


# ---------------------------------------------------------------------------
# 2. EAGER VS LAZY - proof that the genexp waits
# ---------------------------------------------------------------------------

def loud(x):
    print(f"   computing {x} ...")
    return x * 10


print("\nList comprehension (eager):")
loud_list = [loud(i) for i in range(3)]  # all "computing ..." printed HERE
print("list built")

print("Generator expression (lazy):")
loud_gen = (loud(i) for i in range(3))   # nothing printed!
print("generator created, nothing computed yet")
for value in loud_gen:                   # each value computed on demand
    pass


# ---------------------------------------------------------------------------
# 3. MEMORY DEMO - why this matters
# ---------------------------------------------------------------------------

big_n = 1_000_000

big_list = [i for i in range(big_n)]
big_gen = (i for i in range(big_n))

print(f"\nMemory used by the LIST     : {sys.getsizeof(big_list):>12,} bytes")
print(f"Memory used by the GENERATOR: {sys.getsizeof(big_gen):>12,} bytes")
print("The generator size stays constant no matter how big the data is.")


# ---------------------------------------------------------------------------
# 4. FIXING REAL PROBLEMS FROM listcompdemo.py
# ---------------------------------------------------------------------------

# Problem 1: building an intermediate list just to print it once.
# Old:
#     nyaord = [ord for ord in ordLista if "a" in ord]   # also shadows builtin ord()!
# Better: filter lazily straight into the loop.
ord_lista = ["apple", "banana", "cherry", "date"]
for word in (w for w in ord_lista if "a" in w):
    print(word)

# Problem 2: even numbers up to 20.
# Old: listan = [i for i in range(20) if i % 2 == 0]  -> builds a list first.
# Better as a genexp:
for i in (i for i in range(20) if i % 2 == 0):
    print(i)

# Even better: range() is ALREADY lazy, so for a simple range you need nothing extra:
for i in range(0, 20, 2):
    print(i)

# Side note: never name a variable "list" - it shadows the builtin list()
# and breaks things like list("abc") later in the program.


# ---------------------------------------------------------------------------
# 5. GENERATOR FUNCTIONS - the 'yield' keyword
# ---------------------------------------------------------------------------

def even_numbers(limit):
    """A function containing 'yield' IS a generator function."""
    n = 0
    while n < limit:
        yield n          # hand out one value, then PAUSE until asked again
        n += 2


evens = even_numbers(20)      # calling it runs NO code yet
print(evens)
for i in evens:
    print(i)

# Works with any logic, even infinite streams (just don't consume it all!):


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


c = counter()
print(next(c))   # 0
print(next(c))   # 1
print(next(c))   # 2


# ---------------------------------------------------------------------------
# 6. GOTCHAS - know the trade-offs
# ---------------------------------------------------------------------------

gen = (x * x for x in [1, 2, 3])

print(sum(gen))    # 14  - first pass works ...
print(sum(gen))    # 0   - ... second pass gets NOTHING, it's exhausted!

# Generators also can't be indexed or sliced: gen[0] would raise TypeError.

# Need the data more than once, or need len()/indexing? Just materialize it:
squares = list(x * x for x in [1, 2, 3])   # back to a normal list
print(squares, squares[0], len(squares))


# ---------------------------------------------------------------------------
# 7. RULE OF THUMB
# ---------------------------------------------------------------------------
# Use a LIST when you need to reuse/index/slice the results, or the data is small.
# Use a GENERATOR when you iterate once over large, expensive, or endless data -
# you pay for one item at a time instead of everything up front.
