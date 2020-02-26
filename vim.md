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
## Options<!-- {{{ -->
+ `:set xxx` - sets the option "xxx"  
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

<!-- }}} -->
<!-- }}} -->

    vim-fugitive {
      :G :Gstatus - git status
      :Gedit - view any blob, tree, commit, or tag (:Gsplit, :Gvsplit,
                                                    :Gtbedit)
      :Gdiffsplit - bring up the staged vesion of the file side by side
        with the working tree version and use Vim's diff handling
        capabilities to stage a subset of the file's changes
      )
      :Gcommit
      :Gmerge
      :Grebase
      :Gpush
      :Gfetch
      :Gpull
      :Gblame
      :Gmove 
      :Gdelete
      :Ggrep - search the work tree (or any arbitrary commit)
      :Glog - loads all previous revisions of a file into the quickfix
        list
      :Gread == git checkout -- filename that operates on the buffer 
      :Gwrite == git add when called from work tree file and
              == git checkout when caled from the index or blob in hist

      :Git for running any arbitrary command
      :Git! to pen the output of a command in a temp file

      g? - list of mappings
    }

    vim-gitgutter {
      [c,]c - move between hunks
      <leader>hp - preview
      <leader>hs - stage
      <leader>hu - undo

      ic - operates on all lines in the current hunk
      ac - --//-- and trailing empty lines

      zr - to unfold 3 lines above and below a hunk
      or GitGutterFold

      :GitGutterLineHighlightsToggle - toggle line highligning
      
      g:gitgutter_preview_win_location - location of the preview window
    }

    gv.vim {
      :GV - open commit browser
        pass git log oprions to the command, e.g. :GV -S foobar
      :GV! - only list commits that affected the current file
      :GV? - fills the locations list with the revisions of the current
              file
      :GV or :GV? used in visual mode to track the changes in the
              selected lines

      o - on commit to display content
      o - on commits to display the diff in the range
      O - opens a new tab instead
      gv == :Gbrowse
      ]], [[ to move between commits
      . - start command-line with :Git [CURSOR] SHA a la fugitive
      q - close
    }

    vimagit {
      :Magit - opens magit
      C+n - jump to next hunk
      S - stage or unstage hunk 
      CC - commit; then in normal mode "cc" or ":w"
    }

    Nerd Tree {
      <F2> focus on nerd tree
      <C-w-w> focus on vim
      gt next tab
      gT previous tab
      m  - add child
    }

    tcomment {
      :gc comment
      :g<
      :g>
    }

    make buffer region {
      :NR
    }

    allign {
      [v,ga]ip[ga,][number of occurences]<symbol>[start]
        Visual select Inner Paragraph => start easyalign command (ga)
        Start UasyAlign command (ga) for Inner Paragraph
    }
  }
}}}}

$$$$ Generic notes $$$$ {{{
    > echo options
:echo &textwidth
    > use options as variables
:let &textwidth = 100
:set textwidth?
:let &textwidth = &textwidth + 10
:set textwidth?
}}}
$$$$ Command Notes $$$${{{
:execute "write"
    :write<cr>;
    also replaces <cr>, other special characters;
:execute "normal! gg"
    type gg in normal mode

$ Registers ${{{
    > echoing them
:echo @<register_name>
    > set register
:let @a = "hello!"
    > register with `yank`
:echo @"
    > register after search with its content
:echo @/
}}}}}}
$$$$ Create Mappings $$$$

mappings {
  gc or gcc (for line)
  ga<symbol> - allign by symbol
  C+d - go to definition

  C+t - open tree
  S+t - open file in new tab

  C+p - search for something
}

