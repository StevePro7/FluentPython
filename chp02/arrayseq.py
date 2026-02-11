import os

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