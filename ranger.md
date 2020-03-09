# This file describes commands to start use ranger
<!-- 533 line -->
## General configuration <!-- {{{ -->
+ `%ranger/rc.conf` - where all the options are stored  
    * also there are keybindings
+ `%ranger/rifle.conf` - open methods  
+ `%ranger/scope.sh` - preview methods  
<!-- }}} -->
### tags<!-- {{{ -->
`t` - toggle tags  
`"<tagname>` - set tag for selected file  
`ut` - remove any tags of the selection  
<!-- }}} -->
### preview<!-- {{{ -->
__programs to preview__:  

+ _lynx_, _elinks_ - html;  
+ _highlight_ - text/code;  
+ _img2txt_ - for images;  
+ _atool_ - for archives;  
+ _pdftotext_, _mutool_ - for PDFs;  
+ _mediainfo_ - video and audio files;  

`%rangerdir/data/scope.sh` - contains info detailed.  
<!-- }}} -->
### selection<!-- {{{ -->
The **selection** is defined as "All marked files IF THERE ARE ANY,
otherwise the current file."  
Mark files is done by pressing `<Space>`, `v`, etc. __Mrk__ symbol
at the bottom right indicates there are marked files.  
<!-- }}} -->
## Viewing files <!-- {{{ -->
+ show hidden files - `zh`  
<!-- }}} -->
## Macros <!-- {{{ -->
### Abbreviation <!-- {{{ -->
Macros may be used in commands to abbreviate things:  

+ `%f` - the highlighted file  
+ `%d` - the path of the current directory  
+ `%s` - the selected files in the current directory  
+ `%t` - all tagged files in the current directory   
+ `%c` - the full paths of the currently copied/cut files  
+ `%p` - the full paths of selected files  

Macros `%f %d %p %s` have upper case variants which refer to the next
tab.  
To refer to specific tabs, add a number in between %7s - selection of
the seventh tab.  
  
Examples:
+ if you want to diff to files, copy file A (`yy`), 
  move to file B then: `@diff %c %f`  

_**Filename**_ abbreviations:  

+ `%rangerdir` - ranger's python library  
+ `%confdir` - expands to the directory given by _--confdir_  
+ `%datadir` - expands to the directory given by _--datadir_  

Examples: show commands:  
`alias show_commands shell less %rangerdir/config/commands.py`  

+ space - `%space`  
+ % - `%%`  

**Note:** macros are expanded twice when using chain. For example, to
insert a space character in a chained command, you would write `%%space`  
<!-- }}} -->
### Mappings <!-- {{{ -->
When mapping keys you can use the placeholder `<any>`, the key entered
in that position can be used through the `%any` and `%any_path` pacros.  
When using multiple `<any>` placeholders you can index the macros:
`%any0, %any_path0, %any1, %any_path1...`  

+ `%any` - replaced with the key pressed  
+ `%any_path` - will be replaced with the path of the bookmark mapped to
  the key pressed  

Example: pasting of cut/copied files to a bookmarked directory:  
`map p'<any> paste dest=%any_path`  
<!-- }}} -->
<!-- }}} -->
## Bookmarks <!-- {{{ -->
`m<key>` - bookmark current directory, you can re-enter this directory
by typing `` `<key>``  
Typing "\`\`" gets you back to where you were before.  

Note: The bookmarks ' and \` are the same.  
<!-- }}} -->
## Rifle <!-- {{{ -->
Rifle is a file opener of ranger. Rifle can automatically find installed
programs so it can be used effectively out of the box.  
<!-- }}} -->
## Flags <!-- {{{ -->
Flags give you a way to modify the behavior of the spawned process. they
are used in the commands `:open_with` (key "r") and `:shell` (key "!")  

+ `f` fork the process, i.e. run in background.  
+ `c` run the current file only, instead of the selection.  
+ `r` run application with root privilege (requires sude)  
+ `t` run application in a new terminal window  

<!-- TODO: pager???? -->

There are some additional flags that can currently be used only in the
shell command:  

+ `p` redirect output to the pager  
+ `s` silent mode. Output will be discarded  
+ `w` wait for an Enter-press when the process is done  

By default, all the flags are off unless otherwise specified in _rc.conf_ 
key bindings or _rifle.conf_ rules. An uppercase flag negates the effect.  

Examples:  

+ `:open_with c` will open the file that you currently point at.  
+ `:shell -w df` will run "df" and wait for you to press enter before
  switching back to ranger.  

<!-- }}} -->
## Plugins <!-- {{{ -->
Plugins are python files which are located in `~/.config/ranger/plugins/`
and are imported in alphabetical order when startin g ranger.  

Adding new commands via a plugin as simple as specifying them like you
would do in the _commands.py_.  

There are some hooks that are specifically made for the use in plugins.
They are functions that start with *hook\_* and can be found throughout
the code.  
``grep 'def hook_' -r /path/to/rangers/source``  
Also try:  
`pydoc ranger.api`  
There are several sample plugins in the `/usr/share/doc/ranger/examples/`
directory, including a hello-world plugin
that describes this procedure.  
<!-- }}} -->
## Key bindings <!-- {{{ -->
Key bindings are defined in the `%rangerdir/config/rc.conf`. You can
copyt it to your local configuration directory with the
`--copy-config=rc`.  

Many key bindings take an additional numeric argument.  

+ `5j` - move down 5 lines  
+ `2l` - open a file in mode 2  
+ `10<space>` - to mark 10 files  

### Main bindings <!-- {{{ -->
<!-- line 441 man page -->

**Basic movement**  

+ `h`, `j`, `k`, `l` - move left, down, up or right  
+ `^D` or `J`, `^U` or `K` - move a half page down, up  
+ `H`, `L` - move back and forward in the history  
+ `gg`, `G` - move to the top, bottom  
+ `[`, `]` - move up and down in the parent directory  
+ `^R` - **reload** everything
+ `mX` - create a **bookmark** with the name _X_  
+ ```X`` - move to the **bookmark** with the name _X_  
+ `n` - find next file. By default, this gets you to the **newest file** in
  the directory.  
+ `N` - find the previous file  
+ `f` - quickly navigate by entering a part of the filename  

**Performance**  

+ `F` - toggle **freeze\_files** setting. When active, directories and
  files will not be loaded, improving performance. (preview can be
  toggled with `zI`, preview of directories toggled with `zP`)  
+ `i` - inspect the current file in a bigger window  
+ `E` - edit the current file in $VISUAL otherwise $EDITOR otherwise
  "vim"  
+ `S` - open a shell in the current directory  
+ `W` - opens the log window
+ `w` - opens the task window where you can view and modify background
  processes that currently run in ranger  
    * in there you can type `dd` to abour process  
    * `J` or `K` to change the priorit y of a process.  
+ `^C` - stop the currently running background process that ranger has
  started  
+ `oX` - change the **sort method**  
+ `u?` - universal **undo-key**  
    * `uq` restores closed tabs  
    * `ud` clears the copy/cut buffer  
    * `uV` starts the reversed visual move  
    * `uv` **clears the selection**  
+ `^B` - fzf search  

**Basic file manipulation**  

+ `yy` - **copy** the selection (same as Ctrl+C in GUI)  
    * `ya` to add files to the copy buffer  
    * `yr` to remove files again  
    * `yt` for toggling  
+ `dd` - **cut** the selection (same as Ctrl+X in GUI)  
    * `da`, `dr`, and `dt` equivalent to _yy_ section  
+ `pp` - **past** the files which were previously copied or cut (same as
  Ctrl+V in GUI). (conflicts are solved by appending an _ and index if
  necessary)  
    * `po` - past files, overwriting existing files.  
    * `pP`, `pO` - like _pp_ and _po_, but queues the operation so that
  it will be executed after any other operations.  
    * `pl`, `pL` - create syblinks (absolute or relative) to the copied
  files  
    * `phl` - create hardlinks to the copied files  

+ `Space` - mark a file.  
+ `v` - toggle the mark-status of all files  
+ `V` - starts the visual mode.
+ `/` - search for files in the current directory  

**Console**  

+ `:` - open the console  
+ `!` - open the console with the content "shell "  
+ `@` open the console with the content "shell %s", placing the
cursor before the %s so you can quickly run commands with the
current selection as the argument  
+ `r` - open the console with the content "open with " so you can
decide which program to use to open current file selection  
+ `cd` - open the console with the content "cd "  
+ `^P` - open the console with the most recent command.  

**Tabs**  

+ `Alt-N` - N in [0,9] **_open_** a _tab_. If doesn't exist yet, it will be
  created  
+ `Alt-l`, `Alt-r` - **_shift_** a _tab_ left/right  
+ `gn` - **_create_** new tab  
+ `gt`, `gT` - go to **_next/previous_** _tab_ (you may use TAB and Shift+TAB)  
+ `gc` - **_close_** the current _tab_

**Help**  

+ `zX` - change settings. See the settings section for a list of
  settings and their hotkey  
+ `?` - opens this man page

**Filters**  
<!-- more on filters on line 600 man page -->

+ `.d` - apply typefilter **"directory"**  
+ `.f` - apply typefilter **"file"**  
+ `.l` - apply the typefilter **"limlink"**  
+ `.p` - pop the topmost filter from stack  
+ `.c` - clear the filter stack  

+ `M` change line mode (info displaying on same line with filename)  
<!-- }}} -->
<!-- }}} -->
## Settings <!-- {{{ -->
Settings can be changed in the file `~/.config/ranger/rc.conf`  
or using command `:set option value`.  
<!-- }}} -->
