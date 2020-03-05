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

<!-- }}} -->
<!-- }}} -->
