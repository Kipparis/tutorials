# sources

+ [tmux-and-vim](https://www.bugsnag.com/blog/tmux-and-vim): good source file  
+ [Starefossen github](https://github.com/Starefossen/dotfiles/blob/master/.tmux.conf): good source file  

# commands

b4 all commands `<C-a>`  

## pane

+ `%`: open pane horizontally  
+ `"`: open pane vertically  
+ `;`: move to previous active pane  
+ `o`: next pane in the current window  
+ `x`: kill current pane  

+ `{`: swap current pane with the previous pane  
+ `}`: swap current pane with the next pane  

+ `{arrows}`: change to the pane above/below, to the left/right  

+ `{C-arrows}`: resize the current pane  

## window
+ `c`: create new window  
+ `[0..9]`: select window
+ `l`: move to previously selected window  
+ `n`: change to the next window  
+ `f`: search for text in open windows  

+ `&`: kill the current window  

+ `$`: kill the current session  

# locations
plugins are installed to `~/.tmux/plugins`  
