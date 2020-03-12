# Where to read<!-- {{{ -->
+ [git-scm](https://git-scm.com/docs/gittutorial)  
+ book: pro-git  
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

+ **_Tracked_** files are files that were in the last snapshot;  
+ **_Untracked_** files are everything else - anyu files in your working
  directory that were not in your last snapshot and are not in your
  staging area;  

### Checking the Status of Your files <!-- {{{ -->
The main tool you use to determine which files are in which stat is the
`git status` command.  
It shows:  

+ untracked files;  
+ which tracked files are modified;  
+ which branch you are on;  
+ informs you if it has diverged from the same branch on server;  

**_Untracked_** basically means that Git sees a file you didn't have in
the previous snapshot (commit);  
<!-- }}} -->
### Tracking New Files <!-- {{{ -->
In order to begin tracking a new file, you use the command `git add`.  
To begin tracking the _README_ file, you can run this:  
```shell
$ git add README
```
You can pass as argument either a file or a directory; if it's a
directory, the command adds all the files in that directory recursively.  
<!-- }}} -->
### Staging Modified Files <!-- {{{ -->
Use `git add`  
Git commit contains only staged file snapshots.  
<!-- }}} -->
### Short Status <!-- {{{ -->
`git status -s` or `git status --short` will show far more simplified
output  
```shell
$ git status -s
 M README
MM Rakefile
A  lib/git.rb
M  lib/simplegit.rb
?? LICENSE.txt
```

+ Files aren't tracked have a `??` next to them;  
+ New files that have been added to the staging area have an `A`;  
+ Modified files have an `M`;  

There are trwo columns to the output:  

+ left-hand column indicates the status of the staging area;  
+ right-hand column indicates the status of the working tree;  

So in example above: _README_ file is modified in the working directory
but not yet staged, while the _lib/simplegit.rb_ file is modified and
staged. The _Rakefile_ was modified, staged and then modified again, so
there are changes to it that are both staged and unstaged.  

**Help.** `man git-status` after that you may search for `Short Format`  
<!-- }}} -->
### Ignoring Files <!-- {{{ -->
Often, you'll have a class of files that you don't want Git to
automatically add or even show you as being untracked. In such cases,
you can create a file listing patterns to match them named `.gitignore`.
Here is example:  
```shell
$ cat .gitignore
*.[oa]
*~
```

1. Ignore files ending in ".o" or ".a";  
2. Ignore files ending with a tilde;  

Rules for the patterns you can put in the _.gitignore_file are as
follows:  

+ blank likes or lines tarting with **_#_** are ignored;  
+ standard glob patterns work, and will be applied recursively
  throughout the entire working tree;  
    * you can use two asterisks to match nested directories
    `a/**/z` would match `a/z`, `a/b/z`, `a/b/c/z` and so on.  
+ you can start patterns with a forward slash(**/**) to avooid recursivity;  
+ you can end patterns with a forward slash (**/**) to specify a
  directory;  
+ you can negate a pattern by starting it with an exclamation point (**!**);  

Here is another example _.gitignore_ file:  
```txt
# ignore all .a files
*a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its
# subdirectories
doc/**/*.pdf
```

Note: in the simple case, a repository might have a single _.gitignore_
file. However it's possible to have additional _.gitignore_ files in
subdirectories. The rules in these nested files apply only to the files
under the directory where they are located.  
<!-- }}} -->
### Viewing Your Staged and Unstaged Changes <!-- {{{ -->
+ What have you changed but not yet staged?  
+ What have you staged that you are about to commt?  

`git status` answers this questions very generally  
`git diff` shows you the exact lines added and removed - _the patch_ as
it were  

Let's say you edit and stage the `README` file, and then edit the
`CONTRIBUTING.md` file without staging it.  

Then `git diff` will compare you working directory with what is in your
staging area.  
If you want to see what you've **_staged_** what will go into your next
commit, you can use `git diff --staged` or `git diff -cached`
(compares your staged changes to your last commit)  

Run `git difftool --tool-help` to see what **_tools_** are available on your
system.  
<!-- }}} -->
### Commiting Your Changes <!-- {{{ -->
`git commit` launches your editor of choice. (It uses EDITOR environment
variable or can be configured using `git config --global core.editor`
command)  

By default in commit message will contain the most recent output of `git
status`, you can include more detailed information by using `-v` option.
It will also include `diff` of your change.  

When you **_exit_** the editor, Git creates your commit with that commit
message (with the comments and diff stipped out).  

You can pass commit message inline using `-m` flag, like this:  
`$ git commit -m "Story 182: fix menchmarks for speed"`  

<!-- }}} -->
### Skipping the Staging Area <!-- {{{ -->
Adding the `-a` option to the `git commit` stages every file that is
already tracked before doing the commit.  
_but be careful; sometimes this flag will cause you to include unwanted
changes._  
<!-- }}} -->
### Removing Files <!-- {{{ -->
To remove a file from Git, you have to remove it from your tracked files
(e.g. remove from your stagin area &rarr; commit). The `git rm` command
does that (and also removes the file from your working directory).  

If you **_modified_** or **_staged_** the file, you must force the
removal with the `-f` option.  

If you want to remove only from **_staging_** area, and keep in your
working tree, use `git rm --cached`  

You can pass _files_, _directories_, and _file-glob_ patterns to the
`git rm` command. (you have to precede _file-glob symbols_ with the
backslash (\\) because git has its own filename expansion)  
<!-- }}} -->
### Moving Files <!-- {{{ -->
If you want to rename a file in Git, you can run something like:  
`$ git mv file_from file_to`  
above equivalent to:  
```shell
$ mv README.md README
$ git rm README.md
$ git add REAMDE
```

<!-- }}} -->
### Viewing the Commit History <!-- {{{ -->
To see what have commited you may use `git log` command.  

A huge number and variety of options to the `git log` command are
available. Here are the most popular:  

+ `-p` or `--patch` - shows the difference (the _patch_ output)
  introduced in each commit. You can limit the number of log entries
  displayed using `-<number>`.  
+ `--stat` - see some abbreviated stats for each commit (such as what
  file changed, how many insertions/deletions)  
+ `--pretty` - changes the log output to formats other than default  
    * `oneline` option prints each commit on single line  
    * `short`, `full`, `fuller` - show output in roughly the same format
  but with less or more information.  
    `$ git log --pretty=oneline`  
    * `format` allows you to specify your own log output format  
    `$ git log --pretty=format:"%h - %an, %ar : %s"`  

Useful options for `git log --pretty=format`:  

| Option | Description of Output                           |
| ---    | ---                                             |
| `%H`   | Commit hash                                     |
| `%h`   | Abbreviated commit hash                         |
| `%T`   | Tree hash                                       |
| `%t`   | Abbreviated tree hash                           |
| `%P`   | Parent hashes                                   |
| `%p`   | Abbreviated parent hashes                       |
| `%an`  | Author name                                     |
| `%ae`  | Author email                                    |
| `%ad`  | Author date (format respects the --date=option) |
| `%ar`  | Author date, relative                           |
| `%cn`  | Commiter name                                   |
| `%ce`  | Commiter email                                  |
| `%cd`  | Commiter date                                   |
| `%cr`  | Commiter date, relative                         |
| `%s`   | Subject                                         |

What the difference is between _author_ and _committer_? Author is the
person who originally wrote the work. Commiter is the person who last
applied the work ( one of the core members for example ).  

The `oneline`and `format` options are particularly useful with option
`--graph`. This option adds a nice litle ASCII graph showing your branch
and merge history.  

_Common options to_ `git log`:  

| Option            | Description                                             |
| ---               | ---                                                     |
| `-p`              | Show the patch introduced with each commit              |
| `--stat`          | Show statistics for files modified in each commit       |
| `--shorstat`      | Display only the changed/insertions/deletions line      |
| `--name-only`     | Show the list of files modified after the commit        |
| `--name-status`   | Show the list of file afffected with added/mod/del      |
| `--abbrev-commit` | Show only the first few char of the SHA-1               |
| `--relative-date` | Display the date in a relative format ("2 weeks ago")   |
| `--graph`         | Display an ASCII graph of the branch and meerge history |
| `--pretty`        | Show commits in an alternate format                     |
| `--oneline`       | Shorthand for `--pretty=oneline --abbrev-commit`        |

<!-- stopped here -->
<!-- }}} -->
### Limiting Log Output <!-- {{{ -->
+ `-<n>` - where `n` is any integer to show the last `n` commits  

You may use options such as `--since` and `--until`.  
`$ git log --since=2.weeks`  
This command workds with lots of formats - you can specify a specific
date like "2008-01-15" or a relative date "2 years 1 day 3 minutes ago".  

+ `--author` option allows you to filter on a specific author  
+ `--committer` option allows you to filter on a specific commiter  
+ `--grep` option lets you search for keywords in the commit messages  
    You can specify more than one instance of both the `--author` and
    `--grep` search criteria, which will display commits that match _any_ of the patterns
    however, adding the `--all-match` option output those commits
    matching _all_ search criterias.  
+ `-S` takes a string and shows only those commits that changed the
  number of occurrences of that string.  
+ `--no-merges` prevent appearing merge commits  
+ `path` limit the log output to commits that introduced a change to
  those files (in dir or where path indexing). Preceded by double dashes
  (--)  
<!-- }}} -->
### Undoing Things <!-- {{{ -->
When you commit too early and possibly forget to add some files, or you
mess up your commit message - make the additional changes, stage them,
and commit again using the `--amend` option:  
`$ git commit --amend`  

<!-- }}} -->
### Unstaging a Staged File <!-- {{{ -->
`git status` shows by itself how to do that.  
The command to unstage:  
`git reset HEAD <file>...`  
<!-- }}} -->
### Unmodifying a Modified File <!-- {{{ -->
How can you easily unmodify file - revert it back to what it looked like
when you last committed (or initially cloned), git status helps us:  
`git checkout -- <file>...`
    Any local changes you made to that file are gone.  
<!-- }}} -->
<!-- }}} -->
## Working with Remotes <!-- {{{ -->
### Showing Your Remotes <!-- {{{ -->
`git remote` command lists shortnames of each remote handle you've
specified.  
`-v` options shows you the URLs that Git has stored for the shortname.  

<!-- }}} -->
### Adding Remote Repositories <!-- {{{ -->
`git remote add <shortname> <url>`  
<!-- }}} -->
### Fetching and Pulling from Your Remotes <!-- {{{ -->
`$ git fetch <remote>`  
After you do this, you should have references to all the branches from
that remote, which you can merge in or inspect at any time.  
You can use the `git pull` command to automatically fetch and them merge
that remote branch into your current branch.  
<!-- }}} -->
### Pushing to Your Remotes <!-- {{{ -->
If you want to push your changes upstream, use command `git push
<remote> <branch>`.  
`$ git push origin master`  
If someone else fetch and push upstream and then you push upstream, your
push will rightly be rejected.  
<!-- }}} -->
### Inspecting a Remote <!-- {{{ -->
If you want to see more information about a particular remote, you can
use the `git remote show <remote>` command.  
<!-- }}} -->
### Renaming and Removing Remotes <!-- {{{ -->
If you want rename, use `git remore rename <src> <target>` command  
If you want remove, use `git remote remove <branch>` command  
<!-- }}} -->
<!-- }}} -->
## Tagging <!-- {{{ -->
Tagging is frequently used to mark release points.  
### Listing Your Tags <!-- {{{ -->
To list existing tags type `git tag`.  
You may apply filter with `$ git tag -l "v1.8.5*"`
To inspect tag use `$ git show <tag_name>`  
<!-- }}} -->
### Creating Tags <!-- {{{ -->
Git suppports two types of tags: _lightweight_ and _annotated_.  

+ _lightweight_ - just a pointer to a specific commit  
+ _annotated_ - are stored as full objects in the Git database. They're
  checksummed; contain the tagger name, email, and date; have a tagging
  message; and can be signed and verified with GNU Privacy Guard.  
<!-- }}} -->
### Annotated Tags <!-- {{{ -->
The easiest way to create _annotated tag_ is to specify `-a` when you
run the `tag` command:  
```shell
$ git tag -a v1.4 -m "my version 1.4"
$ git tag
v0.1
v1.3
v1.4
```
The `-m` specifies a tagging message.  

<!-- }}} -->
### Lightweight Tags <!-- {{{ -->
Don't supply any of the `-a`, `-s`, or `-m` options, just provide a tag
name:  
```shell
$ git tag v1.4-lw
$ git tag
v0.1
v1.4
v1.4-lw
```

<!-- }}} -->
### Tagging Later <!-- {{{ -->
To tag specific commit in the past, use `git tag -a <tag> <hashsum>`
command (`git log --pretty=oneline` will help you)  
<!-- }}} -->
### Deleting Tags <!-- {{{ -->
To delete tag on local machine, use `git tag -d <tagname>`.  
To remove tag on remove server there are two variations:  

+ `git push <remote> :refs/tags/<tagname>` - null value before the colon 
is being pushed to the remote tag name, effectively deleting it.  
+ `git push origin --delete <tagname>`
<!-- }}} -->
### Sharing Tags <!-- {{{ -->
By default, the `git push` command doesn't transfer tags to remote
servers. This process is jsut like sharing remote branches - you can run
`git push origin <tagname>`.  
`--tags` option will transfer all of your tags.  
<!-- }}} -->
### Checking out Tags <!-- {{{ -->
If you want to view the vrsions of files a tag is pointing to, you can
do a `git checkout` of that tag, although this puts your repository in
"detached HEAD" state, which has some ill side effects:  
`$ git checkout 2.0.0`  
If you want to fix a bug, it's better to create new branch and work
there:  
`$ git checkout -b version2 v2.0.0`  
<!-- }}} -->
<!-- }}} -->
## Git Aliases <!-- {{{-->
Its easy to set up an alias for each command using `git config`:  
```shell
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```
This means that, for example, instead of `git commit` you may type `gitci`.  
You may correct the usability problems:  

+ `$ git config --global alias.unstage 'reset HEAD --'`  
+ `$ git config --global alias.last 'log -1 HEAD'`  

If you want to run external commands - start the command with a `!`
character:  
`$ git config --global alias.visual '!gitk'`  
<!-- }}} -->
<!-- }}} -->
# Git branching <!-- {{{ -->
<!-- p. 62 -->
## Creating a New Branch <!-- {{{ -->
You can create branch with `git branch <name>` command.  
**HEAD** in Git is a pointer to the local branch you're currently on.  
All branches is just pointer to the commit.  
<!-- }}} -->
## Switching Branches <!-- {{{ -->
To switch to an existing branch, you run the `git checkout <name>
command` (this moves _HEAD_ to point to the new branch)  
To show log for another branch use: `git log <branchname>` or  
to show all of the branches, add `--all` to your `git log` command.  

You can  easily see branches with the `git log` command:  
`git log --oneline --decorate --graph --all`  

_Creating_ a branch and _switching_ to it can be done in one command:  
`git checkout -b <newbranchname>`  
<!-- }}} -->
## Basic Branching and Merging <!-- {{{ -->
### Workflow <!-- {{{ -->

In real world, commonly, you'll follow this steps:  

1. Do some work on a website.  
2. Create a branch for a new user story you're working on.  
3. Do some work in that branch.  

At this stage, you'll receive a call that another issue is critical and
you need a hotfix. You'll do the following:  

1. Switch to your production branch.  
2. Create a branch to add the hotfix.  
3. After it's tested, merge the hotfix branch, and push to production.  
4. Switch back you your original user story and continue working.  
<!-- }}} -->
### Basic Branching <!-- {{{ -->
Git won't allow you to checkout to another branch until you have
unstaged files (`stash` or `amend` could help)  

To merge branches you should be on branch you want to remain:  
```shell
$ git checkout master
$ git merge hotfix
Updating .....
Fast-forward
```

**Fast-forward** means that git simply moves pointer of branch forward.  

You can **delete** branch with the `-d` option to `git branch`  
<!-- }}} -->
### Basic Merging <!-- {{{ -->

>            v master
> -C0-C1-C2-C4
>         \C3-C5
>              ^ iss53

Suppose you've decided that you iss53 branch work is completed and ready
to be merged into your _master_ branch.  
In order to do tha, you have to check out the branch you wish to merge
into &rarr; run the `git merge` command:  
```shell
$ git checkout master
Switched to branch 'master'
$ git merge iss53
Merge made by the 'recursive' strategy
...
```
Because the commit on the branch you're on _isn't a direct ancestor_ of
the branch you're mergin in, Git has to do some work. In this case, Git
does a _simple three-way merge_, using the two snapshots pointed to by the
branch tips and the common ancestor of the two.  

After that, Git _creates a new snapshot_ that results from this three-way
merge and automatically _creates a new commit_ that points to it (merge
commit). It's special in that it has more than one parent.  

<!-- }}} -->
### Basic Merge Conflicts <!-- {{{ -->
<!-- TODO: stopped here -->
<!-- }}} -->

<!-- }}} -->

<!-- }}} -->
