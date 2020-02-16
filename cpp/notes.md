<!-- книга: с++ premier -->
# Data types
## Pointers, reference
_diff btw pointer and reference_. reference is not an object, hence, once we 
defined reference, we cannot make that reference refer to another
object.  

`void*` pointer can hold the address of __any object__.  

## Strings
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

### Notes
`string.size()` returns `string::size_type` type which is unsigned. 
So don't mix up _int_ and _unsigned_ values.
    
You need know what type char is __cctype__ library helps.
 For example:  
    + `isalnum()`  
    + `tolower()`  
    + `isgraph()`  
    + `islower()`  

## Arrays
when use arrays, the compiler automatically 
substitutes a __pointer to the first element__.  

when use multidim arrays in range for, 
the loop control variable for all but the innermost array 
__must be references__.

iterating over container:  
`index != s.size() && !isspace(s[index])`  

# Operations
__Division__ is rounded towards zero.  

__Assignment__ operator is right associative.  
__Shift__ operators are left associative.

<!-- hmm -->
<!-- if m = (m / n) * n + m % n  then  m has the same sign as m % n -->

<!-- again hmmm -->
__Comma operator__ is left associative, the result is right-hand expression 
will be lvalue if right-hand operand is an lvalue  

## Conditions
Binary operations are left associative <=> first evaluated left assigment.  
`if (i < j < k)` => _k_ compared to 1 ( bool result of i < j )  
`if ( val == true )` == `if ( val == 1 )`  

condition operator may result as _rvalue_ as _lvalue_.  

## Explicit conversion
_Syntax:_ `cast-name<type>(expression)`  
where type is:  
	+ `static_cast`  
	+ `dynamic_cast`  
	+ `const_cast`  
	+ `reinterpret_cast`  
why? to not loose precision or to cast `void*` to any other pointer  

## Statements
### Decision branches
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

# Exception handling
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

## Assert
`assert` executes only if _NDEBUG_ is not defined.
if your want to turn off asserts => provide #define NDEBUG 
  or
CC -D NDEBUG main.c

# Functions
you may define defaults for parameters, however, if a parameter has a
__default argument__, all the parameters that follow it must also have
default arguments.

__inline function__ usually expanded "in line" at each call:
```cpp
cout << shorterString(s1, s2) << endl;
cout << (s1.size() < s2.size() ? s1 : s2) << endl
```

### Pointers to function
function that return pointers to function:  
`auto f1(int) -> int(*)(int*,int);`  
or make it via typedef:  
```cpp
typedef bool Func(const string&, const string&);	# by type
typedef decltype(lengthCompare) Func2;	# by another function
```


# Classes

### Class or struct
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

## Access Control and Encapsulation
	+ Members defined after a public specifier are accessible to all 
\		parts of the program
	+ Members defined after a private specifier are accessible to the
\		member functions of the class

__To access non public__ members of class precede it's declaration with 
'friend' keyword

## Functions
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

## Constructors
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

### Default Constructor
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

## Implicit Class-Type conversions  
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

### Prevent the use of constructor in implicit conversion  
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

### Library Classes
    + `string` constructor with arg of `const char*` is not explicit  
    + `vector` constructor that takes a size is explicit  

## Aggregate Classes  
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

## Data types  
__mutable__ data member can be changed inside of const functions
Defining class member types: `typedef std::string::size_type pos;`  
or: `using pos = std::string::size_type;`  

to get name __from outer scope__ use ::height;

## Literal Classes  
Literal class - a class whose data members are __all of literal
type__.  
Literal classes may have function members that are `constexpr`. These
member functions are implicitly `const`.  
Restrictions to be literal class:   
    + must have at least one `constexpr` contructor  
    + must use default definition for its destructor

### Constexpr constructors

# IO
manipulating with input and output:
```cpp
istream &read(istream &is, Sales_data &item) {
	double price = 0;
	is >> item.bookNo >> item.units_sold >> price;
	item.revenue = price * item.units_sold;
	return is;
}
```

