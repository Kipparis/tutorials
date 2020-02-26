# This file describes commands to start use ranger
<!-- 327 line -->
## General configuration <!-- {{{ -->
+ `%ranger/rc.conf` - where all the options are stored  
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

