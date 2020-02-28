_book: Learning the bash Shell 3rd Edition. O'Reilly_  
    This file just a notes. If you have no clue what commands and pipes
    are, read the book by yourself.  
# What Is a Shell?<!-- {{{ -->
The shell's job is to traslate the user's command lines into operating
system instructions.  
Remember that the shell itself is not UNIX - just the **_user interface_** to it.
UNIX is one of the first operating systems to make the user interface
independent of the operating system.  
<!-- }}} -->
# Features of bash<!-- {{{ -->
    + command-line editing modes  
    + job control  
    + many options and variables for customization  
    + it have expanded programming features  
<!-- }}} -->
# Structure of commands<!-- {{{ -->
Shell command lines consist of one or more words, which are separated on
a command line by blanks or TABs. The first word one the line is the
**_command_**. The rest (if any) are **_arguments_**.  
An **_option_** is a special type of argument that give the command
specific information on what it is supposed to do. Options usually
consist of a dash followed by a letter.  
<!-- }}} -->
# Directory<!-- {{{ -->
Tilde (~) is abbreviation for homedirectories:  

+ `~alice/story` - story folder inside of _alice_'s home dir  
+ `~/story` - story folder inside of current user home dir  

+ `cd -` - changes to whatever directory you were in before  
<!-- }}} -->
# Filenames, Wildcards, and Pathname Expansion<!-- {{{ -->
The process of matching expressions containing wildcards to filenames is
called **_wildcard expansion_** or **_globbing_**.  

If you need to `ls` all files that end with _.txt_, you may turn their
names into patters, using _**wildcards**_.  

**Basic wildcards**:  

| **Wildcard** | **Matches**                  |
| ---          | ---                          |
| ?            | Any single character         |
| *            | Any string of characters     |
| [_set_]      | Any character in _set_       |
| [!_set_]     | Any character _not_ in _set_ |

+ `[a-z]` - all lowercase letters  
+ `[!0-9]` - all non-digits  
+ `[a-zA-Z]` - all lower- and uppercase letters  

To match **!** itself, place it after the first character in the set, or
precede it with a backslash, as in `[\!]`  
<!-- }}} -->
