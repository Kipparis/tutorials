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
+ builtin - tells the shell to use the built-in command and ignore any
  function of than name
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
<!-- TODO: stopped here -->
<!-- }}} -->
<!-- }}} -->
