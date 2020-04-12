_book: Learning the bash Shell 3rd Edition. O'Reilly_  
    This file just a notes. If you have no clue what commands and pipes
    are, read the book by yourself.  

useful keywords  

scripting:  

<!-- TODO: -->
<!-- + options -->
<!-- + aliases -->
<!-- + functions -->
<!-- + variables (like `unset`) -->
<!-- + bind (опции) -->
+ `builtin` - tells the shell to use the built-in command and ignore any
  function of than name  
+ `test` - use manpage for using **strings in conditions**  
+ `declare` - displays the values of all variables in the environment
or set variable attributes  
+ `readonly name` - makes variable name be a type of readonly  
+ see _Command-line processing_ for order of processing pipelines and
  how to alter this order  
+ `trap` - process signals  
+ `nohup` - executes arguments and ignore HUP signal (default output to
  _nohup.out_)  
+ `disown` - removes process from the list of jobs  

Usefull things:

+ `kill %+` - kill last job (send signal TERM by default)  
<!-- TODO: once read, go throw -->
<!--     options -->
<!--     env variables -->
<!--     aliases -->
<!--     functions -->
<!-- and find out cool, or those need for modification -->
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
# Brace Expansion <!-- {{{ -->
Expands to an arbitrary string of a given form:  

+ optional _preable_  
+ comma-separated strings between braces({})  
+ optional _postscript_  

Each instance of a string inside the braces is combined with the preable
and the postscript. It is also possible to nest the braces.  

```shell
$ echo b{ed,olt,ar}s
beds bolts bars
$ echo b{ar{d,n,k},ed}s
bards barns barks beds
# another example of brace expansion
$ echo {2..5}
2 3 4 5
$ echo {d..h}
d e f g h
```
<!-- }}} -->
# Input and Output <!-- {{{ -->
Everything on the system that produces or accepts data is treated as a
file;
## Standard I/O <!-- {{{ -->
By convention, each UNIX program has a single way of accepting input
called _standard input_, a single way of producint output called
_standard output_, and single way of producing error messages called
_standard error output_.  

All shells handle standard I/O in basically the same way. Each program
that you invoke has all three standard I/O channels set to your terminal
or workstation.  

You can also hook programs together in a _pipeline_, in which the
standard output of one program feeds directly into the standard input of
another.  

This makes it possible to use UNIX utilities as building blocks for
bigger programs:  

| Utility | Purpose                                               |
| ---     | ---                                                   |
| _cat_   | Copy input to output                                  |
| _grep_  | Search for strings in the input                       |
| _sort_  | Sort lines in the input                               |
| _cut_   | Extract columns from input                            |
| _sed_   | Perform editing operations on input                   |
| _tr_    | Translate characters in the input to other characters |
<!-- }}} -->
## I/O Redirection <!-- {{{ -->
The notation `command < filename>` sets things up so that _command_
takes standard input from a file instead of from a terminal.  
Similarly, `command > filename` causes the command's standard output to
be redirected to the named file.  
<!-- }}} -->
## Pipelines <!-- {{{ -->
To redirect the output of a command into the standard input of another
command instead of a file use **_pipe_**, notated as "|". Command line
that contains two or more commands connected with pipes is called a
pipeline.  
<!-- }}} -->
<!-- }}} -->
# Background Jobs <!-- {{{ -->
If you want to run a command that does not require user input and you
want to do other things while the command is running, put an ampersand
(&) after the command.  
This is called **_running the command in the background_**, and a
command that runs in this way is called a **_background job_**; by
contrast a job run the normal way - foreground job.  

You can overview background jobs with `jobs`, printing an indication
lines of the job's status.  
## Background I/O <!-- {{{ -->
If a background job produces screen output, the output will jsut appear
on your screen (which will intersperse with foreground job).  
To solve, use redirect (`>`) to file
<!-- }}} -->
## Background Jobs and Priorities <!-- {{{ -->
Every job on the system is assigned a _priority_, a number that tells
the operating system how much priority to give the job whe it doles out
resources (the higher the nubmer, the lower the priority).  

UNIX command that lets you lower (or higher) the priority of any job - `nice`  
<!-- }}} -->
<!-- }}} -->
# Special Characters and Quoting <!-- {{{ -->
## Table of special characters <!-- {{{ -->
| Character | Meaning                      |
| ---       | ---                          |
| ~         | Home directory               |
| \`        | Command substitution         |
| #         | Comment                      |
| $         | Variable expression          |
| &         | Background job               |
| \*        | String wildcard              |
| (         | Start subshell               |
| )         | End subshell                 |
| \         | Quote next character         |
| \|        | Pipe                         |
| [         | Start character-set wildcard |
| ]         | End character-set wildcard   |
| {         | Start command block          |
| }         | End command block            |
| ;         | Shell command separator      |
| '         | Strong quote                 |
| "         | Weak quote                   |
| <         | Input redirect               |
| >         | Output redirect              |
| /         | Pathname directory separator |
| ?         | Single-character wildcard    |
| !         | Pipeline logical NOT         |
<!-- }}} -->
## Quoting <!-- {{{ -->
Sometimes you will want to use special characters literally, i.e.
without their special meanings. This is called _quoting_.  
``'string'``  
<!-- }}} -->
## Backslash-Escaping <!-- {{{ -->
Another way to change the meaning of a character is to precede it with a
backslash (`\`). This is called _backslash-escaping_ the character.  
<!-- }}} -->
## Control Keys <!-- {{{ -->
Control keys - those that you type by holding down the CTRL key and
hitting another key.  
If you want to see your settings type `stty --all`  

Common control keys:  

| Ctrl key      | stty name | Function description                        |
| ---           | ---       | ---                                         |
| Ctrl-C        | intr      | Stop current command                        |
| Ctrl-D        | eof       | End of input                                |
| Ctrl-\        | quit      | Stop current command if Ctrl-C doesn't work |
| Ctrl-S        | stop      | Halt output to screen                       |
| Ctrl-Q        |           | Restart output to screen                    |
| DEL or Ctrl-? | erase     | Erase last character                        |
| Ctrl-U        | kill      | Erase entire command line                   |
| Ctrl-Z        | susp      | Suspend current command                     |
<!-- }}} -->
<!-- }}} -->
# Help <!-- {{{ -->
In bash you can type `help` by itself to get a list of the built-in
shell commands.  
If you provide `help` with a shell command name it will give you a
detailed description.  
You can also provide _help_ with a **_partial name_**. For example `help
re` will provide details on _read_, _readonly_, _return_.  
<!-- }}} -->
# Command-Line Editing <!-- {{{ -->
`fc` command allows you edit your last command with your favorite
editor.  
## Enabling Command-Line Editing <!-- {{{ -->
Two ways to enter either editing mode:  

+ `$ set -o vi`  
+ set a _readline_ variable in the file _.inputrc_  
    Note about .inputrc. It is only sourced by bash :)  
    If you want to set up eny mode on your shell, search for this  
<!-- }}} -->
## The History List <!-- {{{ -->
Default to *.bash\_history*, buy you can change to whatever you like by
setting the environment varialbe **HISTFILE**.  
<!-- }}} -->
## vi Editing Mode <!-- {{{ -->
vim-mode has two modes of its own: _input_ and _control_ mode.  

| Command     | Description                                     |
| ---         | ---                                             |
| DEL, Ctrl-H | Delete previous character                       |
| Ctrl-W      | Erase previous word (i.e., erase until a blank) |
| Ctrl-V      | Quote the next character                        |
| ESC         | Enter control mode (see below)                  |

Type `<count>G` to move `count` lines up in search history  

**Character-Finding Commands:**  

+ `fx` move right to next occurence of `x`  
+ `Fx` move left  to previous occurence of `x`  
+ `t` and `T` same as `f` and `F` but your coursor placed closely to
  starting position  
+ `;` - redo last character-finding command  
+ `,` - redo last character-finding command in opposite direction  

**Textual Completion:**  
In modern shells it's called via `TAB` key.  

**Miscellaneous Commands:**  

| Command  | Description                                        |
| ---      | ---                                                |
| `~`      | Invert case of current character(s)                |
| `-`      | Append last word of previous command, enter IM     |
| `Ctrl-L` | Clear the screen and redraw the current line on it |
| `#`      | Prepend # to the line and send it to the history   |

<!-- }}} -->
<!-- }}} -->

## The fc Command <!-- {{{ -->
`fc -l` - lists last commands (you may specify 2 arguments - since,
before), time window is specified by number arguments or by prefix
string  

* `-n` suppresses the line numbers  

`f` is usually used to fix a recent command  

+ With no arguments - edit the most recent command  
+ With a numberic argument - edit command with that number  
+ With a string argument - edit command starting with that string  
+ With two arguments you specify the ranger of commands  

**Warning!** After exit fc editor will execute all commands.

<!-- }}} -->
## History Expansion <!-- {{{ -->
The way to recall commands is by the use of _event designators_.  

| Command            | Description                                                                 |
| ---                | ---                                                                         |
| `!`                | Start a history substitution                                                |
| `!!`               | Refers to the last command                                                  |
| `!n`               | Refers to command line _n_                                                  |
| `!-n`              | Refers to the current command line minus _n_                                |
| `!string`          | Refers to the most recent command starting with _string_                    |
| `!?string?`        | Refers to the most recent command containing _string_; ending ? is optional |
| `^string1^string2` | Repeat the last command, replacing _string1_ with _string2_                 |

_Note_:

+ `!!` good for _sudo_  
+ `^string1^string2` - _typos_  

It's also possible to refer to certain words in a previous command by
the use of a _word designator_.  

| Designator | Description                                           |
| ---        | ---                                                   |
| `0`        | First word in a line                                  |
| `n`        | The _n_th word in a line                              |
| `^`        | The frst argument (the second word)                   |
| `$`        | The last argument in a line                           |
| `%`        | The words matched by the most recent _?string_ search |
| `x-y`      | A range of words from _x_ to _y_                      |
| `*`        | All words but the first (_0-y_)                       |
| `x*`       | `x-$`                                                 |
| `x-`       | The words from _x_ to the second to last word         |

The _word designator_ follows the _event designator_ separated by a
colon.  

There are also **_modifiers_**, but it's better to master vi or emacs
mode skills. If you wish to read about **_modifiers_** go to page 168.  
<!-- }}} -->

# Customizing Your Environment <!-- {{{ -->
+ **_Special files_** - like *.bash_profile*(better to use _.profile_),
*.bash_logout*,_.bashrc_ are read by _bash_ when you log in
and out or start a new shell  
+ **_Aliases_** - synonyms for commands or command strings  
+ **_Options_** - controls various apects of your environment that you
  can turn on and off.  
+ **_Variables_** - shell and other programs can modify their behavior
  according to the values stored in the variables  

## The .bash\_profile, .bash\_logout, and .bashrc Files <!-- {{{ -->
Default for *.bash_profile* is _/etc/profile_. This file is read and the
commands in it are executed by _bash_ every time you log in to the
system  
You you done changes, they won't affect until logging in or executing
command `source .bash_profile`  
_.bashrc_ executed every time subshell runs  
*.bash_logout* - every logout  
<!-- }}} -->
## Aliases <!-- {{{ -->
Sytax `alias name=command`  
Two ways of using an alias:  

+ create more mnemonic name for an existing command:  
    `alias search=grep`  
+ correcting typos:  
    `alias emcas=emacs`  
+ shorhand for a longer command string:  
    `alias cdvoy="cd sipp/demo/animation/voyager"`

Notes:  

+ _bash_ makes a textual substitution of the alias for that which it is
  aliasing  
+ aliases are recursive (but it can be prevented by bash by looking at
  first word in the command)  
+ aliases can't be expanded as arguments
    one solution for _cd_ is `alias cd="cd "` this will enable directory
    aliasing  

`alias name` - output alias' value  
`alias` - output all available aliases  
<!-- }}} -->
## Options <!-- {{{ -->
_Options_ allow you to change shell's behavior  
Syntax is: `set +\-o optionname [+\- optionname [...]]`  

+ **+** turn options _off_  
+ **-** turns option _on_  

Basic shell options:  

| Option      | Description                                                          |
| ---         | ---                                                                  |
| emacs       | Enters _emacs_ editing mode                                          |
| ignoreeof   | Doesn't allow use of single ^d to log off (use `exit`)               |
| noclobber   | doesn't allow output redirection to overwrite an existing file       |
| noglob      | Doesn't expand filename wildcards                                    |
| nounset     | Indicates and error when trying to use a variable that is undefined  |
| vi          | Enters _vi_ editing mode                                             |
| cdable_vars | argument to cd that is not a directory assumed as name of a variable |


`set -o` will output all options and their status.  
<!-- }}} -->
## Shell Variables <!-- {{{ -->
To set variable use command `varname=value`  
To unset - `unset varname`  
<!-- }}} -->
## Built-In Variables <!-- {{{ -->
**Editing mode variables:**  

| Variable | Meaning                                               |
| ---      | ---                                                   |
| HISTCMD  | The history number of the current command             |
| HISTFILE | File containing history lines                         |
| HISTSIZE | Maximum number of commands to remember (default 500)  |
| FCEDIT   | Pathname of the editor to use with the **fc** command |
<!-- }}} -->
## Prompting variables <!-- {{{ -->
They are:  

+ **PS1** - primary prompt string  
+ **PS2** - secondary prompt string (default `>`)  
+ **PS3** - relate to shell programming and debugging  
    - `select` uses **PS3** variable as prompt  
+ **PS4** - relate to shell programming and debugging  

**Prompt string customizations:**  

| Command      | Meaning                                                 |
| `\a`         | The ASCII bell character                                |
| `\A`         | The current time in 24-hour HH:MM format                |
| `\d`         | The date in "Weekday Month Day" format                  |
| `\D{foramt}` | The format is passed to strftime                        |
| `\e`         | The ASCII escape character (033)                        |
| `\H`         | The hostname                                            |
| `\h`         | The hostname up to the first "."                        |
| `\j`         | The number of jobs currently managed by the shell       |
| `\l`         | The basename of the shell's terminal device name        |
| `\n`         | A carrieage return and line feed                        |
| `\r`         | A carriage return                                       |
| `\s`         | The name of the shell                                   |
| `\T`         | The current time in 12-hour HH:MM:SS format             |
| `\t`         | The current time in HH:MM:SS format                     |
| `\@`         | The current time in 12-hour a.m./p.m. format            |
| `\u`         | The username of the current user                        |
| `\w`         | The current working directory                           |
| `\W`         | The basename of the current working directory           |
| `\#`         | The command number of the current command               |
| `\!`         | The history number of the current command               |
| `\$`         | if the effective UID is 0, print a `#`, otherwise - `$` |
| `\nnn`       | Character code in octal                                 |
| `\\`         | backslash                                               |
| `\[`, `\]`   | Begin, and a sequence of non-printing characters        |
<!-- }}} -->
## Command search path <!-- {{{ -->
Safe way to extend PATH is `PATH=$PATH":/home/you/bin`  
    You command won't be executed if you already have command with this
    name  
<!-- }}} -->
## Command hashing <!-- {{{ -->
First time you enter command, bash will store its path to hashtable.
When you enter this command again, bash will search for its location in
hastable, and if fails, looks in search path.  

To see your hashtable type: `hash`  

+ `hash -r` - remove everything in the table  
+ `hash -d name` - remove specific name  
+ `hash -p` - enter command in hash table  

Command hashing can be turned on and off with the **hashall** option.  
<!-- }}} -->

<!-- }}} -->
# Customization and Subprocesses <!-- {{{ -->
## Subprocesses and environment variables <!-- {{{ -->
Environment Variables are very basic thing that known to all
subprocesses. You can define **your own environment variables** with
command: `export varname=value`  

It is also possible to define variables to be in the environment of a
**particular subprocess only** by preceding the command with the variable
assignment: `varname=value command`

You can find out which variables are invironment variables and their
values by typing `export` or by using `-p` option to the command  

**Standard variables:**  

| Variable | Meaning                                 |
| ---      | ---                                     |
| COLUMNS  | The number of columns your display has  |
| EDITOR   | Pathname of your text editor            |
| LINES    | The number of lines your display has    |
| SHELL    | Pathname of the shell you are running   |
| TERM     | The type of terminal that you are using |
<!-- }}} -->
## Terminal types <!-- {{{ -->
The value of **TERM** must be ashort character string with lowercase
letters that appears as a filename in the _terminfo_ database. This
database is a two-tiered directory of files `/usr/lib/terminfo`. This
directory contains subdirectories with single-character names; these in
turn contain files of terminal information for all terminals whose names
begin with taht character.  
<!-- }}} -->
<!-- }}} -->

# Basic Shell Programming <!-- {{{ -->
## Shell Scripts and Functions <!-- {{{ -->
Running scripts as `source scriptname` causes the commands in the script
to be read and run as if you typed them in.  
Second way - just type its name and hit RETURN  
If commands aren't in your path, you must type `./scriptname`  
Before you can invoke the shell script by name, you must also give it
"execute" permission. (usually `chmod +x scriptname`)  

More important difference between the two ways of running shell scripts:  

+ **source** causes the commands in the script to be run as if they
  were part of your login session  
+ **just the name** method causes the shell to:  
    + run another copy of the shell (_subshell_)  
    + the subshell then takes commands from the script, runs them, and
  terminates, handing control back to the parent shell  
<!-- }}} -->
## Functions <!-- {{{ -->
You use them to define some shell code by name and store it in the
shell's **_memory_**, to be invoked and run later:  

+ runs faster  
+ organizing long shell scripts into modular "chunks" of code  
+ run in current shell  
+ take precedence over scripts (with same name)  

To define a function, you can use either one of two forms:  
```bash
function functname {
    shell commands
}
# or
functname() {
    shell commands
}
```
You can delete a function definition with the command `unset -f
functname`  

If you want to run function, just type its name followed by any
arguments.  

Find out _**what functions are defined**_ in your
login session - `declare -f`  

**Order of precedence:**  

1. Aliases  
2. Keywords (e.g. _function_, _if_, _for_, etc)  
3. Functions
4. Built-ins like _cd_ and _type_  
5. Scripts and executable programs (from **PATH**)  

If you want to find out a source of command, `type -all/-a` will help you.  

+ `-p` - restrict to executable files or shell scripts  
+ `-P` - forces type to look for executable files or shell scripts  
+ `-f` - suppresses shell function lookup  
+ `-t` - restrict to single word description  

<!-- }}} -->
## Shell Variables <!-- {{{ -->
### Positional Parameters <!-- {{{ -->
_Positional parameters_ hold the command-line arguments to scripts when
they are invoked. Positional parameters have the names
**1**,**2**,**3**, etc (values denoted by **$1**, **$2**, **$3**, etc).
**$0** holds name of the scripts  

Two special variables contain all of the positional parameters (expect
**0**): `*` and `@`.  

+ `"$*"` expands to `"${1}${IFS}${2}${IFS}..."`  
+ `"$@"` expands to `"$1" "$2" "$3"...`  

The variable **#** holds the number of positional parameters  
All of these variables are "read-only".  
<!-- }}} -->
### Positional parameters in functions <!-- {{{ -->
Acting basically the same way as in scripts  
#### Local Variables in Functions <!-- {{{ -->
A **local** statement inside a function definition makes the variables
involved all become _local_ to that function.  
<!-- }}} -->
<!-- }}} -->
### Quoting with $@ and $\* <!-- {{{ -->
For example calling `countargs "$*"` will print **1 args**  
`countargs "$@"` will print **3 args**  
<!-- }}} -->
### More on Variable Syntax <!-- {{{ -->
`$varname` is the same as `${varname}`. Second is used to bring
clarification for bash.  
<!-- }}} -->
<!-- }}} -->
## String Operators <!-- {{{ -->
The _curly-bracket_ syntax allows for the shell's _string operators_. In
particular, string operators let you do the following:  

+ Ensure that variables exist (i.e., are defined and have non-null
  values)  
+ Set default values for variables  
+ Catch errors that result from variables not being set  
+ Remove portions of varialbes' value that match patterns  

Syntax of String Operators<!-- {{{ -->
==========================

Any special characters are inserted between the variable's name and the
right curly bracket. Any argument - to the operator's right.  
<!-- }}} -->
### Existense of variables and substitutions <!-- {{{ -->
+ `${varname:-word}` - if _varname_ exists and isn't null, return its
  value; otherwise return _word_  
+ `${varname:=word}` - if _varname_ exists and isn't null, return its
  value; otherwise set it to _word_ and then return its value.  
+ `${varname:?message}` - if _varname_ exists and isn't null, return its
  value; otherwise print _varname:_ followed by _message_ and abort the
  current command or script  
+ `${varname:+word}` - if _varname_ exists and isn't null, return
  _word_; otherwise return null.  
    Purpose: Testing for the existence of a variable - `${count:+1}`
    returns 1 if **count** is defined.  
+ `${varname:offset:length}` - it returns the substring of $_varname_
  starting at _offset_ and up to _length_ characters. The first
  character in $_varname_ is position 0. If _length_ is ommitted, the
  substring continues to the end of $_varname_. If _offset_ is less than
  0 then the position is taken from the end of $_varname_. If _varname_
  is @, the _length_ is the number of positional parameters starting at
  parameter offset.  
<!-- }}} -->
### Patterns and Pattern Matching <!-- {{{ -->
Patterns are strings that can contain wildcard characters (\*, ?, and []
for character sets and ranges)  

+ `${variable#pattern}` - if pattern matches the **beginning** of the
  variable's value, delete the **shortest** part that matches and return the
  rest.  
+ `${variable##pattern}` - if the pattern matches the **beginning** of the
  varialbe's value, delete the **lognest** part that matches and return
  the rest  
+ `${variable%pattern}` - if the pattern matches the **end** of the
  variable's value, delete the **shortest** part that matches and return the
  rest  
+ `${variable%%pattern}` - if the pattern matches the **end** of the
  variable's value, delete the **longest** part that matches and return the
  rest.  
+ `${varialbe/pattern/string}${variable//pattern/string}` - The
  **longest** match to _pattern_ in _variable_ is replaced by _string_.
    * In the first form, only the first match is replaced. In the second
  form, all matches are replaced.  
    * if the pattern begins with a `#`, it must match at the start of
  the variable. If it begins with a `%`, it must match with the end
  of the variable.  
    * If _variable_ is @ or \*, the operation is applied to each
  positional parameter in turn and the expansion is the resultant
  list.  
<!-- }}} -->
### Length Operator <!-- {{{ -->
`${#varname}` - returns the length of the value of the variable as a
character string  
<!-- }}} -->
### Extended Pattern Matching <!-- {{{ -->
Bash provides a further set of pattern matching operators if the **shopt**
option **extglob** is switched on. Each operator takes one or more
patterns, normally strings, separated by the vertical bar ( | ).  

+ `*(patternlist)` - matches zero or more occurrences of the given
  patterns  
+ `+(patternlist)` - matches one or more occurences of the given
  patterns  
+ `?(patternlist)` - matches zero or one occurences of the give patterns  
+ `@(patternlist)` - matches exactly one of the given patterns  
+ `!(patternlist)` - matches anything except one of the given patterns.  

Patterns can contain shell wildcards and can be nested.  

Example: output all .txt or .md files: `ls -al *(*.txt|*.md)`  
<!-- }}} -->
<!-- }}} -->
## Command Substitution <!-- {{{ -->
Command substitution allows you to use the standard output of a command
as if it were the value of a variable. The syntax is: `$(UNIX command)` (can be nested)  
<!-- }}} -->
## Some examples from `pushd` and `popd` <!-- {{{ -->
If you want to read full paragraph go to page 306  
<!-- }}} -->
<!-- }}} -->
# Flow Control <!-- {{{ -->
Bash supports:  

+ **if/else**  
+ **for**  
+ **while**  
+ **until**  
+ **case**  
+ **select** - allow the user to select one of a list of possibilities
  from a menu  

## if/else <!-- {{{ -->
The **if** construct has the following syntax:  

```bash
if condition
then
    statements
[elif condition
then
    statements...]
[else
    statements]
fi
```

<!-- }}} -->
Exit Status<!-- {{{ -->
===========

Conditions are based on general UNIX concept - _ext status_ of commands  
Every UNIX command returns such. Where 0 is _usually_ the OK exit
status, while anything else (1 to 255) _usually_ denotes an error.  
---  

**if** checks the exit status of the last statement in the list
following the **if**keyword. If status is 0 &rarr; condition evaluates
to true; otherwise - false.  
<!-- }}} -->
Return<!-- {{{ -->
======

`return N` causes the surrounding function to exit with exit status _N_ (defaults to the exit status of the last command).  
<!-- }}} -->
Combinations of Exit Statuses<!-- {{{ -->
=============================

+ `statement1 && statement2` - execute _statement1_, and if its exit
  status is 0, e execute _statement2_.  
+ `statement1 || statement2` - execute _statement1_, and if its exit
  status is _not_ 0, execute _statement2_  
+ `! statement` - return 0 if _statement_ fails, otherwise - 1  
<!-- }}} -->
Condition Tests<!-- {{{ -->
===============

`[[...]]` is just newer version of `[...]`. In first word splitting and
pathname expansion are not performed on the words within the brackets.  

They can also be combined using this syntax:  
```bash
if [ condition ] && [ condition ]; then
# or
if command && [ condition ]; then
```
Also you can negate the truth using preceding exlamation point (**!**).  
Furthermore, you can make complex logical expressions of conditional
operators by grouping them with parentheses (which must be "escaped"
with backslashes), and by using two logical operators: **-a** (AND) and
**-o** (OR). (`-a` and `-o` are working only inside a **test**
conditional expression)  

Example of combining:  
```bash
if [ -n "$dirname" ] && [ \( -d "$dirname" \) -a \( -x "$dirname" \) ]; then
```


<!-- }}} -->
## String Comparisons <!-- {{{ -->
**Operator** - **True if...**  

+ `str1 = str2` - _str1_ matches _str2_  
+ `str1 != str2` - _str1_ does not match _str2_  
+ `str1 < str2` - _str1_ is less than _str2_  
+ `str1 > str2` - _str1_ is greater than _str2_  
+ `-n str1` - _str1_ is not null (length > 0)  
+ `-z str1` - _str1_ is null (length == 0)  
<!-- }}} -->
## File attribute checking <!-- {{{ -->
There are 24 such operators. We will cover those of most general
interest here.  

**Operator** - **True if...**  

+ `-a file` - _file_ exists  
+ `-d file` - _file_ exists and is a directory  
+ `-e file` - same as `-a`  
+ `-f file` - _file_ exists and is a **_regular_** file (i.e., not a
  directory or other special type of file)  
+ `-r file` - you have read permission on _file_  
+ `-s file` - _file_ exists and is not empty  
+ `-w file` - you have write permission on _file_  
+ `-x file` - you have execute permission on _file_, or directory search
  permission if it is a directory.  
+ `-N file` - _file_ was modified since it was last read  
+ `-O file` - you own _file_  
+ `-G file` - _file_'s group ID matches yours (or one of yours)  
+ `file1 -nt file2` - _file1_ is newer(modification time) than _file2_  
+ `file1 -ot file2` - _file1_ is older(modification time) than _file2_  
<!-- }}} -->
Integer Conditionals<!-- {{{ -->
====================

**Test** - **Comparison**  

+ `-lt` - less than  
+ `-le` - less than or equal  
+ `-eq` - equal  
+ `-ge` - greater than or equal  
+ `-gt` - greater than  
+ `-ne` - not equal  
<!-- }}} -->
## for <!-- {{{ -->
The shell's standard **for** loop doesn't
let you specify a number of times to iterate or a range of values over
which to iterate.  

Syntax:
```bash
for name [in list] # defaults to "$@"
do
    statements that can use $name...
done
```

For custom iteration you can do this:
```bash
IFS=:

for dir in $PATH
do
    ls -ld $dir
done
```


<!-- }}} -->
## case <!-- {{{ -->
_bash_'s **case** construct lets you test strings against patterns that
can contain wildcard characters.  
The syntax of **case** is as follows:  
```bash
case expression
    in
    pattern1 )
        statements
        ;;
    pattern2 )
        statements
        ;;
    ...
esac
```
Any of the _patterns_ can actually be several patterns separated by pipe
characters (|).

<!-- }}} -->
## select <!-- {{{ -->
**select** allows you to generate simple menus easily. It has concise
syntax, but it does quite a lot of work. The syntax is:  
```bash
select name [in list]   # default to "$@"
do
    statements that can use $name...
done
```

What **select** does is:  

1. generates a menu of each item in list, formatted with numbers for
   each choice  
2. Prompts the user for a number  
3. Stores the selected choice in the variable name and the selected
   number in the built-in variable **REPLY**  
4. Executes the statements in the body  
5. Repeats the process forver  
    If you want to exit, use `break` statement  

<!-- }}} -->
## while and until <!-- {{{ -->
They both allow a section of code to be run repeatitively while (or
until) a certain condition becomes true.  
Syntax for **while** is:  
```bash
while condition
do
    statements...
done
```
for **until** jsut substitute **until** for **while** in the aboce
example.  

<!-- }}} -->
<!-- }}} -->
# Command-Line Options and Typed Variables <!-- {{{ -->
## Command-Line Options <!-- {{{ -->

shift<!-- {{{ -->
=====

The command `shift` performs the function of:
```
1=$2
2=$3
...
```
you can supply argument to shift that many times over. For example
`shift 3` will do `1=$4 ; 2=$5`  

common example:

```bash
while [ -n "$(echo $1 | grep '-')" ]; do
    case $1 in
        -a ) process option -a
            ;;
        -b ) process option -b
            ;;
        -c ) process option -c
            ;;
        * ) echo 'usage: alice [-a] [-b] [-c] args'
            exit 1
    esac
    shift
done
normal processing of arguments...
```
<!-- }}} -->
Options with Arguments<!-- {{{ -->
======================

```bash
while [ -n "$(echo $1 | grep '-')" ]; do
    case $1 in
        -a ) process option -a
            ;;
        -b ) process option -b
            option=$2       # <--- modified here
            shift
            ;;
        -c ) process option -c
            ;;
        * ) echo 'usage: alice [-a] [-b] [-c] args'
            exit 1
    esac
    shift
done
normal processing of arguments...
```

<!-- }}} -->
getopts<!-- {{{ -->
========

The shell provides a built-in way to deal with multiple comples options
without thse constraints. The built-in command **getopts** can be used
as the condition of the **while** in an option-processing loop.  

`getopts` takes two arguments:

1. string containing letters and colons. Each letter is a valid option.
   If a letter is followed by a colon, the option requires an argument.
2. variable to which **getopts** will assign options.  

As long as there are options left to process, **getopts** will return
exit status 0; when the options are exhausted, it returns exit status 1.  

If the user types an invalid option, **getopts** normally prints an
unfortunate error message and sets **opt** to **?**. But if you begin
the option string with a colon, **getopts** won't print the message.  

If an option has an argument, **getopts** stores it in the variable
**OPTARG**, which can be used in the code that processes the option.  

**OPTIND** - the number of the next argument to be processed. Expression
`shift $(($OPTIND - 1))` shifts all options leaving the "real arguments
as $1, $2, etc"  
<!-- }}} -->
<!-- }}} -->
## Typed Variables <!-- {{{ -->
You can set variable attributes with the `declare` built-in. A `-` turns
the option on, while `+` turns it off.  

| Option | Meaning                                            |
| ---    | ---                                                |
| -a     | The variables are treated as arrays                |
| -f     | Use function names only                            |
| -F     | Display function names without definitions         |
| -i     | the variables are treated as integers              |
| -r     | makes the variables read-only                      |
| -x     | marks the variables for export via the environment |

Equivalent to `declare -r` is `readonly name` - makes variable
name be a type of readonly  

- `-p` prints a list of all read-only names  
- `-a` interprets the name as array  
- `-f` interprets the name as function  

<!-- }}} -->
## Integere Variables and Arithmentic <!-- {{{ -->
### Basic <!-- {{{ -->
The shell interprets words surrounded by `$((` and `))` as arithmetic
expressions.  

Some of the operators contain special characters, there is no need to
backslash-escape them, because they are within the `$((...))` syntax.  

+ `++`, `--` - increment, decrement by one (prefix and postfix)  
+ `+`, `-`, `*`, `/` - sum, sub, multiplication, division (with
  truncation)  
+ `%` - remainder  
+ `**` - exponentiation  
+ `<<`, `>>` - bit-shift left, right  
+ `&`, `|`, `~` - bitwise _and_, _or_, _not_  
+ `^` - bitwise _exclusive or_  
+ `!` - logical _not_  
+ `,` - sequential evaluation  

Parentheses can be used to group subexpressions.  

Relational operators:  

+ `<`, `>` - less/greater than  
+ `<=`, `>=` - less/greater than or equal to  
+ `==` - equal to  
+ `!=` - not equal to  
+ `&&` - logical and  
+ `||` - logical or  

Shell also supports base _N_ numbers, where _N_ can be from 2 to 36. The
notation _B # N_ means "_N_ base _B_".  

<!-- }}} -->
## Arithmetic Conditionals <!-- {{{ -->
Arithmetic conditions can also be tested as strings (in `[[...]]`):  

+ `-lt` - less than  
+ `-gt` - greater than  
+ `-le` - less than or equal to  
+ `-ge` - greater than or equal to  
+ `-eq` - equal to  
+ `-ne` - not equal to  

MOre efficient way of performing an arithmetic test:
by using the `((...))` construct. This returns an exit status of 0 if
the expression is true, and 1 otherwise.  
<!-- }}} -->
## Arithmetic Variables and Assignment <!-- {{{ -->
You can evaluate arithmetic expressions and assign them to variables
with the use of `let`. The syntax is:  
```shell
let intvar=expression
```
It's not necessary to surround expression with `$(())` (it's actually
redundant). There must not be any space on either side of the equal
sign. It is good practive to surround expressions with quotes, since
many characters are treated as special by the shell.  
<!-- }}} -->
## Arithmetic for Loops <!-- {{{ -->
The form of an arithmetic for loop is very similar to those found in
Java and C:
```bash
for (( initialisation ; ending condition ; update ))
do
    statements...
done
```

endless loop:
```bash
for ((;;))
do
    read var
    if [ "$var" = "." ]; then
        break
    fi
done
```


<!-- }}} -->
<!-- }}} -->
## Arrays <!-- {{{ -->
There are several ways to assign values to arrays:  
an array is created automatically by any of the following assignment or
by using `declare -a`  

+ the one straightforward
```bash
names[2]=alice
names[0]=hatter
naems[1]=duchess
```
+ compound assignment:
```bash
names=([2]=alice [0]=hatter [1]=duchess)  
```
+ without indexes (have to reorder elements slightly):
```bash
names=(hatter duchess alice)
```
+ if we provide an index at some point in the _compound_ assignment, the
  values get assigned consecutively from that point on:
```bash
names(hatter [5]=duchess alice) # hatter - 0, duchess - 5, alice - 6
```
An element in an array may be referenced with `${array[i]}`. All
elements are returned with `${array[@]}` or `${array[*]}`. When quoted
first expands to several words, second - to one. Unquoted, expanding to
several words.  

If you want to know what indices currently have values in an array, you
can use `${!array[@]}` (will return array of existing non-empty indices).  

Find length of element in array - `${#array[i]}`, find length of array -
`${#array[@]}` (counts only non-empty elements)  

Reassigning to an existing array with a compound array statement
replaces the old array with the new one.  

Remove element from array - `unset array[i]`, destroy entire array -
`unset array[@]` or `unset array[*]`  

<!-- }}} -->
<!-- }}} -->
# Input/Output and Command-Line Processing <!-- {{{ -->

**I/O redirectors**:  <!-- {{{ -->

+ `cmd1 | cmd2` - pipe; take standard output of _cmd1_ as standard input
  of _cmd2_.  
+ `[n]> file` - direct standard output to _file_  
+ `[n]< file` - take standard input from _file_  
+ `[n]>> file` - direct standard output to _file_; append to _file_ if it
  already exists  
+ `[n]>| file` - force standard output to _file_ even if **noclobber** is
  set.  
+ `<< label` - take standard input and read until line containing only
  _label_  
+ `n>&`, `n<&` - duplicate standard output/input to file descriptor _n_  
+ `n>&m`, `n<&m` - file descriptor _n_ is made to be a copy of the
  output/input file descriptor  
    `comand > out 2>&1` - send standart output to _out_ file and
    standart error to the same place as standart output  
+ `&> file` - directs standard output and standard error to _file_  
+ `[n]<&-`, `[n]>&-` - close the standard input/output  


_[n]_ can be file descriptor  
<!-- }}} -->
File Descriptors<!-- {{{ -->
================

-//- refer to particular streams of data associated with a process. When
a process starts, it usually has three file descriptors open: standart
inpu (0), standard output (1), standard error (2).  
<!-- }}} -->
## String I/O <!-- {{{ -->

echo<!-- {{{ -->
====

`echo` options:  

+ `-e` - turns on the interpretation of backslash-escaped characters  
+ `-E` - turns off the interpretation of backslash-escaped characters  
+ `-n` - omits the final newline  

`echo` escape sequences:  

+ `\a` - ALERT of CTRL-G (bell)  
+ `\b` - BACKSPACE or CTRL-H  
+ `\c` - Omit final NEWLINE  
+ `\e`, `\E` - escape character  
+ `\f` - FORMFEED or CTRL-L  
+ `\n` - NEWLINE or CTRL-J  
+ `\r` - RETURN (ENTER) or CTRL-M  
+ `\t` - TAB or CTRL-I  
+ `\v` - VERTICAL TAB or CTRL-K  
+ `\n` - ASCII character with octal (base-8) value _n_, where _n_ is 1
  to 3 digits  
+ `\0nnn` - the eight-bit character whose value is the octal (base-8)
  value _nnn_ where _nnn_ is 1 to 3 digits  
+ `\xHH` - the eight-bit character whose value is the hexadecimal
  (base-16) value _HH_ (one or two digits)  
+ `\\` - single backslash  
<!-- }}} -->
printf<!-- {{{ -->
======

Same as in C. syntax is `printf format-string [arguments]`  

`printf` format specifiers:  

+ `%c` - ASCII character (prints first character of corresponding
  argument)  
+ `%d`, `%i` - decimal integer  
+ `%e`, `%E` - floating-point format (_[-]d.precisione[+-]dd_, _[-]d.precisionE[+-]dd_)  
+ `%f` - floating point format (_[-]ddd.precision_)  
+ `%g` - `%e` or `%f` conversion, whichever is shorter, with trailing
  zeros removed  
+ `%G` - `%E` or `%f` conversion, whichever is shortest, with trailing
  zeros removed  
+ `%o` - unisgned octal value  
+ `%s` - string  
+ `%u` - unsigned decimal value  
+ `%x` - unsigned hexadecimal number (uses _a-f_)  
+ `%X` - unsigned hexadecimal number (uses _A-F_)  
+ `%%` - literal _%_  

Format expression can take three optional modifiers following _%_ and
preceding the _format specifier_:
```shell
%flags width.precision format-specifier # without spaces in between
```

Examples:
```shell
printf "|%10s|\n" hello     # right-justified
printf "|-%10s|\n" hello    # left-justified
myvar=42.123456
printf "|%*.*G|\n" 5 6 $myvar   # dinamically specify width and precision
> |42.1235|
```

Meaning of presision:  

+ simple num output (not floating) - minimum number of digits to print.
  When the value has fewer digits, it is padded with leading zeros.  
+ `%e`, `%E` - minimum number of digits to print.  
+ `%f` - the number of digits to the right of the decimal point.  
+ `%g`, `%G` - the maximum number of signifiicant digits.  
+ `%s` - the maximum number of characters to print  

**Flags for printf**:  

+ `-` left-justify the formatted value within the field.  
+ `space` - prefix positive values with a space and negative values with
  a minus.  
+ `+` - always prefix numeric values with a sign, even if the value is
  positive.  
+ `#` - use an alternate form  
    - `%o` has a preceding _0_;  
    - `%x`, `%X` are prefixed with _0x_ and _0X_;  
    - `%e`, `%E`, `%f` always have a decimal point in the result;  
    - `%g`, `%G` do not have trailing zeros removed.  
+ `0` - pad output with zeros, not spaces (only for numeric formats)  

**Additional bash printf specifiers**:

+ `%b` - when used instead of `%s`, expands **echo**-style escape
  sequences in the argument string.  
+ `%q` - when used instead of `%s`, prints the string argument in such a
  way that it can be used for shell input.  


<!-- }}} -->
read<!-- {{{ -->
====

_read_ allows you to read values into shell variables. The basic syntax
is:
```bash
read var1 var2...
```
takes line from standart input, depending of the **IFS** splits it on
variables (exceeding words are assigned to last variable). If you omit
the variables altogether, the entire line of input is assegned to the
`REPLY` variable.  

`read` exit status is 1 when there is nothing to read.  

**Options**:  

+ `-a` - read into array  
+ `-d` - delimiter. read a line up until the _first_ character of the delimiter is
  reached  
```bash
$ read -s stop aline
alice duches
$ echo $aline
alice duche
```
+ `-e` can be used only with scripts run from interactive shells. It
  causes _readline_ to be used to gather the input line.  
+ `-n` specifies how many characters will be read by **read**  
+ `-p` followed by a string argument prints the string before reading
  input.  
    useful for prompting: `read -p 'directory? ' REPLY`  
+ `-r` preserves any escape sequences the input might contain  
+ `-s` forces **read** to not echo the characters that are typed to the
  terminal.  
    useful for keybindings: `read -s -n1 key`  
+ `-t` specifies a time in seconds. **read** will wait the specified
  time for input and then finish.  


to redirect file to function the uses `read` you can do one of the
following techniques:  
```bash
findterm() {
    TERM=vt100  # assume this as a default
    like=$(tty)
    while read dev termtype; do
        if [ $dev = $line ]; then
            TERM=$termtype
            echo "TERM set to $TERM."
            break;
        fi
    done
}

findterm < /etc/terms
```
or
```bash
findterm() {
    TERM=vt100  # assume this as a default
    like=$(tty)
    while read dev termtype; do
        if [ $dev = $line ]; then
            TERM=$termtype
            echo "TERM set to $TERM."
            break;
        fi
    done
} < /etc/terms
```
or
```bash
TERM=vt100  # assume this as a default
like=$(tty)
while read dev termtype; do
    if [ $dev = $line ]; then
        TERM=$termtype
        echo "TERM set to $TERM."
        break;
    fi
done < /etc/terms
```
you can use this technique with any flow-control construct.  


<!-- }}} -->
### Command blocks <!-- {{{ -->
The coude surrounded by curly brackets (_{}_) will behave like a
function that has no name. This code will also standard I/O descriptors.  

```bash
{
    TERM=vt100  # assume this as a default
    like=$(tty)
    while read dev termtype; do
        if [ $dev = $line ]; then
            TERM=$termtype
            echo "TERM set to $TERM."
            break;
        fi
    done
} < /etc/terms
```

or in case of creating a standard algebraic notation frontend to the _dc_ command:
```bash
{
    while read like; do
        echo "$(alg2rpn $line)"
    done
} | dc
```

<!-- }}} -->
### Reading user input <!-- {{{ -->
Shell convention dictates that prompts should go to standard _error_,
not standard output.  

You may use `-p "propmt"` option to **read** and redirect it to
stderr (`>&2`).  
<!-- }}} -->
<!-- }}} -->
## Command-Line Processing <!-- {{{ -->
Each line that the shell reads from the standard input or a script
- **_pipeline_** (contains one or more _commands_ separeted by zero or
  more pipe characters (`|`))  

**Steps in command-line processing:**  {{{

1. Splits the command into tokens that are separeted by the fixed set of
   metacharacters: SPACE, TAB, NEWLINE,**:**,**(**, **)**, **<**,
   **>**, **|** and **&**. Types of tokens include words, keywords, I/O
   redirectors and semicolons.  
2. Checks the first token of each command to see if it is a keyword with
   no quotes or backslashes if it's an opening keyword, like
   control-structure openers, **function**, **{**, **(**, then the
   command is actually compound command. The shell sets things up
   internally, reads the next command and starts the process again. If
   the keyword isn't a compund command opener the shell signals a syntax
   error.  
3. Checks the first word of each command against the list of aliases. If
   a match is found, it substitutes the alias's definition and goes back
   to Step 1; otherwise, it goes on to Step 4. This scheme allows
   recursive aliases. Also allows aliases for keywords (`alias
   aslongas=while` or `alias procedure=function`)  
4. Performs brace expansion.  
5. Substitutes the user's home directory for tilde if it is at the
   beginning of a word.  
6. Performs parameter (variable) su bstitution for any expression that
   starts with a dollar sign (**$**).  
7. Does command substitution for any expression of the form `$(string)`  
8. Evaluates arithmetic expressions of the form `$((string))`.  
9. Takes the parts of the line that resulted from paremeter, command,
   and arithmetic substitution and splits them into words again. This
   time depending on $IFS as delimiter instead of the set of
   metacharacters in Step 1.  
10. Performs pathname expansion, a.k.a. wildcard expansion, for any
   occurrences of \*,?, and [] pairs  
11. Uses the first word as a command by looking up its source, i.e., as
   a function command, then as a built-in, then as a file in any of the
   directories in $PATH  
12. Runs the command after setting up I/O redirection and other such
   things.  

Example or command
```shell
ll $(type -path cc) ~alice/.*$(($$%1000))
```

1. `ll $(type -path cc) ~alice/.*$(($$1000))` splits the input into
   words.  
2. `ll` is not a keyword, so Step 2 does nothing.  
3. `ls -l $(type -path cc) ~alice/.*$(($$%1000))` substitutes **ls -l**
   for its alias "ll". The shell then repeats Steps 1 through 3; Step 2
   splits the **ls -l** into two words.  
4. `ls -l $(type -path cc) ~alice/.*$(($$%1000))` does nothing.  
5. `ls -l $(type -path cc) /home/alice/.*$((%1000))` - expands **~alice** into `home/alice`  
6. `ls -l $(type -path cc) /home/alice/.*$((2537%1000))` substitutes **2537** for **$$**.  
7. `ls -l /usr/bin/cc /home/alice/.*$((2537%1000))` does command
   substiturion on "type -path cc".  
8. `ls -l /usr/bin/cc /home/alice/.*537` evaluates the arithmetic
   expression **2537%1000**  
9. `ls -l /usr/bin/cc /home/alice/.*537` does nothing  
10. `ls -l /usr/bin/cc /home/alice/.hist537` substitutes the filename
  for the wildcard expression `.*537`  
11. The command **ls** is found in `/usr/bin`/  
12. `/usr/bin/ls` is run with the option `-l` and the two arguments.  

The are still five ways to _modify_ the process: quoting; using
**command**, **builtin**, or **enable**; and using the adbanced command
**eval**.  
<!-- }}} -->

Quoting<!-- {{{ -->
=======

+ **Single quotes** bypass everything through Step 10 - including
  aliasing.  
+ **Souble quotes** bypass Steps 1 through 4, plus steps 9 and 10. They
  ignore pipe characters, aliases, tilde substitution, wildcard
  expansion, and splitting into words via delimiters inside the double
  quotes. They allow parameter substitution, command substitution, and
  arithmetic expression evaluation.  
<!-- }}} -->
command, builtin, and enable<!-- {{{ -->
============================
+ **command** removes alias and function lookup.  
    - `-p` option guarantees that the command lookup will find all of
  the standard UNIX utilities.  
+ **builtin** looks up only built-in commands, ignoring functions and
  commands found in **PATH**.  
+ **enable** disables built-ins  
    - `-a` displays every built-in  
    - `-d` deletes a bult-in loaded with **-f**  
    - `-f filename` loads a new built-in from the shared-object
  _filename_  
    - `-n` disables a built-in or displays a list of disabled built-ins  
    - `-p` displays a list of all of the built-ins  
    - `-s` restricts the output to POSIX "special" built-ins  
<!-- }}} -->
eval<!-- {{{ -->
====
**eval** lets you go through the process again. It lets you write
scripts that create command strings on the fly and then pass them to the
shell for execution.  

examples:
```shell
eval sort -nr \$1 ${2:+"| head -\$2"}
```
if you have _start_ command that lets you run command in the background
and save output to log file you could run
```shell
eval "$@" > logfile 2>&1 &
```


<!-- }}} -->

<!-- }}} -->

<!-- }}} -->
# Process Handling <!-- {{{ -->
## Process IDs and Job Nubmers <!-- {{{ -->
```shell
$ alice &
[1] 93
```
where `[1]` - job number (assigned by the shell, refer to background
processes that are currently running under your shell), while `93` -
process ID refer to all processes currently running on the entire
system.  
<!-- }}} -->
## Job Control <!-- {{{ -->

Foreground and Background<!-- {{{ -->
=========================
The built-in command **fg** brings a background
job into the foreground. To use pass reference to the job as described
in the underneath table:  

**Options:**  

+ `-l` lists process IDs.  
+ `-p` lists _only_ process IDs (could be useful with command
  substitution)  
+ `-n` lists only those jobs whose status has changed since the shell
  last reported it  
+ `-r` restricts the list to jobs that are running  
+ `-s` restricts the list to jobs that are stopped  
+ `-x` execute a command  
    `jobs -x echo %1` - will print the process ID of _alice_.  

**Ways to refer to background jobs:**  

+ `%N` - job number _N_  
+ `%string` - job whose command begins with _string_  
+ `%?string` - job whose command contains _string_  
+ `%+` - most recently invoked background job  
+ `%%` - same as above  
+ `%-` - second most recently invoked background job  
<!-- }}} -->
Suspending a Job<!-- {{{ -->
================
To suspend a job, type CTRL-Z while it is running.  
If you need the command to finish, but you would also like to control of
your terminal back - you can type `bg`, which moves the job to the
background.  
<!-- }}} -->
### Signals <!-- {{{ -->
A signal is a message that one process sends to another when it wants
the other process to do something.  

To list all signals on your system, by name and number type `kill -l`
(signal names are more portable to other versions of UNIX that signal
numbers)  

Control-Key Signals <!-- {{{ -->
===================
+ Typing CTRL-C make shell to send the INT (for "interrupt") signal to the
current job;  
+ CTRL-Z sends TSTP (on most systems, for "terminal stop").  
+ CTRL-\ sends QUIT signal (stronger version of CTRL-C) use it only when
CTRL-C doesn't work  

There are also "panic" signal called KILL that you can send to a process
when even CTRL-\ doesn't work.  

You can customize the control keys used to send signals with options of
the _stty_ command.  

<!-- }}} -->
kill<!-- {{{ -->
====
**kill** - send signal to any process you created. It takes as an
argument: process iD, job number, or command name of the process. By
default it sends the TERM (terminate) signal ( which usually similar to INT).
`-<SIGNAL>` - send different signal  

How do you should stop programs from running:

+ `kill`  
+ `kill -QUIT`  
+ `kill -KILL`  
<!-- }}} -->
ps<!-- {{{ -->
==
Use this when you need to know the ID of a process. By default lists all
processes started from the current terminal or pseudo-terminal. To get
all processes pass `-a` option  

To output _zombies_ and _orphants_ use `-ax` or `-e`option to `ps`
command  
<!-- }}} -->
<!-- }}} -->
trap<!-- {{{ -->
====
React appropriately to abnormal events.  
Syntax is:
```bash
trab cmd sig1 sig2 ...
```
that is, when any of _sig1_, _sig2_, etc., are received, run _cmd_, then
resume execution.  

By default outputs list of traps that have been set.  

**traps and functions**.  
Traps defined in the invoking shell will be recognized inside the
function, and any traps defined in the function will be recognized by
the invoking shell. (traps can be overwritten)  

### Process ID Variables and Temporary Files <!-- {{{ -->
+ `$$` - process ID of the current shell  
+ `$!` - process ID of the most recent background job  
<!-- }}} -->
### Ignoring Signals <!-- {{{ -->
Signal called HUP (hangup) called when network disconnection occure. You
could write function that ignore that signal. Also there's keyword
`nohup` which does the same.  
<!-- }}} -->
disown<!-- {{{ -->
======
Removes job from list of jobs.  

+ `disown -h` - same os `nohup` command  
+ `disown -a` - disown's all jobs owned by the shell  
+ `disown -r` - same as above but only for currently running jobs  
<!-- }}} -->
### Resetting Traps <!-- {{{ -->
When you pass `-`(dash) as the command argument trap is resetted to
default (usually is termination of the process).  
<!-- }}} -->
<!-- }}} -->
### Coroutines <!-- {{{ -->
Coroutines - two or more processes are explicitly programmed to run
simultaneously and possibly communicate with each other.  

our initial solution would be this:
```bash
alice &
hatter
```

If **alice** is still running when the script finishes, then it becomes
an _orphant_.  

wait<!-- {{{ -->
====
By default `wait` simpy waits until all background jobs have finished.  

If you have specific job you need to wait, you can pass PID as argument
to `wait`.  
<!-- }}} -->
#### Advantages and Disadvantages of Coroutines <!-- {{{ -->
Three characteristics of process:  

+ _CPU-intensive_  
+ _I/O-intensive_  
+ _interactive_  

It's usefull to parallel processes of different type.
But harmfull to parallel same type.  
<!-- }}} -->
#### Parallelization <!-- {{{ -->
Breaking up a process into coroutines is sometimes called _parallelizing_ the job.  

Simple program that parallels copying file to multiple dests:
```bash
for dest in "$@"; do
    cp $file $dest &
done
wait
```
nothing would go wrong. But what if user specifies two same dest's?
Generaly speaking this is _concurrency control_ issues.  

<!-- }}} -->

<!-- }}} -->
<!-- }}} -->
## Subshells <!-- {{{ -->
We saw earlier that when you run a shell script, you actually invoke
another copy of the shell that is a subprocess of the main, or _parent_,
shell process.  

### Subshell Inheritance <!-- {{{ -->
They _inherit_ from their parents:  

+ the current directory  
+ environment variables  
+ standard input, output, error, plus any other open file descriptors  
+ signals that are ignored  

Does not inherit:  

+ shell variables, except environment variables and those defined in the
  environment file (usually _.bashrc_)  
+ Handling of signals that are not ignored  
<!-- }}} -->
### Nested Subshells <!-- {{{ -->
Just surround some shell code with parentheses, and that code will run
in a subshell. That is _nested_ subshell.  
Example:
```bash
( while read line; do
    echo "$(alg2rpn $line)"
    done
) | dc
```
This is usually less efficient than a command block.  
Variable and traps defined inside a command block are known to the shell
code after the block, whereas those defined in a subshell are not.  

<!-- }}} -->
<!-- }}} -->
## Process Substitution <!-- {{{ -->
Two forms:  

+ input to a process: `>(proc)`  
+ output from a process: `<(proc)`  

It actually creates _names pipe_. Or simply a temporary file that acts
like a pipe with a name  

For example, if we want to compare output of two programms:
```bash
cmp <(prog1) <(prog2)
```
_prog1_ and _prog2_ are run concurrently and connect their outputs to
names pipes. _cmp_ reads from each of the pipes and compares the
information.  

<!-- }}} -->
<!-- }}} -->
# Debugging Shell Programs <!-- {{{ -->
The debugger, called _bashdb_, is a basic yet functional program that
will not only serve as an extended example of various shell programming
techniques, but will also provide you with a useful tool for examining
the working of your own shell scripts.  

## Basic Debugging Aids <!-- {{{ -->
Sterps through debugging code:

+ first you decide _what_ is causing your program to behave badly  
+ then _where_ the problem occure  
+ then _how_ to fix it  

First aid is **echo**, but you'll spend a lot of time  

### Set Options <!-- {{{ -->
Debugging options:
`set -o` option - command-line option - action

+ `noexec` - `-n` - don't run commands; check for syntax errors only  
    - note, once you nurned it on, you won't be able to turn it off;
  a `set+o noexec` will never be executed  
+ `verbose` - `-v` - echo commands before running them  
+ `xtrace` - `-x` - echo commands after command-line processing  
    - uses `PS4` variable to mark levels of expanding  
    - `PS4='$0 line $LINENO: '` - good way to set this variable  

<!-- }}} -->
<!-- }}} -->
## Fake Signals <!-- {{{ -->
Fake singlas work in the same way as ordinary do, but they are generated
by the shell itself, as opposed to the other signals which are generated
externally. They represent runtime events that are likely to be of
interest of debuggers.  

List of them:  

+ EXIT - the shell exits from script  
    - will be called whenever the script within which it was set exits  
+ ERR - a command returning a non-zero exit status  
    - `$?` survives trap and accessible at the beginning of the
  trap-handling code  
    - For debugging purposes to pass line number to trap-function:  
    ```bash
    function errtrap {
        es=$?
        echo "ERROR line $1: Command exited with status $es."
    }
    trap 'errtrap $LINENO' ERR
    ```
    - ERR trap is not inherited by shell functions, command
  substitutions, and commands executed in a subshell. To toggle this
  feature use `set -o errtrace` (or `set -E`)  
+ DEBUG - the shell has executed a statement  
    - not inherited in subshells, command substitution, etc. To toggle
  you may either `declare -t` the function or `set -o functrace` (or
  `set -T`)  
+ RETURN - a shell function or script executed with the `.` or `source`
  builtins finishes executing  
    - to turn on ineritence use `declare -t` to define functions and\or
  `set -o functrace` (`set -T`)  

Some debugging features bash 3.0 introduced:  

+ **extdebug** option to the **shopt** command:  
    - `-F` option to **declare** displays the source filename and line
  number  
    - the command that is runned by the DEBUG trap returning a non-zero
  value, the next command is skipped and not executed  
    - if the command run by the DEBUG trap returns a value of 2, and the
  shell is executing in a subroutine (a shell function or a shell
  script by the `.` or `source`), a call to **return** is simulated.  
+ `debugger` option, which switches on both the **extdebug** nad
  **functrace** functionality.  
<!-- }}} -->
## Debugging Variables <!-- {{{ -->
Bash 3.0 added some useful environment variables to facilitate
developing:  

+ BASH_SOURCE - contains an array of filnames that correspond to what is
  currently executing;  
+ BASH_LINENO - an array of line numbers that correspond to function
  calls that have been made;  
+ BASH_ARGC, BASH_ARGV - number of parameters in each frame and
  parameters themselves  
<!-- }}} -->
exec<!-- {{{ -->
====
**exec** takes its arguments as a command line and runs the ocmmand in
place of the current program, in the same process.  
<!-- }}} -->
<!-- }}} -->
# Bash Administration <!-- {{{ -->
Two fields for system administrators maintaining shell:  

+ generic environment for users  
+ for system security  

## Installing bash as the Standard Shell <!-- {{{ -->
Better way to install bash is to install it in any directory, than
simplink `/bin/sh` to it (it'll mimic the Bourne shell as closely as
possible, ignoring `~/.bash_profile` on login and `~/.bashrc` when
interactive).  
<!-- }}} -->
## POSIX Mode <!-- {{{ -->
The POSIX (Portable Operating System Interface) standard defines
guidelines for standardizing UNIX.  
_bash_ is nearly 100% POSIX-compliant in its native mode. It you want
strict POSIX adherence, you can either start _bash_ with the `posix`
option, or set it from within the shell with `set -o posix`  
<!-- }}} -->
## Command-Line Options <!-- {{{ -->
I won't list those. Open man, type `/OPTIONS` and here you are.  
<!-- }}} -->
## Environment Customization <!-- {{{ -->
_bash_ uses the file _/etc/profile_ for system-wide customization and
login. After which he reads *.bash_profile*  

umask<!-- {{{ -->
=====
It lets you specify the default permissions that files have when users
create them.  
Digits in permissions stands from left to right - owner, owner's group,
and all other users. Each digit consists of read, write, execute bits.  

022 is a common **umask** value. This implies that when a file created,
the 'most' permission it could possibly have is 755 - which is the usual
permission of an executable that a compiler might create (which is
common file permissions for file craeted by compiler). A text editor, on
the other hand, might create a file with 666 mermission, but the **umask**
forces it to be 644 isntead.  
<!-- }}} -->
ulimit<!-- {{{ -->
======
Originaly used to specify the limit on file creation size. But _bash_'s
(zsh too) version has options that let you put limits on several
different system resources.  

**Option** - **Resource limited**  

+ `-a` - output all limits  
+ `-c` - core file size ( 1 Kb blocks)  
+ `-d` - process data segment ( Kb )  
+ `-f` - file size (1 Kb blocks )  
+ `-l` - maximum size of a process that can be locked in memory (Kb)  
+ `-m` - maximum resident set size  
+ `-n` - file descriptors  
+ `-p` - pipe size (512 byte blocks)  
+ `-s` - process stack segment (Kb)  
+ `-t` - process CPU time (seconds)  
+ `-u` - maximum number of processes available to a user  
+ `-v` - virtual memory (Kb)  

**ulimit** provides _hard_ and _soft_ limits. Hard could be decreased by
user and only increased by superuser. Whereas soft limits can be
inc/decreased by user as well as _hard_ limits allow this.  

+ `-H` set hard limits  
+ `-S` set soft limits  

Example:
```bash
ulimit -Sn 64
ulimit -Hn unlimited
```

<!-- }}} -->
<!-- }}} -->
## Types of Global Customization <!-- {{{ -->
file _/etc/profile_ contains definitions such as **PATH** and **TERM**.  

The variable **TMOUT** is useful when your system supports dialup lines
and you want to set timeout for prompt.  

Also you can set up global functions.  
<!-- }}} -->
## System Security Features <!-- {{{ -->
_bash_ has two features that help solve security problem:  

+ _restricted shell_ which is intentionally "brain damaged"  
+ _privileged mode_ which is used with shell scripts that run as if the
  user were **root**.  

### Restricted Shell <!-- {{{ -->
It's designed to put the user into an environment where her ability to
move around and write files is severely limited. You can make a user's
login shell restricted by putting **rbash** in the user's /etc/passwd
entry (`git` utility has the same feature, but session restricts only to
manipulate git directory with internal commands).  

Constraints imposed by the restricted shell are disallow the user from
doing the following:  

+ change working directory  
+ redirect output to a file  
+ assigning a new value to the environment variables **ENV**,
__BASH_ENV__, __SHELL__, or **PATH**  
+ specifying any commands with slashes in them  
+ using the **exec** built-in.  
+ specifying a filename containing a / as an argument to the . built-in
  command.  
+ import function definitions from the shell environment at startup  
+ adding or deleting built-in commands  
+ specifying the **-p** option to the bultin command.  
+ turning off restricted mode with **set +r**  
<!-- }}} -->
### A System Break-In Scenario <!-- {{{ -->
<!-- TODO: stopped here -->
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
