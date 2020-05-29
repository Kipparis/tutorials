<!-- книга: с++ premier -->
<!-- если какой-либо термин непонятен, в книге, в конце каждой главы есть -->
<!-- определения -->
# Data types<!-- {{{ -->
## Pointers, reference<!-- {{{ -->
_diff btw pointer and reference_. reference is not an object, hence, once we 
defined reference, we cannot make that reference refer to another
object.  

`void*` pointer can hold the address of __any object__.  
<!-- }}} -->
## Strings<!-- {{{ -->
include:  
```cpp
#include <string>
using std::string;
```
init:  
    + __direct__ init: `string s7(10, 'c')` <=> `"cccccccccc"`
    + __copy__ init: `string s8 = string(10, 'c')` -- result is same but creates temp string to make copy.  

you can use __conditions__ while working with strings:  
```cpp
while (cin >> word)         { /* body */ }
while (getline(cin, line))  { /* body */ }
```
### Notes<!-- {{{ -->
`string.size()` returns `string::size_type` type which is unsigned. 
So don't mix up _int_ and _unsigned_ values.
    
You need know what type char is __cctype__ library helps.
 For example:  
    + `isalnum()`  
    + `tolower()`  
    + `isgraph()`  
    + `islower()`  
<!-- }}} -->
<!-- }}} -->
## Arrays<!-- {{{ -->
when use arrays, the compiler automatically 
substitutes a __pointer to the first element__.  

when use multidim arrays in range for, 
the loop control variable for all but the innermost array 
__must be references__.

iterating over container:  
`index != s.size() && !isspace(s[index])`  
<!-- }}} -->
<!-- }}} -->
# Operations<!-- {{{ -->
__Division__ is rounded towards zero.  

__Assignment__ operator is right associative.  
__Shift__ operators are left associative.

<!-- hmm -->
<!-- if m = (m / n) * n + m % n  then  m has the same sign as m % n -->

<!-- again hmmm -->
__Comma operator__ is left associative, the result is right-hand expression 
will be lvalue if right-hand operand is an lvalue  

## Conditions<!-- {{{ -->
Binary operations are left associative <=> first evaluated left assigment.  
`if (i < j < k)` => _k_ compared to 1 ( bool result of i < j )  
`if ( val == true )` == `if ( val == 1 )`  

condition operator may result as _rvalue_ as _lvalue_.  
<!-- }}} -->
## Explicit conversion<!-- {{{ -->
_Syntax:_ `cast-name<type>(expression)`  
where type is:  

+ `static_cast`  
+ `dynamic_cast`  
+ `const_cast`  
+ `reinterpret_cast`  

why? to not loose precision or to cast `void*` to any other pointer  
<!-- }}} -->
## Statements<!-- {{{ -->
### Decision branches<!-- {{{ -->
__if-else -- wrong path__
```cpp
// execution does not match indentation; the else goes with the inner if
if (grade % 10 >= 3)
    if (grade % 10 > 7)
        lettergrade += '+';
else
    lettergrade += '-';
```

__define and init variable for a particular case__
```cpp
case true:
  { // defining without curly braces may lead to bypassing
    string file_name = get_file_name();
  }
```
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Exception handling<!-- {{{ -->
Throw exception - `throw exception;`  

To catch it use:  
```cpp
try {
  program-statements
} catch (exception-declaration) {
  handler-statements
} catch (exception-declaration) {
  handler-statements
}
```

__exception classes__ defined in `<stdexcept>`:
+ `exception`  
+ `runtime_error`  
+ `range_error`  

+ `overflow_error`  
+ `underflow_error`  
+ `logic_error`  
+ `domain_error`  
+ `invalid_argument`  
+ `length_error`  
+ `out_of_range`  

## Assert<!-- {{{ -->
`assert` executes only if _NDEBUG_ is not defined.
if your want to turn off asserts => provide #define NDEBUG 
  or
CC -D NDEBUG main.c
<!-- }}} -->
<!-- }}} -->
# Functions<!-- {{{ -->
you may define defaults for parameters, however, if a parameter has a
__default argument__, all the parameters that follow it must also have
default arguments.

__inline function__ usually expanded "in line" at each call:
```cpp
cout << shorterString(s1, s2) << endl;
cout << (s1.size() < s2.size() ? s1 : s2) << endl
```

### Pointers to function<!-- {{{ -->
function that return pointers to function:  
`auto f1(int) -> int(*)(int*,int);`  
or make it via typedef:  
```cpp
typedef bool Func(const string&, const string&);	# by type
typedef decltype(lengthCompare) Func2;	# by another function
```
<!-- }}} -->
<!-- }}} -->
# Classes<!-- {{{ -->
### Class vs struct<!-- {{{ -->
The only difference is that variables before the first access specifier:  

+ in class they are private  
+ in struct they are public  

assume next struct:
```cpp
struct Sales_data {
  std::string isbn() const { return bookNo; }
  Sales_data& combine(const Sales_data&);
  double avg_price() const;
  
  std::string bookNo;
  unsigned units_sold = 0;
  double revenue = 0.0;
};
```
<!-- }}} -->
## Access Control and Encapsulation<!-- {{{ -->
+ Members defined after a public specifier are accessible to all 
parts of the program  
+ Members defined after a private specifier are accessible to the
member functions of the class  

__To access non public__ members of class precede it's declaration with 
'friend' keyword
<!-- }}} -->
## Functions<!-- {{{ -->
__member functions__ access the object on which they were called through an
extra implicit parameter named this. So when we call `total.isbn()` 
the compiler calls `Sales_data::isbn(&total)`  

__const member functions__ - modify type of _this_ so function doesn't
change it (becouse _this_ doesn't appear in parameter list, write
_const_ before body).  

To __define Member Function__ outside the Class use following structure:  
```cpp
double Sales_data::avg_price() const {
    if (units_sold)
        return revenue/units_sold;
    else
        return 0;
}
```

To __return this__ object (for chaining like +=)
```cpp
Sales_data& Sales_data::combine(const Sales_data& rhs) {
  units_sold += rhs.units_sold;
  revenue += rhs.revenue;
  return *this;
}
```

Returning current object as reference allows 
us __chain operations__ like: `myScreen.move(4,0).set('#');`  

__Member functions defined inside the class are automatically inline!__
<!-- }}} -->
## Constructors<!-- {{{ -->
Force compiler to provide default constructor: `Sales_data() = default;`  
Constructor initializer list provides initial values for data members:
```cpp
Sales_data(const std::string &s, unsigned n, double p):
  bookNo(s), units_sold(n), revenue(p*n) { }
```

We must use the constructor initializer list to provide values for
members that are const, reference, or of a class type that __does not have
a default constuctor__.  

__Init list doesn't specify order__ in witch variables are initialized, they
are init in order they appear in class definition.  

__Delegating contructors *(c++11)*__
```cpp
// deligate-to constructor
Sales_data(std::string s, unsigned cnt, double price):
    bookNo(s), units_sold(cnt), revenue(cnt*price) {}
// contructor that delegate to another constructor
Sales_data(): Sales_data("", 0, 0) {}
```
### Default Constructor<!-- {{{ -->
Default constructor is used automatically on object default or value
initialization.  
__Default__ initializetion happens:  
    + Define `nonstatic` variables or `arrays` at block scope without initializers  
    + Class itself has members of class usesthe synthesized default 
  constructor  
    + Members of class type are not explicitly initialized in a
  constructor initializer list  
__Value__ initialization happens:  
    + During array initialization when we provide fewer initializers
  than the size of the array  
    + Define a local static object without an initializer  
    + Explicitly request value initialization by writing an expressions
  of the form T() where T is the name of a type (vector use that to
  value initialize its element inializer).  
  
Using default constructor:   
```cpp
Sales_data obj();   // ok: but it defines a function, not an object
Sales_data obj;     // ok: object
```
<!-- }}} -->
<!-- }}} -->
## Implicit Class-Type conversions  <!-- {{{ -->
_aka converting contructors._  
Every constructor that can be called with a __single argument__ defines an
__implicit conversion__ to a class type.  
_Note:_ Compiler applies only one class-type conversion:   
```cpp
// error: requires two user-defined conversions:
//      (1) convert "9-999-99999-9" to string
//      (2) convert that(temporary) string to Sales_data
item.combine("9-999-99999-9");
```
We can do this, by explicitly calling conversion
```cpp
item.combine(string("9-999-99999-9"));      // ok
item.combine(Sales_data("9-999-99999-9"));  // ok
```
### Prevent the use of constructor in implicit conversion  <!-- {{{ -->
```cpp
explicit Sales_data(const std::string &s): bookNo(s) { }
explicit Sales_data(std::istream&);
```
`explicit` keyword is meaningful only on constructors with single
argument.  
__Note!__ Explicit keyword is used only on the constructor declaration
inside the class.  
More `explicit` examples:  
```cpp
Sales_data item1(null_book);    // ok: direct initialization
Sales_data item2 = null_book;   // error: can't use copy form of init
```
We can use explicit constructors for an implicit conversion:  
```cpp
item.combine(Sales_data(null_book));
```
<!-- }}} -->
### Library Classes<!-- {{{ -->
    + `string` constructor with arg of `const char*` is not explicit  
    + `vector` constructor that takes a size is explicit  
<!-- }}} -->
<!-- }}} -->
## Aggregate Classes  <!-- {{{ -->
__aggregate class__ gives users direct access to its members and has
special initialization syntax. A class is aggregate if:  
    + All of its data members are public  
    + It does not define any constructors  
    + It has no in-class initializers  
    + It has no base classes or `virtual` functions  
_example_:  
```cpp
struct Data {
    int ival;
    string s;
};
```
Initialize data members by providing a praced list of member
initializers: `Data val1 = { 0, "Anna" };`  
<!-- }}} -->
## Data types <!-- {{{ -->
__mutable__ data member can be changed inside of const functions
Defining class member types: `typedef std::string::size_type pos;`  
or: `using pos = std::string::size_type;`  

to get name __from outer scope__ use ::height;
<!-- }}} -->
## Literal Classes<!-- {{{ -->
Literal class - a class whose data members are __all of literal
type__.  
Literal classes may have function members that are `constexpr`. These
member functions are implicitly `const`.  
Restrictions to be literal class:   

+ must have at least one `constexpr` contructor  
+ must use default definition for its destructor

### Constexpr constructors<!-- {{{ -->
+ Declared as `= default;`  
+ Or must meet the requirements of a constructur.  
+ the only executable statement it can have is a _return_ statement.  
+ must initilize every data member  
    * initializers either constexpr constructors  
    * either constant expression  

Example: `constexpr Debug(book b = true): hw(b), io(b), other(b) {}`  
<!-- }}} -->
<!-- }}} -->
## Static Class Members <!-- {{{ -->
Use **_static class members_** when value represent more class value
than object value. When changing **_static_** field it changing in all
objects.  
### Declaring  `static` Members <!-- {{{ -->
```cpp
class Account {
public:
    void calculate() { amount += amount * interestRate; }
    static double rate() { return interestRate; }
    static void rate(double);
private:
    std::string owner;
    double amount;
    static double interestRate;
    static dou ble initRate();
};
```

+ `static` members of a class exist outside any object, they are shared
  by all the _Account_ objects.  
+ `static` member function are not bound to any object &rarr; they do
  not have a `this` pointer. &rarr; `static` member functions may not be
  declared as a `const`.  

<!-- }}} -->
### Defining `static` Members <!-- {{{ -->
When we define `static` member outside the class, we do not repeat the `static` keyword.  
Because `static` data members are not part of objects, they are not defined when we
create objects of the class. They are not initialized by the class' constructor.
We may not initialize a `static` member inside the class.  
Instead, we must define and initilize each `static` data member **outside
the class body**.  
Like _global objects_, `static` data members are defined outside any
function &rarr; once they are defined, they continue to exist until the
program completes.  

Example:  
```cpp
// define and initialize a static class member
double Account::interestRate = initRate();
```

Once the class name is seen, the remainder of the definition is **_in
the scope of the class_** &rarr; we can use `initRate` without
qualification.  
Not also that even though `initRate` is _private_, we can use this
function to initialize `interestRate`. The definition of last _(like any
other member definition)_, has access to the _private_ members of the
class.  
<!-- }}} -->
### In-Class Initialization of `static` Data Members <!-- {{{ -->
<!-- p. 391 -->
Example:
```cpp
class Account {
public:
    static double rate() { return interestRate; }
    static void rate(double);
private:
    static constexpr int period = 30;   // perios is a constant
    //  expression
    double daily_tbl[period];
};
```

If we use the member in a context in which the value cannot be
substituted, then there must be a definition for that member.  

**Best Practices.** Even if a `const static` data member is initialized
in the class body, that member ordinarily should be defined outside the
class definition.  
<!-- }}} -->
### Using a Class `static` Member <!-- {{{ -->
+ Access static member using the scope operator  
    `double r = Account::rate()`  
+ through object or reference  
    `r = ac1.rate();`  
+ through pointer to an Account object  
    `r = ac2->rate();`  
+ **_member functions_** can use `static` members directly, without the
  scope operator  
<!-- }}} -->
### `static` Members Can Be Used in Ways Ordinary Members Can't <!-- {{{ -->
+ Can have **_incomplete_** type:  
```cpp
class Bar {
public:
    // ...
private:
    static Bar mem1;    // ok: static member can have incomplete type
    Bar *mem1;          // ok:pointer member can have incomplete type
    Bar mem3;           // error:data members must have complete type
};
```
+ A one can use `static` member as a default argument:  
```cpp
class Screen {
public:
    // bkground refers to the static member
    // declared later in the class definition
    Screen& clear(char = bkground);
private:
    static const char bkground;
};
```


<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# IO Library<!-- {{{ -->
manipulating with input and output:
```cpp
istream &read(istream &is, Sales_data &item) {
    double price = 0;
    is >> item.bookNo >> item.units_sold >> price;
    item.revenue = price * item.units_sold;
    return is;
}
```
## IO classes <!-- {{{ -->
All support to different kinds of IO processing in splitted on 3
headers:  

+ `iostream` - defines the basic types used to read from and write to a
  stream  
    * `istream`, `wistream` reads from a stream  
    * `ostream`, `wostream` writes to a stream  
    * `iostream`, `wiostream` reads and writes a stream  
+ `fstream` - defines the types used to read and write named files  
    * `ifstream`, `wifstream` reads from a file  
    * rest two  
+ `sstream` - defines the types used to read and write in-memory
  _strings_  
    * `istringstream`, `wistringstream` reads from a _string_  
    * rest two  

To support languages that use wide characters, the library defines a set
of types and objects that manipulate `wchar_t` data. The names of the
wide-character versions begin with a `w` (`wcin`, `wcout`, etc)  

The library lets us ignore the difference between different kinds of
stream by using **_inheritance_**. _For example._ Types _ifstream_ and
_istringstream_ inherit from _istream_. Thus, we can call `getline` on
an _ifstream_ or _istringstream_ object and we can use the `>>` operator
on both of them.  

**No copy or Assign for IO Objects.** Thus we cannot have a parameter or
return type that is one of stream types. Stream is passed only by
reference.  
<!-- }}} -->
## Condition States <!-- {{{ -->
IO classes define functions and flags, listed below, that let us access
and manipulate the **_condition state_** of a stream.  

_strm_ is one of the IO types.  

|                   |                                                                                |
| ---               | ---                                                                            |
| strm::iostate     | machine-dependent integral type that represents the condition state of stream. |
| strm::badbit      | it's value is used to indicate that a stream is corrupted (`s.bad()`)          |
| strm::failbit     | it's value is used to indicate that an IO operation failed (`s.fail()`)        |
| strm::eofbit      | used to indicate that a stream hit end-of-file (or `s.eof()` bit)              |
| strm::goodbit     | used to indicate that a stream is not in an error state (`s.good()`)           |
| s.clear()         | reset all condition values in the stream s to valid state                      |
| s.clear(flags)    | reset the condition of s to flags. Type of slags is stdm::iostate              |
| s.setstate(flags) | adds specified conditions to s.  _flags_'s type is strm::iostate               |
| s.rdstate()       | strm::iostate value from _s_                                                   |

Consider this:  
```cpp
int ival;
cin >> ival;    // we enter Boo on the sti
```

Executed this, cin will be in an error state.  
The easiest way to determine **_the state of a stream_** object is to use that
object as a condition:  
```cpp
while (cin >> word)
    // ok: read operation successful
```
<!-- }}} -->
## Integrrogating the State of a Stream <!-- {{{ -->
Using a stream as a condition tells us only whether the stream is valid, not
telling what happened.  

IO library defines a machine-dependent integral type named _iostate_ -
collection of bits. Also IO classes define four _constexpr_ values of type
iostate that represent particular bit patterns.  

Right way to determine the state of a stream is to use either `good()`
or `fail()`.  
<!-- }}} -->
## Managing the Condition State <!-- {{{ -->
The following turns off `failbit` and `badbit` but leaves eofbit untouched:  
```cpp
cin.clear(cin.rdstate() & ~cin.failbit & ~cin.badbit);
```

<!-- }}} -->
## Managing the Output Buffer <!-- {{{ -->
When the following code is executed:
```cpp
os << "plrese enter a value: ";
```
the string might be printed immediately, or the operating system might store
the data in a buffer to be printed later.  

There are several conditions that cause the buffer to be flushed: 

+ The program completes normally. All output buffers are flushed as part of the
  `return` from `main`;  
+ At some indeterminate time, the buffer can become full, in which case it will
  be flushed before writing the next value;  
+ We can flush the buffer explicitly using a manipulator such as `endl`;  
+ We can use the `unitbuf` manipulator to set the stream's intewrnal staate to
  mepty the buffer after each output operation;  
+ Stream might be tied to another stream. In this case, the buffer of the tied
  stream is flushed whenever the tied stream is read or written;  
    `cin` and `cerr` are both tied to `cout`. Hence, reading `cin` or writing to
    `cerr`flushed the buffer in `cout`.  

<!-- }}} -->
## Flushing the Output Buffer <!-- {{{ -->
```cpp
cout << "hi!" << endl;  // writes hi and a newline, then flushes the buffer
cout << "hi!" << flush; // writes hi, then flushes the buffer; adds no data
cout << "hi!" << ends;  // writes hi and a null, then flushes the buffer
```

**The unitbuf Manipulator**  

If we want to flush after every output:  

```cpp
cout << unitbuf;    // all writes will be flushed immediately
cout << nounitbuf;  // returns to normal buffering
```

**Caution: Buffers Are Not Flushed If the Program Crashes**  

#### Tying Input and Output Streams Together <!-- {{{ -->
When _cout_ tied to _cin_, the statement:  
`cin >> ival;`  
causes the buffer associated with _cout_ to be flushed. (so the welcom
message will appear before user input)  
**_Examples:_**

```cpp
cin.tie(&cout);     // illustration only: the library ties cin and cout
// old_tie points to the stream (if any) currently tied to cin
ostream *old_tie = cin.tie(nullptr);    // cin is no longer tied
// ties cin and cerr
cin.tie(&cerr);     // reading cin flushes cerr, not cout
cin.tie(old_tie);   // reestablish normal tie between cin and cout
```

<!-- }}} -->

<!-- }}} -->
## File Input and Output <!-- {{{ -->
The _fstream_ header defines three types to support file IO:  

+ `ifstream` to read from given file  
+ `ofstream` to write to a given file  
+ `fstream` which reads and writes a given file  

_fstream_-Specific Operations:  

+ _fstream_ fstrm; - Creates an unbound file stream.  
+ _fstream_ fstrm(s); - Creates an _fstream_ and opens the file named _s_.
  _s_ can have type `string` or pointer to a C-style character string.
  The default file mode depends on the type of _stream_.
+ _fstream_ fstrm(s, mode); - Like previous but opens in given mode
+ fstrm.open(s) - open and bind file to object
+ fstrm.open(s, mode) - -//- with given mode. Returns `void`.  
+ fstrm.close() - Closes the file to which _fstrm_ is bound. Returns `void`  
+ fstrm.is_open() - REturns a _bool_ indicating whether the file
  associated with  fstrm was successfully opened and has not been closed.  

_fstream_ is one of the types defined in the `fstream` header  

### Using File Stream Objects <!-- {{{ -->
When we supply a file name, `open` is called automatically:  
```cpp
ifstream in(ifile);     // construct an ifstream and open the given file
ofstream out;           // output file stream that is not associated with any file
```

<!-- }}} -->
### The open and close Members <!-- {{{ -->
If a call to _open_ fails, _failbit_ is set. Because a call to open
might fail, it is good to check this:  
```cpp
if (out)    // check that the open succeeded
    // the open succeeded, so we can use the file
```

To **_associate new file_**, we must close existing file, and then open
another.  

<!-- }}} -->
### Automatic Construction and Destruction <!-- {{{ -->
Consider a folowing program:  
```cpp
// for each file passed to the program
for (auto p = argv + 1; p != argv + argc; ++p) {
    ifstream input(*p);     // create input and open the file
    if (input) {            // if the file is ok, "process" this file
        process(input);
    } else
        cerr << "couldn't open: " + string(*p);
} // input goes out of scope and is destroyed on each iteration
```

Each iteration constructs a new `ifstream` object. Because `input` is
local to the _while_, it is created and destroyed on each iteration.
When an `fstream` object **_goes out of scope_**, the file it is bound to is
**_automatically closed_**.

<!-- }}} -->
### File Modes <!-- {{{ -->
Each stream has an associated _file mode_that represents how the file
may be used:  

|        |                                    |
| ---    | ---                                |
| in     | Open for input (_ifstream_, _fstream_)                      |
| out    | Open for output (_ofstrem_, _fstream_)                   |
| app    | Seek to the end before every write (trunc is not specified) |
| trunc  | Truncate the file (out is specified)                  |
| binary | Do IO operations in binary mode    |

By default a file opened in _out_ mode is truncated, to preserve
content, we must specify _app_.  

**Opening a File in out Mode Discards Existing Data**  
```cpp
// file 1 is truncated in each of these cases
ofstream out("file1");  // out and trunc are implicit
ofstream out2("file1", ofstream::out);  // trunc is implicit
ofstream out3("file1", ofstream::out | ofstream::trunc);

// to preserve the file's contents, we must explicitly specify app mode
ofstream app("file2", ofstream::app);   // out is implicit
ofstream app2("file2", ofstream::out | ofstream::app);
```
**File Mode is Determined Each Time open Is Called**  
<!-- }}} -->
<!-- }}} -->
## `string` Streams <!-- {{{ -->
The `sstream` header defines three types to support in-memory IO; these
types read from or write to a string as if the string were an IO stream.  
_sstream_ is one of the type defined in the `sstream` header  
| | |
| --- | --- |
| _sstream_ strm; | strm is an unbound stringstream. |
| _sstream_ strm(s); | strm holds a copy of the string s (explicit constructor) |
| strm.str() | Returns a copy of the string that strm holds |
| strm.str(s) | Copies the string s into strm. Returns void |

### Using an `istringstream` <!-- {{{ -->
An `istringstream` is often used when we have some work to do on an
entire line, and other work to do with individual words within a line.  

Assume we have file with structure:  
```txt
<person_name> <phone_number1> [<phone_number2> [...]]
<person1_name> <phone1_number1> [<phone1_number2> [...]]
...
```

Then creating this program will help us to parse this file:  
```cpp
string line, word;          // will hold aline and word from input, respectively
vector<PersonInfo> people;  // will hold all the records from the input
// read the input a line at a time until cin hits end-of-file
while (getline(cin, line)) {
    PersonInfo info;        // create an object to hold this record's data
    istringstream record(line); // bind record to the line we just read
    record >> info.name;    // read the name
    while (record >> word)  // read the phone numbers
        info.phones.push_back(word);    // and store them
    people.push_back(info); // append this record to people
}
```



<!-- }}} -->
### Using `ostringstream`s <!-- {{{ -->
An `ostringstream` is useful when we need to build up our output a
little at a time but do not want to print the output until later.  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Sequential Containers <!-- {{{ -->
## Preface <!-- {{{ -->
+ _sequential_ container - order corresponds to the positions in whic the
  elements are added  
+ _associative_ container - position depends on a key associated with each
  element  

Container classes share common interface, which each of the containers
extends in its own way.  

Container holds a collection of objects of a specified type. The
**_sequential containers_** let the programmer control the order in
which the elements are stored and accessed.  

The library also provide three _container adaptors_ - adapts a container
type by defining a different interface to the container's operations.  
<!-- }}} -->
## Overview of the Sequential Containers <!-- {{{ -->
Sequential Container Types:  

+ `vector` - Flexible-size array. Supports fast random access. Inserting
  or deleting elements other than at the back may be slow.  
+ `deque` - Double-ended queue. Supports fast random access. Fast
  insert/delete at front or back.  
+ `list` - Doubly linked list. Supports only bidirectional sequential
  access. Fast insert/delete at any point in the list.  
+ `forward_list` - Singly linked list. Su pports only sequential acces
  in one direction. Fast insert/delete at any point in the list.  
+ `array` - Fixed-size array. Supports fast random access. Cannot add or
  remove elements  
+ `string` - A specialized container, similar to `vector`, that contains
  characters. Fast random access. Fast insert/delete at the back.  
<!-- }}} -->
## Container Library Overview <!-- {{{ -->
### Container Operations <!-- {{{ -->
Some operations are provided by all container types:  

**Type Aliases:**  
+ `iterator` - type of the iterator for this container type  
+ `const_iterator` - iterator type that can read but not change its
  elements  
+ `size_type` - unsigned integral type big enough to hold the size of
  the largest possible container of this container type  
+ `difference_type` - signed integral to hold distance between two
  iterators  
+ `value_type` - element type  
+ `reference` - element's lvalue type; synonym for `value_type&`  
+ `const_reference` - `const value_type&`  

**Construction:**  
+ `C c;` - default constructor, empty container  
+ `C c1(c2);` - Construct `c1` as a copy of `c2`  
+ `C c(b, e);` - copy elements from the range denoted by iterators `b`
  and `e` (**not valid for array**)  
+ `C c{a,b,c...};` - list initialize `c`  

**Assignment and swap:**  
+ `c1 = c2` - replace elements in c1 with those in c2  
+ `c1 = {a,b,c,...}` - replace elements in c1 with those in the list (**not valid for array**)  
+ `a.swap(b)` - swap elements in `a` with those in `b` (eqv to `swap(a,b)`)  

**Size:**  
+ `c.size()` - number of elements in `c` (**not valid for
  `forward_list`**)  
+ `c.max_size()` - Maximum number of elements `c` can hold  
+ `c.empty()` - _false_ if `c` has any elements, _true_ otherwise  

**Add/Remove Elements _(not valid for array)_**  
**_Note: the interface to these operations varies by container type_**  
+ `c.insert(args)` - copy element(s) as specified by _args_ into `c`  
+ `c.emplace(inits)` - use _inits_ to construct an element in `c`  
+ `c.erase(args)` - remove element(s) specified by _args_  
+ `c.clear()` - remove all elements from `c`; returns `void`  

**Equality and Relational Operators:**  
+ `==`, `!=` - equality valid for all container types  
+ `<`, `<=`, `>`, `>=` - not valid for unordered associative containers  

**Obtain Iterators:**  
+ `c.begin()`, `c.end()` - return iterator to the first, one past the
  last element in `c`  
+ `c.cbegin()`, `c.cend()` - --//-- `const_iterator`  

**Additional Members of Reversible Containers (not valid for
`forward_list`)**  
+ `reverse_iterator` - iterator that addresses elements in reverse order  
+ `const_reverse_iterator` - reverse iterator that cannot write the
  elements  
+ `c.rbegin()`, `c.rend()` - return iterator to the last, one past the
  first element  
+ `c.crbegin()`, `c.crend()` - return `const_reverse_iterator`  

Each container is defined in a header file with the same name as the
type.  
The containers are **_class templates_**  
Commonly we supply element type to container:  
```cpp
list<Sales_data>    // list that holds Sales_data object
deque<double>       // deque that holds doubles
```
<!-- }}} -->
### Constraints on Types That a Container Can Hold <!-- {{{ -->
Some container operations impose requirements of their own on the
element type. As an example:  
```cpp
// assume noDefault is a type without a default constructor
vector<noDefault> v1(10, init); // ok: element initializer supplied
vector<noDefault> v2(10);       // error: must supply an element initializer
```
<!-- }}} -->
### Iterators <!-- {{{ -->
They are provide access to element from container.  
#### Iterator Ranges <!-- {{{ -->
**Iterator range** is denoted by a pair of iterators each of which
refers to element, or to _one past the last element_, in the same
container (usually `begin` and `end`).  
This element range is called a **left-inclusive interval** or `[begin,
end)`  

Requirements on Iterators Forming an Iterator Range:  
+ They refer to elements of, or one past the end of, the same container.  
+ It is possible to reach end by repeatedly incrementing begin.  
##### Programming Implications of Using Left-Inclusive Ranges <!-- {{{ -->
Assuming begin and end denote a valid iterator range, then:  

+ if `begin == end` - the range is empty  
+ if `begin != end` - there is at least one element in the range, and
  begin refers to the first element in that range  
+ we can increment `begin` until `begin == end`  

Example:  
```cpp
while (begin != end) {
    *begin = val;       // ok: range isn't empty so begin denotes an element
    ++begin;            // advance the iterator to get the next element
}
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
### Container Type Members <!-- {{{ -->
To use one of these type, we must name the class of which they are a
member:  
```cpp
// iter is the iterator type defined by list<string>
list<string>::iterator iter;
// count is the difference_type type defined by vector<int>
vector<int>::difference_type count;
```

<!-- }}} -->
### `begin` and `end` Members <!-- {{{ -->
These iterators are most often used to form an iterator range that
encompasses all the elements in the container.  
<!-- }}} -->
### Defining and Initializing a Container <!-- {{{ -->
#### Initializing a Container as a Copy of Another Container <!-- {{{ -->
Two ways to create a new container as a copy of another one:  

1. directly ocpy the container  
    1. the container and element types must match  
2. (excepting array) copy a range of elements denoted by a pair of
   iterators  
    1. Element types in the new and original containers can differ as
   long as it is possible to convert 
    2. Container types can differ  
<!-- }}} -->
#### List Initialization <!-- {{{ -->
Since _c++11_ standart we can list initialize a container:  
```cpp
list<string> authors = {"Milton", "Shakespeare", "Austen"};
```
<!-- }}} -->
#### Sequential Container Size-Related Constructors <!-- {{{ -->
We can also initialize the sequential containers (other than array) from
a size and an (optional) element initializer. If we do not supply
element initializer, the library creates a value-initialized one for us:  
```cpp
vector<int> ivec(10, -1);   // ten int elements, each initialized to -1
list<string> svec(10, "hi!")    // ten strings, each element is "hi!"
forward_list<int> ivec(10); // ten elements, each initialized to 0
deque<string> svec(10); // ten elements, each an empty string
```

<!-- }}} -->
#### Library `arrays` Have Fixed Size <!-- {{{ -->
The size of a library `array` is part of its type.  
```cpp
array<int, 42>  // type is: array that holds 42 ints  
```
To use an array type we must specify both the element type and the size:  
```cpp
array<int, 10>::size_type i;    // array type includes element type and size
array<int>::size_type j;        // error: array<int> is not a type
```
If we list initialize the `array`, the number of the initializers myst
be equal to or less than the size of the array.  

Although we cannot copy or assign objects of built-in array types, there
is no such restriction on array:  
```cpp
int digs[10] = {0,1,2,3,4,5,6,7,8,9};
int cpy[10] = digs; // error: no copy or assignment for built-in arrays
array<int, 10> digits = {0,1,2,3,4,5,6,7,8,9};
array<int, 10> copy = digits;   // ok: so long as array types match
```


<!-- }}} -->
<!-- }}} -->
### Assignment and `swap`<!-- {{{ -->
+ `c1 = c2` - replace the elements in `c1` with copies of the elements
  in `c2`. `c1` and `c2` must be the same type.  
+ `c = {a,b,c...}` - replace the elements in `c1` with copies of the
  elements in the initializer list **(Not valid for array.)**  
+ `swap(c1, c2)`, `c1.swap(c2)` - exchanges elements in `c1` with those in `c2`. `c1`
  and `c2` must be the same type. `swap` is usually _much_ faster than
  copying elements from `c2` to `c1`.

**assign operations not valid for associative containers or array**

+ `seq.assign(b,e)` - replaces (copies) elements in `seq` with those in the range
  denoted by iterators `b` and `e`. The iterators `b` and `e` must not
  refer to elements in `seq`.  
+ `seq.assign(il)` - replaces the elements in `seq` with those in the
  initializer list `il`  
+ `seq.assign(n,t)` - replaces the elements in `seq` with _n_ elements
  with value _t_.

Unlike built-in arrays, the library `ar ray` type does allow assignment
(types must be the same)  

#### Using `swap`<!-- {{{ -->
Excepting `array`, `swap` does not copy, delete, or insert any elements
and is guaranteed to run in constant time. Swapping two `arrays` does
exchange the elements. As a result, swapping two `arrays` requires time
proportional to the number of elements in the array.  
<!-- }}} -->
<!-- }}} -->
### Relational Operators <!-- {{{ -->
Every container type support the equality operators (== and !=), and
(except unordered associative) support relational operators (>, >=, <,
<=). The right- and left-hand operands must be the same kind of
acontainer and must hold elements of the same type.  

Comparing two containers performs lexicographic comparison:  

+ if both containers are the same size and all the elements are equal,
  the the two containers are equal  
+ if the containers have different sizes bu t every element of the
  smaller one is equal to the corresponding element of the larger one,
  then the smaller one it less than the other  
+ if neither container is an initial subsequence of the other, then the
  comparison depends on a comparing the first unequal elements  

**Relational Operators Use Their Element's Relational Operator**  
<!-- }}} -->
<!-- }}} -->
## Sequential Container Operations <!-- {{{ -->
**Container Operations May Invalidate Iterators**  
### Adding elements to a Sequential Container <!-- {{{ -->
Excepting `array`, all of the library containers provide flexible memory
management. We can add or remove elements dynamically changing the size
of the container at run time.  

+ `c.push_back(t)`, `c.emplace_back(args)` - creates an element with value `t`
  or constructed from _args_ at the end of `c`. Returns void.  
    not valid for `forward_list`  
+ `c.push_front(t)`, `c.emplace_front(args)` - creates an element with value `t`
  or constructed from _args_ on the front of `c`. Returns void.  
    not valid for `forward_list`  
+ `c.insert(it, t)`, `c.emplace(it, args)` - creates an element with value _t_
  or constructed from _args_ before the element denoted by iterator _it_.
  Returns an iterator referring to the element that was added.  
+ `c.insert(it,n,t)` - inserts _n_ elements with value _t_ before the
  element denoted by iterator _it_. Returns an iterator to the first
  element inserted; if _n_is zero, returns _it_.  
+ `c.insert(p, b, e)` - inserts the elements from the range denoted by
  iterators _b_ and _e_ before the element denoted by iterator _p_. _b_
  and _e_ may not refer to elements in `c`. Returns an iterator to the
  first element inserted; if the range is empty, returns _p_.  
+ `c.insert(it,il)` - _il_ is a braced list of element values. Inserts
  the given values before the element denoted by the iterator _it_.
  Returns an iterator to the first inserted element; if the list is
  empty returns _it_  

When use these operations, we must remember that the containers use
different strategies for allocating elements and that these strategies
affect performance.  

#### Using `push_back` <!-- {{{ -->
The call to `push_back` creates a new element at the end of `container`,
increasing the `size` of container by 1. The value of that element is a
copy of _word_. The type of container can be any of list, vector, or
deque.  
**Key concept: Container Elements Are Copies**  
<!-- }}} -->
#### Using `push_front` <!-- {{{ -->
This operatrion inserts a new element at the front of the container.  
As with `vector`, inserting elements other than at the front or back of
a `deque` is ponentially expensive operation.  
<!-- }}} -->
#### Adding Elements at a Specified Point in the Container <!-- {{{ -->
The `insert` members let us insert zero or more elements at any point in
the container. Elements are inserted _before_ the position denoted by
the iterator.  
<!-- }}} -->
#### Using the Return from `insert` <!-- {{{ -->
We can use the this value to repeatedly insert elements at a specified
position in the container:
```cpp
list<string> 1st;
auto iter = 1st.begin();
while (cin >> word)
    iter = 1st.insert(iter, word);  // same as calling push_front
```

<!-- }}} -->
<!-- }}} -->
### Accessing Elements <!-- {{{ -->
The access operations are undefined if the container has no elements.  

+ `c.back()` - returns a reference to the last element in _c_.  
+ `c.front()` - returns a reference to the first  element in _c_.  
+ `c[n]` - returns a reference to the element indexed by the unsigned
  integral value _n_. Undefined if `n >= c.size()`  
+ `c.at(n)` - returns a reference to the element indexed by _n_. If the
  index is out of ranger, throws an `out_of_range` exception. (safe
  random access)  

All seq. containers, including `array`, has a `front` member.  
All (except `forward_list`) have a `back` member.  

#### The Access Members Return References <!-- {{{ -->
If the ocntainer is `const` object, the return is a reference to
`const`. If the container is not `const`, the return is a ordinary
reference that we can use to change the value of the fetched element:
```cpp
if (!c.empty()) {
    c.front() = 42;     // assigns 42 to the first element in c
    auto &v = c.back()  // get a reference to the last element
    v = 1024;           // changes the element in c
    auto v2 = c.back(); // v2 is not a reference; it's a copy of c.back()
    v2 = 0;             // no change to the element in c
}
```

<!-- }}} -->
<!-- }}} -->
### Erasing Elements <!-- {{{ -->
Undefined if container is empty.  

+ `c.pop_back()` - removes last element in _c_. Returns _void_.  
+ `c.pop_front()` - removes first element in _c_. Returns _void_.  
+ `c.erase(p)` - removes the element denoted by the iterator _p_ and
  returns an iterator to the element after the one deleted or the
  off-the-end iterator if _p_ denotes the last element.  
+ `c.erase(b,e)` - removes the range of elements. Returns last element
  deleted, or an off-the-end iterator if _e_ is itself an off-the-end
  iterator.  
+ `c.clear()` - removes all the elements in _c_. Returns _void_.  

**Removing elements invalidates pointers, references.**  
**The programmer must ensure that elements exist before removing them.**  

#### The `pop_front` and `pop_back` Members <!-- {{{ -->
There's no `pop_front` for `vector` and `string`.  
There's no `pop_back` for `forward_list`.  

These operatrions return _void_. If you need the value you are about to
pop, you must store that value before doing the pop.  
<!-- }}} -->
#### Removing an Element from within the Container <!-- {{{ -->
Both forms of `erase` return an iterator referring to the location after
the (last) element that wasa removed.  

```cpp
list<int> lst = {0,1,2,3,4,5,6,7,8,9};
auto it = lst.begin();
while (it != lst.end())
    if (*it % 2)            // if the element is odd
        it = lst.erase(it); // erase this element
    else
        ++it;
```

<!-- }}} -->
<!-- }}} -->
### Specialized `forward_list` Operations <!-- {{{ -->
Operatrions to add or remove element in a `forward_list` operate by
changing the element _after_ the given element. Instead of common
`insert`, `emplace`, or `erase` it defines `insert_after`,
`emplace_after`, and `erase_after`.  

**erase** operators return pointer to the element after the one deleted.  
<!-- }}} -->
### Resizing a Container <!-- {{{ -->
+ current size > requested size &rarr; elements are deleted from
  the back of the container;  
+ current size < new size &rarr; elements are added to the back of the
  container:  

```cpp
list<int> ilist(10,42); // ten ints: each has value 42
ilist.resize(15);   // adds five elements of value 0 to the back of ilist
ilist.resize(25,-1) // adds ten elements of value -1 to the back of ilist
ilist.resize(5);    // erases 20 elements from the back of ilist
```

<!-- }}} -->
<!-- }}} -->
## How a `vector` Grows <!-- {{{ -->
Because reallocation every time new element is inserted is too
expensive, library implementors use allocation strategies that reduce
the number of times the container is reallocated. Thus `vector` usually
grows more efficiently than a `list` or a `deque`.  

### Members to Manage Capacity <!-- {{{ -->
+ `c.shring_to_fit()` - request to reduce `capacity()` to equal `size()`  
+ `c.capacity()` - number of elements _c_ can have before reallocation
  is necessary  
+ `c.reserve(n)` - allocate space for a least _n_ elements  

Under the **c++11**, we can call `shrink_to_fit` to ask a `deque`,
`vector`, or `string` to return unneeded memory.  
<!-- }}} -->
### `capacity` and `size` <!-- {{{ -->
**size** - number of elements it already holds;  
**capacity** - how many element it can hold before more space must be
allocated.  
<!-- }}} -->
<!-- }}} -->
## Additional `string` Operations <!-- {{{ -->
More constructors:  

+ `string s(cp, n)` - _s_ is a copy of the first _n_ characters in the
  array to which _cp_ points. That array must have at least _n_
  characters.  
+ `string s(s2, pos2)` - _s_ is a copy of the characters in the `string
  s2` starting at the index _pos2_.  
+ `string s(s2, pos2, len2)` - _s_ is a copy of _len2_ characters from
  _s2_ starting at the index _pos2_. Regardless of the value of _len2_,
  copies at most `s2.size() - pos2` characters.  
+ `s.substr(pos, n)` - return a `string` containing _n_ characters from
  _s_ starting at _pos_.  

### Other Ways to Change a `string` <!-- {{{ -->
In addition to the versions of `insert` and `erase` that take iterators,
`string` provides versions that take an index.  

+ `s.insert(pos, args)` - insert characters specified by _args_ before
  _pos_. _pos_ can be an index or an iterator. Versions taking an index
  return a reference to _s_; those taking an iterator return an iterator
  denoting the first inserted character.  
+ `s.erase(pos, len)` - remove _len_ characters starting at position
  _pos_. If _len_ is omitted, removes characters from _pos_ to the end
  of the _s_. Returns a reference to _s_.  
+ `s.assign(args)` - replace characters in _s_ according to _args_.
  Returns a reference to _s_.  
+ `s.append(args)` - append _args_ to _s_. Returns a reference to _s_.  
+ `s.replace(range, args)` - remove _range_ of characters from _s_ and
  replace them with the characters formed by _args_. _range_ is either
  an index and a length or a pair of iterators into _s_. Returns a
  reference to _s_.  

_args_ can be:  

+ `str` - the `string str`  
+ `str, pos, len` - up to _len_ characters from _str_ starting at _pos_  
+ `cp, len` - up to _len_ characters from the character array pointed to
  by _cp_  
+ `cp` - null-terminated array pointed to by pointer _cp_  
+ `n, c` - _n_ copies of character _c_  
+ `b, e` - characters in the range formed by iterators _b_ and _e_  
+ _initializer list_ - comma-separated list of characters enclosed in
  braces.  

<!-- }}} -->
### `string` Search Operations <!-- {{{ -->
Eache of these search operations returns a `string::size_type` value
that is the index of wehre the match occured. If these is no match, the
function returns a `static` member names `string::npos` (it equals `-1`
by default ==  largest possible size of string).  

+ `s.find(args)` - find the first occurrence of _args_ in _s_.  
+ `s.rfind(args)` - find the last occurrence of _args_ in _s_.  
+ `s.find_first_of(args)` - find the first occurrence of any character
  from _args_ in _s_  
+ `s.find_last_of(args)` - find the last occurrence of any character
  from _args_ in _s_  
+ `s.find_first_not_of(args)` - find the first character in _s_ that is
  not in _args_  
+ `s.find_last_not_of(args)` - find the last character in _s_ that is
  not in _args_  

_args_ **must be one of**:  

+ `c, pos` - character _c_ starting at position _pos_  
+ `s2, pos` - string _s2_ starting at position _pos_  
+ `cp, pos` - C-style string _cp_ starting at position _pos_  
+ `cp, pos, n` - look for the first _n_ characters in the array pointed
  to by the pointer _cp_. Start looking at position _pos_  

Common programming pattern to iterate over all specified characters in
string:
```cpp
string::size_type pos = 0;
// each iteration finds the next number in name
while ((pos = name.find_first_of(numbers, pos)) != string::npos) {
    cout << "found number at index: " << pos
        << " element is " << name[pos] << endl;
    ++pos;  // move to the next character
}
```

<!-- }}} -->
### The `compare` Functions <!-- {{{ -->
`s.compare` returns zero or a positive or negative value depending on
whether _s_ is equal to, greter than, or less than the string formed
from the given arguments.  

**Possible Arguments to `s.compare`**

+ `s2` - compare _s_ to _s2_.  
+ `pos1, n1, s2` - compares _n1_ characters starting at _pos1_ from _s_
  to _s2_.  
+ `pos1, n1, s2, pos2, n2` - --//-- additional args for _s2_.  
+ `cp` - compares _s_ to the null-terminated array pointed to by _cp_.  
+ `pos1, n1, cp` - similar to one for string.  
+ `pos1, n1, cp, n2` - cimilar to one for string.  
<!-- }}} -->
### Numeric conversions <!-- {{{ -->
**c++11** introduced several functions that convert between numeric data
and library `string`s:

+ `to_string(val)` - overloaded functions returning the `string`
  representation of _val_. _val_ can be any arithmetic type.  
+ `stoi(s,p,b)` - return the initial substring of _s_ that has numeric
  ontent as an `int`, `long`, `unsigned long`, `long long`, `unsigned
  long long`, respectively. _b_ - numeric base (defaults to 10). _p_ is
  a pointer to a `size_t` in which to put the index of the first
  nonnumeric character in _s_ (defaults to 0, in which case the function
  doesn't store the index)  
+ `stol(s,p,b)`  
+ `stoul(s,p,b)`  
+ `stoll(s,p,b)`  
+ `stoull(s,p,b)`  
+ `stof(s,p)` - return the initial numeric substring in _s_ as a
  `float`, `double`, or `long double`, respectively. _p_ is the same as
  above.  
+ `stod(s,p)`  
+ `stold(s,p)`  

```cpp
string s2 = "pi = 3.14";
// convert the first substring in s that starts with a digit, d = 3.14
d = stod(s2.substr(s2.find_first_of("+-.0123456789")));
```

The first non-whitespace character in the `string` must be a sign (+ or
-) or adigit.  
The `string` can begin with 0x, or 0X to indicate hexadecimal.  
May contain an e or E to designate the exponent.  
<!-- }}} -->

<!-- }}} -->
## Container Adaptors <!-- {{{ -->
An **adaptor** is a general concept in the library. There are container,
iterator, and function adaptors. Essentially, an adaptor is a mechanism
for making one thing act line another.  

**Operations and Types Common to the Container Adaptors:**  {{{

+ `size_type` - type large enough to hold the size of the largest
  object.  
+ `value_type` - element type  
+ `container_type` - type of the underlying container on which the
  adaptor is implemented  
+ `A a;` - create a new empty adaptor named _a_  
+ `A a(c);` - create a new adaptor named _a_ with a copy of the
  container _c_  
+ `relational operators` - each adaptor supports all the relational
  operators: _==_, _!=_, _<_, _>=_, etc. These operators return the
  result of comparing the underlying containers.  
+ `a.empty()`  
+ `a.size()`  
+ `swap(a,b)`, `a.swap(b)`  
<!-- }}} -->
### Defining an Adaptor <!-- {{{ -->
We can override the default container type:
```cpp
// empty stack implemented on top of vector
stack<string, vector<string>> str_stk;
// str_stk2 is implemented on top of vector and initially holds a copy of svec
stack<string, vector<string>> str_stk2(svec);
```

Constraints:  

+ require the ability to add and remove elements (as a result, they
  cannot be built on an _array_)  

<!-- }}} -->
### Stack Adaptor <!-- {{{ -->
Stack Operations:  

+ `s.pop()` - removes the top element from the _s_.  
+ `s.push(item)` - creates a new top element  
+ `s.emplace(args)` - constructs top element from _args_  
+ `s.top()` - returns top element  
<!-- }}} -->
### Queue Adaptor <!-- {{{ -->
`queue` and `priority_queue` adaptors are defined in the _queue_ header.  

+ `q.pop()` - removes the front element or highest-priority element  
+ `q.front()`, `q.back()` - returns the front or back element  
+ `q.top()` - returns, the highest-priority element  
+ `q.push(item)` - create an element or construct it from _args_ and
  insert in the appropriate position  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Generic Algorithms <!-- {{{ -->
Rather than define each of these operations as members of each container
type, the standard library defines a set of **generic algorithms**:
"algorithms" because they implement common classical algorithms such as
sorting and searching, and "generic" because they operate on elements of
differing type and across multiple container types.  

## Overview <!-- {{{ -->

+ most of the algorithms are defined in the _algorithm_ header  
+ numeric algorighms are defined in the _numeric_ header  

Alghorithms require some comparison operators to be defined. However
we'll see, most algorithms provide a way for us to supply our own
operation to use in place of the default operator.  
<!-- }}} -->
## A First Look at the Algorithms <!-- {{{ -->
**input range** - range of elements on which algorithms operate.  
How alghorithms use the elements in that range:  

+ read elements;  
+ write elements;  
+ rearrange the order of the elments;  

Elements in the sequence must match or be convertible to the type of the
third argument.  

Algorithms that write to a destination iterator _assume_ the destination
is large enough to hold the number of elements being written.  

### Read-Only Algorithms <!-- {{{ -->

+ `find` - finds element in input range  
    - `find_if` (third argument as predecate)  
+ `count` - calculates number of elements in input range  
+ `accumulate` (defined in the _numeric_ header) - sums elements in input
  range with starting point as third argument  
    `int sum = accumulare(vec.cbegin(), vec.cend(), 0);`
+ `equal(itb1,ite1,itb2)` - compares input range against second
  iterator (must be at least as long as input range)  

<!-- }}} -->
### Algorithms That Write Container Elements <!-- {{{ -->
Algorithms do not perform container operations,  so you must set correct
size of container by yourself.  

+ `fill` takes input range and value as third argument. It fills all
  elements in specified range with that value.  
+ `fill_n(dest_it, count, value)` writes _count_ times _value_ starting
  from *dest\_it* iterator.  
+ `copy(src_b,src_e,dest_b)` - copies input range from _src_ to _dest_  
```cpp
int a1[] = {0,1,2,3,4,5,6,7,8,9};
int a2[sizeof(a1)/sizeof(*a1)];
// ret points just past the last element copied into a2
auto ret = copy(begin(a1), end(a1), a2);
```
+ `replace(beg,end,match,repl)` - replaces every entry of _match_ in
  input range with _repl_.  
+ `replace_copy(beg,end,dest,match,repl)` - same us above but leave
  source sequence unchanged  

<!-- }}} -->
### Introducing `back_inserter` <!-- {{{ -->
One way t o ensure that an algorithm has enough elements to h old the
output is to use an **insert iterator**. An insert iterator is an
iterator that _adds_ elements to a container. When we assign through an
insert iterator, a new element equal to the right-hand value is added to
the container.  

For now we will use `back_inserter` which is a function defined in the
_iterator_ header.  

`back_inserter` takes a reference to a container and returns an insert
iterator. When we assign through that iterator, the assignment calls
`push_back` to add an element with the given value to the container.  
<!-- }}} -->
### Algorithms That Reorder Container Elements <!-- {{{ -->

+ `sort` - arranges the elements in the input range into sorted order  

#### Eliminating Duplicates <!-- {{{ -->

+ sort so duplicates are appear adjacent to each other  
+ unique so unique elements will go at the beginning (returns iterator
  one past the last unique element)  
+ erase with range to erase non-unique elements  

<!-- }}} -->

<!-- }}} -->
<!-- }}} -->
## Customizing Operations <!-- {{{ -->
The library also defines versions of these algorithms that let us supply
our own operation to use in place of the default operator.  

### Passing a Function to an Algorithm <!-- {{{ -->
Other version of `sort` takes a third argument that is a
**predicate** (and uses it instead of default `<`).  
**Predicate** - unary or binary function that returns bool.  
<!-- }}} -->
### Sorting Algorithms <!-- {{{ -->
We may use `stable_sort` if we want to.  
<!-- }}} -->
### Lambda Expressions <!-- {{{ -->
When we need to do processing that requires more arguments that the
algorithm's predicate allows, we use **lambda expressions**.  

A lambda expression represents a callable unit of code (e.g. unnamed,
inline function).  
Lambda expression has the form:
```cpp
[capture list] (parameter list) -> return type { function body }
```

We can omit either or both of the parameter list and return type but
must always include the capture list (often empty) and function body  

> Lambdas with function bodies that contain anything other than a single
> return statement that do not specify a return type return void.  

#### Using the Capture List <!-- {{{ -->
Inside the `[]` that begins a lambda we can provide a comma-separated
list of names defined in the surrounding function.  
A lambda can use names that re defined outside the function in which the
lambda appears.  

`make_plural` to print _word_ or _words_, depending on whether that size
is equal to 1.  
<!-- }}} -->

<!-- }}} -->
### The `for_each` Algorithm <!-- {{{ -->
`for_each` takes a callable object and calls that object on each element
in the input range.  
<!-- }}} -->
### Lambda Captures and Returns <!-- {{{ -->
By default, the class generated from a lambda contains a data member
corresponding to the variables captured by the lambda. Like the data
members of any class, they are initialized when a lambda object is
created  

**Type of capturing**:  <!-- {{{ -->

+ `[]` - empty capture list. The lambda may not use variables from the
  enclosing function  
+ `[names]` - _names_ is a comma-separated list of names. By default,
  variables are copied. A name preceded by _&_ is captured by reference.  
+ `[&]` - implicit by reference capture list. Entities from the
  inclosing function used in the lambda body are used by reference.  
+ `[=]` - same but for copying  
+ `[&,identifier_list]` - *identified_list* is a comma-separated list of
  zero or more variables from the enclosing function. These variables
  are captured by value; any implicitly captured variables are captured
  by reference.  
+ `[=,reference_list]` - same as above but reversed logic.  

Note: avoid capturing pointers or references  
<!-- }}} -->
#### Mutable Lambdas <!-- {{{ -->
If you want to change variable value that passed to lambda via copying,
you may use `mutable` keyword after parameter list.
```cpp
void fcn3()
{
    size_t v1 = 42; // local variable
    // f can change the value of the variables it captures
    auto f = [v1] () mutable { return ++v1; };
    v1 = 0;
    auto j =  f();  // j is 43
}
```

<!-- }}} -->
<!-- }}} -->
### Binging Arguments <!-- {{{ -->
To create function that _imitates_ lambda capture list we can use
**library** `bind` **function** (defined in the `functional` header).  
General for is:
```cpp
auto newCallable = bind(callable, arg_list);
```
The arguments in *arg_list* may include names of the form *_n*, where
_n_ is an integer. Those are placed into corresponding position(starting
with 1).  
To use placeholders you must insert `use` statement before it:
```cpp
// you must provide separate using declaration for each placeholder
using std::placeholders::_1;
// or include all
using namespace std::placeholders;
```

For example:
```cpp
auto g = bind(f, a, b, _2, c, _1);
// calling g will behave like this
g(a, b, Y, c, X);
```

#### Using to `bind` to Reorder Parameters <!-- {{{ -->
```cpp
// normal sort
sort(words.begin(), words.end(), isShorter);
// inverse order
sort(words.begin(), words.end(), bind(isShorter, _2, _1));
```

<!-- }}} -->
#### Binding Reference Parameters <!-- {{{ -->
We can't use bind directly, because it copies all elements. In this case
we want to use the library `ref` function:
```cpp
for_each(words.begin(), words.end(), bind(print, ref(os), _1, ' '));
// there's also a cref function that generates a reference to const
```
_Backward Compatibility: Binding Arguments: library provides functions
named bind1st and bind2nd._  

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Revisiting Iterators <!-- {{{ -->
In addition to the iterators defined for each of the containers, the
library defines several additional kinds in the `iterator` header:  

+ **insert iterators** - bound to a container and can be used to insert
  elements into the container.  
+ **stream iterators** - iterate through the associated IO stream  
+ **reverse iterators** - move backward, rather than forward  
+ **move iterators** - move rather than copy their elements  

### Insert Iterators <!-- {{{ -->

+ `it = t` - inserts the value _t_ at the current position. Depending on
  given container calls `c.push_back(t)`, `c.push_front(t)`, or
  `c.insert(t, p)`  
+ `*it`, `++it`, `it++` - Each operator returns _it_.  

 There are three kinds of inserters:  

 + `back_inserter` - iterator that uses `push_back`  
 + `front_inserter` - iterator that uses `push_front`  
 + `inserter` - creates an iterator that uses `insert`, which inserts
   element ahead of iterator (takes iterator as second argument).  

Assume _it_ is an iterator generated by `inserter`, then assignment such
us
```cpp
*it = va1;
```
behaves as
```cpp
it = c.insert(it, val); // it points to the newly added element
++it;   // increment is so that id denotes the same element as before
```




<!-- }}} -->
### `iostream` Iterators <!-- {{{ -->
Using a stream iterator, we can use the generic algorithms to read data
from or write data to stream objects.  

`istream` iterator operations:

+ `istream_iterator<T> in(is);` - _in_ reads values of type `T` from
  input stream _is_.  
+ `istream_iterator<T> end;` - off-the-end iterator.  
+ `in1 == in2`, `in1 != in2` - _in1_ and _in2_ must read the same type.
  They are equal if they are both the end value or are bound to the same
  input stream.  
+ `*in` -   returns the value read from the stream  
+ `in->mem` - synonym for `(*int).mem`  
+ `++in`, `in++` - reads the next value from the input stream using the
  `>>` operator for the element type.  

Example:
```cpp
istream_iterator<int> in_iter(cin); // read ints from cin
istream_iterator<int> eof;          // istream "end" iterator
while (in_iter != eof) // while thre's valid input to read
    vec.push_back(*in_iter++)
```
or
```cpp
istream_iterator<int> in_iter(cin), eof;    // read ints from cin
vector<int> vec(in_iter, eof);
```
#### Using Stream Iterators with the Algorithms <!-- {{{ -->
You should already know how to use algorithms and iterators, so here's
an example:
```cpp
istream_iterator<int> in(cin), eof;
// outputs sum of ints from input
cout << accumulate(in, eof, 0) << endl;
```

<!-- }}} -->

`ostream` iterator operations:

+ `ostream_iterator<T> out(os);` - _out_ writes values of type `T` to
  output stream _os_.  
+ `ostream_iterator<T> out(os, d)` - _out_ writes values of type `T`
  followed by _d_ (null-terminated character array) to output stream _os_.  
+ `out = val` - writes _val_ to the _ostream_ using the `<<` operator  
+ `*out`, `++out`, `out++` - These operations exist but do nothing to
  out. Each operator returns _out_.  

#### Operations on `ostream_iterators` <!-- {{{ -->
We may provide a string to print after each element:
```cpp
ostream_iterator<int> out_iter(cout, " ");  // writes " " after each elemnt
for (auto e : vec)
    *out_iter++ = e;    // the assignment writes this element to cout
cout << endl;
```
Provided string must be literal string or null-terminated C-style array.  

It's worth noting we can omit the dereference and the increment when we
assign to `ostream_iterator<>`, that is:
```cpp
for (auto e : vec)
    out_iter = e;   // the assignment writes this element to cout
cout << endl;
```

Rather than writing the loop by hands, we can more easily print the
elements in _vec_ by calling `copy`:
```cpp
copy(vec.begin(), vec.end(), out_iter);
cout << endl;
```


<!-- }}} -->
#### Using Stream Iterators with Class Types <!-- {{{ -->
WE can create an `istream_iterator` and `ostream_iterator` for any type
as long as it has corresponding operator (`>>`, `<<`)  
```cpp
istream_iterator<Sales_item> item_iter(cin), eof;
ostream_iterator<Sales_item> out_iter(cout, "\n");
// store the first transaction in sum and read the next record
Sales_item sum = *item_iter++;
while (item_iter != eof) {
    // if the current transaction (which is stored in item-iter)
    // has the same ISBN
    if (item_iter->isbn() == sum.isbn())
        sum += *item_iter++;    // add it to sum and read the next
        // transaction
    else {
        out_iter = sum;     // write the current sum
        sum = *item_iter++; // read the next transaction
    }
}
out_iter = sum;     // remember to print the last set of records
```

<!-- }}} -->

<!-- }}} -->
### Reverse Iterators <!-- {{{ -->
A reverse iterator inverts the meaning of increment (and decrement).  
```cpp
sort(vec.begin(), vec.end());   // sorts in "normal" order
sort(vec.rbegin(), vec.rend()); // sorts in reverse order
```
**Reverse Iterators Require Decrement Operators**.  
If you want to use reversed iterators in place of forward &rarr; you
want to use `reverse_iterator`'s `base` member:
```cpp
cout << string(rcomma.base(), line.end()) << endl;
```

> When we initialize or assign a reverse iterator from a plain iterator,
> the resulting iterator dies not refer to the same element as the
> original.  

<!-- }}} -->
<!-- }}} -->
## Structure of Generic Algorithms <!-- {{{ -->
The it erator operations required by the algorithms are grouped into
five **iterator categories**. Each algorithms specifies what kind of
iterator must be supplied for each of its iterator parameters:  

+ `input iterator` - read, but not write; single-pass, increment only  
+ `output iterator`- write, but not read; single-pass, increment only  
+ `forward iterator` - read and write; multi-pass, increment only  
+ `bidirectional iterator` - read and write; multi-pass, increment and
  decrement  
+ `random-access iterator` - read and write; multi-pass, full iterator
  arithmetic  

### The Five Iterator Categories <!-- {{{ -->
For each parameter, the iterator must be at least as powerful as the
stipulated minimum. Passing an iterator of a lesser power is an error.  

#### The Iterator Categories <!-- {{{ -->
**Input iterators**: can read elements in a sequence. It must provide:  

+ Equality and inequality operators - `==`, `!=`  
+ Prefix and postfix increment - `++`  
+ Dereference operator - `*`  
+ The arrow operator `->` as a synonym for `(*it)->member`  

With input iterators we are guaranteed that `*it++` is valid, but it may
invalidate all other iterators into the stream. Input iterators,
therefore, may be used only for single-pass algorithms.  

**Output iterators**: they can be thought of as having complementary
functionality to input iterators - they write rather than read elements.
They must provide:  

+ Prefix and postfix increment - `++`  
+ Dereference - `*`  

This type of iterators can be used only for single-pass algorithms. The
`ostream_iterator` type is an output iterator.  

**Forward iterators**: all operations of both input iterators and output
iterators. Moreover, they can read or write the same element multiple
times. Therefore, we can use the save state of a forward iterator.
Hence, algorithms that use forward iterators may make multiple passes
through the sequence.  

**Bidirectional iterators**: all operations of a forward iterator +
prefix and postfix decrement `--`. Library containers supply iterators
that meet the requirement for a bidirectional iterator.  

**Rendom-access iterators**: all the functionality of bidirectional
iterators + contant-time access to any position in the sequence. Must
provide:  

+ Relational operators - `<`, `<=`, `>`, and `>=` to compare the
  relative positions of two iterators  
+ Addition and substraction operators - `+`, `+=`, `-`, and `-=` on an
  iterator and an integral v alue. The result in the iterator advance
  (or retreated) the integral number of elements within the sequence.  
+ The subtraction operator `-` when applied to two iteratos, which
  yields the distance between two iterators.  
+ The subscript operator `iter[n]` as a synonym for `*(iter+n)`  

The _sort_ algorithms require random-access iterators.  
<!-- }}} -->
<!-- }}} -->
### Algorithm Parameter Patterns <!-- {{{ -->
Most of the algorithms have one of the following four forms:
```cpp
alg(beg, end, other args);
// algorithms can write its output
// it's assumed that it iss safe to write as many elements as needed
alg(beg, end, dest, other args);
// typically use the elements from the second range in combination with
// the input range to perform a computation
alg(beg, end, beg2, other args);
alg(beg, end, beg2, end, other args);
```

<!-- }}} -->
### Algorithm Naming Conventions <!-- {{{ -->
Theses conventions deal with how we supply and operation to use in place
of the default `<` or `==` operator and with whether the algorithm write
to its input sequence or to a sepaarate destination.  

**Some Algorithms Use Overloading to Pass a Predicate**  
```cpp
unique(beg, end);   // uses the == operator to compare the elements
unique(beg, end, comp); // uses comp to compare the elements
```

**Algorithms with** \_if **versions**  
Algorithms that take and element value typically have a second named
(not overloaded) version that takes a predicate in place of the value.
The algorithms that take a predicate have the suffix `_if` appended:
```cpp
find(beg, end, val);    // find the first instance of val
find_if(beg, end, pred);    // find the first instance for which pred is true
```

**Distinguishing Versions That Copy from Those That Do Not**  
By default, algorithms that rearrange elements write new version back
into the given input range. These algorithms provide a second version
that writes to a specified output destination (`_copy` suffix):
```cpp
reverse(beg, end);  // reverse elements in the input range
reverse_copy(beg, end, dest);   // copy elements in reverse order into dest
```
Some algorithms provide both `_copy` and `_if` versions:
```cpp
// removes the odd elements from v1
remove_if(v1.begin(), v1.end(), [](int 1){return i % 2; });
// copies only the even elements from v1 into v2; v1 in uncahnged
remove_copy_if(v1.begin(), v1.end(), back_inserter(v2),
        [](int i) { return 1 % 2; });
```



<!-- }}} -->
<!-- }}} -->
## Container-Specific Algorithms <!-- {{{ -->
Unlike the other containers, `list` and `forward_list` define several
algorithms as members.  

+ `lst.merge(lst2)`, `lst.merge(lst2, comp)` - merges elements from
  _lst2_ onto _lst_. After the merge _lst2_ is empty.  
+ `lst.remove(val)`, `lst.remove_if(pred)` - calls `erase` to remove
   matching elements.  
+ `lst.reverse()` - reverses the order of the elements in _lst_.  
+ `lst.sort()`, `lst.sort(comp)` - sorts the elements  
+ `lst.unique()`, `lst.unique(pred)` - calls `erase` to remove
  consecutive copies of the same value.  
+ `lst.splice(p, lst2[, args])` - moves elements to or from _lst_ or
  _lst2_. For _args_:
    - _p_ is usually iterator TO an elemnt (in _list_), or an iterator
  just BEFORE an element (in *forward_list*)  
    - ` ` - just move elements from _lst2_ to _lst_ where the iterator
  points  
    - `p2` - moves elements right after the _p2_ located in _lst2_   
    - `b, e` - same as above, but range given  
    - afterwards those elements are removed from _lst2_  

**The List-Specific Operations Do Change the Containers.**  
<!-- }}} -->
<!-- }}} -->
# Associative Containers <!-- {{{ -->
Associative containers support efficient lookup and retrieval by a key.
The two primary associative-conatiner types are `map` and `set`.  

The elements in a `map` are key-value pairs: the key serves as an index
into the `map`, and the value represents the data associated with that
index.  

A `set` element contains only a key; a `set` supports efficient queries
as to whether a given key is present.  

The library provides eight associative containers. Each differing along
three dimensions:  

+ `set` or `map`.  
+ unique keys required or not.  
    * allowed multiple keys has prefix `multi`  
+ stores the elements in order or not.  
    * order is not stored - `unordered`  

Example: unordered_multi_set, multimap, unordered_map  

## Using an Associative Container <!-- {{{ -->
Like the sequential containers, the associative containers are
templates.  
### Using a `map` <!-- {{{ -->
If key is not already in the map, the subscript operator creates a new
element with that key.  
When we fetch an element from a `map` we get an object of type `pair` -
template type that holds two (public) data elements called `first` (key)
and `second` (value).
<!-- }}} -->
### Using a `set` <!-- {{{ -->
Check that element not exists in set:
```cpp
if (set_name.find(element) == set_name.end())
```

<!-- }}} -->
<!-- }}} -->
## Overview of the Associative Containers <!-- {{{ -->
Differences from sequential containers:  

+ do not support position-specific operations (`push_front`, `back`)  
+ do not support the constructors or insert operations that take an
  element value and a count  
+ provide operations and type aliases that sequential containers do not  
+ provide operations for tuning their hash performance  

### Defining an Associative Container <!-- {{{ -->
Initialization:  

+ default constructor &rarr; creates empty container  
+ copy of another container of the same type  
+ from a ranger of values  

```cpp
map<string, size_t> words_count;    // empty
// list initialization
set<string> exclude = {"the", "but", "and", "or"};
// three elements; authors maps last name to firsts
map<string, string> authors = { {"Joyce", "James"},
            {"Austen", "Jane"}, {"Dickens", "Jane"}};
```

<!-- }}} -->
### Initializing a `multimap` or `multiset` <!-- {{{ -->
```cpp
// define a vector holding two copies of each number from 0 to 9
vector<int> ivec;
for (vector<int>::size_type i=0; i != 10; ++i) {
    ivec.push_back(i);
    ivec.push_back(i);  // duplicate copies of each number
}
// iset holds unique elements from ivec
// miset holds all 20 elements
set<int> iset(ivec.cbegin(), ivec.cend());
multiset<int> miset(ivec.cbegin(), ivec.cend());
cout << ivec.size() << endl;    // prints 20
cout << iset.size() << endl;    // prints 10
cout << miset.size() << endl;   // prints 20
```

<!-- }}} -->
### Requirements on Key Type <!-- {{{ -->
Ordered containers require keys to define `<` operator.  

#### Key Types for Ordered Containers <!-- {{{ -->
We can provide our own operation to use in place of the `<` operator.
The specified operation must define a **strict weak ordering** (less
than) over the key type:  

+ two keys cannot both be "less than" each other;  
+ if _k1_ < _k2_ and _k2_ < _k3_, then _k1_ must be < _k3_  
+ if there're two keys, and neither key is "less than" the other, then
  we'll say that those keys are "equivalent".  

When used as a key to a `map`, there will be only one element associated
with those keys, and either key can be used to access the corresponding
value.  
<!-- }}} -->
#### Usign a Comparison Function for the Key Type <!-- {{{ -->
To specify our own operation, we must supply the type of that operation
when we define the type of an associative container.  

```cpp
bool comareIsbn(const Sales_data &lhs, const Sales_data &rhs) {
    return lhs.isbn() < rhs.isbn();
}

// we could have written &compareIsbn with the same effect
multiset<Sales_data, decltype(compareIsbn)*> bookstore(compareIsbn);
```

<!-- }}} -->
<!-- }}} -->
### The `pair` Type <!-- {{{ -->

`pair` is a template from which we generate specific types. We must
summpy two type names when we create a `pair`.
```cpp
pair<string, string> anon;
pair<string, size_t> word_count;
```

The default `pair` constructor value initializes the data members. But
we can also provide initializers for each member:
```cpp
pair<string, string> author{"James", "Joyce"};
```

Data members of `pair` are `public`. First element called `first`
and `second` respectively.  

**Operations on **`pair`**s:**  

+ `pair<T1, T2> p;` - _p_ value initialized  
+ `pair<T1, T2> p(v1,v2)` - first and second elmeents are initialized
  from _v1_ and _v2_  
+ `pair<T1, T2> p = {v1, v2}` - equivalent to `p(v1, v2)`  
+ `make_pair(v1, v2)` - returns a pair initialized from _v1_, _v2_  
+ `p.first` - returns the first element  
+ `p.second` - returns the second element  
+ `p1 relop p2` - relational operators (<,>,<=,>=). Comparing goes in
  lexicographic order  
+ `p1 == p2`, `p1 != p2` - two pairs are equal if their first and second
  members are respectively equal.  

Since c++11 we can list initialize return value of type `pair`:
```cpp
pair<string, int> process(vector<string> &v) {
    // process v
    if (!v.empty())
        return {v.back(), v.back().size()}; // list initialize
    else
        return pair<string, int>(); // explicitly constructed return value
}
```



<!-- }}} -->
<!-- }}} -->
## Operations on Associative Containers <!-- {{{ -->
In addition to the already listed types (like size type or iterator type),
associative containers define:  

+ `key_type` - type of the key for this container type  
+ `mapped_type` - type associated with each key; **map types only**  
+ `value_type` - for sets, same as the key type;
  for maps, `pair<const key_type, mapped_type>`  

### Associative Container Iterators <!-- {{{ -->
When we dereference an iterator, we get a reference to a value of the
container's `value_type`.

Iterators for `set`s Are `const`
================================
ALthough the `set` types define both the `iterator` and `const_iterator`
types, both types five us read-only access to the elements in the set.  
<!-- }}} -->
### Associative Containers and Algorithms <!-- {{{ -->
Just don't use algorithms if associative container already has this
feature (like `find`). Because Generic algorithms actually slower than
native container's algorithm.  
<!-- }}} -->
### Adding Elements <!-- {{{ -->
`insert` members add one element or a range of elements. Because `map`
or `set` contain unique keys, inserting an element that is already
present has no effect.  

Associative Container `insert` Operations:  

+ `c.insert(v)`, `c.emplace(args)` - _v_ - *value_type* object; _args_ are used to
  construct an element. Returns a `pair` containing an iterator
  referring to the element with the given key and a `bool` indicating
  whether the element was inserted.  
  For `multi-` returns an iterator to the new element  
+ `c.insert(b,e)` - _b_, _e_ - iterators that denote a range of values  
+ `c.insert(il)` - _il_ is braced list of such values.  
+ `c.insert(p,v)`, `c.emplace(p,args)` - like `insert(v)` but uses
  iterator _p_ as a hint for where to begin the search for where
  the new element should be stored. Returns an iterator to the
  elment with the given key.  

#### Adding Elements to a `map` <!-- {{{ -->
```cpp
// four ways to add word to word_count
word_count.insert({word, 1});
word_count.insert(make_pair(word, 1));
word_count.insert(pair<string, size_t>(word, 1));
word_count.insert(map<string, size_t>::value_type(word, 1));
```

<!-- }}} -->
#### Adding Elements to `multiset` or `multimap` <!-- {{{ -->
Assume we want to map authors to titles of the books they have written.
In this case, there might be multiple entries for each author, so we'd
use a `multimap` rather than `map`
<!-- }}} -->
<!-- }}} -->
### Erasing Elements <!-- {{{ -->
+ `c.erase(k)` - remove every element with key _k_ from _c_. Returns
  `size_type` indicating the number of elements removed  
+ `c.erase(p)` - removes element denoted by the iterator _p_ from _c_.
  Returns an iterator to the element after _p_ or _c.end()_  
+ `c.erase(b,e)` - removes the elements in the range denoted by the
  iterator pair _b_, _e_. Returns _e_.  
<!-- }}} -->
### Subscripting a `map` <!-- {{{ -->
+ `map` and `unordered_map` provide the subscript operator and a
  corresponding `at` function.  
    - `c[k]` - returns the element with key _k_; if _k_ is not in _c_,
  adds a new, value-initialized element with key _k_.  
    - `c.at(k)` - checked access to the element with key _k_; throws an
  `out_of_range` exception if _k_ is not in _c_  
+ `set` types do not support subscripting  
+ `multimap` or `unordered_multimap` do not support, because there may
  be more than one value associated with a given key.  
<!-- }}} -->
### Accessing Elements <!-- {{{ -->
Operations to Find Elements in an Associative Container:  

+ `c.find(k)` - returns an iterator to the first element with key _k_,
  or the off-the-end iterator if _k_ is not in the container.  
+ `c.count(k)` - returns the number of elements with key _k_.  
+ `c.lower_bound(k)` - returns an iterator to the first element with key
  not less than _k_ (>= k). Used to generate iterator range for
  searching key. off-the-end if key is not presented  
+ `c.upper_bound(k)` - returns an iterator to the first element with key
  greater than _k_ (> k). Used to generate iterator range for searching
  key.  
+ `c.equal_range(k)` - returns a `pair` of iterators denoting the
  elements with key _k_. If _k_ is not present, both members are
  _c.end()_  

#### Finding Elements in a `multimap` or `multiset` <!-- {{{ -->
When a `multimap` or `multiset` has multiple lements of a given key,
those lements will be adjacen within the container.  
To output all search entries:
```cpp
string search_item("Alain de Botton");  // author we'll look for
auto entries = authors.count(search_item);  // number of elements
auto iter = authors.find(serach_item);  // first entry for this author
// loop through the number of entries there are for this author
while (entries) {
    cout << iter->second << endl;   // print each title
    ++iter; // advance to the next title
    --entries;  // keep track of how many we've printed
}
```

<!-- }}} -->
#### A Different, Iterator-Oriented Solution <!-- {{{ -->
Using `c.lower_bound(k)` or `c.upper_bound(k)` we can rewrite above
example as follows:
```cpp
// definitions of authors and search_item as above
// beg and end denote the range of elements for this author
for (auto beg=authors.lower_bound(search_item),
            end=authors.upper_bound(search_item);
    beg != end; ++beg)
    cout << beg->second << endl;    // print each title
```

<!-- }}} -->
#### The `equal_range` Function <!-- {{{ -->
```cpp
// definitions of authors and search_item as above
// pos holds iterators that denote the range of elements for this key
for (auto pos = authors.equal_range(search_item);
    pos.first != pos.second; ++pos.first)
    cout << pos.first->second << endl;  // print each title
```

<!-- }}} -->
<!-- }}} -->
### A Word Transformation Map <!-- {{{ -->

```cpp
map<string, string> buildMap(ifstream &map_file) {
    map<string, string> trans_map;  // holds the transformations
    string key;     // a word to transform
    string value;   // phrase to use instead
    // read the first word into key and the rest of the line into value
    while (map_file >> key && getline(map_file, value))
        if (value.size() > 1)   // check that there is a transformation
            trans_map[key] = value.substr(1);   // skip leading space
        else
            throw runtime_error("no rule for " + key);
    return trans_map;
}
```


<!-- }}} -->
<!-- }}} -->
## The Unordered Containers <!-- {{{ -->
### Using the Unordered Containers <!-- {{{ -->

They are provide same operations (`find`, `insert`, and so on) as the
ordered containers.  

Elements are stored in buckets in unordered containers. Latest provide a
set of functions, that let us manage the buckets:  

**Bucket Interface**  

+ `c.bucket_count()` - number of buckets in use.  
+ `c.max_bucket_count()` - largest number of buckets this container can
  hold.  
+ `c.bucket_size(n)` - number of elements in the nth bucket.  
+ `c.bucket(k)` - bucket in which elements with key _k_ would be found.  

**Bucket Iteration**  

+ `local_iterator` - iterator type that can access elements in a bucket  
+ `const_local_iterator` - `const` version of the bucket iterator  
+ `c.begin(n)`, `c.end(n)` - iterator to the first, one past the last
  element in bucket _n_.  
+ `c.cbegin(n)`, `c.cend(n)` - returns `const_local_iterator`.  

**Hash Policy**  

+ `c.load_factor()` - average number of elements per bucket. Returns
  `float`  
+ `c.max_load_factor()` - average bucket size that _c_ tries to
  maintain. _c_ adds buckets to keep *load_factor <= max_load_factor*.
  Returns `float`  
+ `c.rehash(n)` - reorganize storage so that *bucket_count >= n* and
  *bucket_count > size/max_load_factor*.  
+ `c.reserve(n)` - reorganize so that _c_ can hold _n_ elements without
  _rehash_.  

<!-- }}} -->
### Requirements on Key Type for Unordered Containers <!-- {{{ -->
By default unordered containers use `==` operator and `hash<key_type>`.
The library supplies versions of the `hash` template for the built-in
types, including pointers, strings, smart pointers.  

However, we cannot directly define an unordered container that uses a
our own class types for its key type. We must supply our own version of
the `hash` template.

To use `Sales_data` as the key, we'll need to supply functions to
replace both the `==` operator and to calculate a hash code:
```cpp
size_t hasher(const Sales_data &sd) {
    return hash<string>()(sd.isbn());
}
bool eqOp(const Sales_data &lhs, const Sales_data &rhs) {
    return lhs.isbn() == rhs.isbn();
}
```

Now we can use these functions to define an `unordered_multiset` as
follows:
```cpp
using SD_multiset = unordered_multiset<Sales_data,
                    decltype(hasher)*, decltype(eqOp)*>;
// arguments are the bucket size and pointers to the hash function and equality operator
SD_multiset bookstore(42, hasher, eqOp);
```

If our class has its own `==` operator we can override just the hash
function:
```cpp
// use FooHash to generate the hash code; Foo must have an == operator
unordered_set<Foo, decltype(FooHash)*> fooSet(10, FooHash);
```



<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Dynamic Memory <!-- {{{ -->

+ `static` objects are allocated before they are used, and they are
  destroyed when the program ends  
+ `stack` objects exist only while the block in which they are defined
  is executing  

In addition to static or stack memory, every program also has a pool of
memory that it can use. This memory is referred to as the **free store**
or `heap`. Programs use the heap for objects that they dynamically
allocate. The program controls the lifetype of dynamic objects; our code
must explicitly destroy such objects when they are no longer needed.  

## Dynamic Memory and Smart Pointers <!-- {{{ -->
Dynamic memory is managed through a pair of operators:  

+ `new` - allocates and optionally initializes an object in dynamic
  memory and returns pointer to that object;  
+ `delete` - which takes a pointer to a dynamic object destroys that
  object and frees the associated memory.  

To make using dynamic memory easier (and safer), the new library
provides two smart pointer types:  

+ `shared_ptr` - allows multiple pointers to refer to the same object.  
+ `unique_ptr` - which "owns" the object to which it points.  
+ `weak_ptr` - weak reference to an object managed by a `share_ptr`.  

### The `shared_ptr` Class <!-- {{{ -->
Smart pointers are templates. Therefore, when we create one, we must
supply additional information - type to which the pointer can point.
```cpp
shared_ptr<string> p1;      // shared_ptr that can point to a string
shared_ptr<list<int>> p2;   // shared_ptr that can point to a list of ints
```
A default initialized smart pointer holds a null pointer.  

Dereferencing a smart pointer returns the object to which the pointer
points. When we use a smart pointer in a condition, the effect is to
test whether the pointer is null:
```cpp
// if p1 is not null, check whether it's the empty string
if (p1 && p1->empty())
    *p1 = "hi"; // if so, dereference p1 to assign a new value to that string
```

**Operations Common to** `shared_ptr` **and** `unique_ptr`:  

+ `shared_ptr<T> sp`, `unique_ptr<T> up`- null smart pointer that can
  point to objects of type `T`.  
+ `p` - use _p_ as a condition; _true_ if _p_ points to an object.  
+ `*p` - dereference _p_ to get the object to which _p_ points.  
+ `p->mem` - synonym for `(*p).mem`  
+ `p.get()` - returns the pointer in _p_. Use with caution; the object
  to which the returned pointer points will disappear when the smart
  pointer deletes it.  
+ `swap(p,q)`, `p.swap(q)` - swaps the pointers in _p_ and _q_.  

**Operations Specific to** `shared_ptr`:  

+ `make_shared<T>(args)` - returns a `shared_ptr` pointing to a
  dynamically allocated object of type `T`. Uses _args_ to initialize
  that object.  
+ `shared_ptr<T> p(q)` - _p_ is a copy of the `shared_ptr q`; increments
  the count in _q_ the pointer in _q_ must be convertible to `T*`  
+ `p = q` - _p_ and _q_ are `shared_ptr`s holding pointers that can be
  converted to one another. Decrements _p_'s reference count and
  increments _q_'s count; deletes _p_'s existing memory if _p_'s count
  goes to 0.  
+ `p.unique()` - returns _true_ if `p.use_count()` is one;  
+ `p.use_count()` - returns the number of objects sharing with _p_; may
  be a slow operation, intended primarily for debugging purposes.  

#### Copying and Assigning `shared_ptr`s <!-- {{{ -->
Key point is that the class keeps track of how many `shared_ptr`s point
to the same object and automatically frees that object when appropriate.  

One way that `shared_ptr`s might stay around after you need them is if
you put `shared_ptr`s in a container and subsequently reorder the
container so that you don't need all the elements. You should be sure to
`erase` `shared_ptr` elements once you no longer need those elements.  
<!-- }}} -->
#### Classes with Resources That Have Dynamic Lifetime <!-- {{{ -->

1. They don't know how many objects they'll need  
2. They don't know the precise type of the objects they need  
3. They want to share data between several objects  

So far, the classes we've use allocate resources that exist only as long
as the corresponging objects. For example, each `vector` "owns" its own
elements
```cpp
vector<string v1;   // empty vector
{ // new scope
    vector<string> v2 = {"a", "an", "the"};
} // v2 is destroyed, which destroys the elements in v2
  // v1 has three elements, which are copies of the ones originally in v2
```

Some classes allocate resources with a lifetime that is independent of
the original object. AS an example, assume we want to define a class
named _Blob_ that will hold a collection of elements. Unlike the
containers, we want _Blob_ objects that are copies of one another to
share the same elements. That is, when we copy a _Blob_, the original
and the copy should refer to the same underlying elements.  
In general, when two objects share the same underlying data, we can't
unilaterally destroy the data when an objects of that type goes away:
```cpp
Blob<string> b1;    // empty Blob
{ // new scope
    Blob<string> b2 = {"a", "an", "the"};
    b1 = b2;    // b1 and b2 share the same elements
} // b2 is destroyed, but the elements in b2 must not be destroyed
  // b1 points to the elements originally created in b2
```


<!-- }}} -->
#### Defining the `StrBlob` Class <!-- {{{ -->
We can't store the `vector` directly in a Blob object. To ensure that
the elements continue to exist, we'll store the `vector` in synamic
memory. To implement the sharing we want, we'll give each `StrBlob` a
`shared_ptr` to a dynamicaly allocated `vector`.  

We still need to decide what operations our class will provide.
Operations that access elements will throw an exception if a user
attempts to access an element that doesn't exist.  

```cpp
class StrBlob {
public:
    typedef std::vector<std::string>::size_type size_type;
    StrBlob();
    StrBlob(std::initializer_list<std::string> il);
    size_type size() const { return data->size(); }
    bool empty() const { return data->empty(); }
    // add and remove elements
    void push_back(const std::string &t) { data->push_back(t); }
    void pop_back();
    // element access
    std::string& front();
    std::string& back();
private:
    std::shared_ptr<std::vector<std::string>> data;
    // throws msg if data[i] isn't valid
    void check(size_type i, const std::string &msg) const;
}
```

**Constructors**  
```cpp
StrBlob::StrBlob(): data(make_shared<vector<string>>()) { }
StrBlob::StrBlob(initializer_list<string> il):
            data(make_shared<vector<string>>(il)) { }
```

**Element Access Members**  
```cpp
void StrBlob::check(size_type i, const string &msg) const {
    if (i >= data->size())
        throw out_of_range(msg);
}
```



<!-- }}} -->

<!-- }}} -->
### Managing Memory Directly <!-- {{{ -->

+ `new` operator allocates memory  
+ `delete` frees memory allocated by `new`  

#### Using `new` to Dynamically Allocate and Initialize Objects <!-- {{{ -->
`new` returns a pointer to the object it allocates:
```cpp
int *pi = new int;  // pi points to a dynamically allocated,
                    // unnamed, default initialized int
```
This new expression constructs an object of type `int` on the free store
and returns a pointer to that object.  

we can initialize a dynamically allocated object using direct
initialization:
```cpp
int *pi = new int(1024);
string *ps = new string(10, '9');
vector<int> *pv = new vector<int>{0,1,2,3,4,5,6,7,8,9};
```

We can also value initialize a dynamically allocated object by following
the type name with a pair of empty parentheses:
```cpp
string *ps1 = new string;   // default initialized to the empty string
string *ps = new string();  // value initialized to the empty string
int *pi1 = new int;         // default initialized; *pi1 is undefined
int *pi2 = new int();       // value initialized to 0; *pi2 is 0
```

If you want to use auto:
```cpp
auto p1 = new auto(obj);    // p points to an object of the type of obj
                            // that object is initalized from obj
auto p2 = new auto{a,b,c};  // error: must use parentheses for the initializer
```


<!-- }}} -->
#### Dynamically Allocated `const` Objects <!-- {{{ -->
It is legal to use `new` to allocate `const` objects:
```cpp
// allocate and initialize a const int
const int *pci = new const int(1024);
// allocate a default-initialized const empty string
const string *pcs = new const string;
```

<!-- }}} -->
#### Memory Exhaustion <!-- {{{ -->
Once a program was used all of its available memoryh, `new` expressions
will fail, and `bad_alloc` exception will be thrown. We can preven `new`
from throwing an exception by using a different form of `new`:
```cpp
// if allocation fails, new returns a null pointer
int *p1 = new int;  // if allocation fails, new throws `std::bad_alloc`
int *p2 = new (nothrow) int;    // if allocation fails, new returns a null pointer
```

<!-- }}} -->
#### Freeing Dynamic Memory <!-- {{{ -->
We return memory through a `delete` expression. It takes a pointer to
the object we want to free:
```cpp
delete p;   // p must point to a dynamically allocated object or be null
```
It destroys th eojbect to which its given pointer points, and it frees
the correspoinding memory.  

<!-- }}} -->
#### Pointer Values and `delete` <!-- {{{ -->
Directly deleting `int` object will generate error. But deleting pointer
or reference to dynamically allocated pointer is silently skipped.  
<!-- }}} -->
#### Dynamically Allocated Objects Exist until They Are Freed <!-- {{{ -->
Functions that return pointers (rather than smart pointers) to dynamic
memory put a burden on their callers - the caller must remember to
delete the memory.  
<!-- }}} -->
#### Resetting the Value of a Pointer after a `delete` <!-- {{{ -->
Consider following code:
```cpp
int *p(new int(42));
auto q = p;
delete p;
p = nullptr;
```
_q_ is now invalid pointer. Be sure to not write it in your code.  

<!-- }}} -->
<!-- }}} -->
### Using `shared_ptr`s with `new` <!-- {{{ -->
We can also initialize a smart pointer from a pointer returned by `new`:
```cpp
shared_ptr<double> p1;  // shared_ptr that can point at a double
shared_ptr<int> p2(new int(42));    // p2 points to an int with value 42
```

Other ways to define and change `shared_ptr`s:  

+ `shared_ptr<T> p(q)` - _p_ manages the object to which the built-in
  pointer _q_ points; _q_ must point to memory allocated by `new` and
  must be convertible to `T*`  
+ `shared_ptr<T> p(u)` - _p_ assumes ownership from the `unique_ptr u`;
  makes _u_ null.  
+ `shared_ptr<T> p(q, d)` - _p_ assumes ownership from the object to
  which the built-in pointer _q_ points. _q_ must be convertible to
  `T*`. _p_ will use the callable object _d_ in place of `delete` to
  free _q_.  
+ `shared_ptr<T> p(p2, d)` - _p_ is a copy of the `shared_ptr p2`. _p_
  uses callable object _d_ in place of `delete`  
+ `p.reset()`, `p.reset(q)`, `p.reset(q,d)` - if _p_ is the only
  `shared_ptr` pointing at its object, `reset` free _p_'s existing
  object. If the optional built-in pointer _q_ is passed, makes _p_
  point to _q_, otherwise makes _p_ null. If _d_ is supplied, will call
  _d_ to free _q_ otherwise uses `delete` to free _q_.  

The smart pointer constructors that take pointers are `explicit`. Hence
we must use the direct form of initialization:
```cpp
shared_ptr<int> p1 = new int(1024); // error: must use direct initialization
shared_ptr<int> p2(new int(1024));  // ok: uses direct initialization
```
For the same reason, a function that returns a `shared_ptr` cannot
implicitly convert a plain pointer in its return statement:
```cpp
shared_ptr<int> clone(int p) {
    return new int(p);  // error: implicit conversion to `shared_ptr<int>`
}
```
Correct:
```cpp
shared_ptr<int> clone(int p) {
    // ok: explicitly create a shared_ptr<int> from int*
    return shared_ptr<int>(new int(p));
}
```

#### Don't Mix Ordinary Pointers and Smart Pointers <!-- {{{ -->
```cpp
int *x(new int(1024));  // dangerous: x is a plain pointer, not a smart pointer
process(x); // error: cannot convert int* to shared_ptr<int>
process(shared_ptr<int>(x));    // legal, but the memory will be deleted!
int j = *x; // undefined: x is a dangling pointer!
```

Another example:
```cpp
shared_ptr<int> p(new int(42)); // reference count is 1
int *q = p.get();   // ok: but don't use q in any way that might delete its pointer
{ // new block
// undefined:two independent shared_ptrs point to the same memory
shared_ptr<int>(q);
} // block ends, q is destroyed, and the memory to which q points is freed
int foo = *p; // undefined; the memory to which p points was freed
```


<!-- }}} -->

<!-- }}} -->
### Smart Pointers and Exceptions <!-- {{{ -->
Smart pointers are automatically destroy elements well they're leaving
their's scope. In other side, built-in pointers can't do that if
exception is not handled:
```cpp
void f()
{
    int *ip = new int(42);  // dynamically allocate a new object
    // code that throws an exception that is not caught inside f
    delete ip;  // free the memory before exiting
}
```

#### Smart Pointers and Dumb Classes <!-- {{{ -->
Classes that allocate resources and that do not define destructors to
free those resources - can be subject to the same kind of errors that
arise when we use dynamic memory. It is easy to forget to release the
resource. Similarly, if an exception happens between when the resource
is allocated and when it is freed, the program will leak that resource.  
<!-- }}} -->
#### Using Our Own Deletion Code <!-- {{{ -->
To use a `shared_ptr` to manage a `connection`, we must first define a
function to use in place of `delete`. In this case, our deleter must
take a single argument of type `connection*`:
```cpp
void end_connection(connection *p) {disconnect(*p); }
```
When we create a `shared_ptr`, we can pass an optional argument that
points to a deleter function:
```cpp
void f(destination &d /* other parameters */)
{
    connection c = connect(&d);
    shared_ptr<connection> p(&c, end_connection);
    // use the connection
    // when f exits, even if by an exception, the connection will be properly closed
}
```

<!-- }}} -->

<!-- }}} -->
### `unique_ptr` <!-- {{{ -->
Unlike `shared_ptr`, only one `unique_ptr` at a time can point to a
given object.  

`unique_ptr` Operations:  

+ `unique_ptr<T> u1`, `unique_ptr<T,D> u2` - null `unique_ptr` that can point to objects of
  type `T`. _u1_ will use `delete` to free its pointer; _u2_ will use a
  callable object of type _D_ to free its pointer.  
+ `unique_ptr<T,D> u(d)` - null `unique_ptr` that point to objects of
  type `T` that uses _d_, which must be an object of type `D` in place
  of `delete`.  
+ `u = nullptr` - deletes the object to which _u_ points; makes _u_
  null.  
+ `u.release()` - relinquishes control of the pointer _u_ had held;
  returns the pointer _u_ had held and makes _u_ null.  
+ `u.reset()`, `u.reset(q)`, `u.reset(nullptr)` - deletes the object to
  which _u_ points; if the built-in pointer _q_ is supplied, makes _u_
  point to that object. Otherwise makes _u_ null.  

Unlike `shared_ptr`, there is no library function comparable to
`make_shared`. Instead, when we define a `unique_ptr`, we bind it to a
pointer returned by `new`. As with `shared_ptr`s, we must use the direct
form of initialization  

Because a `unique_ptr` owns the object to which it points, `unique_ptr`
does not support ordinary copy or assignment:
```cpp
unique_ptr<string> p1(new string("Stegosaurus"));
unique_ptr<string> p2(p1);  // error: no copy for `unique_ptr`
unique_ptr<string> p3;
p3 = p2;                    // error: no assign for unique_ptr
```

Although we can't copy or assign a `unique_ptr`, we can transfer
ownership from one (nonconst) `unique_ptr` to another by calling
`release` or `reset`:
```cpp
// transfers ownership from p1 (which points to the string "Stegosaurus") to p2
unique_ptr<string> p2(p1.release());    // release make p1 null
unique_ptr<string> p3(new string("Trex"));
// transfers ownership from p3 to p2
p2.reset(p3.release()); // reset deletes the memory to which p2 had pointed
```

Calling `release` breaks the ocnnection between a `unique_ptr` and the
object it had been managing.
```cpp
p2.release();   // WRONG: p2 won't free the memory and we've lost the pointer
auto p = p2.release();  // ok, but we must remember to delete(p)
```

#### Passing and Returning `unique_ptr`s <!-- {{{ -->
There is one exception to the rule that we cannot copy a `unique_ptr`:
We can copy or assign a `unique_ptr` that is about to be destroyed:
```cpp
unique_ptr<int> clone(int p) {
    // ok: explicitly create a unique_ptr<int> from int*
    return unique_ptr<int(new int(p))
}
```
Alternatively, we can also return a copy of a local object:
```cpp
unique_ptr<int> clone(int p) {
    unique_ptr<int> ret(new int(p));
    // . . .
    return ret;
}
```
In both cases, the compiler knows that the object being returned is
about to be destroyed. In such cases the compiler does a special kind of
"copy".  


<!-- }}} -->
#### Passing a Deleter to `unique_ptr` <!-- {{{ -->
Overridding the deleter in a `unique_ptr` affects the `unique_ptr` type
as well as how we construct (or `reset`) objects of that type. Thus we
must supply the deleter type inside the angle brackets along with the
type to which the `unique_ptr` can point.  

As a example, we'll rewrite our connection program to use a `unique_ptr`
in place of a `shared_ptr`:
```cpp
void f(destination &d /* other needed parameters */) {
    connection c = connect(&d); // open the connection
    /// when p is destroyed, the connection will be closed
    unique_ptr<connection, decltype(end_connection)*>
        p(&c, end_connection);
    // use the connection
    // when f exits, even if by an exception, the connection will be properly closed
}
```

<!-- }}} -->

<!-- }}} -->
### `weak_ptr` <!-- {{{ -->
A `weak_ptr` is a smart pointer that does not control the lifetime of
the object to which it points. Instead, a `weak_ptr` points to an object
that is managed by a `shared_ptr` (binding to a `shared_ptr` does not
change the reference count of last).  

+ `weak_ptr<T> w` - null `weak_ptr` that can point at objects of type `T`  
+ `weak_ptr<T> w(sp)` - `weak_ptr` that points to the same object as the
  `shared_ptr` _sp_. `T` must be convertible to the type to which _sp_
  points.  
+ `w = p`- _p_ can be a `shared_ptr` or a `weak_ptr`. After the
  assignment _w_ shares  ownership with _p_.  
+ `w.reset()` - makes _w_ null.  
+ `w.use_count()` - the number of `shared_ptr`s that share ownership
  with _w_.  
+ `w.expired()` - returns `true` if `w.use_count()` is zero, `false`
  otherwise.  
+ `w.lock()` - if `expired` is `true`, returns a null `shared_ptr`;
  otherwise returns a `shared_ptr` to the object to which _w_ points.  

When we create a `weak_ptr`, we initialize it from a `shared_ptr`:
```cpp
auto p = make_shared<int>(42);
weak_ptr<int> wp(p);    // wp weakly shares with p; use count in p is unchanged
```
We cannot use a `weak_ptr` to access its object directly:
```cpp
if (shared_ptr<int> np = wp.lock()) { // true if np is not null
    // inside the if, np shares its objects with p
}
```

#### Checked Pointer Class <!-- {{{ -->
Check was vector been destoyed:
```cpp
std::shared_ptr<std::vector<std::string>>
StrBlobPtr::check(std::size_t i, const std::string &msg) const
{
    auto ret = wptr.lock(); // is the vector still around?
    if (!ret)
        throw std::runtime_error("unbound StrBlobPtr");
    if (i >= ret->size())
        throw std::out_of_range(msg);
    return ret; // otherwise, return a `shared_ptr` to the `vector`
}
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Dynamic Arrays <!-- {{{ -->
### `new` and Arrays <!-- {{{ -->
We ask `new` to allocate an array of objects by specifying the number of
objects to allocate in pair of square brackets after a type name. In
this case, `new` allocates requested number of objects and (assuming the
allocation succeeds) returns a pointer to the first one:
```cpp
// call get_size to determine how many ints to allocate
int *pia = new int[get_size()]; // pia points to the first of these ints
```
We can also allocate an array by using a type alias to represent an
array type:
```cpp
typedef int arrT[42];   // arrT names the type array of 42 ints
int *p = new arrT;  // allocates an array of 42 ints; p points to the first one
```

#### Initializing an Array of Dynamically Allocated Objects <!-- {{{ -->
```cpp
int *pia = new int[10]; // block of ten unitialized ints
int *pia2 = new int[10]();  // block of ten ints value initialized to 0
string *psa = new string[10];   // block of ten empty strings
string *psa2 = new string[10];  // block of ten empty strings
```

Under **c++11** standard, we can also provide a braced list of element
initializers:
```cpp
// block of ten ints each initialized from the corresponding initializer
int *pia3 = new int[10]{0,1,2,3,4,5,6,7,8,9};
// block of ten strings; the first four are initialized from the given initializers
// remaining elements are value initialized
string *psa3 = new string[10]{"a","an","the",string(3,'x')};
```

If there are more initializers than the given size, then the `new`
expression fails and no storage is allocated. In this case, `new` thows
an exception of type `bad_array_new_length`.  

Under **c++11** standart **it is legal to dynamically allocate an empty
array**  

<!-- }}} -->
#### Freeing Dynamic Arrays <!-- {{{ -->
```cpp
delete p;       // p must point to a dynamically allocated object or be null
delete [] pa;   // pa must point to a dynamically allocated array or be null
```

<!-- }}} -->
#### Smart Pointers and Dynamic Arrays <!-- {{{ -->
The library provides a version of `unique_ptr` that can manage arrays
allocated by `new`. To use a `unique_ptr` to manage a dynamic array, we
must include a pair of empty brackets after the object type:
```cpp
// up points to an array of ten unitialized ints
unique_ptr<int[]> up(new int[10]);
up.release();   // automatically uses delete[] to destroy its pointer
```

`unique_ptr`s to Arrays:  

+ `unique_ptr<T[]> u` - _u_ can point to a dynamically allocated array
  of type `T`  
+ `uniqut_ptr<T[]> u(p)` - _u_ points to the dynamically allocated array
  to which the built-in pointer _p_ points. _p_ must be convertible to `T*`  
+ `u[i]` - returns the object at position _i_ in the array that _u_
  owns. _u_ must point to an array.  

Unlike `unique_ptr`, `shared_ptr`s provide no direct support for
managing a dynamic array:
```cpp
// to use a shared_ptr we must supply a deleter
shared_ptr<int> sp(new int[10], [](int *p) {delete[] p; });
sp.reset(); // uses the lambda we supplied that uses delete[] to free the array
```
The fact that `shared_ptr`does not directly support managing arrays
affects how we access the elements in the array:
```cpp
// shared_ptrs don't have subscript operator and don't support pointer
arithmetic
for (size_t i = 0; i != 10; ++i)
    *(sp.get() + i) = i;    // use get to get a built-in pointer
```

<!-- }}} -->
<!-- }}} -->
### The `allocator` Class <!-- {{{ -->
When we allocate a block of memory, we often plan to construct objects
in that memory as needed. In this case, we'd like to decouple memory
allocation from object construction.  

#### The `allocator` Class <!-- {{{ -->
Standard `allocator` Class and Customized Algorithms:  

+ `allocator<T> a`- defines an `allocator` object named _a_ that can
  allocate memory for objects of type `T`.  
+ `a.allocate(n)` - allocates raw, unconstructed memory to hold _n_
  objects of type `T`.  
+ `a.deallocate(p, n)` - deallocates memory that held _n_ objects of
  type `T` starting at the addres in the `T*` pointer _p_; _p_ must be a
  pointer previously returned by `allocate`, and _n_ must be the size
  requested when _p_ was created. The user must run `destroy` on any
  object that were constructed in this memory before calling
  `deallocate`.  
+ `a.construct(p, args)` - _p_ must be a pointer to type `T` that points
  to raw memory; _args_ are passed to a constructor for type `T`, which
  is used to construct an object in the memory pointed to by _p_.  
+ `a.destroy(p)` - runs the destructor on the object pointed to by the
  `T*` pointer _p_  

```cpp
allocator<string> alloc;    // object that can allocate strings
auto const p = alloc.allocate(n);   // allocate n unconstructed strings
```

Constructing:
```cpp
auto q = p; /// q will point to one past the last constructed element
alloc.construct(q++);   // *q is the empty string
alloc.construct(q++, 10, 'c');  // *q is ccccccccccc
alloc.construct(q++, "hi"); // *q is hi!
```

It is an error to use raw memory in which an object has not been
constructed.  

When we're finished using the objects, we must destroy the elements we
constructed:
```cpp
while (q != p)
    alloc.destroy(--q); // free the strings we actually allocated
```

Once the elements have been destroyed, we can either reuse the memory to
hold other `string`s or return the memory to system:
```cpp
alloc.deallocate(p, n);
```

As a companion to the `allocator` class, the library also defined two
algorithms that can construct objects in unitialized memory:  

+ `uninitialized_copy(b, e, b2)` - copies elements from the input ranger
  denoted by iterators _b_ and _e_ into unconstructed, raw memory
  denoted by the iterator _b2_. The memory denoted by _b2_ must be large
  enough to hold a copy of the elements in the input range  
+ `uninitialized_copy_n(b,n,b2)` - copies _n_ elements starting from the
  iterator _b_ into raw memory starting at _b2_.  
+ `unitialized_fill(b, e, t)` - constructs objects in the range of raw
  memory denoted by iterators _b_ and _e_ as a copy of _t_.  
+ `unitialized_fill_n(b, n, t)`  

```cpp
// allocate twice as many elements as vi holds
auto p = alloc.allocate(vi.size() * 2);
// construct elements starting at p as copies of elements in vi
auto q = uninitialized_copy(vi.begin(), vi.end(), p);
// initialize the remaining elements to 42
uninitialized_fill_n(q, vi.size(), 42);
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Using the Library: A Text-Query Program <!-- {{{ -->
We'll implement a simple text-query program. Our program will let a user
search a given file for words that might occur in it. The result of a
query will be the number of times the word occurs and a list of lines on
which that word appears.  

### Design of the Query Program <!-- {{{ -->
A good way to start the design of a program is to list the program's
operations:  

+ When it reads the input, the program must remember the line(s) in
  which each word appears. Hence, the program will need to read the
  input a line at a time and break up the lines from the input file into
  its separate words  
+ When it generates output:  
    - The program must be aple to fetch the line numbers associated with
  a given word  
    - The line numbers must appear in ascending order with no
  duplicates  
    - The program must be aple to print the text appearing in the input
  file at a given line number.  

These requirements can be met quite neatly by using various library
facilities:  

+ We'll use a `vector<string>` t ostore a copy of the entire input file.
  Each line in the input file will be an element in this `vector`.
  When we want to print a line, we can fetch the line using its
  line number as the index.  
+ We'll use an `istringstream` to break each line into words.  
+ We'll use a `set` to hold the line numbers on which each word in the
  input appears. Using a `set` guarantees that each line will appear
  only once and that the line numbers will be stored in ascending order.  
+ We'll use a `map` to associate each word with the `set` of line
  numbers on which the word appears. Using a `map` will let us fetch the
  `set` for any given word.  
+ We'll use a `shared_ptr` so returned data structure may have valid
  pointer to containers in main class  


#### Data Structures <!-- {{{ -->
We must return number of occurances as well as line number for each of
occurences. The easiest way to return all the data is define asecond
clas, which we'll name `QueryResult`.  
<!-- }}} -->
#### Using the `TextQuery` Class <!-- {{{ -->
When we design a class, it can be helpful to write programs using the
class before actually implementing the members. That way, we can see
whether the class has the operations we need.  
For instance this function takes an `ifstream` that points to the file
we want to process, and interacts with a user, printing the results for
the given words:
```cpp
void runQueries(ifstream &infile) {
    // infile is an ifstream that is the ifle we want to query
    TextQuery tq(infile);   // store the file and build the query map
    // iterate with the user: prompt for a word to find and print results
    while (true) {
        cout << "enter word to look for, or q to quit: ";
        string s;
        // stop if we hit end-of-file on the input or if a 'q' is entered
        if (!(cin >> s) || s == "q") break;
        // run the query and print the results
        print(cout, tq.query(s)) << endl;
    }
}
```

<!-- }}} -->
<!-- }}} -->
### Defining the Query Program Classes <!-- {{{ -->
```cpp
class QueryResult;  // declaration needed for return type in the query function
class TextQuery {
public:
    using line_no = std::vector<std::string>::size_type;
    TextQuery(std::ifstream&);
    QueryResult query(const std::string&) const;
private:
    std::shared_ptr<std::vector<std::string>> file; // input file
    // map of each word to the set of the line in which that word appears
    std::map<std::string,
             std::stared_ptr<std::set<line_no>>> wm;
}
```

#### The `TextQuery` Constructor <!-- {{{ -->

```cpp
// read the input file and build the map of line to line numbers
TextQuery::TextQuery(ifstream &is): file(new vector<string>) {
    string text;
    while (getline(is, text)) {     // for each line in the file
        file->push_back(text);      // remember this line of text
        int n = file->size() - 1;   // the current line number
        istringstream line(text);   // separate the line into words
        string word;
        while (line >> word) {      // for each word in that line
            // if word isn't already in wm, subsripting adds a new entry
            auto &lines = wm[word]; // lines is a shared_ptr
            if (!lines) // that pointer is null the first time we see word
                lines.reset(new set<line_no>);  // allocate a new set
            lines->insert(n);   // insert this line number
        }
    }
}
```

<!-- }}} -->
#### The `QueryResult` Class <!-- {{{ -->

```cpp
class QueryResult {
friend std::ostream& print(std::ostream&, const QueryResult&);
public:
    QueryResult(std::string s,
                std::shared_ptr<std::set<line_no>> p,
                std::shared_ptr<std::vector<std::string>> f):
        sought(s), lines(p), file(f) { }
private:
    std::string sought; // word this query represents
    std::shared_ptr<std::set<line_no>> lines;   // lines it's on
    std::shared_ptr<std::vector<std::string>> file; // input file
}
```

<!-- }}} -->
#### The `query` Function <!-- {{{ -->
The only question is: What should we return if the given `string` is not
found? We'll solve this problem by defining a local `static` object that
is a `shared_ptr` to an empty `set` of line numbers. When the word is
not found, we'll return a copy of this `shared_ptr`:
```cpp
QueryResult
TextQuery::query(const string &sought) const {
    // we'll return a pointer to this set if we don't find sought
    static shared_ptr<set<line_no>> nodata(new set<line_no>);
    // use find and not a subscript to avoid adding words to wm!
    auto loc = wm.find(sought);
    if (loc == wm.end())
        return QeryResult(sought, nodata, file);    // not found
    else
        return QueryResult(sought, loc->second, file);
}
```

<!-- }}} -->
#### Printing the Results <!-- {{{ -->
```cpp
ostream &print(ostream &os, const QueryResult &qr) {
    // if the word was found, print the count and all occurences
    os << qr.sought << " occurs " << qr.lines->size() << " "
        << make_plural(qr.lines->size(), "time", "s") << endl;
    // print each line in which the word appeared
    for (auto num : *qr.lines) // for every element in the set
        // don't confound the user with text lines starting at 0
        os << "\t(line " << num + 1 << ") "
            << *(qr.file->begin() + num) << endl;
    return os;
}
```

<!-- }}} -->

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Copy Control <!-- {{{ -->
Class defines five special member functions:  

+ **copy contstructor**  
+ **move constructor**  
+ **copy-assignment operator**  
+ **move-assignment operator**  
+ **destructor**  

+ Copy/move constructors define what happens when an obje ct is
initialized from another object of the same type.  
+ Copy-/move-assignment operators define what happens when we assign an
object of a class type to another object of that same class type.  
+ The destructor defines what happens when an object of the type ceases to
exist.  

## Copy, Assign, and Destroy <!-- {{{ -->
### The Copy Constructor <!-- {{{ -->
A constructor is the _copy constructor_ if its first parameter is a
reference to the class type and any additional parameters have default
values:
```cpp
class Foo {
public:
    Foo();              // default constructor
    Foo(const Foo&);    // copy constructor
    // ...
}
```
Copy constructor usually should not be `explicit`. Also we can define
the copy constructor to take a reference to non`const`.  

#### The Sunthesized Copy Constructor <!-- {{{ -->
When we do not define a copy constructor for a class, the compiler
synthesizes one for us. THe compiler copies each non`static` member in
turn from the given object into the one being created.  

The type of each member determines how that member is copied:  

+ members of class type are copied by the copy constructor for that
  class;  
+ members of built-in type are copied directly  
+ although we cannot directly copy an array, the synthesized copy
  constructor copies members of array type by copying each element.  
<!-- }}} -->
#### Copy Initialization <!-- {{{ -->

```cpp
string dots(10, '.');               // direct initialization
string s(dots);                     // direct initialization
string s2 = dots;                   // copy initialization
string null_book = "9-999-99999-9"; // copy initialization
string nines = string(100, '9');    // copy initialization
```

When we use direct initialization, we are asking the compiler to use
ordinary function matching to select the constructor that best matches
the arguments we provide. When we use copy initialization, we are asking
the compiler to copy the right-hand operand into the object being
created, converting that operand if necessary.  

Copy initialization happens not only when we define variables using an `=`, but also when we:  

+ pass an object as an argument to a parameter of nonreference type  
+ return an object from a function that has a nonreference return type  
+ brace initialize the elements in an array or the members of an
  aggregate class  

<!-- }}} -->
#### Constraints on Copy Initialization <!-- {{{ -->
```cpp
vector<int> v1(10); // ok: direct initialization
vector<int> v2 = 10;    // error: constructor that takes a size is explicit
void f(vector<int>);    // f's parameter is copy initialized
f(10);  // error: can't use an explicit constructor to copy an argument
f(vector<int>(10)); // ok: directly construct a temporary vector from an int
```

<!-- }}} -->
<!-- }}} -->
### The Copy-Assignment Operator <!-- {{{ -->
```cpp
Sales_data trans, accum;
trans = accum;  // uses the Sales_data copy-assignment operator
```

#### Introducing Overloaded Assignment <!-- {{{ -->
Assignment operator is a function named `operator=`. Like any other
function, an operator function has the return type and a parameter list.  

When operator is a member function, the left-hand operand is bound to
the implicit `this` parameter. The right-hand operand in a binary
operator, such as assignment, is passed as an explicit parameter.  

```cpp
class Foo {
public:
    Foo& operator=(const Foo&); // assignment operator
}
```

<!-- }}} -->
#### The Synthesized Copy-Assignment Operator <!-- {{{ -->
```cpp
// equivalent to the synthesized copy-assignment operator
Sales_data& Sales_data::operator=(const Sales_data &rhs) {
    bookNo = rhs.bookNo     // calls the string::operator=
    units_sold = rhs.units_sold;    // uses built-in int assignment
    revenue = rhs.revenue;  // uses the built-in double assignment
    return *this;           // return a reference to this object
}
```

<!-- }}} -->

<!-- }}} -->
### The Destructor <!-- {{{ -->
Destructors do whatever work is needed to free the resources used by an
object and destroy the non`static` data members of the object. The
destructor is a member function with the name of the class prefixed by a
tilde (`~`). It has no return value and takes no parameters:
```cpp
class Foo {
public:
    ~Foo();     // destructor
}
```

#### What a Destructor Does <!-- {{{ -->
Members are destroyed in reverse order from the order in which they were
initialized.  
<!-- }}} -->
#### The Synthesized Destructor <!-- {{{ -->
```cpp
class Sales_data {
public:
    // no work to do other than destroying the members, which happens automatically
    ~Sales_data() { }
}
```
It is important to realize that the destructor body does not directly
destroy the members themselves. Members are destroyes as part of the
implicit destruction phase that follows the destructor body.  

<!-- }}} -->

<!-- }}} -->
### The Rule of Three/Five <!-- {{{ -->
Classes That Need Destructors Need Copy and Assignment  
Classes That Need Copy Need Assignment, and Vice Versa  

<!-- }}} -->
### Using `= default` <!-- {{{ -->
We can explicitly ask the compiler to generate the synthesized versions
of the copy-control members by defining them as `= default`.  

```cpp
class Sales_data {
public:
    // copy control; use defaults
    Sales_data() = default;
    // synthesized function is inline
    Sales_data(const Sales_data&) = default;
    Sales_data& operator = (const Sales_data&);
    ~Sales_data() = default;
};
// synthesized function is not inline
Sales_data& Sales_data::operator=(const Sales_data&) = default;
```

When we specify `= default` on the declaration of the member inside the
class body, the synthesized function is implicitly inline. If we do not
want the synthesized member to be an inline function, we can specify `=
default` on the member's definition, as we do in the definition of the
copy-assignment operator.  

<!-- }}} -->
### Preventing Copies <!-- {{{ -->
#### Define a Function as Deleted <!-- {{{ -->
We indicate that we want to define a function as deleted by following
its parameter list with `= delete`:
```cpp
struct NoCopy {
    NoCopy() = default;     // use the synthesized default constructor
    NoCopy(const NoCopy&) = delete;                 // no copy
    NoCopy& operator = (const Nocopy&) = delete;    // no assignment
    ~NoCopy() = default;    // use the synthesized destructor
}
```

<!-- }}} -->
#### The Destructor Should Not be a Deleted Member <!-- {{{ -->
The compiler will not let us define variables or create temporaries of a
type that has a deleted destructor. Although we cann define variables or
members of such types, we can dynamically allocate objects with a
deleted destructor. However, we cannot free them:
```cpp
struct NoDtor {
    NoDtor() = default;
    ~noDtor() = delete; // we can't destroy objects of type NoDtor
};
NoDtor nd;  // error: NoDtor destructor is deleted
NoDtor *p = new Nodtor();   // ok: but we can't delete p
delete p;   // error: NoDtor destructor is deleted
```

<!-- }}} -->
#### The Copy-Control Members May Be Synthesized as Deleted <!-- {{{ -->
For some classes, the compiler defines these synthesized members as
deleted functions:  

+ The synthesized destructor is defined as deleted if the class has a
  member whose own destructor is deleted or is inaccessible.  
+ The synthesized copy constructor is defined as deleted if the class
  has a member whose own copy constructor is deleted or inaccessible. It
  is also deleted if the class has a member with a deleted or
  inaccessible destructor.  
+ The synthesized copy-assignment operator is defined as deleted if a
  member has a deleted or inaccessible copy-assignment operator, or if
  the class has a `const` or reference member.  
+ The synthesized default constructor is defined as deleted if the class
  has a member with a deleted or inaccessible destructor; or has a
  reference member that does not have an in-class initializer; or has a
  `const` member whose type does not explicitly define a default
  constructor and that member does not have an in-class initializer.  

<!-- }}} -->
#### `private` Copy Control <!-- {{{ -->
Prior to the new standard, classes prevented copies by declaring their
copy constructor and copy-assignment operator as `private`:
```cpp
class PrivateCopy {
    // no control is private and so is inaccessible to ordinary user code
    // friends and members of the class can still make copies
    PrivateCopy(const PrivateCopy&);
    PrivateCopy &operator=(const PrivateCopy&);
public:
    PrivateCopy() = default;    // use the synthesized default constructor
    ~PrivateCopy(); // users can define objects of this type but not copy them
};
```


<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Copy Control and Resource Management <!-- {{{ -->
To illustrate two approaches (value-/pointer-like), we'll define the
copy-control members for the HasPtr class used in the exercises. First,
we'll make the class act like a value; then we'll reimplement the class
making it behave like a pointer.  

### Classes That Act Like Values <!-- {{{ -->

To implement valuelike behavior HasPtr needs:  

+ A copy constructor that copies the `string`, not just the pointer  
+ A destructor to free the `string`  
+ A copy-assignment operator to free the object's existing `string` and
  copy the `string` from its right-hand operand.  

```cpp
class HasPtr {
public:
    HasPtr(const std::string &s = std::string()):
        ps(new std::string(s)), i(0) { }
    // each HasPtr has its own copy of the new string to which ps points
    HasPtr(const HasPtr& p):
        ps(new std::string(*p.ps)), i(p.i) { }
    HasPtr& operator=(const HasPtr&);
    ~HasPtr() { delete ps; }
private:
    std::string *ps;
    int i;
}
```

#### Valuelike Copy-Assignment Operator <!-- {{{ -->
Assignment operators typically combine the actions of the destructor and
the copy constructor.  

```cpp
HasPtr& HasPtr&::operator = (const HasPtr &rhs) {
    auto newp = new string(*rhs.ps);    // copy the underlying string
    delete ps;      // free the old memory
    ps = newp;      // copy data from rhs into this object
    i = rhs.i;
    return *this;   // return this object
}
```

There are two points to keep in mind when you write an assignment
operator:  

+ assignment operators must work correctly if an object is assigned to
  itself.  
+ most assignment operators share work with the destructor and copy
  constructor.  

A good pattern to use when you write an assignment operator is to first
copy the right-hand operand into a local temporary. After the copy is
done, it is safe to destroy and replace the existing members of the left-hand
operand.  

<!-- }}} -->


<!-- }}} -->
### Defining Classes That Act Like Pointers <!-- {{{ -->
The easiest way to make a class act like a pointer is to use `shared_ptr`s.
However, sometimes we want to manage a resource directly. In such cases,
it can be useful to use a _reference count_.  

#### Reference Counts <!-- {{{ -->

+ on initialization we initialize the counter to 1  
+ copy constructor does not allocate a new counter; instead, it shares
  it with the one who get copied and sums 1.  
+ destructor decrements the counter  
+ copy-assignment operator increments the right-hand operand's counter
  and decrements the ocunter of the left-hand operand. If the counter
  for the left-hand operand goes to zero, there are no more users. In
  this case, the copy-assignment operator must destroy the state of the
  left-hand operand.  

<!-- }}} -->
#### Defining a Reference-Counted Class <!-- {{{ -->
Using a dynamic reference count, we can write the pointerlike version of
HasPtr as follows:
```cpp
class HasPtr {
public:
    // constructor allocates a new string and a new counter, which it sets to 1
    HasPtr(const std::string &s = std::string()):
        ps(new std::string(s)), i(0), use(new std::size_t(1)) { }
    // copy constructor copies all three data members and increments the counter
    HasPtr(const HasPtr &p):
        ps(p.ps), i(p.i), use(p.use) { ++*use; }
    HasPtr& operator=(const HasPtr&);
    ~HasPtr();
private:
    std::string *ps;
    int i;
    std::size_t *use;   // member to keep track of how many objects share *ps
}
```

<!-- }}} -->
#### Pointerlike Copy Members "Fiddle" the Reference Count <!-- {{{ -->

The destructor cannot unconditionally delete ps:

```cpp
Hasptr::~HasPtr() {
    if (--*use == 0) {  // if the reference count goes to 0
        delete ps;      // delete the string
        delete use;     // and the counter
    }
}
```

Also, as usual, the assign operator must handle self-assignment:

```cpp
HasPtr& HasPtr::operator=(const HasPtr &rhs) {
    ++*rhs.use; // increment the use ocunt of the right-hand operand
    if (--*use == 0) {  // then decrement this object's counter
        delete ps;      // if no other users
        delete use;     // free this object's allocated members
    }
    ps = rhs.ps;        // copy data from rhs into this object
    i = rhs.i;
    use = rhs.use;
    return *this;       // return this object
}
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Swap <!-- {{{ -->
If a class defines its own `swap`, then the algorithm uses that
class-specific version. Otherwise, it uses the `swap`function defined by
the library.  

Simple swap we can do:
```cpp
string* temp = v1.ps;   // make a temporary copy of the pointer in v1.ps
v1.ps = v2.ps;          // assign the pointer in v2.ps to v1.ps
v2.ps = temp;           // assign the saved pointer in v1.ps to v2.ps
```

### Writing Our Own `swap` Function <!-- {{{ -->
The typical implementation of swap is:
```cpp
class HasPtr {
    friend void swap(HasPtr&, HasPtr&);
};
void swap(HasPtr &lhs, HasPtr &rhs) {
    using std::swap;
    swap(lhs.ps, rhs.ps);   // swap the pointers, not the string data
    swap(lhs.i, rhs.i);     // swap the int members
}
```

<!-- }}} -->
### `swap` Functions Should Call `swap`, Not `std::swap` <!-- {{{ -->
If you write:
```cpp
void swap(Foo& lhs, Foo& rhs) {
    //  WRONG: this function uses the library vesion of swap, not the HasPtr version
    std::swap(lhs.h, rhs.h);
}
```
The right way to write this `swap` function is:
```cpp
void swap(Foo& lhs, Foo& rhs) {
    using std::swap;
    swap(lhs.h, rhs.h); // uses the HasPtr version of swap
}
```
If there is a type-specific version of `swap`, that version will be a
better match than the one defined in `std`.  



<!-- }}} -->
### Using `swap` in Assignment Operators <!-- {{{ -->
These operators use a technique known as **copy and swap**. This
technique _swaps the left-hand operand with a copy of the right-hand
operand_:
```cpp
// note rhs is passed by value, which means the HasPtr copy constructor
// copies the string in the right-hand operand into rhs
HasPtr& HasPtr::operator=(HasPtr rhs) {
    // swap the ocntents of the left-hand operand with the local variable rhs
    swap(*this, rhs);   // rhs now points to the memory this object had used
    return *this;       // rhs is destroyed, which deletes the pointer in rhs

}
```

<!-- }}} -->

<!-- }}} -->
## A Copy-Control Example <!-- {{{ -->
Some classes have bookkeeping or other actions that the copy-control
members must perform.  
As an example we'll sketch out two classes that might be used in a
mail-handling application. These classes, `Message` and `Folder`,
represent, respectively, email messages and directories in which a
message might appear. Each `Message` can appear in multiple `Folders`.
However, there will be only one copy of the ocntents of any given
`Message` (if the contents of `Message` are changed, those changes will
appear when we view that `Message` from any of its `Folders`)  
To keep track of which `Messages` are in which `Folders`, each `Message`
will store a set of pointers to the `Folders` in which it appears, and
vica verse.  

Our `Message` class will provide `save` and `remove` operations. To
create a new `Message`, we will specify the contents of the message. To
put a `Message` in a particular `Folder`, we must call `save`.  

> The copy-assignment operator often does the same work as is needed in
> the copy constructor and destructor. In such cases, the common work
> should be put in `private` utility functions.  

Assume `Folder`class has members named `addMsg` and `remMsg` that do
whatever work is need to add or remove this `Message`, respectively,
from the set of messages in the given `Folder`.  

### The `Message` Class <!-- {{{ -->

```cpp
class Message {
    friend class Folder;
public:
    // folders is implicitly initialized to the empty set
    explicit Message(const std::string &str = ""):
        contents(str) { }
    // copy control to manage pointers to this message
    Message(const Message&);            // copy constructor
    Message& operator=(const Message&); // copy assignment
    ~Message();                         // destructor
    // add/remove this Message from the specified Folder's set of messages
    void save(Folder&);
    void remove(Folder&);
private:
    std::string contents;               // actual message text
    std::set<Folder*> folders;          // Folders that have this Message
    // utility functions used by copy constructor, assignment, and destructor
    // add this Message to the folders that point to the parameter
    void add_to_Folders(const Message&);
    // remove this Message from every Folder in folders
    void remove_from_Folders();
}
```


<!-- }}} -->
### The `save` and `remove` Members <!-- {{{ -->

```cpp
void Message::save(Folder &f) {
    foldrs.insert(&f);  // add the given Folder to our list of Folders
    f.addMsg(this);     // add this Message to f's set of Messages
}
void Message::remove(Folder &f) {
    foldrs.erase(&f);   // take the given Folder out of our list of Folders
    f.addMsg(this);     // remove this Message to f's set of Messages
}
```

<!-- }}} -->
### Copy Control for the `Message` Class <!-- {{{ -->
```cpp
// add this Message to Folders that point to m
void Message::add_to_FOlders(const Message &m) {
    for (auto f : m.folders) // for each Folder that holds m
        f->addMsg(this); // add a pointer to this Message to that Folder
}
```

The `Message` copy constructor copies the data members of the given
object:
```cpp
Message::Message(const Message &m):
    contents(m.contents), folders(m.folders) {
    add_to_Folders(*this);  // add this Message to the Folders that point to m
}
```



<!-- }}} -->
### The `Message` Destructor <!-- {{{ -->
```cpp
// remove this Message from the corresponding Folders
void Message::remove_from_Folders() {
    for (auto f : folders)  // for each pointer in folders
        f->remMsg(this);    // remove this Message from that Folder
}
```
Given the `remove_from_Folders` function, writing the destructor is
trivial:
```cpp
Message::~Message() {
    remove_from_Folders();
}
```


<!-- }}} -->
### `Message` Copy-Assignment Operator <!-- {{{ -->
To protect against self-assignment you remove pointers to this `Message`
from the _folders_ of the left-hand operand before inserting pointers in
the _folders_ in the right-hand operand:
```cpp
Message& Message::operator=(const Message &rhs) {
    // handle self-assignment by removing pointers before inserting them
    remove_from_Folders();      // update existing Folders
    contents = rhs.contents;    // copy message contents from rhs
    folders = rhs.folders;      // copy FOlder pointers from rhs
    add_to_Folders(rhs);        // add this Message to those Folders
    return *this;
}
```

<!-- }}} -->
### A `swap` Function for `Message` <!-- {{{ -->
Our `swap` function must also manage the `Folder` pointers that point to
the swapped `Messages`. After a call such as `swap(m1, m2)`, the
`Folder`s that had pointed to _m1_ must now point to _m2_, and vice
versa.  
```cpp
void swap(Message &lhs, Message &rhs) {
    using std::swap;    // not strictly needed in this case, but good habit
    // remove pointers to each Message from their (original respective Folders)
    for (auto f: lhs.folders)
        f->remMsg(&lhs);
    for (auto f: rhs.folders)
        f->remMsg(&rhs);
    // swap the contents and Folder pointer sets
    swap(lhs.folders, rhs.folders);     // uses swap(set&, set&)
    swap(lhs.contents, rhs.contents);   // swap(string&, string&)
    // add pointers to each Message to their (new) respective Folders
    for (auto f: lhs.folders)
        f->addMsg(&lhs);
    for (auto f: rhs.folders)
        f->addMsg(&rhs);
}
```

<!-- }}} -->
<!-- }}} -->
## Classes That Manage Dynamic Memory <!-- {{{ -->
Usually classes that use dynamic memory should use a library container
to hold their data. However, some classes need to do their own
allocation.  

As an example, we'll implement a simplification of the library `vector`
class.  

### `StrVec` Class Design <!-- {{{ -->
We'll use an `allocoator` to obtain raw memory. Because the memory an
allocator allocates is unconstructed, we'll use the allocator's
`construct` member to create objects in that space when we need to add
an element. Similarly, when we remove an element, we'll use the `destroy`
member to destroy the element.  

Each `StrVec` will have three pointers:  

+ `elements` - points to the first element in the allocated memory  
+ `first_free` - points just after the last actual element  
+ `cap` - points just past the end of the allocated memory  

In addition to these pointers, `StrVec` will have a member named `alloc`
that is an `allocator<string>`. Our class will also have four utility
functions:  

+ `alloc_n_copy` will allocate space and copy a given range of elements  
+ `free` will destroy the constructed elements and deallocate the space.
+ `chk_n_alloc` will ensure that there is room to add at least one more
  element. If there isn't room for another element, the function will
  call `reallocate` to get more space.  
+ `reallocate` will reallocate the `StrVec` when it runs out of space  

<!-- }}} -->
### `StrVec` Class Definition <!-- {{{ -->

```cpp
// simplified implementation of the memory allocation strategy for a vector-like class
class StrVec {
public:
    StrVec():   // the allocator member is default initialized
        elements(nullptr), first_free(nullptr), cap(nullptr) { }
    StrVec(const StrVec&);  // copy constructor
    StrVec& operator = (const StrVec&); // copy assignment
    ~StrVec();  // destructor
    void push_back(const std::string&); // copy the element
    size_t size() const { return first_free - elements; }
    size_t capacity() const { return cap - elements; }
    std::string* begin() const { return elements; }
    std::string* end() const { return first_free; }
    // ...
private:
    std::allocator<std::string> alloc;  // allocates the elements
    // used by the functions that add elements to the StrVec
    void chk_n_alloc() { if (size() == capacity()) reallocate(); }
    // utilities used by the copy constructor, assignment operator, and destructor
    std::pair<std::string*, std::string*> alloc_n_copy
        (const std::string*, const std::string*);
    void free();        // destroy the elements and free the space
    void reallocate();  // get more space and copy the existing elements
    std::string* elements;      // pointer to the first element in the array
    std::string* first_free;    // pointer to the first free element in the array
    std::string* cap;           // pointer to one past the end of the array
};
```


<!-- }}} -->
### Using `construct` <!-- {{{ -->
```cpp
void StrVec::push_back(const string& s) {
    chk_n_alloc();  // ensure that there is room for anothe element
    // construct a copy of s in the element to which first_free points
    alloc.construct(first_free++, s);
}
```

<!-- }}} -->
### The `alloc_n_copy` Member <!-- {{{ -->
The `alloc_n_copy` member will allocate enough storage to hold its given
range of elements and will copy those elements into the newly allocated
space.
```cpp
pair<string*, string*>
StrVec::alloc_n_copy(const string* b, const string* e) {
    // allocate space to hold as many elements as are in the range
    auto data = alloc.allocate(e - b);
    // initialize and return a pair constructed from data and
    // the value returned by unitialized_copy
    return {data, uninitialized_copy(b, e, data)};
}
```

<!-- }}} -->
### The `free` Member <!-- {{{ -->
```cpp
void StrVec::free() {
    // may not pass deallocate a 0 pointer; if elements is 0, there's no work to do
    if (elements) {
        // destroy the old elements in reverse order
        for (auto p = first_free; p != elements; /* empty */)
            alloc.destroy(--p);
        alloc.deallocate(elements, cap - elements);
    }
}
```

<!-- }}} -->
### Copy-Control Members <!-- {{{ -->
```cpp
StrVec::StrVec(const StrVec& s) {
    // calll alloc_n_copy to allocate exactly as many elements as in s
    auto newdata = alloc_n_copy(s.begin(), s.end());
    elements = newdata.first;
    first_free = cap = newdata.second;
}

StrVec::~StrVec() { free(); }

StrVec& StrVec::operator = (const StrVec& rhs) {
    // call alloc_n_copy to allocate exactly as many elements as in rhs
    auto data = alloc_n_copy(rhs.begin(), rhs.end());
    free();
    elements = data.first;
    first_free = cap = data.second;
    return *this;
}
```

<!-- }}} -->
### Moving, Not Copying, Elements during Reallocation <!-- {{{ -->
This function must:  

+ Allocate memory for a new, larger array of `string`s  
+ Construct the first part of that space to hold the existing elements  
+ Destroy the elements in the existing memory and deallocate that memory  

<!-- }}} -->
### Move Constructors and `std::move` <!-- {{{ -->
```cpp
void StrVec::reallocate() {
    // we'll allocate space for twice as many elements as the current size
    auto newcapacity = size() ? 2 * size() : 1;
    // allocate new memory
    auto newdata = alloc. allocate(newcapacity);
    // move the data from the old memory to the new
    auto dest = newdata;    // points to the next free position in the new array
    auto elem = elements;   // points to the next element in the old array
    for (size_t i = 0; i != size(); ++i)
        alloc.construct(dest++, std::move(*elem++));
    free(); // free the old space once we've moved the elements
    // update our data structure to point to the new elements
    elements = newdata;
    first_free = dest;
    cap = elements + newcapacity;
}
```

<!-- }}} -->
<!-- }}} -->
## Moving Objects <!-- {{{ -->
### Rvalue References <!-- {{{ -->
An rvalue reference is a reference that must be bound to an rvalue. An
rvalue reference is obtained by using `&&` rather thatn `&`. As we'll
see, rvalue references have the important property that they may be
bound only to an object that is about to be destroyed. As a result, we
are free to "move" resources from an rvalue reference to another object.  

```cpp
int i         = 42; // ok: r refers to i
int &r        = i; // ok: r refers to i
int &&rr      = i;   // error: cannot bind an rvalue reference to an lvalue
int &r2       = i * 42;   // error: i*42 is an rvalue
const int &r3 = i * 42; // ok: we can bind a reference to const to an rvalue
int &&rr2     = i * 42; // ok: bind rr2 to the result of the multiplication
```

Functions that return lvalue references, along with the assignment,
subscript, dereference, and prefix increment/decrement operators, are
all examples of expressions that return lvalues. We can bind an lvalue
reference to the result of any these expressions.  

Functions that return a nonreference type, along with the arithmetic,
relational, bitwise, and postfix increment/decrement operators, all
yield rvalues. We cannot bind an lvalue reference to these expressions,
but we can bind either an lvalue reference to a `const` or an rvalue
reference to such expressions.  

#### Lvalues Persist; Rvalues Are Ephemeral <!-- {{{ -->
Because rvalue references can only be bound to temporaries, we know
that:  

+ the refrerred-to object is about to be destroyed  
+ There can be no other users of that object  

These facts together mean that ocde that uses an rvalue reference is
free to take over resources from the object to which the reference
refers.  
<!-- }}} -->
#### The Library `move` Function <!-- {{{ -->
The `move` function returns an rvalue reference to its given object:
```cpp
int &&rr3 = std::move(rr1); // ok
```

We can destroy a moved-from object and can assign a new value to it, but
we cannot use the value of a moved-from object.  

<!-- }}} -->

<!-- }}} -->
### Move Constructor and Move Assignment <!-- {{{ -->
As an example, we'll define the `StrVec` constructor to move rather than
copy the elements from one `StrVec` to another:
```cpp
StrVec::StrVec(StrVec &&s) noexcept // promise that move won't throw any exceptions
    // member initializers take over the resources in s
    : elements(s.elements), first_free(s.first_free), cap(s.cap) {
    // leave s in a state in which it is safe to run the destructor
    s.elements = s.first_free = s.cap = nullptr;
}
```

<!-- }}} -->
### Move-Assignment Operator <!-- {{{ -->
As with the move constructor, if our move-assignment operator won't
throw any exception, we should make it `noexcept`. Like a
copy-assignment operator, a move-assignment operator must guard against
self-assignment:
```cpp
StrVec &StrVec::operator=(StrVec &&rhs) noexcept {
    // direct test for self-assignment
    if (this != &rhs) {
        free();         // free existing elements
        elements = rhs.elements;    // take over resources from rhs
        cap = rhs.cap;
        // leave rhs in a destructible state
        rhs.elements = rhs.first_free = rhs.cap = nullptr;
    }
    return *this;
}
```


<!-- }}} -->
### The Synthesized Move Operations <!-- {{{ -->
The ocmpiler synthesizes the move constructor and move assignment only
if a class does not define any of its own copy-control members and only
if all the data members can be moved constructed and move assigned.  

Classes that define a move constructor or move-assignment operator must
also define their own copy operations. Otherwise, those members are
deleted by default.  
<!-- }}} -->
#### Rvalues Are Moved, Lvalues Are Copies, But Rvalues Are Copied If there Is No Move Constructor. <!-- {{{ -->

```cpp
StrVec v1, v2;
v1 = v2;                    // v2 is an lvalue; copy assignment
StrVec getVec(istream &);   // getVec returns an rvalue
v2 = getVec(cin);           // getVec(cin) is an rvalue; move assignment
```

```cpp
class Foo {
public:
    Foo() = default;
    Foo(const Foo&);    // copy constructor
    // other members, but Foo does not define a move constructor
};
Foo x;
Foo y(x);               // copy constructor; x is an lvalue
Foo z(std::move(x));    // copy constructor, because there is no move constructor
```
<!-- }}} -->
#### Copy-and-Swap Assignment Operators and Move <!-- {{{ -->
If we add a move constructor to this class, it will effectively get a
move assignment operator as well:
```cpp
class HasPtr {
public:
    // added move constructor
    HasPtr(HasPtr &&p) noexcept : ps(p.ps), i(p.i) {p.ps = 0;}
    // assignment operator in both the move- and copy-assignment operator
    HasPtr& operator=(HasPtr rhs) { swap(*this, rhs); return *this; }
}
```

<!-- }}} -->
#### Move Operations for the `Message` Class <!-- {{{ -->
We'll start by defining an operation to do this common work:
```cpp
void Message::move_Folders(Message *m) {
    folders = std::move(m->folders);    // uses set move assignment
    for (auto f : folders) {    for each Folder
        f->remMsg(m);       // remove the old Message from the Folder
        f->addMsg(this);    // add this Message to that Folder
    }
    m->folders.clear();     // ensure that destroying m is harmless
}
```
It is worth noting that inserting an element to a set might throw an
exception-adding an element to a container requires memory to be
allocated, which means that a `bad_alloc` exception might be thrown.
Hence `Message` move constructor and move-assignment operators might
throw exceptions.  

The `Message` move constructor calls `move` to move the contents and
default initializes its _folders_ member:
```cpp
Message::Message(Message contents &&m) : contents(std::move(m.contents))
{
    move_Folders(&m);   // moves folders and updates the Folder pointers
}
```

The move-assignment operator does a direct check for self-assignment:
```cpp
Message& Message::operator=(Message &&rhs) {
    if (this != &rhs) {                     // direct check for
    self-assignment
        remove_from_Folders();
        contents = std::move(rhs.contents); // move assignment
        move_FOlders(&rhs); // reset the Folders to point to this Message
    }
    return *this;
}
```



<!-- }}} -->
### Move Iterators <!-- {{{ -->
The new library defines a _move iterator_ adaptor. A move iterator
adapts its given iterator by changing the behavior of the iterator's
dereference operator. Ordinarily, an iterator dereference operator
returns an lvalue reference to the element. Unlike other iterators, the
dereference operator of a move iterator yields an rvalue reference.  

```cpp
void StrVec::reallocate() {
    // allocate space for twice as many elements as the current size
    auto newcapacity = size() ? 2 * size() : 1;
    auto first = alloc.allocate(newcapacity);
    // move the elements
    auto last = uninitialized_copy(make_move_iterator(begin()),
        make_move_iterator(end()), first);
    free();                         // free the old space
    elements = first;               // update the pointers
    first_free = last;
    cap = elements + newcapacity;
}
```

That algorithm uses the iterator dereference operator to fetch elements
from the input sequence. Because we passed move iterators, the
dereference operator yields an rvalue reference, which means `construct`
will use the move constructor to construct the elements.  

<!-- }}} -->
### Rvalue References and Member Functions <!-- {{{ -->
The library containers that define `push_back` provide two versions:
```cpp
void push_back(const X&);   // copy: binds to any kind of X
void push_back(X&&);        // move: binds only to modifiable rvalues of type X
```

As a more concrete example, we'll give our `StrVec` class a second
version of `push_back`:
```cpp
class StrVec {
public:
    void push_back(const std::string&); // copy the element
    void push_back(std::string&&);      // move the element
};
// unchanged from the original version
void StrVec::push_back(const string& s) {
    chk_n_alloc();  // ensure that there is room for another element
    // construct a copy of s in the element to which first_free points
    alloc.construct(first_free++, s);
}
void StrVec::push_back(string &&s) {
    chk_n_alloc();  // reallocates the StrVec if necessary
    alloc.construct(first_free++, std::move(s));
}
```

When we call `push_back` the type of the argument determines whether the
new element is copied or moved into the container:
```cpp
StrVec vec; // empty StrVec
string s = "some string or another";
vec.push_back(s);       // calls push_back(const string&)
vec.push_back("done");  // calls push_back(string&&)
```

<!-- }}} -->
#### Rvalue and Lvalue Reference Member Functions <!-- {{{ -->
We can call member function on an object, regardless of whether that
object is an lvalue or an rvalue:
```cpp
string s1 = "a value", st = "another";
auto n = (s1 + s2).find('a');
```

Prior to the new standard there are some weird usage:
```cpp
s1 + s2 = "wow!";
```
To prevent this we indicate the lvalue/rvalue property of _this_ in the
same way that we define `const` member functions. We place a _reference
qualifier_ after the parameter list:
```cpp
class Foo {
public:
    Foo &operator=(const Foo&) &;   // may assign only to modifiable lvalues
}
Foo &Foo::operator=(const Foo &rhs) & {
    // do something
    return *this;
}
```

WE may run a function qualified by `&` only on an lvalue and may run a
function qualified by `&&` only on an rvalue:
```cpp
Foo &retFoo();  // returns a reference; call ro retFoo is an lvalue
Foo retVal();   // returns by value; a call to retVal is an rvalue
Foo i, j;       // i and j are lvalues
i = j;          // ok: i is an lvalue
retFoo() = j;   // ok: retFoo() returns an lvalue
retVal() = j;   // error: retVal() returns an rvalue
i = retVal();   // ok: we can pass an rvalue as the right-hand operand to assignment
```

A function can be both `const` and `reference` qualified:
```cpp
class Foo {
public:
    Foo someMem() & const;      // error: const qualifier must come first
    Foo anotherMem() const &;   // ok: const qualifier comes first
}
```


<!-- }}} -->
#### Overloading and Reference Functions <!-- {{{ -->
We may overload a function by its reference qualifier and by whether it
is a `const` member. AS an example, we'll give _Foo_ a _vector_ member
and a function named _sorted_ that returns a copy of the _Foo_ object in
which the vector is sorted:
```cpp
class Foo {
public:
    Foo sorted() &&;        // may run on modifiable rvalues
    Foo sorted() const &;   // may run on any kind of Foo
private:
    vector<int> data;
};
// this object is an rvalue, so we can sort in place
Foo Foo::sorted() && {
    sort(data.begin(), data.end());
    return *this;
}
// this object is either const or its is an lvalue; either way we can't sort in place
Foo Foo::sorted() const & {
    Foo ret(*this);                         // make a copy
    sort(ret.data.begin(), red.data.end()); // sort the copy
    return ret;                             // return the copy
}
```

When we define two or more members that have the same name and the same
parameter list, we must provide a reference qualifier on all or none of
those functions:
```cpp
class Foo {
public:
    Foo sorted() &&;
    Foo sorted() const; // error: must have reference qualifier
    // Comp is type alias for the function type
    // that can be used to compare int values
    using Comp = bool(const int&, const int&);
    Foo sorted(Comp*);          // ok: different parameter list
    Foo sorted(Comp*) const;    // ok: neither version is reference qualifier
}
```


<!-- }}} -->


<!-- }}} -->
<!-- }}} -->
# Overloaded Operations and Conversions <!-- {{{ -->
<!-- TODO: stopped here -->
<!-- }}} -->
