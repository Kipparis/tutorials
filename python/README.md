# General Structure of file <!-- {{{ -->
__primitive call__ == nonrecursive function call  
```python
def _test():				# for testing purpose
    import doctest	# may be used any package from `testing` section
    doctest.testmod()

if __name__ == "__main__":  # for execution
    _test()
```
<!-- }}} -->
# Debugging, Testing, and Profiling <!-- {{{ -->
## Debugging <!-- {{{ -->
__Tracebacks__ should be read from last line.   
__!Warning!__ catching all exceptions will lead to when user presses Ctrl+C the
  program won't stop and you lock the user.  
### Exception chaining
```python
class InvalidDataError(Exception): pass

def process(data):
  try:
    i = int(data)
    ...
  except ValueError as err:
    raise InvalidDataError("Invalid data received") from err
```

### Scientific Debugging
1. Think up an explanation  
2. Create an experiment to test  
3. Tun the experiment  
Check the incoming parameters up to call stack. Check local variables
and return value.  
Use statement: `print(locals(), "\n")`  

Use debugger __pbd__ as
```
$ python3 -m pdb my_program.py
```
orrrrrr
```	python
import pdb
pdb.set_trace()
```
Use of debugger __IDLE__  
<!-- }}} -->
## Testing <!-- {{{ -->
__Unit testing__ - e.g. testing individual functions, classes, and methods, to ensure that
they begave as expected.  
Key point of __TDD__(Test Driven Development) is when we want to add a feature - we first write a
test for it.  
In functions that __doesn't return anything__, can be usefull to return fake
objects - thurd-party modules that provide "mock" objects.  
  
Python provides two unit testing modules:  
+ doctest  
+ unittest  
__Third-party__ testing tools:
+ nose  
+ py.test  

Writing doctests:  
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
For programs:  
```python
if __name__ == "__main__":
    main()
```
then: `python3 -m doctest blocks.py`   

Module __unittest__ can act like doctest:  
```python
import doctest
import unittest
import blocks
suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(blocks))
runner = unittest.TextTestRunner()
print(runner.run(suite))
```

__Unittest__ module defines four key concepts:   
+ test fixture - the code necessary to set up a test  
+ test suite - collection of test cases  
+ test case - basic unit of testing  
+ test runner - object that executes one or more test suites  

__Test suite__ created by inheritace _unittest.TestCase_ class.  
__Test case__ = each method with name starting with "test".  
+ set up in `setUp();`  
+ cleanup in `tearDown();`  
various __unittest.TestCase__ methods:
+ `assertTrue()`  
+ `assertEqual()`  
+ `assertAlmostEqual()` -- testing floating-point numbers  
+ `assertRaises()`  
+ many more
ends with:
```python
if __name__ == "__main__":
    unittest.main()
```

Running from __external file__:
```python
import unittest
import test_Atomic

suite =
unittest.TestLoader().loadTestsFromTestCase(test_Aromic.TestAtomic)
runner = unittest.TextTestRunner()
print(runner.run(suite))
```

__asserting exceptions__:
```python
with self.asssertRaises(AttributeError):
    ...
```
<!-- }}} -->
## Profiling <!-- {{{ -->
Best practices:  
+ prefer tuples to lists when a __read-only sequence is needed__  
+ __use generators__ rather than creating large upbles or lists  
+ use python's __built-in data structures__  
+ instead of concatenating strings, turn them into list of strings and 
\   then join the list of strings into a single string at the end  
+ when object accessed a large number of times using attribute access, 
\   it may be better to create and use local variable that refers to the
\   object to provide faster access  
+ fast creating constants:  
    ```python
    Const = collections.namedtuple("_", "min max")(191, 591)
    Const.min, Const.max
    ```
<!-- }}} -->

two modules for investigating the performance of out code:  
+ timeit - timing small pieces of out code  
+ cProfile - find bottlenecks  

### timeit
```python
if __name__ == "__main__":
    repeats = 1000
    for function in ("func_a", "func_b", "func_c"):
        t = timeit.Timer("{0}(X, Y)".format(function), "from __main__ import
            {0}, X, Y".format(function))
    sec = t.timeit(repeats)/ repeats
    print("{function}() {sec:.6f} sec".format(**locals()))
```
run it from cli:  
```shell
python3 -m timeit -n 1000 -s "from MyModule import function_a, X, Y"
    "function_a(X, Y)"
```

### cProfile
```python
if __name__ == "__main__":
    for function in ("function_a", "function_b", "function_c":
        cProfile.run("for i in range(1000): {0}(X, Y)".format(function))
```
cli:  
```shell
python3 -m cProfile programOrModule.py
```
we can do:
```python
cProfile.run("function_b()")
python3 -m cProfile -o profileDataFile programOrModule.py
```
, then use __pstats__
<!-- }}} -->
<!-- }}} -->
# Classes <!-- {{{ -->
## Special Methods <!-- {{{ -->
+ __bool__ - useful for if  
+ __format__ - provides str.format()  
+ __init__  
+ etc
<!-- }}} -->
## Variables <!-- {{{ -->
### How they are inited
```
f = FuzzyBool(0.7) <=> {
    FuzzyBool.__new__(FuzzyBool, 0.7)
    fuzzy.__init__()
}
```
### Optimizing class variables
when assigning object attributes we can use folowing structure
```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
```
it works __faster__. if subclassing, we have to reimplement __slots__  
if empty => __slots__ = ()  
### Creating attributes on fly
```python
class Ords:
    def __getattr__(self, char):
        return ord(char)
```
when accessing attributes first call is __getattribute__(), then __getattr__()  
+ getattribute -- invoked before looking at the actual attributes  
    Warning! Using this function may lead to recursion in field lookup  
+ getattr -- invoked if the attribute wasn't found the usual ways  

<!-- }}} -->
## Function manipulation <!-- {{{ -->
make function unimplemented
```python
def __add__(self, other):
    raise NotImplementedError()
# more nicely
raise TypeError("unsupported operand type(s) for +: "
                "'{0}' and '{1}'".format(self.__class__.__name__, other.__class__.__name__))
                )
```
calling functions according to input:
```python
functions = dict(a=add_dvd, e=edit_dvd, l=list_dvds, 
            r=remove_dvd, i=import_, x=export, q=quit)
functions[action](db)
```
<!-- }}} -->
## Descriptors <!-- {{{ -->
Descriptors are classes which provide access control for the attributes of
other classes.
<!-- }}} -->
## Context managers <!-- {{{ -->
syntax:  
_`with expression as variable: suite`_
open 2 or more context managers in one statement
```python
try:
    with(open(source) as fin, open(target, "w") as fout:
```
<!-- }}} -->
## Class Decorators <!-- {{{ -->
same as func decorators
<!-- }}} -->
## Abstract Base Classes <!-- {{{ -->
__Why?__ kind of promise - a promise that any derived class will provide the methods and properties that
the abstract base class specifies  
__two main groups__ of abs -- numbers and collections.  

example abstract class
```python
class Appliance(metaclass=abc.ABCMeta): # any subclass can be used
  # defines method that _must be_ reimplemented
  @abc.abstractmethod
  def __init__(self, model, price):
    self.__model = model
    self.price = price

  def get_price(self):
    return self.__price

  def set_price(self):
    self.__price = price

  # force reimplementing price property
  price = abc.abstractproperty(get_price, set_price)
  
  @property
  def model(self):
    return self.__model
```
default use of abs
```python
class Cooker(Appliance):
  def __init__(self, model, price, fuel):
    super().__init__(model, price)
    self.fuel = fuel

  price = property(lambda self: super().price,
                  lambda self, price: super().set_price(price))
```
simpler example of abs:  
```python
class TextFilter(metaclass=abc.ABCMeta):
  @abc.abstractproperty
  def is_transformet(self):
    raise NotImplementedError()

  @abc.abstractmethod
  def __call__(self):
    raise NotImplementedError()
```

register subcluss to python standart abc hierarchy
```python
class SortedList:
  ...
collections.Sequence.register(SortedList)
```
_now we can check if subclass is list or not_  
  

metaclass that checks that methods are present
```python
class LoadableSaveable(type):
	def __init__(cls, classname, bases, dictionary):
		super().__init__(classname, bases, dictionary)
		assert hasattr(cls, "load") and isinstance(getattr(cls, "load"), collections.Callable),
                      ("class '" + classname + "' must provide a load() method")
```
cls - instance of calling class
bases - base classes
dictionary - attributes
<!-- }}} -->
<!-- }}} -->
# Lists <!-- {{{ -->
generator expressions:  
+ `(expression for item in iterable)`  
+ `(expression for item in iterable if condition)`  
generator via functions:  
```python
def quarters(next_quarter=0.0):
    while True:
        yield next_quarter
        next_quarter += 0.25
```
generators with control flow
```python
def quarters(next_quarter=0.0):
    while True:
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received
```
use:
```python
generator = quarters()
x = next(generator)
x = generator.send(1.0)
```
<!-- }}} -->
# Dynamic code execution <!-- {{{ -->
```python
import math
code = '''
def area_of_sphere(r):
  return 4 * math.pi * r ** 2
'''
context = {}
context['math'] = math
exec(code, context)
# grab the function after execution
area_of_sphere = context["area_of_sphere"]
```
all we path in context will be available in prog, and vice versa all is stored after
code execution will be available in context. so we can use 
context = globals().copy() to not override current dict  
+ `exec` -- can handle any amount of code  
+ `eval` -- can handle only single expression  
use of function.cache = {} to memoize data, _like here `https://jeremykun.com/2012/03/22/caching-and-memoization/`_  
<!-- }}} -->
# Functions <!-- {{{ -->
## Decorators <!-- {{{ --> 
__decorators__ - one who take function and incorporates it with additional functionality and returns it
example:
```python
def positive_result(function):
	def wrapper(*args, **kwargs):
		result = function(*args, **kwargs)
		assert result >= 0, function.__name__ + "() result isn't >= 0"
		return result
	wrapper.__name__ = function.__name__
	wrapper.__doc__ = function.__doc__
	return wrapper
```
or:
```python
def positive_result(function):
	@functools.wraps(function)
	def wrapper(*args, **kwargs):
		result = function(*args, **kwargs)
		assert result >= 0, function.__name__ + "() result isn't >= 0"
		return result
	return wrapper
```
decorators __with argumets__
```
@bounded(0, 100)
def percent(amount, total):
	return( amount / total) * 100

# implementation:
def bounded(min, max):
	def decorator(function):
		@functools.wraps
		def wrapper(*args, **kwargs):
			result = function(*args, **kwargs)
			if result < min: return min
			if result > max: return max
		return wrapper
	return decorator
```
<!-- }}} -->
## Functors <!-- {{{ -->
```python
class Strip:	# strip passed characters
    def __init__(self, characters):
        self.characters = characters

    def __call__(self, string):
        return string.string(self.characters)
```
more simple way (and less greedy)  
```python
def make_strip_function(characters):
    def strip_function(string):
        return string.strip(characters)
    return strip_function
```
enother example
```python
class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names

    def __call__(self, instance):
        values = []
        for attribute_name in self.attribute_names:
            values.append(getattr(instance, attribute_name))
        return values
```
<!-- }}} -->
## Functional-Style Programming <!-- {{{ -->
__mapping__ - calling function on each item from iterable:  
`list(map(lambda x: x**2, [1, 2, 3, 4]))   # returns: [1, 4, 9, 16]`  

__filtering__ - taking one iterable and producing anothe:  
`list(filter(lambda x: x > 0, [1, -2, 3, -4]))   # returns: [1, 3]`

__reduce__ - upply function on first two elements, then on result and  third element and etc:  
```python
functools.reduce(lambda x, y: x * y, [1, 2, 3, 4]) # returns: 24
functools.reduce(operator.mul, [1, 2, 3, 4]) # returns: 24
```
python built-in reducing functions:  
_all(), any(), max(), min(), sum()_  
  
operator contains all operators  
operator module provides the operator.attrgetter() and operator.itemgetter()  
if list holds objects with priority attribute, we can sort the list like this:  
`L.sort(key=operator.attrgetter("priority"))`

iterate over several lists:
```python
for value in itertools.chain(data_list1, data_list2, data_list3):
	total += value
```
<!-- }}} -->
## Partial Function Application <!-- {{{ -->
Creating one function from another but with fixed arguments
```python
enumerate1 = functools.partial(enumerate, start=1)
for lino, line in enumerate1(lines):
  process_line(i, line)
```
<!-- }}} -->
## Coroutines <!-- {{{ -->
Coroutine - function that has at least one _yield_ expression.  
to gain from function: `while True: match = (yield)`  
to send to function:   `matcher.send(html)`  
at the end call:	   `matcher.close()`  
<!-- }}} -->
## Creating pipelines <!-- {{{ -->
`pipeline = get_data(process(reporter()))`
<!-- }}} -->
<!-- }}} -->
# Processes and Threading <!-- {{{ -->
## Subprocess
__Subprocess__ module provides facilities for tunning other programs and
communicating using pipes.  
example in grep-p, and grep-p-child:  

+ how to create child  
+ how to pass arguments and nicely call same interpreter  
+ how to write and read  
+ how to wait for them and exit  

## Threading
Threads __are created__ by `threading.Thread(callable)` or we can pass subclass
of `threading.Thread`.  
Threads __are only started__ by `.start()` and they will wait until it's
possible.

**_example in grep-t.py_**  
methods to use:  

+ Worker class inherits `multiprocessing.Process`  
+ `multiprocessing.JoinableQueue` instead of `queue.Queue`  

### Serialized queue 
__queue.Queue__ provides:
+ FIFO  
+ LIFO  
+ PriorityQueue - garantee that only one thread has access
 (_serialize access_)  

use of working __queue__:  

+ `queue.put()` to add task  
+ `queue.get()` to get task  
+ `queue.task_done()` complete task  
+ `queue.join()` wait until all tasks are done  

### Locking 
to use own __lock__ write next:  
in class: `_lock = threading.Lock()`  
in function:   
```python
with self._lock:
    ***
```
this will ensure that all class objects share the same lock and not
access object at the same time.  

other available locks:  

+ `threading.RLock` - can be used again by thread who blocked  
+ `threading.Semaphore` - protect specific number of resources  
+ `threading.Condition` - provides a wait condition  

---  

Could use __multiprocessing__ module. It could be faster becouse each 
processor can be executed on separate core.  

You can't archive best performance becouse CPython enterpreter can
execute Python code on only one processor at a time, even using multiple
threads.  

With threading we devise come kind of communication, shared memory (mmap
module), shared files or networking.  
<!-- }}} -->
# Networking <!-- {{{ p. 465 -->
__UDP__ - it's not necessary to create reliable connection  
__TCP__ - reliable connection and stream-oriented protocol  

__socketserver__ module handles the communication,
servicing each connection request, either serially or on own separate thread or
process  

Create server using inheritance from `socketserver.Threading(Forking)MixIn` and
`socketserver.TCPServer # or UDP`  

`-> server = CarRegistrationServer(("", 9653), RequestHandler)` - 
__RequestHandler__ - class which will handle request  
`-> server.serve_forever()` - 
at the end of try block with server write saving and shutdown  

in `handle(self)` function read data from self.rfile 
and write data to self.wfile  
<!-- }}} -->
# Database programming <!-- {{{ -->
Pypi contains many database-related packages and interfaces to popular
client/server databases.  
More Pythonic way to interact with databases is use of __ORM__ _(Object
Relational Mapper)_ : SQLAlchemy and SQLObject  
<!-- }}} -->
# Regular Expressions <!-- {{{ -->
Every character match one occurance.  
Special characters have to be escaped: `\.^$?+*{}[]()|`  
	+ `[]` - character class: means __match one of the set__.
	+ `[0-9]` - means range, ^ in the beginning negate condition so
	+ `[^0-9]` - not a digit.
_example:_ `[\dA-Fa-f]` matches any hexadecimal digit.  
	+ `e{m,n}` - e is minimum m and max n times meet in expression  
	+ `e{m,m}` can be write as `e{m}`  
	+ `?` means `{0,1}`  
example: travell?ed matches: traveled, travelled   
	+ `+` means `{1,n}` - detecting typos couse 
by pressing a key too long (bevell+ed)  
	+ `*` means `{0,n}` - leads to unexpected results
	+ `??`, `+?`, `*?` - nongreedily match  
### Shortcuts
	+ `.` any character except newline (or any character with re.DOTALL flag)  
	+ `\d` Unicode digit; `[0-9]` with re.ASCII flag  
	+ `\D` Unicode nondigit; `[^0-9]`  
	+ `\s` Unicode whitespace; `[ \t\n\r\f\v]`  
	+ `\S` Unicode nonwhitespace; `[^ --\\--]`  
	+ `\w` Unicode "word" character; `[a-zA-Z0-9_]`  
	+ `\W` Unicode non-"word" character; `[^ --\\--]`  

<!-- }}} -->

