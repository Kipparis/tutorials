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
If you change the same part of the same file differently in the two
branches you're merging, Git won't be able to merge them cleanly.  
To see which files are unmerged run `git status`  

Git adds standard conflict-resolutin markers to the files that have
conflicts, so you can open them manually and resolve those conflicts.
Example:  
```
<(7 times) HEAD:index.html
example text
=(7 times)
example text example
>(7 times) iss53:index.html
```
This means the version in _HEAD_ (your _master_ branch, because that was
what you had checked out when you ran your merge command) is the **_top_**
part of that block, while the version in your _iss53_ branch looks like
everything in the mottom. To resolve the conflict, you must choose either
side on merge them manually.  

Afterfwards, staging the file marks it as _resolved_.  

Also, you may run `git mergetool`, which fires up an appropriate visual
merge tool.  
<!-- }}} -->
### Branch Management <!-- {{{ -->
Get all your current branches: `$ git branch`. Notice `*` character
marks the branch that you currently have checked out.  
To see the **_last commit** on each branch, you can run `git branch -v`.  

+ `--merged` lists branches that you already merged  
    Its fine to delete those without * in front of them with `git branch -d`  
+ `--no-merged` lists branches that are not merged yet  
    If you really want to delete those branches, pass `-D` argument  
<!-- }}} -->
### Branching Workflows <!-- {{{ -->
This section cover some common workflows that this lightweight
branching makes possible.  
#### Long-Running Branches <!-- {{{ -->
+ Having code the at is entirely stable in `master` branch  
+ Branch you work on - `develop` or `next`. Whenever it gets to a stable
  state, it can be merged into `master`  

The commit history should look like this:  
master &larr; ... &larr; develop &larr; ... &larr; topic  
It's generally easier to think about them as work silos, where sets of
commits graduate to a more stable silo when they're fully tested.  
<!-- }}} -->
#### Topic Branches <!-- {{{ -->
A **_topic branch_** is a short-lived branch that you create and use for
a single particular feature or related work.  
<!-- }}} -->
<!-- }}} -->
### Remote Branches <!-- {{{ -->
You can get a full list of remote references explicitly with:  

+ `git ls-remote <remote>`  
+ `git remote show <remote>`  

Remote-tracking branch names take the form `<remote>/<branch>`. It's
updated by every network communication with git server.  

To synchronize your work with a given remote, you run a `git fetch
<remote>` command.  

#### Pushing <!-- {{{ -->
Pushing can be done with `git push <remote> <branch>` command.  
If you want to push local branch to another remote branch (or just give
another name on remote server) use command - `git push origin
<localbranch>:<remotebranch>`  

If you use an HTTPS URL to push over, the Git will ask you for your
username and password every push. To prevent it you may set up cache
that will hold your credentials for a few minutes:  
`git config --global credential.helper cache`  

After `git fetch` you don't have local branch. But if you want, run `git
checkout -b <localbranchname> <remotebranchname>`. You can merge remote
branch into yours as well  
<!-- }}} -->
#### Tracking Branches <!-- {{{ -->
Checking out a local branch from a remote-tracking branch automatically
creates what is called a _"tracking branch"_ (and the branch it tracks
is called an _"upstream branch"_). If you're on a _tracking branch_ and
type `git pull`, Git automatically knows which from where to fetch to
merge in. (same happends on `git clone` with _master_ branch)  

To _**create**_ _tracking branch_ run `git checkout -b <branch>
<remote>/<branch>` or `git checkout --track <remote>/<branch>`  

To **_change upstream branch_** type `git branch -u <remote>/<branch>`  
    When you have a tracking branch, you can reference its upstream
    branch with the `@{upstream}` or `@{u}` shorhand.  

If you want to find your tracking branches and see additional info
(ahead, begind, both), you can use `-vv` option to `git branch`  

Good practive for viewing branches is: `git fetch --all; git branch -vv`  
<!-- }}} -->
#### Pulling <!-- {{{ -->
It's the same as `git fetch` than `git merge`. Generally it's better to
simply use those commands explicitly as the magic of `git pull` can
often be confusing  
<!-- }}} -->
#### Deleting Remote Branches <!-- {{{ -->
You can delete remote branch with:  
`git push <remote> --delete <branch>`  
_basically it just removes the pointer from the server_  
<!-- }}} -->
<!-- }}} -->
### Rebasing <!-- {{{ -->
In Git, there are two main ways to integrate changes from one branch
into another:  

+ `merge`  
+ `rebase`  

#### The Basic Rebase <!-- {{{ -->
With the `rebase` command, you can take all the changes that were
committed on one branch and replay them on a different branch.  
Rebasing makes a cleaner history. If you examine the log of a rebased
branch, it looks like a linear history.  

For this example, you would check out the `experiment` branch, and the
rebase it onto the `master` branch as follows:  
```shell
$ git checkout experiment
$ git rebase master
...
```
At this point, you can go back to the `master` branch and do a
fast-forward merge.  
```shell
$ git checkout master
$ git merge experiment
```

Often, you'll do this to make sure your commits apply cleanly on a
remote branch - perhaps in a project to which you're trying to
contribute but that you don't maintain.  
<!-- }}} -->
#### More Interesting Rebases <!-- {{{ -->
Take a history like _A history with a topic branch off another topic
branch_, for example.  

You:  

1. Branched a topic branch (_server_), and made a commit  
2. Then, you branched off that to make the client-side changes (_client_) and commited a few times.  
3. Went back to your server branch and did a few more commits.  

Suppose you decide that you want to merge your **_client-side_** changes
into your mainline. You can take the changes on `client` that aren't on
`server` and replay them on your `master` branch by using the `--onto`
option of `git rebase`:  
```shell
$ git rebase --onto master server client
```
This basically says, "Take the `client` branch, figure out the patches
since it diverged from the `server` branch, and replay these patches in
the `client` branch as if it was base directly off the `master` branch
instead".  
Now you can _fast-forward_ your `master` branch.  
```shell
$ git checkout master
$ git merge client
```
Then you decide to pull in your server branch. You can use `git rebase
<basebranch> <topicbranch>` command - `$ git rebase master server`  

The rest you can do by yourself.
_Remember delete branches with_ `git branch -d <branch>` _command_  
<!-- }}} -->
#### The Perils of Rebasing <!-- {{{ -->
**Do not rebase commits that exist outside your repository and that
people may have based work on.**  
It's really messy and hard to understand without pictures. If you want,
see page 99 (105 pdf) in book _pro git_.  
<!-- }}} -->
#### Rebase When You Rebase <!-- {{{ -->
If you **do** find yourself in a situation like this, Git has some
further magic that might help you out.  

If you pull down work that was rewritten and rebase it on top of the new
commmits  from your partner, Git can often successfully figure out what
is uniquely yours nad apply them back on top of the new branch. (git
also computes checksum that is based jsut on the patch introduced with
the commit - _match-id_)  

You can simplify this by running `git pull --rebase` or `git fetch ; git
rebase <remote>/<branch>`  
You can turn this option by default with `git config --global
pull.rebase true`  
<!-- }}} -->
#### Rebase vs. Merge <!-- {{{ -->
The commit history has two points of view:  

+ record of what actually happened.  
+ story of how your project was made. This is the camp that uses tools
  like `rebase` and `filter-branch` to tell the story in the way that's
  best for future readers.  

In general the way to get the best of both worlds is to **_rebase local
changes_** you've made but haven't shared yet before you push them in order
to clean up your story, but **never** rebase _anything_ you've **_pushed
somewhere_**  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Git on the Server <!-- {{{ -->
A remote repository is generally a _bare repository_ - a Git repository
that has no working directory. In the simplest terms, a bare repository
is the ocntents of your project's `.git` directory and nothing else.  
## Protocols <!-- {{{ -->
Git can use four distinct protocols to transfer data:  

+ Local  
+ HTTP  
+ Secure Shell (SSH)  
+ Git  

### Local Protocol <!-- {{{ -->
The remote repository is in another directory on the same host. This is
often used if everyone on your team has access to a shared filesystem
such as an _NFS_.  

To clone repository like this, use the path to the repository as the
URL:  
```shell
$ git clone /srv/git/project.git    # Git tries to use  hardlinks or direclty copy the files it needs
# or this
$ git clone file:///srv/git/project.git # extraneous reference or objects left out
```

**Pros:**  

+ They're simple and they use existing file permissions and network
  access.  
+ Has a nice option for quicly grabbing work from someone else's working
  repository: `git pull /home/john/project`  

**Cons:**  

+ It can be difficult to set up and reach from multiple locations.  
+ A repository on NFS is often slower than the repository over SSH on
  the same server, allowing Git to run off local disks on each system.  
+ Not protected against accidental damage.  

<!-- }}} -->
### HTTP Protocols <!-- {{{ -->
**Pros:**  

+ Having a single URL for all types of access  
+ Having the server prompt only  when authentication is needed  
+ Ability to authenticate with a username and password  
+ Fast and efficient protocol, similar to the SSH one.  
+ You can also serve your repositories read-only over HTTPS.  
+ HTTP and HTTPS are such commonly used protocols that corporate
  firewalls are often set up to allow traffic though their ports  

**Cons:**  

+ Tricky to set up  
+ Providing your credentials is sometimes more complicated than using
  keys over SSH  
<!-- }}} -->
### The SSH Protocol <!-- {{{ -->
To clone a Git repository over SSH, you can specify an `ssh://` URL like
this:  
```shell
$ git clone ssh://[user@]server/project.git
```
Or you can use the shorter scp-like syntax for the SSH protocol:  
```shell
$ git clone [user@]server:project.git
```

**Pros:**  

+ Easy to set up  
+ Access over SSH is secure  
+ SSH is efficient, making the data as compact as possible before
  transferring it.  

**Cons:**  

+ Doesn't support anonymous access  

<!-- }}} -->
### The Git Protocol <!-- {{{ -->
You must create a `git-daemon-export-ok` file - the Git daemon won't
serve a repository without that file in it.  

**Pros:**  

+ Fastest network transfer protocol  

**Const:**  

+ Lack of authentication.  
+ The most difficult protocol to set up.  
<!-- }}} -->
<!-- }}} -->
## Getting Git on a Server<!-- {{{ -->
To initially set up you have to export an existing repository into a new
bare repository - clone your repository with `--bare` option. By
convention, bare repository directory names end with the suffix `.git`
like so:  
```shell
$ git clone --bare my_project my_project.git
```

<!-- }}} -->
## Putting the Bare repository on a Server <!-- {{{ -->
Users who have SSH-based read access to the directory on that server can
clone repository by running  
```shell
$ git clone user@git.example.com:<dir>/<bare_repo>.git
```
Git will automatically add group write permissions to a repository
properly if you run the `git init` command with the `--shared` option.  
```shell
$ shh user@git.example.com
$ cd /srv/git/my_project
$ git init --bare--shared
```


<!-- }}} -->
## Small Setups <!-- {{{ -->
If you want some repositories to be read-only for certain users and
read/write for others, access and permissions can be a bit more
difficult to arrange.  
### SSH Access <!-- {{{ -->
If you have a server to which all your developers already have SSH
access, it's generally easiest to set up your first repository there
(you don't have to do any work). If you want more complex access control
type permissions, you can handle them with the normal filesystem
permissions of your server's operating system.  

Other way:  

1. Set up accounts for everybody. You may not want to run `adduser` and
   have to set termorary pawwords for every new user.  
2. Create a single _git_ user account on the machine, ask every user who
   is to have write access to send you an SSH publick key, and add that
   key to the `$HOME/.ssh/authorized_keys` file of that new _git_
   accout. At that point, everyone will be able to access that machin
   via the _git_ accout. This doesn't affect the commit data in any way
   - the SSH user you connect as doesn't affect the commmits you've
   recorded
3. Have your SSH server authenticate from an LDAP server or some other
   centralized authentication source that you may already have set up,.
   As long as each user can get shell access on the machine, any SSH
   auth mechanism you can think of should work.  
<!-- }}} -->
<!-- }}} -->
## Generating Your SSH Public Key <!-- {{{ -->
First, you should check to make sure you don't already have a key (by
default they are stored in `$HOME/.ssh` directory)  
You are looking for pair of files named something like `id_dsa` or
`id_rsa` (private keys) and a matching file with a `.pub` extension (public key).  

In order to generate them user program called `ssh-keygen`:  
```shell
$ ssh-keygen -o
```
When it asks for passphrase, you can leave it empty, if you don't want
to type a password when you use the key.  

<!-- }}} -->
## Setting Up the Server <!-- {{{ -->
Let's walk through setting up SSH access on the server side. We'll use `authorized_keys`
method for authenticating your users.  

> A good deal of what is described here can be automated by using the
> `shh-copy-id` command, rather than manually copying and installing
> public keys  

Create a `git` user account and a `.ssh` directory for that user.
```shell
$ sudo adduser git
$ su git
$ cd
$ mkdir .ssh && chmod 700 .ssh
$ touch .ssh/authorized_keys && chmod 600 .ssh/authorized_keys
```
Add developers SSH public keys to the `authorized_keys` file under the `git` user.  
```shell
$ cat /tmp/id_rsa.john.pub >> ~git/.ssh/authorized_keys
$ cat /tmp/id_rsa.josie.pub >> ~git/.ssh/authorized_keys
$ cat /tmp/id_rsa.jessica.pub >> ~git/.ssh/authorized_keys
```

You should note that currently all these users can also log into the
server and get a shell as the `git` user. If you want to restrict that,
you will have to change the shell to something else in the `/etc/passwd`
file.  

You can easily restrict the `git` user account to only Git-related
activities with a limited shell tool called `git-shell` that comes with
Git. If you set this as the `git` user account's login shell, then that
account can't have normal  shell access to your server. To use this,
specify `git-shell` as login shell. To do so:  

+ specify full pathname of the `git-shell` command to `/etc/shells`  
+ edit the shell for a user using `chsh <username> -s <shell>`:  
    `$ sudo chsh git -s $(which git-shell)`  

Now they can't login in to interactive mode into shell. But they still
able to use SSH port forwarding to access any host the git server is
able to reach. To prevent that, edit the `authorized_keys` file and
prepend the following options to each key you'd like to restrict:  
```
no-port-forwarding,no-X11-fowarding,no-agent-forwarding,no-pty 
```

Run `git help shell` for more information on customizing the shell.  

<!-- }}} -->
## Git Daemon <!-- {{{ -->
_p 113_  
Set up a daemon serving repositories using the "Git" protocol. This is a
common choice for fast, anauthenticated access to your Git data.  
<!-- }}} -->
## Smart HTTP <!-- {{{ -->
_p 115_  
It's a protocol that can do both authenticated and unauthenticated
access at the same time.  
<!-- }}} -->
## GitWeb <!-- {{{ -->
_p. 116_  
To set up a simple web-base visualizer use CGI script (that comes with
Git) called GitWeb.  
<!-- }}} -->
## GitLab <!-- {{{ -->
_p. 118_  
More complex than the GitWeb option and likely requires more
maintenance, but it is much more fully featured option.  
<!-- }}} -->
<!-- }}} -->
# Distributed Git <!-- {{{ -->
You'll learn how to contribute code successfuly to a project and make it
as easy on you and the project maintainer as possible, and also how to
maintain a project successfully with a number of developers
contributing.  

## Distributed Workflows <!-- {{{ -->
### Centralized Workflow <!-- {{{ -->
One central hub, or _repository_, can accept code, and everyone
synchronizes their work with it.  
This means that if two developers clone
from the hub and both make changes, the first developer to push their
changes back up can do so with no problems. The second developer must
merge in the first one's work before pushing changes up.  
<!-- }}} -->
### Integration-Manager Workflow <!-- {{{ -->

1. The project maintainer pushes to their public repository.  
2. A contributor clones that repository and makes changes.  
3. The contributor pushes to their own public copy.  
4. The contributor sends the maintainer an email asking them to pull
   changes.  
5. The maintainer adds the contributor's repository as a remote and
   merges locally.  
6. The miantainer pushes merged changes to the main repository.  

<!-- }}} -->
### Dictator and Lieutenants Workflow <!-- {{{ -->
Variant of _Integration-Manager workflow_.  
Common developer pushes his changes to lietenant. Group of lieutenants
pushes its changes to dictator, which in order pushes to main branch.  

1. Regular developers work on their topic branch and rebase their work
   on top of master. The mast er branch is that of the reference
   repository to which dict ator pushes.  
2. Lieutenants merge the developers' topic branches into their `master`
   branch.  
3. The dictator merges the lieutenants' `master` branches into the
   dictator's `master` branch.  
4. Finally, the dictator pushes that `master` branch to the reference
   repository so the other developers can rebase on it.  
<!-- }}} -->
<!-- }}} -->
## Contributing to a Project <!-- {{{ -->
You should consider following _variables_:  

+ active contributor count.  
+ workflow in use for the project.  
+ commit access.  

All these questions can affect how you contribute effectively to a
project and what workflows are preferred or available to you.  

### Commit Guidelines <!-- {{{ -->
The Git project provides a document that lays out a **number of good tips**
for creating commits from which to submit patches - you can read it in
the Git source code in the `Documentation/SubmittingPatches` file.  

1. Your submission should not contain any whitespace errors. You can
   check this via `git diff --check` command.  
2. Try to make each commit logically separate changeset. If some of the
   changes modify the same file, try to use `git add --patch` to
   partially stage files.  
3. Commit message:  
    1. first line no longer than 50 characters (72 if necessary),
   followed by a blank line, followed by a more detailed
   explanation.  
    2. Write in imperative: "Fix bug" and not "Fixed bug" or "Fixes
   bug".  

Git project requires more detailed explanation to contain your
motivation for the change and contrast its implementation with previous
version.  
<!-- }}} -->
### Private Small Team <!-- {{{ -->
Private - not accessible to the outside world. You and the other
developers all have push access to the repository.  

+ work on `topic` branch
+ merge `topic` into `master`
+ merge `<remote>/master` into `master`
+ push changes to server

<!-- }}} -->
### Private Managed Team <!-- {{{ -->
<!-- TODO: stopped here -->
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
