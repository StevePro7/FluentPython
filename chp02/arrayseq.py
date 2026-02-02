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


# Ex 2-8        Unpacking sequences and iterables
latitude, longitude = lax_coordinates       # unpacking
print(latitude)
print(longitude)