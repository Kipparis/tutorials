# This file describes commands to start use ranger
<!-- 336 line -->
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

<!-- }}} -->
<!-- }}} -->
