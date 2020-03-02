
# Where to read<!-- {{{ -->
+ [git-scm](https://git-scm.com/docs/gittutorial)  
<!-- }}} -->
# About Version Control<!-- {{{ -->
Version control is a system that records changes to a file or set of
files so that you can recall specific versions later.  
<!-- }}} -->
# The Three States<!-- {{{ -->
Those are:  

+ _modified_ - you have changed the file, but have not committed it to
  your database yet.  
+ _staged_ - you have marked modified file in its current version to go
  into your next commit snapshot.  
+ _committed_ - means that the data is safely stored in your local
  database.  

This leads us to the three main sections of a Git project: 

+ Working tree - files are pulled out of the compressed database in the Git 
directory and placed on disk for you to use or modify.  
+ Staging area - file that stores information about what will go into 
your next commit. Its technical name in Git parlance is the "index"  
+ Git directory (.git directory / repository) - where Git stores the
metadata and object database for your project.  

The basic Git workflow goes something like this:  

1. You modify files in your working tree.  
2. You selectively stage just those changes you want to be part of your
   next commit, which adds _only_ those changes to the staging area.  
3. You do a commit , which takes the files as they are in the stagin
   area and stores that snapshot permanently to your Git directory.  
<!-- }}} -->
# First-Time Git Setup <!-- {{{ -->
## Configuration <!-- {{{ -->
`git config` lets you get and set configuration variables. These
variables can be stored in three different places:  

1. `/etc/gitconfig` - contains values applied to every user on the
   system and all their repositories. To modify pass `--system` option
   to `git config`.  
2. `~/.gitconfig` or `~/.config/git/config` - values specific for you.
   To read and modify pass `--global` option.  
3. `config` file in the Git directory. Values are local to repository.
   To read and modify pass `--local` option.  

Each level overrides values in the previous level, so values in
`.git/config` trump those in `/etc/gitconfig`  

You can view **_all of your settings_** and where they are coming from
using:  
```shell
git config --list --show-origin
```
You can also check specific value by typing: `git config <key>`:  
```shell
$ git config user.name
John Doe
```
<!-- }}} -->
## Your Identity <!-- {{{ -->
The first thing is to set your user name and email address. This is
important because every Git commit uses this information:  
```shell
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
<!-- }}} -->
## Your Editor <!-- {{{ -->
You can configure the default text editor that will be used when Git
needs  you to type in a message:  
```shell
$ git config --global core.editor vim
```

<!-- }}} -->
## Getting Help <!-- {{{ -->
```shell
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

If you don't need the full-blown manpage:  
```shell
git <verb> -h
```
<!-- }}} -->
<!-- }}} -->
# Git basics <!-- {{{ -->
## Getting a Git Repository <!-- {{{ -->
### Initializing a Repository in an Existing Directory <!-- {{{ -->
`cd` into working directory and type `$ git init`. This will create
_.git_ subdirectory containing all of your necessaryt repository files.  

If you want to start version-controlling existing files, you should
probably begin tracking those files and do an initial commit:  
```shell
$ git add *.c
$ git add LICENSE
$ git commit -m 'initial project version'
```
<!-- }}} -->
### Cloning an Existing Repository <!-- {{{ -->
You clone a repository with `git clone <url>`. For example, if you want
to clone the Git linkable library called `libgit2`, you can do so like
this:  
```shell
$ git clone https://github.com/libgit2/libgit2
```
That creates a directory names `libgit2`, initializes a _.git_ directory
inside it, pulls down all the data for repository, and checks out a
working copy of the lates version.  

To specify other directory name, use additional argument:  
```shell
$ git clone https://github.com/libgit2/libgit2 mylibgit
```

Git has a number of different transfer protocols you can use. Examples
above use HTTPS protocol, buy you may also see `git://` or
`user@server:path/to/repo.git` which uses the SSH transfer protocol.  
<!-- }}} -->
<!-- }}} -->
## Recording Changes to the Repository <!-- {{{ -->
Typically, you'll want to start making changes and committing snapshots
of those changes into your repository each time the project reaches a
state you want to record.  
<!-- }}} -->
<!-- }}} -->
