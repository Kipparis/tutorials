# Options<!-- {{{ -->
+ `:set xxx` - sets the option "xxx"  
+ `:set xxx?` - displays value of "xxx"  

Echo options: `:echo &textwidth`  
Use options as variables:  
```
:let &textwidth = 100
:set textwidth?
:let &textwidth = &textwidth + 10
:set textwidth?
```
<!-- }}} -->
# Registers <!-- {{{ -->
+ echoing them  
    `:echo @<register_name>`
+ set register  
    `:let @a = "hello!"`  
+ register with `yank`  
    `:echo @"`  
+ register after search with its content  
    `:echo @/`  
<!-- }}} -->
# Movement <!-- {{{ -->
## Cursor history position<!-- {{{ -->
+ `C+o` - go to previous position - helpful when got to definition or something else  
+ `C+i` - got to newer position  
<!-- }}} -->
## Position in file<!-- {{{ -->
+ `G`   - end of file  
+ `gg`  - start of file  
<!-- }}} -->
## Search<!-- {{{ -->
+ `/` - start search
    useful to define mapping to turn off highlight of search (after you
    see it)  
+ `/ignore\c` or `/\c` - ignore case for that search  
+ `n` - search forward  
+ `N` - search backward  
<!-- }}} -->
<!-- }}} -->
# Vim windows <!-- {{{ -->
+ `C+w` + `C+w` - move btw windows  
## Buffers <!-- {{{ -->
### Split <!-- {{{ -->
+ `:buffers` - view list of buffers  
+ `:vsp | b<number>` - open buffer as split  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Selecting <!-- {{{ -->
+ `v` - visual mode  
+ `C+v` - block visual mode  
+ `V` - select lines  
<!-- }}} -->
# Mappings <!-- {{{ -->
`:verbose imap <Tab>` -- see which plugin is overriding your map  

+ `:execute "write"` replaces `<cr>`, other special characters  
  same as `:write<cr>`  
+ `:execute "normal! gg"`  
  same as: type `gg` in normal mode  
<!-- }}} -->
# Useful things <!-- {{{ -->
+ `:so %` - source current file  
+ `gx` - open link under cursor  
<!-- }}} -->
# Where to read <!-- {{{ -->
+ vimtutor  
+ `:help user-manual`  
+ book - Vim- Vi IMproved - by Steve Oulline  
+ how to build vimrc - `:help vimrc-intro`  
+ book - learn vim hardway  
<!-- }}} -->
# Pluggins <!-- {{{ -->
## Ultisnips <!-- {{{ -->
+ `:UltiSnipsEdit` - edit snippets for this particular filetype  
+ `:tabedit ~/.vim/Ultisnips/all.snippets` - edit snippets file for all
  filetypes  
+ `:help UltiSnips<tab>` - search for all available help pages  

### Snippet syntax <!-- {{{ -->
```
snippet _name_ "_description_" _options_
_what are typed_
endsnippet
```

options - `:h UltiSnips-snippet-options`. Most commonly used:

+ `i` - allow snippet to expand everywhere

Placeholders:  

+ `${1:default_value}`  
+ `$0` - where you will at the end  
<!-- }}} -->
<!-- }}} -->
## Vim-fugitive <!-- {{{ -->
+ `:G` `:Gstatus` - git status  
+ `:Gedit` - view any blob, tree,
commit, or tag (`:Gsplit`, `:Gvsplit`,`:Gtbedit`)  
+ `:Gdiffsplit` - bring up the staged vesion of the file side by side
with the working tree version and use Vim's diff handling
capabilities to stage a subset of the file's changes
+ `:Gcommit`  
+ `:Gmerge`  
+ `:Grebase`  
+ `:Gpush`  
+ `:Gfetch`  
+ `:Gpull`  
+ `:Gblame`  
+ `:Gmove`   
+ `:Gdelete`  
+ `:Ggrep` - search the work tree (or any arbitrary commit)  
+ `:Glog` - loads all previous revisions of a file into the quickfix
list  
+ `:Gread` == git checkout -- filename that operates on the buffer  
+ `:Gwrite` == git add when called from work tree file and
== git checkout when caled from the index or blob in hist
+ `:Git` for running any arbitrary command  
+ `:Git!` to pen the output of a command in a temp file  
<!-- }}} -->
## Vim-gitgutter <!-- {{{ -->
_for operating on hunks of code in file pushing to git._  

+ `[c,]c` - move between hunks  
+ `<leader>hp` - preview  
+ `<leader>hs` - stage  
+ `<leader>hu` - undo  

+ `ic` - operates on all lines in the current hunk  
+ `ac` - --//-- and trailing empty lines  

+ `zr` - to unfold 3 lines above and below a hunk  
    or GitGutterFold

+ `:GitGutterLineHighlightsToggle` - toggle line highligning  
+ `g:gitgutter_preview_win_location` - location of the preview window  
<!-- }}} -->
## gv.vim <!-- {{{ -->
_primary operating on commit history of git in general_  

+ `:GV` - open commit browser  
    pass git log options to the command, e.g. `:GV -S foobar`  
+ `:GV!` - only list commits that affected the current file  
+ `:GV?` - fills the locations list with the revisions of the current
  file  

NOTE: `:GV` or `:GV?` used in visual mode to track the changes in the
selected lines  

In commit mode (via `:GV`):  

+ `o` - on commit to display content  
+ `o` - on commits to display the diff in the range  
+ `O` - opens a new tab instead  
+ `gv` == `:Gbrowse`  
+ `]]`, `[[` to move between commits  
+ `.` - start command-line with :Git [CURSOR] SHA a la fugitive  
+ `q` - close  
<!-- }}} -->
## Vimagit <!-- {{{ -->
_easy way to stage hunks of code in several files_  

+ `:Magit` - opens magit  
+ `C+n` - jump to next hunk  
+ `S` - stage or unstage hunk  
+ `CC` - commit; then in normal mode `cc` or `:w`  
<!-- }}} -->
## Nerd Tree <!-- {{{ -->
+ `<F2>` focus on nerd tree  
+ `<C-w-w>` focus on vim  
+ `gt` next tab  
+ `gT` previous tab  
+ `m`  add child  

Mappings:  

+ `C+t` - open tree  
+ `S+t` - open file in new tab  
<!-- }}} -->
## Tcomment <!-- {{{ -->
+ `:gc` comment  
+ `:g<`  
+ `:g>`  

Mappings:  

+ `gc` or `gcc` (for line) - comment/comment selected region  
<!-- }}} -->
## Narrow Region <!-- {{{ -->
_operating on part of code and upply changes on exit_  

+ `:NR` create new region from selected  
<!-- }}} -->
## Easy allign <!-- {{{ -->
`[v,ga]ip[ga,][number of occurences]<symbol>[start]`
Visual select Inner Paragraph $rarr; start easyalign command (ga)
Start EasyAlign command (ga) for Inner Paragraph

Examples:  

+ `ga<symbol>` - allign by symbol  
<!-- }}} -->
## fzf <!-- {{{ -->
+ `:Files` - opens file manager  
+ `<C-t>`, `<C-x>`, `<C-v>` - opens in new tab \ split \ vertical split  
<!-- }}} -->
<!-- }}} -->
# Programming <!-- {{{ -->

+ `<c-w>gf` - open file under cursor in new tab  
+ `<c-w>f` - open file under cursor in split  
+ `<c-d>` - go to definition  
+ `<c-e>` - go to declaration  
+ `<c-o>` - go to documentation  

+ `<c-s>` - move split to tab  
+ `S` - merge next and current tabs  

## Window moving <!-- {{{ -->
`:help window-moving`:  

+ `<c-w>L` - move window to the right  
+ `<c-w>H` - move window to the left  
+ `<c-w>J` - move window to the bottom  
+ `<c-w>K` - move window to the top  
<!-- }}} -->

<!-- }}} -->
# Git <!-- {{{ -->
For more info `tpope/vim-fugitive`  

+ `<leader>gd` - opens 3 way merging  
+ `gdh` - accept chank from target (left window)  
+ `gdl` - accept chank from merge branch (right window)  
+ `]c`, `[c` - go to next \ previous chank respectively  

<!-- }}} -->

<!-- TODO: search for this -->{{{
<!-- mappings { -->
<!--   C+d - go to definition -->
<!--  -->
<!--  -->
<!--   C+p - search for something -->
<!-- } -->
<!-- }}} -->
