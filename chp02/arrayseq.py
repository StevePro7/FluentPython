import os
import dis
from array import array as arr
from random import random, seed
import numpy as np
import collections



# Ex 2-1
symbols = '$¢£¥€¤'
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)


# Ex 2-2
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC'
codes = [ord(x) for x in x]
print(codes)

codes = [last := ord(c) for c in x]
print(codes)


# Ex 2-3
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)


# Ex 2-4
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))


# Ex 2-5
x = tuple(ord(symbol) for symbol in symbols)
print(x)

import array
y = array.array('I', (ord(symbol) for symbol in symbols))
print(y)


# Ex 2-6
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)


# Ex 2-7
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' %passport)

for country, _ in traveler_ids:
    print(country)

# Tuples as Immutable Lists
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])
print(a == b)

b[-1].append(99)
print(a == b)
print(b)


def fixed(o):
    try:
        hash(o)
    except TypeError:
        return False
    return True

tf = (10, 'alpha', (1, 2))      # Contains no mutable items
tm = (10, 'alpha', [1, 2])      # Contains a mutable item (list)
print(fixed(tf))
print(fixed(tm))


# Unpacking sequences and iterables

# Ex 2-8        Unpacking sequences and iterables
latitude, longitude = lax_coordinates       # unpacking
print(latitude)
print(longitude)


print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient, remainder)

_, filename = os.path.split("~/.ssh/id_rsa.pub")
print(filename)


# Using * to grab excess items
a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)


# Unpacking with * in function calls and sequence literals
def fun(a, b, c, d, *rest):
    return a, b, c, d, rest

print(fun(*[1, 2], 3, *range(4, 7)))

print((*range(4), 4))
print([*range(4), 4])
print({*range(4), 4, *(5, 6, 7)})


# Nested unpacking
# Ex 2-8        Unpacking nested tuples to access the longitude
# metro_lat_lon.py


# Pattern Matching with Sequences
# Ex 2-9        Method from an imaginary Robot class


# Ex 2-10       Destructuring nested tuples
# match_lat_lon.py

# Pattern Matching Sequences in an Interpreter
# Ex 2-11       Matching patterns without match/case
# py39_lis.py

# Ex 2-12       Pattern matching with match
# py310_lis.py


# Slicing
# Why Slices and Range Exclude the Last Item
l = [10, 20, 30, 40, 50, 60]
print(l[:2])    # Idx: 0, 1
print(l[2:])    # Idx: 2, 3, 4, 5

print(l[:3])    # Idx: 0, 1, 2
print(l[3:])    # Idx: 3, 4, 5

# Slice objects
s = 'bicycle'
print(s[::3])   # Idx: 0, 3, 6
print(s[::-1])  # Idx: 6, 5, 4, 3, 2, 1
print(s[::-2])  # Idx: 6, 4, 2, 0


# Ex 2-13       Line items from a flat-file invoice
invoice = """
0.....6.................................40........52...55........
1909 Pimoroni PiBrella                      $17.50    3    $52.50
1489 6mm Tactile Switch x20                  $4.95    2    $9.90
1510 Panavise Jr. - PV-201                  $28.00    1    $28.00
1601 PiTFT Mini Kit 320x240                 $34.95    1    $34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])



# Assigning to Slices
l = list(range(10))
print(l)                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l[2:5] = [20, 30]
print(l)                # [0, 1, 20, 30, 5, 6, 7, 8, 9]

del(l[5:7])
print(l)                # [0, 1, 20, 30, 5, 8, 9]

# exception
try:
    l[2:5] = 100
except TypeError as e:
    print(repr(e))      # TypeError('can only assign an iterable')


# Using + and * with Sequences
l = [1, 2, 3]
print(l * 5)            # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

print(5 * 'abcd')       # abcdabcdabcdabcdabcd


# Building a List of Lists
# Ex 2-14               A list with three lists of length 3 can represent tic-tac-toe board
board = [['_'] * 3 for i in range(3)]
print(board)            # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[1][2] = 'X'
print(board)            # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]


# Ex 2-15               A list with three references to the same list is useless
weird_board = [['_'] * 3] * 3
print(weird_board)      # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

weird_board[1][2] = '0'
print(weird_board)      # [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]


# Explanation
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)            # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[2][0] = 'X'
print(board)            # [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]


# Augmented Assignment with Sequences
l = [1, 2, 3]
idl = id(l)
print(idl)

l *= 2
print(l)

print(id(l) == idl)

t = (1, 2, 3)
idt = id(t)
print(idt)

t *= 2
print(id(t) == idt)


# A += Assignment Puzzler
# Ex 2-16       A riddle
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError as e:
    print(repr(e))              # TypeError("'tuple' object does not support item assignment")


# Ex 2-17       unexpected item t2 is changed and exception raised
print(t)


# Ex 2-18       bytecode for the expression s[a] += b
x = dis.dis('s[a] += b')
print(x)


# list.sort and the sorted built-in function
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))

print(fruits)

print(sorted(fruits, reverse=True))

print(sorted(fruits, key=len))

print(sorted(fruits, key=len, reverse=True))

fruits.sort()
print(fruits)


# When a List is not the Answer
# Ex 2-19       creating, saving, loading large array of floats
#seed(10)
#floats = arr('d', (random() for i in range(10 ** 7)))
#print(floats[-1])

#with open('floats.bin', 'wb') as fp:
#    floats.tofile(fp)

#floats2 = arr('d')
#with open ('floats.bin', 'rb') as fp:
#    floats2.fromfile(fp, 10 ** 7)

#print(floats2[-1])
#print(floats == floats2)


# Ex 2-20          handling 6 bytes of memory as 1x6, 2x3, 3x2 views
octets = arr('B', range(6))
m1 = memoryview(octets)
print(m1.tolist())

m2 = m1.cast('B', [2, 3])
print(m2.tolist())

m3 = m1.cast('B', [3, 2])
print(m3.tolist())

m2[1, 1] = 22
m3[1, 1] = 33
print(octets)       # array('B', [0, 1, 2, 33, 22, 5])


# Ex 2-21           changing the value of 16-bit integer array item by poking one of its bytes
numbers = arr('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])

memv_oct = memv.cast('B')       # [254, 255, 255, 255, 0, 0, 1, 0, 2, 0]

memv_oct[5] = 4
print(numbers)                  # array('h', [-2, -1, 1024, 1, 2])


# NumPy
# Ex 2-22           basic operations with rows and cols in numpy ndarray
a = np.arange(12)
print(a)
print(type(a))
print(a.shape)

a.shape = 3, 4
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[2])         # row 2     [ 8  9 10 11]
print(a[2, 1])
print(a[:, 1])      # col 1     [1 5 9]

a = a.transpose()
print(a)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]


# Ex 2-22           loading, saving and vectorized operations
# with open('floats-1M-lines.txt', 'wt') as fp:
#     for _ in range(1_000_000):
#         fp.write(f'{random()}\n')

#floats = np.loadtxt('floats-1M-lines.txt')
#print(floats[-3:])

#floats *= .5
#floats[-3:]

from time import perf_counter as pc
# t0 = pc()
# floats /= 3
# print((pc() - t0) < 0.01)

# np.save('floats-1M', floats)
# floats2 = np.load('floats-1M.npy', 'r+')
# floats2 *= 6

# floats2[-3:]


# Deques and other queues
# Ex 2-23       working with a queue
dq = collections.deque(range(10), maxlen=10)
print(dq)                   # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.rotate(3)
print(dq)                   # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)

dq.rotate(-4)
print(dq)                   # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)

dq.appendleft(-1)
print(dq)                   # deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

dq.extend([11, 22, 33])
print(dq)                   # deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)

dq.extendleft([10, 20, 30, 40])
print(dq)                   # deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)


# Soapbox
# Mixed bag lists
l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]

try:
    sorted(l)
except TypeError as e:
    print(repr(e))          # TypeError("'<' not supported between instances of 'str' and 'int'")



# Key is brilliant
l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
print(sorted(l, key=int))   # [0, '1', 5, 6, '9', 14, 19, '23', 28, '28']
print(sorted(l, key=str))   # [0, '1', 14, 19, '23', 28, '28', 5, 6, '9']