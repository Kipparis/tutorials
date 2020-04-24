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

<!-- }}} -->

