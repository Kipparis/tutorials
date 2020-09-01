# Book
Learn Vimscript the Hard Way by Steve Losh

# Interesting options <!-- {{{ -->

+ `numberwidth` - how wide the column containing line numbers  
+ `help lh<TAB>` - various vim highlighting groups  

<!-- }}} -->
# Creating a Vimrc File <!-- {{{ -->
A `~/.vimrc` file is a file that contains some Vimscript code. Vim will
automatically run the code inside this file every time you open Vim.  

To easily find the location of the file, run `:echo $MYVIMRC` in Vim.  
<!-- }}} -->
# Echoing Messages <!-- {{{ -->
You can use either `:echo` or `:echom`  
## Persisntent Echoing <!-- {{{ -->
`:messages` - list of messages displayed via `:echom ""`  
<!-- }}} -->
## Comments <!-- {{{ -->
That is lines starting with `"` character  

Doesn't work when:  

+ placed on the same line as mapping  
<!-- }}} -->
From `:help messages`:  

+ `g<` - used to display last message  
<!-- }}} -->
# Setting Options <!-- {{{ -->
There are two main kinds of options:  

+ boolean - either "on" or "off"  
+ that take a value  

## Boolean Options <!-- {{{ -->
All boolean work this way. `:set <name>` turns the option on and `:set
no<name>` turns it off.  
<!-- }}} -->
## Toggling Boolean Options <!-- {{{ -->
`:set <name>!` - adding a `!` (exlamation point or "bang") to a boolean
ooption toggles it.  
<!-- }}} -->
## Checking Options <!-- {{{ -->
`:set <name>?`  
<!-- }}} -->
## Options with Values <!-- {{{ -->
`:set <name>=<value>` - change non-boolean options  
<!-- }}} -->
## Setting Multiple Options at Once <!-- {{{ -->
`:set number numberwidth=6` - delimit options with space  
<!-- }}} -->
<!-- }}} -->
# Basic Mapping <!-- {{{ -->
Mapping keys lets you tell Vim:  

> When I press this key, I want you to do this stuff instead of whatever
> you would normally do.  

Remove mapping with `:nunmap <character>`  

## Special Characters <!-- {{{ -->
You can use `<keyname>` to tell Vim about special keys.
```vim
:map <space> vim
```
You may also map modifier keys like Ctrl and Alt:
```vim
:map <c-d> dd
```

<!-- }}} -->
<!-- }}} -->
# Modal Mapping <!-- {{{ -->
Be more specific:  

+ `nmap` - normal mode mapping  
+ `vmap` - visual mode  
+ `imap` - insert mode  

## Insert Mode <!-- {{{ -->
If you want to run Vim command from mappings in insert mode, you have to
implicitly pass `<esc>` for vim.  
<!-- }}} -->
<!-- }}} -->
# Strict Mapping <!-- {{{ -->
## Recursion <!-- {{{ -->
If you call `:nmap dd O<esc>jddk` it will go into recursion. The reason
is key is a part mapped command  
<!-- }}} -->
## Nonrecursive Mapping <!-- {{{ -->
Vim offers another set of mapping commands that will not take mappings
into account when they perform their actions.  
Each of the `*map` commands has a `*noremap` conterpart that ignores
other mappings.  

**You should use it always**  
<!-- }}} -->
<!-- }}} -->
# Leaders <!-- {{{ -->
There are a bunch of keys that you don't normally need in your
day-to-day Vim usage: `-`, `H`, `L`, `<space>`, `<cr>`, and `<bs>`.  

## Mapping Key Sequences <!-- {{{ -->
You can map key sequences in vim. They are work if you press them
quickly.  
<!-- }}} -->
## Leader <!-- {{{ -->
Vim calls this "prefix" key the "leader". To set your own:
```vim
:let mapleader = "-"
```

Now you can use special character `<leader>` in your mappings.  
<!-- }}} -->
## Local Leader <!-- {{{ -->
Vim has a second "leader" key called "local leader". This is meant to be
a prefix for mappings that only take effect for certain types of files,
like Python files or HTML files.  

You can set it via:
```vim
:let maplocalleader = "\\"
```

Now you can use `<localleader>` in mappings and it will work just like `<leader>` does  
<!-- }}} -->
<!-- }}} -->
# Editing Your Vimrc <!-- {{{ -->
If you have something on your mind, you don't want to loose your
concentration to add useful mapping to vimrc.  

## Editing Mapping <!-- {{{ -->
Mapping that will open your `$HOME/.vimrc` file in a split so you can
quickly edit it and get back to cofing.
```vim
:nnoremap <leader>ev :vsplit $MYVIMRC<cr>
```
If you prefer a horizontal split, you can replace `vsplit` with `split`  

<!-- }}} -->
## Sourcing Mapping <!-- {{{ -->
Vimrc file is read upon startup only. Let's add a mapping get rid of
useless restarting vim:
```vim
:nnoremap <leader>sv :source $MYVIMRC<cr>
```

The `source` command tells Vim to take the contents of the given file
and execute it as Vimscript.  
<!-- }}} -->
<!-- }}} -->
# Abbreviations <!-- {{{ -->
Vim has a feature called "abbreviations" that feel similar to mappings
but are meant for use in insert, replace, and command modes.  

`:iabbrev adn and` - abbreviations expanded after you type word and
something that is not a letter, number or underscore afterwards.  

## Keyword Characters <!-- {{{ -->
Vim will substitute an abbreviation when you type any "non-keyword
character" after an abbreviation. "Non-keyword character" = any
character not in the `iskeyword` option:
```vim
:set iskeyword?
```
You'll see output like `@,48-57,_,192-255`:  

+ underscore character (`_`)  
+ all alphabetic ASCII characters, both upper and lower case, and their
  accented versions.  
+ any characters with an ASCII value between 48 and 57 (the digits zero
  through nine)  
+ any characters with an ASCII value between 192 and 255 (some special
  ASCII characters)  

Read about it: `:help isfname`  
<!-- }}} -->
## Why Not Use Mappings <!-- {{{ -->
Mappings could be expanded inside of word, whereas abbreviations take
care of such cases.  
<!-- }}} -->
<!-- }}} -->
# More Mappings <!-- {{{ -->
You can find out which mapings did you overwrote by reading `:help <key>`  
<!-- }}} -->
# Training Your Fingers <!-- {{{ -->
## Learning the Map <!-- {{{ -->
The trick to relearning a mapping is to _force_ yourself to use it by
_disabling_ the old key(s). Run the following command:
```vim
:inoremap <esc> <nop>
```
This effectively disables the escape key in insert mode by telling Vim
to perform `<nop>` (no operation) instead. Now you _have_ to use
your `jk` mapping to exit insert mode.  

<!-- }}} -->
<!-- }}} -->
# Buffer-Local Options and Mappings <!-- {{{ -->
## Mappings <!-- {{{ -->
Consider following mappings:
```vim
:nnoremap          <leader>d dd
:nnoremap <buffer> <leader>x dd
```
First will set mapping globally (for all opened files and buffers),
while second only to the current opened buffer.  

<!-- }}} -->
## Settings <!-- {{{ -->
Some options always apply to all of Vim, but others can be set on a
per-buffer basis:
```vim
:setlocal wrap
:setlocal number
```

+ `:help local-options` for how this work  
+ `:help setlocal`  
    - `:setlocal all` displays all local values  
    - `:setlocal` displays local values which are different from the
      default  
    - when used global value - "--" is desplayed before the option name.  
+ `:help map-local`  
    - `:unmap <buffer> ,w` - unmaps only locally  

<!-- }}} -->
## Shadowing <!-- {{{ -->
Consider following mappings:
```vim
:nnoremap <buffer> Q x
:nnoremap          Q dd
```
Vim will execute first mapping, because it's _more specific_ than the
second.  

<!-- }}} -->
<!-- }}} -->
# Autocommands <!-- {{{ -->
Autocommands are a way to tell Vim to run certain commands whenever
certain events happen.  

By default Vim doesn't actually _create_ the file until you save it for
the first time. To change this behaviour run this:
```vim
:autocmd BufNewFile * :write
```

## Autocommand Structure <!-- {{{ -->
```vim
:autocmd BufNewFile * :write
         ^          ^ ^
         |          | |
         |          | The command to run.
         |          |
         |          A "pattern" to filter the event.
         |
         The "event" to watch for.
```

Some of the events:  

+ Starting to edit a file that doesn't already exist.  
+ Reading a file, whether it exists or not.  
+ Switching a buffer's `filetype` setting.  
+ Not presing a key on your keyboard for a certain amount of time.  
+ Entering insert mode.  
+ Exiting insert mode.  

`:help autocmd-events` to see a list of all the events you can bind
autocommands to.  


<!-- }}} -->
## Another Example <!-- {{{ -->
```vim
:autocmd BufWritePre *.html :normal gg=G
```
Re-indent whole file before saving.  

<!-- }}} -->
## Multiple Events <!-- {{{ -->
```vim
:autocmd BufWritePre,BufRead *.html :normal gg=G
```
This is almost like our last command, except it will also reindent the
code whenever we _read_ and HTML file as well as when we write it.  

A common idiom in Vim scripting is to pair the `BufRead` and `BufNewFile`
events together to run a command whenever you open a certain kind of file,
regardless of whether it happend to exist already or not.  
```vim
:autocmd BufNewFile,BufRead *.html setlocal nowrap
```

<!-- }}} -->
## FileType Events <!-- {{{ -->
One of the most useful events is the `FileType` event. this event is
fired whenever Vim sets a buffer's `filetype`.  

Mappings to comment current line:
```vim
:autocmd FileType javascript nnoremap <buffer> <localleader>c I// <esc>
:autocmd FileType python     nnoremap <buffer> <localleader>c I# <esc>
```

<!-- }}} -->
<!-- }}} -->
# Buffer-Local Abbreviations <!-- {{{ -->
You should understand easily how this words:
```vim
:iabbrev <buffer> --- &mdash;
```

## Autocommands and Abbreviations <!-- {{{ -->
```vim
:autocmd FileType python :iabbrev <buffer> iff if:<left>
:autocmd FileType javascript :iabbrev <buffer> iff if ()<left>
```

Remember: the best way to learn to use these new snippets is to _disable_
the old way of doing things. Running `:iabbrev <buffer> return
NOPENOPENOPE` will _force_ you to use your abbreviation instead. Add
these "training" snippets to match all theo nes you created to save
time.  

<!-- }}} -->
<!-- }}} -->
# Autocommand Groups <!-- {{{ -->
## The Problem <!-- {{{ -->
Sourcing your `vimrc` file rereads the entire file, including any
autocommands you've defined! This means that every time you source your
`vimrc` you''be duplicating autocommands, which will make Vim run slower
because it executes the same commands over and over.  
<!-- }}} -->
## Grouping Autocommands <!-- {{{ -->
Vim has a solution to the problem. The first step is to group related
autocommands into names groups:
```vim
:augroup testgroup
:   autocmd BufWrite * :echom "Foo"
:   autocmd BufWrite * :echom "Bar"
:augroup END
```
The indentation in the middle two lines is insignificant.  
Every time Vim reads same group, it will combine readed with previous one.  

`:help autocmd-groups`  
<!-- }}} -->
## Clearing Groups <!-- {{{ -->
If you want to _clear_ a group you can use `autocmd!` inside the group:
```vim
:augroup testgroup
:   autocmd!
:   autocmd BufWrite * :echom "Cats"
:augroup END
```

<!-- }}} -->
<!-- }}} -->
# Operator-Pending Mappings <!-- {{{ -->
An operator is a command that waits you to enter a movement command, and
then does something on the text between where you currently are and
where the movement would take you.  

## Movement Mappings <!-- {{{ -->
Vim letse you create new movements that work with all existing commands:
```vim
:onoremap p i(
```

When you're trying to think about how to define a new operator-pending
movement, you can think of it like this:  

1. Start at the cursor position  
2. Enter visual mode (charwise)  
3. ... mapping keys go here ...
4. All the text you want to include in the movement should now be
   selected.  

`:help omap-info`  

<!-- }}} -->
## Changing the Start <!-- {{{ -->
If our movements always have to start at the current cursor position it
limits what we can do. Of course there's a way around this problem:
```vim
:onoremap in( :<c-u>normal! f(vi(<cr>
```
This is equivalent to "inside next parantheses". Let's make a companion
"inside last parentheses":
```vim
:onoremap il( :<c-u>normal! F)vi(<cr>
```

<!-- }}} -->
## General Rules <!-- {{{ -->

+ If your operator-pending mapping ends with some t ext visually
  selected, Vim will operate on that text.  
+ Otherwise, Vim will operate on the text between the original cursor
  position and the new position.  
<!-- }}} -->
<!-- }}} -->
# More Operator-Pending Mappings <!-- {{{ -->
Assume following text in markdown:
```markdown
Topic One
=========

This is some text about topic one.

It has multiple paragraphs.

Topic Two
=========

This is some text about topic two. It has only one paragraph.
```

Lets create some mappings that let us target headings with movements.
Run the following command:
```vim
:onoremap ih :<c-u>execute "normal! ?^==\\+$\r:nohlsearch\rkvg_"<cr>
```
That is operator-pending mapping for acting on current section's heading.

## Normal <!-- {{{ -->
The `:normal` command takes a set of characters and performs whatever
action they would do if they were typed in normal mode.  
<!-- }}} -->
## Execute <!-- {{{ -->
The `execute` command takes a Vimscript string and performs it as a
command. For example this:
```vim
:execute "write"
```
will write your file, just as if you had typed `:write<cr>`. But why
bother with this when we could just run the `normal!` command itself?
Look at the following command:
```vim
:normal! gg/a<cr>
```
The problem is that `normal!` doesn't recognize "special characters"
like `<cr>`. When `execute` looks at the string you tell it to run, it
will substitute any special characters it finds _before_ running it.  

If we perform this replacement in our mapping and look at the result we
can see that the mapping is going to perform:
```vim
:normal! ?^==\+$<cr>:nohlsearch<cr>kvg_
```

So now `normal!` will execute these characters as if we had typed them
in normal mode.

The final piece is a sequence of three normal mode commands:  

+ `k`: move up a line. Since we were on the first character of the line
  of equal signs, we're now on the first character of the heading text.  
+ `v`: enter (characterwise) visual mode  
+ `g_`: move to the last non-blank character of the current line. We use
  this instead of `$` because `$` would highlight the newline character
  as well, and this isn't what we want.  

<!-- }}} -->
## Results <!-- {{{ -->
Let's look at one more mapping:
```vim
:onoremap ah :<c-u>execute "normal! ?^==\\+\r:nohlsearch\rg_vk0"
```
this will execute operation on whole header (including equal signs)  

+ `:help pattern-overview` - regex help  
+ `:help normal`  
+ `:help execute`  
+ `:help expr-quote` to see the escape sequences you can use in strings  

<!-- }}} -->

<!-- }}} -->
# Status Lines <!-- {{{ -->
Vim allows you to customize the text in the status line at the bottom
through the `statusline` option:
```vim
:set shtatusline=%f
```
you can use `+=` to build up the option one piece at a time:
```vim
:set statusline=%f
:set statusline+=\ -\ 
:set statusline+=FileType:\ 
:set statusline+=%y
```

## Width and Padding <!-- {{{ -->
You can change how the information is displayed:
```vim
set statusline=[%4l]
```
Now the line number in the status line will be preceded by enough spaces
to make it at lest four characters wide. By default the padding spaces
are added on the left side of the value:
```vim
:set statusline=Current:\ %4l\ Total:\ %4L
```
You can use `-` to place padding on the right instead of the left:
```vim
:set statusline=Current:\ %-4l\ Total:\ %-4L
```
You can tell Vim to pad with zeros instead of spaces:
```vim
:set statusline=%04l
```
You can also set a maximum width of a code's output:
```vim
:set statusline=%.20F
```




<!-- }}} -->
## General Format <!-- {{{ -->
```txt
%-0{minwid}.{maxwid}{item}
```
Everything except the `%` and the item is optional.  

`:help statusline`
<!-- }}} -->
## Splitting <!-- {{{ -->
The `%=` code tells Vim that everything coming after that should be
aligned (as a whole) to the right instead of the left:
```vim
:set statusline=%f
:set statusline+=%=
:set statusline+=%l
:set statusline+=\ 
:set statusline+=%L
```

<!-- }}} -->

<!-- }}} -->
# Responsible Coding <!-- {{{ -->
## Commenting <!-- {{{ -->
Be defensive when writing anything that takes more than a few lines of
Vimscript. Add a comment explaining what it does, and if there is a
relevant help topic, mention it in the comment!  
<!-- }}} -->
## Grouping <!-- {{{ -->
Use folding and autgroups  

+ `:help foldlevelstart` Vim may fold everything automatically  
<!-- }}} -->
## Short Names <!-- {{{ -->
Vim allows you to use abbreviated names for most commands and options.
For example, both of these commands do exactly the same thing:
```vim
:setlocal wrap
:setl wrap
```
Vimscript is terse and cryptic enough to begin with; shortening things
further is only going to make it even harder to read.  
Abbreviated forms are _great_ for running commands manually in the
middle of coding.  
<!-- }}} -->
<!-- }}} -->
# Variables <!-- {{{ -->
You can create them by running:
```vim
:let foo = "bar"
:echo foo
```
Vim will display `bar`. Now run these commands:
```vim
:let foo = 42
:echo foo
```

## Options as Variables <!-- {{{ -->
You can read and set options as variables by using an ampersand in front
of a name:
```vim
:set textwidth=80
:echo &textwidth
```
You can also set options as variables:
```vim
:let &textwidth = 100
:set textwidth?
```

<!-- }}} -->
## Local Options <!-- {{{ -->
If you want to set the local value of an option as a varialbe, you need
to prefix the variable name:
```vim
:let &l:number = 1
```

<!-- }}} -->
## Registers as Variables <!-- {{{ -->
You can also read and set registers as variables:
```vim
:let @a = "hello!"
```
Now put your cursor somewhere in your text and type `"ap`. This command
tells vim to "paste the contents of register `a` here". We just set the
contents of that register, so Vim pastes `hello!` into your text.  

Registers can also be read. Run the following command:
```vim
:echo @a
```

Display content from an unnamed register (that is location is where text
you yank without specifying a destination):
```vim
:echo @"
```

Search register (register containing text that you recently searched):
```vim
:echo @/
```

+ `:help registers` to look over the list of registers you can read and
  write  

<!-- }}} -->
<!-- }}} -->
# Variable Scoping <!-- {{{ -->
Consider following code:
```vim
:let b:hello = "world"
:echo b:hello
```
In current buffer Vim displays `world`. But if you switch buffer,
nothing happend. When you precede variable name with `b:` Vim make
variale local to the current buffer.  

+ `:help internal-variables` - list of scopes  

<!-- }}} -->
# Conditionals <!-- {{{ -->
## Multiple-Line Statements <!-- {{{ -->
You can separate each line with a pipe character (`|`). As ion the
following command:
```vim
:echom "foo" | echom "bar"
```

<!-- }}} -->
## Basic `if` <!-- {{{ -->
example syntax is:
```vim
:if condition
:   statements
:endif
```

Several informed conclusions about Vimscript:  

+ Vim will try to coerce variables (and literals) when necessary. When
  `10 + "20foo"` is evauated Vim will convert "20foo" to an integer
  (which result in 20) and then add it to 10  
+ String that start with a number are coerced to that number, otherwise
  they're coerced to 0.  
+ Vim will execute the body of an `if` statement when its condition
  evaluates to a non-zero integer, _after_ all coercion takes place.  

<!-- }}} -->
## Else and Elseif <!-- {{{ -->
Example is the following commands:
```vim
:if 0
:   echom "if"
:elseif "nope!"
:   echom "elseif"
:else
:   echom "finlly!"
:endif
```
Vim echoes `finally!`.  
<!-- }}} -->
<!-- }}} -->
# Comparisons <!-- {{{ -->
## Case Sensitivity <!-- {{{ -->
Consider following code:
```vim
:set ignorecase
:if "foo" == "FOO"
:   echom "no, it couldn't be"
:elseif "foo" == "foo"
:   echom "this must be the one"
:endif
```

**The behavior of == depends on a user's settings**  

<!-- }}} -->
## Code Defensively <!-- {{{ -->

+ `==?` is the "case-insensitive no matter what the use has set"
  comparison
+ `==#` is the "case-sensitive no matter what the use has set"
  comparison

You should _always_ use explicit case sensitive or insensitive
comparisons.  

Using `==#` and `==?` with integers will work just fine.  

+ `:help ignorecase` to see why someone might set that option  
+ `:help expr4` to see all available comparison operators  
<!-- }}} -->
<!-- }}} -->
# Functions <!-- {{{ -->
**Vimscript functions _must_ start with a capital letter if they are
unscoped!** Even if you do add a scope to a function you may as well
capitalize the first letter of function names anyway. Most Vimscript
coders seem to do it.  

Let's define a function:
```vim
:function Meow()
:   echom "Meow!"
:endfunction
```
Let's try running it:
```vim
:call Meow()
```
Vim will display `Meow!` as expected.  

Let's try returning a value. Run the following commands:
```vim
:function GetMeow()
:   return "Meow String!"
:endfunction
```
Now try it out by running this command:
```vim
:echom GetMeow()
```

## Calling Functions <!-- {{{ -->
You can directly call a function, like here:
```vim
:call Meow()
:call GetMeow()
```
in second call return value is thrown away and nothing happend.  

The second way to call functions is in expressions:
```vim
:echom GetMeow()
```

<!-- }}} -->
## Implicit Returning <!-- {{{ -->
If Vimscript function doesn't a value, it implicitly returns 0.  
<!-- }}} -->

+ `:help :call` - how many arguments can you pass to a funciton  
+ `:help E124` - what character you're allowed to use in function names.  
+ `:help return` - look up for short form of return  

<!-- }}} -->
# Function Arguments <!-- {{{ -->
Run the following commands:
```vim
:function DisplayName(name)
:   echom "Hello! My name is:"
:   echom a:name
:endfunction
```
Run the function:
```vim
:call DisplayName("Your Name")
```

When you write a Vimscript function that takes arguments you _always_
need to prefix those arguments with `a:` when you use them to tell Vim
that they're in the argument scope.  

## Varargs <!-- {{{ -->
Vimscript functions can optionally take variable-length argument lists.  

```vim
:function Varg(foo, ...)
:   echom a:foo
:   echom a:0
:   echom a:1
:   echo a:000
:endfunction
```

+ `...` indicates that function can take variable-length argument list  
+ `a:<name>` is filled with appropriate variable argument  
+ `a:<index>` is filled with the rest of the variables  
+ `a:0` contains number of extra arguments  
+ `a:000` list containing all extra arguments that were passed (it's
  list, so we cannot display it with `echom`)  

<!-- }}} -->
## Assignment <!-- {{{ -->
Consider following commands:
```vim
:function Assign(foo)
:   let a:foo = "Nope"
:   echom a:foo
:endfunction
```
```vim
:call Assign("test")
```
Vim will throw an error, because you can't reassign argument variables.  

<!-- }}} -->

+ `:help function-argument`  
    - you can't change the function arguments. If the function argument
  is list, you can change it's content (python lol). To prevent
  this behavior use `:lockvar`  
+ `:help local-variables`  

<!-- }}} -->
# Numbers <!-- {{{ -->
Vimscript has two types of numeric variables: Numbers and Floats.  

## Number Formats <!-- {{{ -->

+ specify hex notation by prefixing with `0x` or `0X`  
+ specify ocal notation by prefixing with `0`
<!-- }}} -->
## Float Formats <!-- {{{ -->

+ `:echo 100.1`  
+ `:echo 5.45e+3` - sign in front of power of ten is optional (by
  default it's positive)  
+ `:echo 15.45e-2`  
<!-- }}} -->
## Coercion <!-- {{{ -->
When you combine a Number and a Float through arithmetic, comparison, or
any other operation Vim will cast the Number to a Float, resulting in a
Float.  
<!-- }}} -->
## Division <!-- {{{ -->
When dividing Numbers, the remainder is dropped.  

If you want Vim to perform floating point division one of thenumbers
needs to be a Float  
<!-- }}} -->

+ `:help Float` when might floating point number not work in Vimscript  
+ `:help floating-point-precision` what you need to remember about
  floating point numbers when write Vim plugin  
<!-- }}} -->
# Strings <!-- {{{ -->
## Concatenation <!-- {{{ -->
```vim
:echom "Hello, " . "world"
```
But notice:
```vim
:echom 10 . "foo"
```
Vim will display "10foo".
```vim
:echom 10.1 . "foo"
```
This time Vim throws an error, saying we're using a Float as String.

<!-- }}} -->
## Special Characters <!-- {{{ -->
Like most programming languages, Vimscript lets you use escape sequences
in strings to represent hard-to-type characters.  
Some of the usage:
```vim
:echom "foo \"bar\""
:echom "foo\\bar"
:echo "foo\nbar"
```

But if you run this command:
```vim
:echom "foo\nbar"
```
Vim will display something like `foo^@bar`. When you use `echom` instead
of `echo` with a String Vim will echo the _exact_ characters of the
string (`^@` is Vim's way of saying "newline character")  

<!-- }}} -->
## Literal Strings <!-- {{{ -->
Using single quotes tells Vim that you want the string `exactly` as-is,
with no escape sequences. The one exception is that two single quotes in
a row will produce one single quote:
```vim
:echom 'That''s enough.'
```
Vim will display "That's enough."

<!-- }}} -->

+ `:help expr-quote` - list of escape sequences you can use in a normal
  Vim string  
+ `:help i_CTRL-V`  
+ `:help literal-string`  
<!-- }}} -->
# String Functions <!-- {{{ -->
## Length <!-- {{{ -->
Get length of strings:
```vim
:echom strlen("foo")
:echom len("foo")
```
When used with Strings `len` and `strlen` have identical effects.  
<!-- }}} -->
## Splitting <!-- {{{ -->
The `split` function splits a String into a List.
```vim
:echo split("one two three")
```
You can also tell Vim to use a separator other than "whitespace" for
splitting:
```vim
:echo split("one,two,three", ",")
```
In both cases Vim display `['one', 'two', 'three']`  

+ `:help split()`

<!-- }}} -->
## Joining <!-- {{{ -->
```vim
:echo join(["foo", "bar"], "...")
```
Vim will display "foo...bar". `split` and `join` can be paired to great
effect:
```vim
:echo join(split("foo bar"), ";")
```

+ `:help join()`  

<!-- }}} -->
## Lower and Upper Case <!-- {{{ -->
Vim has two functions to change the case of Strings:
```vim
:echom tolower("Foo")
:echom toupper("Foo")
```
Vim displays `foo` and `FOO`.  
<!-- }}} -->

+ `:help functions` - list of built-in functions  
<!-- }}} -->
# Execute <!-- {{{ -->
The execute command is used to evaluate a string as if it were a
Vimscript command.  

## Basic Execution <!-- {{{ -->
Execute is a very powerfull tool because it lets you build commands out
of arbitrary strings.  

For instance, following code will open previous buffer in vertical
split:
```vim
:execute "rightbelow vsplit " . bufname("#")
```
<!-- }}} -->
## Is Execute Dangerous? <!-- {{{ -->

1. Vim is a unique environment where the normal security concerns simply
   aren't common.  
2. It let's you collapse many lines into a single one.  
<!-- }}} -->

+ `:help execute`  
+ `:help leftabove`, `:help rightbelow`, `:help :split`, `:help :vsplit`  

<!-- }}} -->
# Normal <!-- {{{ -->
The `normal` command simply takes a sequence of keys and pretends they
were typed in normal mode.  

## Avoiding Mappings <!-- {{{ -->
Vim has a `normal!` command that does not take into account user
mappings.  
<!-- }}} -->
## Special Characters <!-- {{{ -->
`normal!` doesn't parse special character sequences. For instance
following command won't work as expected:
```vim
:normal! /foo<cr>
```

<!-- }}} -->

+ `:help normal`  
+ `:help helpgrep`  
<!-- }}} -->
# Execute Normal! <!-- {{{ -->
`execute` ltes you build commands programmatically, so you can use Vim's
normal string escape sequences to generate the non-printing characters
you need.
```vim
:execute "normal! mqA;\<esc>`q"
```
will append `;` to the current line.  

<!-- }}} -->
# Basic Regular Expressions <!-- {{{ -->
## Highlighting <!-- {{{ -->
Before we start lets turn on some of the highlighting features:
```vim
:set hlsearch incsearch
```
`hlsearch` tells Vim to highlight all matches in a file when you perform
a search, and `incsearch` tells Vim to highlight the _next_ match while
you're still typing out your seach pattern.  

<!-- }}} -->
## Seaching <!-- {{{ -->

```vim
:execute "normal! gg/print\<cr>"
```
Searches for word "print" from top of the file and places you cursor on
first occurence.
```vim
:execute "normal! gg/print\<cr>n"
```
Same as above but places your cursor on second occurence.
```vim
:execute "normal! G?print\<cr>"
```
Searches backward from bottom


<!-- }}} -->
## Magic <!-- {{{ -->
Command
```vim
:execute "normal! gg/for .+ in .+:\<cr>"
```
won't work because Vim thinks you search for literal `+`. To make it
mean "1 or more of the preceding character" you should place a backslash
before the `+` character.  
So resulting command is:
```vim
:execute "normal! gg/for .\\+ in .\\+:\<cr>"
```
(remember about special characters for execute)  

<!-- }}} -->
## Literal Strings <!-- {{{ -->
If you don't want to place double slashes everywhere, you use literal
strings:
```vim
:execute "normal! gg" . '/for .\+ in .\+:' . "\<cr>"
```

<!-- }}} -->
## Very Magic <!-- {{{ -->
`\v` tells Vim to use its "very magic" regex parsing mode, which is
pretty mush the same as you're used to in any other programming
language:
```vim
:execute "normal! gg" . '/\vfor .+ in .+:' . "\<cr>"
```

<!-- }}} -->

+ `:help magic` - how characters are interpreted in patterns  
+ `:help pattern-overview` - kinds of things Vim regexes support  
+ `:help match` - define a pattern to highlight in the current window.  
<!-- }}} -->
# Case Study: Grep Operator, Part One <!-- {{{ -->
## Grep <!-- {{{ -->

Our example is going to make `:grep` easier to invoke by adding a "grep
operator" you can use with any of Vim's built-in (or custom!) motions to
select the text you want to search for.  

<!-- }}} -->
## Usage <!-- {{{ -->
The first thing you should think about when creating any non-trivial
piece of Vimscript is: "how will this functionaliry be used?".  

Some examples of how you might end up using it:  

+ `<leader>giw` - grep for the word under the cursor  
+ `<leader>giW` - grep for the WORD under the cursor  
+ `<leader>gi'` - grep for the contents of the single-quated string
  you're currently in.  
+ `viwe<leader>g` - visually select a word, extend the selection to the
  end of the word after it, then grep for the selected text.  
<!-- }}} -->
## A Preliminary Sketch <!-- {{{ -->
Let's simplify our goal to: "create a mapping to search for the word
under the cursor". This is useful but should be easier, so we can get
something running much faster.
```vim
:nnoremap <leader>g :grep -R something .<cr>
```

<!-- }}} -->
## The Search Term <!-- {{{ -->
First we need to search for the word under the cursor, not the string
something. Run the command:
```vim
:nnoremap <leader>g :grep -R <cword> .<cr>
```
Vim will replace `<cword>` with the word under the cursor before running
the command.  

You can use `<cWORD>` to get a WORD instead of a word.
```vim
:nnoremap <leader>g :grep -R <cWORD> .<cr>
```

There is a problem with our search term: if there are any special shell
characters in it Vim will happily pass them along to the external grep
command, which will explode ("foo;ls" will break it).  

To try to fix this we'll quote the argument in the grep call:
```vim
:nnoremap <leader>g :grep -R '<cWORD>' .<cr>
```

<!-- }}} -->
## Escaping Shell Command Arguments <!-- {{{ -->
There appears another problem, if we try the mapping on the word
`that's` single quote inside the word will interfere with the
quotes in the grep command!  

To get around this we can use Vim's `shellescape` function. Because
`shellscape()` works on Vim strings, we'll need to dynamically build the
command with `execute`. First run the following command to transform the
`:grep` mapping into `:execute "..."`:
```vim
:nnoremap <leader>g :execute "grep -R '<cWORD>' ."<cr>
```

Then use `shellescape` to fix the search term:
```vim
:nnoremap <leader>g :execute "grep -R " . shellescape(<cWORD>) . " ."<cr>
```

You'll see one problem if you run:
```vim
:echom shellescape("<cWORD>")
```
Vim will output `'<cWORD>'`. To fix this we'll use the `expand()`
function to force the expansion of `<cWORD>`.

Now that we know how to get a fully escaped version of the word under
the cursor, it's time to concatenate it into our mapping:
```vim
:nnoremap <leader>g :exe "grep -R " . shellescape(expand("<cWORD>")) . " ."\
<cr>
```


+ `:help escape()`  
+ `:help shellescape()`  
<!-- }}} -->
## Cleanup <!-- {{{ -->
First, we said that we don't want to go to the first result
automatically, and we can use `grep!` instead of plain `grep` to do
that.  

Afterwards we open quickfix window with `:copen`  

Then we'll remove all the grep output Vim displays while searching with
`silent`  

The final command:
```vim
:nnoremap <leader>g :silent execute "grep! -R " . shellescape(expand("<cWOR\
D>")) . " ."<cr>:copen<cr>
```

<!-- }}} -->

+ `:help :grep`  
+ `:help :make`  
+ `:help quickfix-window`  
+ `:help cnext`, `:help cprevious`  
+ `:help expand`  
+ `:help copen`  
+ `:help silent`  
<!-- }}} -->
# Case Study: Grep Operator, Part Two <!-- {{{ -->
## Create a File <!-- {{{ -->
Create separate file named `grep-operator.vim` and place it in
`~/.vim/plugin` directory. We'll type the command there instead of in
command line.  
<!-- }}} -->
## SKeleton <!-- {{{ -->
To create a new Vim operator you'll start with two components: a
function and a mapping:
```vim
nnoremap <leader>g :set operatorfunc=GrepOperator<cr>g@

function! GrepOperator(type)
    echom "Test"
endfunction
```

Source and run this mapping. Vim will echo `Test` after accepting any
motion, which means we've laid out the skeleton.  

That mapp ing is a bit more complicated. First we set the `operatorfunc`
option to our function, and then we run `g@` which calls this function
as an operator.  

<!-- }}} -->
## Visual Mode <!-- {{{ -->
We've added the operator to normal mode, but we'll want to be able to
use it from visual mode as well. Add another mapping below the first:
```vim
vnoremap <leader>g :<c-u>call GrepOperator(visualmode())<cr>
```

The `<c-u>` removes ranges that Vim automatically inserts.
`visualmode()` is a built-in VIm function that returns a one-character
string representing the last type of visual mode used: "v" for
characterwise, "V" for linewise, and a `Ctrl-v` character for blockwise.  

<!-- }}} -->
## Motion Types <!-- {{{ -->
Change function body:
```cpp
function! GrepOperator(type)
    echom a:type
endfunction
```

Source the file, then go agead and try it our in a variety of ways. Some
examples of the output you get are:  

+ `viw<leader>g` - echoes `v`  
+ `Vjj<leader>g` - echoes `V`  
+ `<leader>giw` - echoes `char`  
+ `<leader>gG` - echoes `line`  
<!-- }}} -->
## Copying the Text <!-- {{{ -->
Our function is going to need to somehow get access to the text the user
wants to search for, and the easiest way to do that is to simply copy
it. Edit hte function to look like this:
```vim
nnoremap <leader>g :set operatorfunc=GrepOperator<cr>g@
vnoremap <leader>g :<c-u>call GrepOperator(visualmode())<cr>

function! GrepOperator(type)
    " echom a:type
    if a:type ==# 'v'
        execute "normal! `<v`>y"
    elseif a:type ==# 'char'
        execute "normal! `[v`]y"
    else
        return
    endif

    echom @@
endfunction
```

Each time Vim will echo the text that the motion covers.  

<!-- }}} -->
## Escping the Search Term <!-- {{{ -->
Now that we've got the text we need in a Vim string we can escape it
like we did in the previous chapter. Modify the `echom` command so it
looks like this:

```vim
function! GrepOperator(type)
    " echom a:type
    if a:type ==# 'v'
        execute "normal! `<v`>y"
    elseif a:type ==# 'char'
        execute "normal! `[v`]y"
    else
        return
    endif

    echom shellescape(@@)
endfunction
```

<!-- }}} -->
## Running Grep <!-- {{{ -->
We're finally ready to add the `grep!` command that will perform the
actual search:
```vim
nnoremap <leader>g :set operatorfunc=GrepOperator<cr>g@
vnoremap <leader>g :<c-u>call GrepOperator(visualmode())<cr>

function! GrepOperator(type)
    if a:type ==# 'v'
        execute "normal! `<v`>y"
    elseif a:type ==# 'char'
        execute "normal! `[v`]y"
    else
        return
    endif

    silent execute "grep! -R " . shellescape(@@) . " ."
    copen
endfunction
```

Now the command is wrote.  

<!-- }}} -->

+ `:help visualmode()`  
+ `:help c_ctrl-u`  
+ `:help operatorfunc`  
+ `:help map-operator`  

<!-- }}} -->
# Case Study: Grep Operator, Part Three <!-- {{{ -->
Part of writing Vimscript is being considerate and making your users'
lives easier.  

## Saving Registers <!-- {{{ -->
By yanking the text into the unnamed register we destroy anything that
was previously in there. Let's save the contents of that register before
we yank and restore it after we've done:

```vim
function! GrepOperator(type)
    let saved_unnamed_refister = @@

    if a:type ==# 'v'
        execute "normal! `<v`>y"
    elseif a:type ==# 'char'
        execute "normal! `[v`]y"
    else
        return
    endif

    silent execute "grep! -R " . shellescape(@@) . " ."
    copen

    let @@ = saved_unnamed_register
endfunction
```

<!-- }}} -->
## Namespacing <!-- {{{ -->
Our script created a function named `GrepOperator` in the global
namespace. This probably isn't a big deal, but when you're writing
Vimscript it's far better to be safe than sorry.  

We can avoid polluting the global namespace by tweaking a couple of line
in our code:
```vim
nnoremap <leader>g :set operatorfunc=<SID>GrepOperator<cr>g@
vnoremap <leader>g :<c-u>call <SID>GrepOperator(visualmode())<cr>

function! s:GrepOperator(type)
```

FIrst, we modified the function name to start with `s:` which places it
in the current script's namespace. We also prepended the `GrepOperator`
function name with `<SID>` so they could find the function.  

<!-- }}} -->

+ `:help <SID>`  
<!-- }}} -->
# Lists <!-- {{{ -->
Vimscript lists are ordered, heterogeneous collections of elements.
```vim
:ehco ['foo', 3, 'bar']
```

Vim displays the list. Lists can of course be nested.
```vim
:echo ['foo', [3, 'bar']]
```

## Indexing <!-- {{{ -->
Vimscript lists are zero-indexed, you can get at the elements in the
usual way as well as in reverse order.
```vim
" displays [1,2]
:echo [0, [1,2]][1]
" displays 0
:echo [0, [1,2]][-2]
```
<!-- }}} -->
## Slicing <!-- {{{ -->
This will look familiar to Python programmers, but it does not always
act the same way!
```vim
:echo ['a', 'b', 'c', 'd', 'e'][0:2]
```
Vim displays `['a','b','c']`. You can safely exceed the upper bound as
well.
```vim
:echo ['a','b','c','d','e'][0:100000]
```
Vim simply displays the entire list. Slice indexes can be negative.
```vim
:echo ['a','b','c','d','e'][-2:-1]
```
Vim displays `['d','e']`. When slicing lists you can leave off the first
index to mean "the beginning" and/or the last index to mean "the end".
```vim
:echo ['a','b','c','d','e'][:1]
:echo ['a','b','c','d','e'][3:]
```
Vim displays `['a','b']` and `['d','e']`  

Like Python, Vimscript allows you to index and slice string too.
```vim
:echo "abcd"[0:2]
```
Vim displays `abc`.  

However! You can't use negative bare indices with strings. You can use
negative indices when slicing string though!
```vim
"            v - not ok;  v - ok
:echo "abcd"[-1] . "abcd"[-2:]
```

<!-- }}} -->
## Concatenation <!-- {{{ -->
You can combine Vim lists with `+`.
```vim
:echo ['a', 'b'] + ['c']
```
Vim displays `['a','b','c']`.  

<!-- }}} -->
## List Functions <!-- {{{ -->
Append `b`:
```vim
:let foo = ['a']
:call add(foo, 'b')
:echo foo
```
Vim mutates the list `foo` in-place to append 'b' and displays `['a','b']`.
Get length of list:
```vim
:echo len(foo)
```
Vim displays 2. Get the item at the given index from the given list, or
return the given default value if the index is out of range in the list:
```vim
:echo get(foo, 0, 'default')
:echo get(foo, 100, 'default')
```
Vim displays `a` and `default`. Return the first index of the given item
in the given list, or -1 if the item is not in the list:
```vim
:echo index(foo, 'b')
:echo index(foo, 'nope')
```
Vim displays 1 and -1. `join` will join the items in the given list
together into a string separated by the given separator string (or a
space if none is given), coercing each item to a string if
necessary/possible.
```vim
:echo join(foo)
:echo join(foo, '---')
:echo join([1,2,3], '')
" Vim displays a b, a---b, and 123
```
`reverse` reverses the given list in place:
```vim
:call reverse(foo)
:echo foo
:call reverse(foo)
:echo foo
" Vim displays ['b','a'] and then ['a','b']
```


<!-- }}} -->

+ `:help List`  
+ `:help add()`  
+ `:help len()`  
+ `:help get()`  
+ `:help index()`  
+ `:help join()`  
+ `:help reverse()`  
+ `:help functions`  
<!-- }}} -->
# Looping <!-- {{{ -->
These are two main kinds of loops Vim supports.

## For Loops <!-- {{{ -->
There's no equivalent to the C-style `for (int i = 0; i < foo; ++i)`
loop form in Vimscript. But you'll never miss it.  

```vim
:let c = 0

:for i in [1,2,3,4]
:   let c += i
:endfor

:echom c

" vim displays 10
```

<!-- }}} -->
## While Loops <!-- {{{ -->
Vim also  supports the classic `while` loop. Run the following commands:

```vim
:let c = 1
:let total = 0

:while c <= 4
:   let total += c
:   let c += 1
:endwhile

:echom total
```
Once again Vim displays 10.  

<!-- }}} -->

+ `:help for`  
+ `:help while`  
<!-- }}} -->
# Dictionaries <!-- {{{ -->
Dictionaries are created using curly brackets. Values are heterogeneous,
but _keys are always coerced to strings_.  

Run this command:
```vim
:echo {'a': 1, 100: 'foo'}
```
Vim displays `{'a': 1, '100': 'foo'}`. Vim allows you to use a comma
after the last element in a dictionary.  

## Indexing <!-- {{{ -->
To look up a key in a dictionary you use the same syntax as most
languages:
```vim
:echo {'a': 1, 100: 'foo',}['a']
```
Vim displays 1. Try it with a non-string index:
```vim
:echo {'a': 1, 100: 'foo',}[100]
```
Vim coerces the index to a string. Vimscript also supports the
Javasccript-style "dot" lookup:
```vim
:echo {'a': 1, 100: 'foo',}.a
:echo {'a': 1, 100: 'foo',}.100
```

<!-- }}} -->
## Assigning and Adding <!-- {{{ -->
Adding entries to dictionaries is done by simply assigning them like
variables:
```vim
:let foo = {'a': 1}
:let foo.a = 100
:let foo.b = 200
:echo foo
```
Vim displays `{'a': 100, 'b': 200}`.  

<!-- }}} -->
## Removing Entries <!-- {{{ -->
There are two ways to remove entries from a dictionary. Run the
following commands:
```vim
:let test = remove(foo, 'a')
:unlet foo.b
:echo foo
:echo test
```
Vim displays `{}` and 100. The `remove`function remove the entry with
the given key from the given dictionary and return the removed value.
The `unlet` command also removes adictionary entries, but you can't use
the value.  

<!-- }}} -->
## Dictionary Functions <!-- {{{ -->
Get key's value and, if not exist, return default:
```vim
:echom get({'a': 100}, 'a', 'default')
:echom get({'a': 100}, 'b', 'default')
```
Vim displays 100 and `default`, just like the `get` function for lists.  

You can also check if a given key is present in a given dictionary:
```vim
:echom has_key({'a': 100}, 'a')
:echom has_key({'a': 100}, 'b')
```
Vim displays 1 and 0.  

You can pull the key-value pairs out of a dictionary with `items`. Run
this command:
```vim
:echo items({'a': 100, 'b': 200})
```
Vim will display a nested list that looks something like `[['a', 100], ['b',  200]]`.
You can get just the keys or just the values with the `keys` and `values` functions.

<!-- }}} -->

+ `:help Dictionary`  
+ `:help get()`  
+ `:help has_key()`  
+ `:help items()`  
+ `:help keys()`  
+ `:help values()`  

<!-- }}} -->
# Toggling <!-- {{{ -->
## Toggling Options <!-- {{{ -->
Let's start by creating a function that will toggle an option for us,
and a mapping that will call it.

```vim
nnoremap <leader>f :call FoldColumnToggle()<cr>

function! FoldColumnToggle()
    echom &foldcolumn
endfunction
```

Let's add in the actual toggling functionality:
```vim
nnoremap <leader>f :call FoldColumnToggle()<cr>

function! FoldColumnToggle()
    if &foldcolumn
        setlocal foldcolumn=0
    else
        setlocal foldcolumn=4
    endif
endfunction
```


<!-- }}} -->
## Toggling Other Things <!-- {{{ -->
Let's create a mapping that "toggles" quickfix window.
To get the "toggling" behavior we're looking for we'll use a quick,
dirty solution: a gloval variable:
```vim
nnoremap <leader>q :call QuickfixToggle()<cr>

let g:quickfix_is_open = 0

function! QuickfixToggle()
    if g:quickfix_is_open
        cclose
        let g:quickfix_is_open = 0
    else
        copen
        let g:quickfix_is_open = 1
    endif
endfunction
```

<!-- }}} -->
## Restoring Windows/Buffers <!-- {{{ -->
If the user runs the mapping when they're already in the quickfix
window, Vim closes it and dumps them into the last split instead of
sending them back where they were. We'll add two line in this mapping.
One of them sets another global variable which saves the current window
number before we run `:copen`. The second line executes `wincmd w` with
that number prepended as a count, which tells Vim to go to that window:

```vim
nnoremap <leader>q :call QuickfixToggle()<cr>

let g:quickfix_is_open = 0

function! QuickfixToggle()
    if g:quickfix_is_open
        cclose
        let g:quickfix_is_open = 0
        execute g:quickfix_return_to_window . "wincmd w"
    else
        let g:quickfix_return_to_window = winnr()
        copen
        let g:quickfix_is_open = 1
    endif
endfunction
```

<!-- }}} -->

+ `:help foldcolumn`  
+ `:help winnr()`  
+ `:help ctrl-w_w`  
+ `:help wincmd`  
<!-- }}} -->
# Functional Programming <!-- {{{ -->
## Immutable Data Structures <!-- {{{ -->
Vim doesn't have any immutable collections like Clojure's vectors and
maps built-in, but by creating some helper functions we can fake it to
some degree.  

Add the following function to your file:
```vim
function! Sorted(1)
    let new_list = deepcopy(a:1) 
    call sort(new_list)
    return new_list
endfunction
```

Source and write the file, then run `:echo Sorted([3, 2, 4, 1])`. Vim
echoes `[1, 2, 3, 4]`.  

Let's add a few more helper function in this same style:
```vim
function! Reversed(1)
    let new_list = deepcopy(a:1)
    call reverse(new_list)
    return new_list
endfunction

function! Append(1, val)
    let new_list = deepcopy(a:1)
    call add(new_list, a:val)
    return new_list
endfunction

" returns a new list with the element at the given index replaced by the new
" value
function! Assoc(1, i, val)
    let new_list = deepcopy(a:1)
    let new_list[a:i] = a:val
    return new_list
endfunction

" returns a new list with the element at the given index removed
function! Pop(1, i)
    let new_list = deepcopy(a:1)
    call remove(new_list, a:i)
    return new_list
endfunction
```


<!-- }}} -->
## Functions as Variables <!-- {{{ -->
Vimscript supports using variables to store functions, but the syntax is
a bit obtuse:
```vim
:let Myfunc = function("Append")
:echo Myfunc([1, 2], 3)
```
If a Vimscript variable refers to a function it must start with a
capital letter.

Functions can be stored in lists just like any other kind of variable:
```vim
:let funcs = [function("Append"), function("Pop")]
:echo funcs[1](['a', 'b', 'c'], 1)
```

The _funcs_ variable does not need to start with a capital letter
because it's storing a list, not a function.  


<!-- }}} -->
## Higher-Order Functions <!-- {{{ -->
Higher-order functions are functions that take other functions and do
something with them. We'll begin with the trusty `map` function. Add
this to your file:
```vim
function! Mapped(fn, 1)
    let new_list = deepcopy(a:1)
    call map(new_list, string(a:fn) . '(v:val)')
    return new_list
endfunction
```
Source and write the file, and try it out by running the following
commands:
```vim
:let mylist = [[1, 2], [3, 4]]
:echo Mapped(function("Reversed"), mylist)
```
Vim displays `[[2, 1], [4, 3]]`. Read `:help map` now to see how it works.  

Now we'll create a few other common higher-order functions:
```vim
function! Filtered(fn, 1)
    let new_list = deepcopy(a:1)
    call filter(new_list, string(a:fn) . '(v:val)')
    return new_list
endfunction
```

Try `Filtered()` out with the following commands:
```vim
:let mylist = [[1, 2], [], ['foo'], []]
:echo Filtered(function('len'), mylist)
```

Vim displays `[[1, 2], ['foo']]`. `Filtered()` takes a preficate
function and a list. It returns a copy of the list that contains only
the elements of the original where the result of calling the function on
it is "truthy".  

Finally we'll create the counterpart to `Filtered()`:
```vim
function! Removed(fn, 1)
    let new_list = deepcopy(a:1)
    call filter(new_list, '!' . string(a:fn) . '(v:val)')
    return new_list
endfunction
```


<!-- }}} -->

+ `:help sort()`  
+ `:help reverse()`  
+ `:help copy()`  
+ `:help deepcopy()`  
+ `:help map()`  
+ `:help function()`  
+ `:help type()`  

<!-- }}} -->
# Paths <!-- {{{ -->
## Absolute Paths <!-- {{{ -->

```vim
" displays the relative path of whatever file you're currently editing
echom expand('%')
" the :p tells Vim that you want the absolute path
echom expand('%:p')
" displays an absolute path to the file `foo.txt`, regardless of whether
" that file actually exists
echom fnamemodify('foo.txt', ':p')
```

<!-- }}} -->
## Listing Files <!-- {{{ -->
To display all files and directories in the current directory run:
```vim
:echo globpath('.', '*')
```
To get a list you'll need to `split()` it yourself:
```vim
:echo split(globpath('.', '*'), '\n')
```

`globpath()`'s wildcards work mostly as you would expect. This would
list all `.txt` files:
```vim
:echo split(globpath('.', '*.txt'), '\n')
```

You can recursively list files with `**`:
```vim
:echo split(globpath('.', '**'), '\n')
```

<!-- }}} -->

+ `:help expand()`  
+ `:help fnamemodify()`  
+ `:help filename-modifiers`  
+ `:help simplify()`  
+ `:help resolve()`  
+ `:help globpath()`  
+ `:help wildcards`  
<!-- }}} -->

# Creating a Full Plugin <!-- {{{ -->
The plugin we're going to make is going to add support for the _Potion_
programming language.  
<!-- }}} -->
# Plugin Layout in the Dark Ages <!-- {{{ -->
## `~/.vim/colors/` <!-- {{{ -->
Files inside `~/.vim/colors/` are treated as color schemes. For example:
if you run `:color mycolors` Vim will look for a file at
`~/.vim/colors/mycolors.vim` and run it. That file should contain all
the Vimscript commands necessary to generate your color scheme.  

If you want to create your own colorscheme, you should copy an existing
scheme and modify it (remember `:help` is your friend).  
<!-- }}} -->
## `~/.vim/plugin/` <!-- {{{ -->
Files inside the directory will each be run once _every time_ Vim
starts.  
<!-- }}} -->
## `~/.vim/ftdetect/` <!-- {{{ -->
Any files in `~/.vim/ftdetect/` will also be run every time you start
Vim. `ftdetect` stands for "filetype detection". The files in this
directory should set up autocommands that detect and set the `filetype`
of files, and _nothing else_.  
<!-- }}} -->
## `~/.vim/ftplugin/` <!-- {{{ -->
The naming of these files matters! When Vim sets a buffer's `filetype`
to a value it then looks for a file in `~/.vim/ftplugin/` that maches
and if there is file, it will run it. Also Vim runs all the files inside
matching directory in `~/.vim/ftplugin/`.  

Because these files are run every time a buffer's `filetype` is set they
_must_ only  set buffer-local options! If they set options globally they
would overwrite them for all open buffers!  

<!-- }}} -->
## `~/.vim/indent/` <!-- {{{ -->
`indent` files should set options related to indentation for their
filetypes, and those options should be buffer-local.  
<!-- }}} -->
## `~/.vim/compiler/` <!-- {{{ -->
File in the directory set compiler-related options in the current buffer
based on their names.  
<!-- }}} -->
## `~/.vim/after/` <!-- {{{ -->
File in this directory will be loaded every time Vim starts, but _after_
the files in `~/.vim/plugin/`. This allows you to override Vim's
internal files.  
<!-- }}} -->
## `~/.vim/autoload/` <!-- {{{ -->
In a nutshell: `autoload` is a way to delay the loading of your plugin's
code until it's actually needed.  
<!-- }}} -->
## `~/.vim/doc/` <!-- {{{ -->
This directory is where you can add documentation for your plugin.  
<!-- }}} -->
<!-- }}} -->

# A New Hope: Plugin Layout with Pathogen <!-- {{{ -->
<!-- TODO: stopped here -->
## Runtimepath <!-- {{{ -->

When Vim looks for file in a spacific directory, Vim has the
`runtimepath` setting which tells it where to find files to load.  

<!-- }}} -->
## Pathogen <!-- {{{ -->

This means that each directory inside `bundle/` should contain some or
all of the standard Vim plugin directories, like `colors/` and `syntax/`  

<!-- }}} -->
## Being Pathogen-Compatible <!-- {{{ -->

We simply put our files in the appropriate directories inside the
plugin's repository!  

Our plugin's repository will wind up looking like this:  
```txt
potion/
    README
    LICENSE
    doc/
        potion.txt
    ftdetect/
        potion.vim
    syntax/
        potion.vim
    ... etc ...
```

<!-- }}} -->

+ `:help runtimepath`  
<!-- }}} -->
# Detecting Filetypes <!-- {{{ -->

Create simple factorial function (write it on potion language):
```txt
factorial = (n):
    total = 1
    n to 1 (i):
        total *= i.
    total.

10 times (i):
    i string print
    '! is : ' print
    factorial (i) string print
    "\n" print.
```

You can run this by command: `potion factorial.pn`  

## Detecting Potion Files <!-- {{{ -->
If you run `:set filetype?`, Vim will display `filetype=` because it
doesn't know what a `.pn` file is yet.  

Create `ftdetect/potion.vim` in your plugin's repo. Put the following
lines into it:
```vim
au BufNewFile,BufRead *.pn set filetype=potion
```
Vim automatically wraps the contents of `ftdetect/*.vim` files in
autocommand groups for you.  

Close the `factorial.pn` file and reopen it. Now run the previous
command again:
```vim
:set filetype?
```
This time Vim displays `filetype=potion`  
<!-- }}} -->

+ `:help ft`  
+ `:help setfiletype`  

<!-- }}} -->
