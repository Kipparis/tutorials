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
<!-- TODO: stopped here -->
<!-- }}} -->
<!-- }}} -->
## `string` Streams <!-- {{{ -->

<!-- }}} -->
<!-- }}} -->
