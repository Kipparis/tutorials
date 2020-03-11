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

<!-- }}} -->

<!-- }}} -->
