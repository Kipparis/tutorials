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
}}}
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
<!-- TODO: stopped here -->
<!-- }}} -->

