# special methods

look [here](https://docs.python.org/3/reference/datamodel.html)  

## str vs repr

+ __repr__ goal is to be unambiguous  
+ __str__ goal is to be readable  
+ Container’s __str__ uses contained objects’ __repr__  

## bool

By default considered as truth, unless...  
Calls `__bool__` and, if not defined, returns the result of `__len__`  

# Containers

+ _container sequences_: hold references to the objects they contain  
    - `list`, `tuple`, `collections.deque`  
+ _flat sequences_: hold items of one type (those are faster)  
    - `str`, `bytes`, `bytearray`, `memoryview`, `array.array`  

If you frequently add elements to end or start: `deque`  
If you frequenly use `in` operator: `set`  
Have strict memory: any flat sequence (`array.array`)  

## Generating sequences

Listcoms (compute all and then return):  
```python
[ord(symbol) for symbol in symbols]
```

Generator Expressions (use iterator protocol (returning one a time) which saves
memory)  
```python
(ord(symbol) for symbol in symbols)
```
_useful example_:  
```python
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
```

## Tuple unpacking

use `*` to grab excess elements (will be zero array, if there are no excess
elements).  

read more [here](https://www.python.org/dev/peps/pep-3132/)  

## Named Tuples

Just generator for sublasses of `tuple` enhanced with field names and a class
name (helps debugging)  
You can define namedtuple field with space-delimited string or by iterable of
strings  
Use less memory then regular class instance, because it doesn't store `__dict__`
per object  

Few attributes:  
+ `_fields`  
+ `_make(iterable)`: allow to instantiate a named tuple from an iterable  
+ `_asdict()`: returns a `collections.OrderedDict`  

## Slices

When you call `seq[1:2:3]` you actually call `seq.__getitem__(slice(1,2,3))`.
Also you can name your slices for reuse  

Ellipsis can be used (return `ellipsis` class):  
```python
x[i, ...] # same as
x[i, :, :, :,]
```

Also, you can assign to slices `l[3::2] = [11, 22]` (but only iterable).  

Beware of expressions like `a * list` with mutable objects because `my_list =
[[]] * 3` will produce three references to the same inner list. Best way to do
this, is with list comprehension: `my_list = [[] for _ in range(3)]`  

## Arrays

+ `arr.tofile(fp)`: save bytecode (`open("file", "wb")`)  
+ `arr.fromfile(fp, qty)`: reads `qty` elements from file  

Read\write is much faster then list, but you may use `pickle` for that as well  

## Queues

### Dequeue

+ `deque(range(10), maxlen=10)`: set maximum number of items (extending further
  will cut off items on other edge)  
+ `deque.rotate`: rotates items  
+ `deque.extend(container)`: extends (if inserted on left, order is reversed)  

### Queue (LifoQueue, PriorityQueue)

When extended number `maxsize`, object will wait till some thread will decrease
number of elements (handy for thread population)  

### Multiprocessing

Desisgned for interprocess communication. `multiprocessing.JoinableQueue` for
easier task management.  

### Asyncio

All above queues together. Developed for managing tasks in asynchronous
programming.  

### Heqapq

Provides functions that let you use a mutable sesquence as a heap queue or
priority queue.  

## Memory Views

It is shared-memory sequence type:  

+ allows to handle slices of arrays without copying bytes  
+ `memoryview.cast`: change how bytes interpreted (cast float to int)  

read more [here](https://eli.thegreenplace.net/2011/11/28/less-copies-in-python-with-the-buffer-protocol-and-memoryviews/)  

## Sorting

[read this](https://docs.python.org/3/howto/sorting.html)

## Sorted containers

+ `bisect.bisect`: searches position to insert  
+ `bisect.insort`: inserts in sorted container so order is not disrupted  

## NumPy

Advanced array operations  

+ offers high-level operations for loading, saving, and operating on all
  elements of a `numpy.ndarray`  

## SciPy

Scientific computing algorithms  

## Pandas and Blaze

Data analysis libraries. Provide efficient array types that can hold nonnumeric
data. As well can import/export functions compatible with with many different
formats (`.csv`, `xls`, SQL dumps, etc)  

## Conventions

If you change object, you should return `None`  

# Profiling

Example:  

```python
import numpy

floats = numpy.loadtxt('floats-10M-lines.txt')

from time import perf_counter as pc

t0 = pc(); floats /= 3; pc() - t0
```

