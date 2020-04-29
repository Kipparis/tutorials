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
You must already know how to work on those teams. To read about workflow
open p. 136.  
<!-- }}} -->
### Forked Public Project <!-- {{{ -->
Contributing to public project is a bit different. Because you don't
have the permissions to directly update branches on the project, you
have to get the work to the maintainers some other way. This first
example describes contribuing via forking.  

First, you'll probably want to clone the main repository, create a topic
branch.  

> You may want to use `rebase -i` to squash your work down to a single
> commit, or rearrange the work in the commits to make the patch easier
> for the maintainer to review.  

When you ready to contribute go to original project page and clike the
"Fork" button, creating your own writable fork of the project. You then
need to add this repository URL as a new remote of your local
repository; for example:  
```shell
$ git remote add myfork <url>
```

Then push your local branch into remote fork. You won't want to merge
into your `master` branch because:  

+ your work might not be accepted  
+ your work might be cherry-picked  

To push to remote - `git push -u myfork featureA`. Not `-u` option which
adds default remote for this branch.  

Then you may want to generate **pull request**. You can do it on GitHub,
or via `git request-pull` command (generates summary of all changes you
are asking to be pulled). This output can be sent to the maintainer.  
```shell
$ git checkout -b featureB origin/master
    ... work ...
$ git commit
$ git push myfork featureB
$ git request-pull origin/master myfork
    ... email generated request pull to maintainer ...
$ git fetch origin
```
---  


Let's say the project maintainer has pulled in a bunch of other patches
and now your branch doesn't clenly merges. In this case, you can try to
rebase that branch on top of `origin/master`, resolve the ocnflicts for
the maintainer, and then resumbit your changes:  
```shell
$ git checkout featureA
$ git rebase origin/master
$ git push -f myfork featureA
```
Because you rebased the branch, you have to specify the `-f` to your
push command in order to be able to replace the `featureA` branch on the
server with a commit that isn't a descendant of it.  

---  

Assume that: the maintainer has looked at work in your second branch and
likes the concept but would like you to change an implementation detail.
You also can base your work on current `origin/master` branch:  
```shell
$ git checkout -b featureBv2 origin/master
$ git merge --squash featureB
    ... change implementation ...
$ git commit
$ git push myfork featureBv2
```

The `--squash` option takes all the work on the merged branch and
squashes it into one changeset producing the repository state as if a
real merge happened, without actually making a merge commit. (also
`--no-commit` option can be helpful)  


<!-- }}} -->
### Public Project over Email <!-- {{{ -->
Many projects have established procedures for accepting patches - you'll
need to check the specific rules for each project.  

Since there are several older, larger projects thich accept patches via
a developer mailing list, we'll go over it:  

the workflow is similar to the previous use case:  

1. you create a topic branches for each patch  
2. instead of forking the project and pushing to your own writable
   version, you generate email versions of each commit series nad email
   them to the developer mailing list  

```shell
$ git checkout -b topicA
    ... work ...
$ git commit
    ... work ...
$ git commit
```

To sent to the mailing list use `git format-patch` to generate the
**mbox-fomatted** files (turn each commit into an email message with the
first line of the commit message as the subject and the rest + patch = body)
that yuo can email to the list.  
`format-patch` outputs generated filenames. `-M` option tells Git to
look for renames.  

> You can also edit this patch files to add more infotmation - you may
> add text between the `---` line and the beginning of the patch (the `diff --git` line)  

To email this you can either paste the file into your email program
(often causes formatting issues) or
send it via a command-line program.  

To send via IMAP program:  

+ set imap section in your `~/.gitconfig` file.  
```txt
[imap]
    folder = "[Gmail]/Drafts"
    host = imaps://imap.gmail.com
    user = user@gmail.com
    pass = YX]8g76G_2^sFbd
    port = 993
    sslverify = false
```
+ `git imap-send` to place the patch series in the drafts folder of the
  specified IMAP server  
    `$ cat *.patch | git imap-send`  

To send via SMTP server:

+ configure following section in
  `~/.gitconfig` file:  
```txt
[sendemail]
    smtpencryption = tls
    smtpserver = smtp.gmail.com
    smtpuser = user@gmail.com
    smtpserverport = 587
```
+ use `git send-email` to send your patches:  
    `$ git send-email *.patch`  


<!-- }}} -->
<!-- }}} -->
## Maintaining a Project <!-- {{{ -->
Whether you maintain a canonical repository or want to help by verifying
or approving patches, you need to know how to accept work in a way that
is clearest for other contributors and sustainable by you over the long
run.  

### Working in Topic Branches <!-- {{{ -->
It's generally a good idea to try new work in a _topic branch_. The name
is better to be based on the theme of the work you're going to try or
something similarly descriptive, youcan easily remember. You can
namespace them as well - such as `sc/ruby_client`, where `sc` is short
for the person who contributed the work.  
<!-- }}} -->
### Applying Patches from Email <!-- {{{ -->
There are two ways to apply an emailed patch:  

+ `git apply`  
+ `git am`  

#### Applying a Patch with `apply` <!-- {{{ -->
If you received the patch from someone who generated it with `git diff`
or some variation of the Unix `diff` comand (which is not recommended),
you can apply it with the `git apply` command. Assuming you saved the
patch at `/tmp/patch-ruby-client.patch`, you can apply it like this:  
```shell
$ git apply /tmp/patch-ruby-client.patch
```
This modified the files in your working directory. It's almost identical
to running a `patch -p1`, but better than it.  

To see whether patch applies cleanly run `git apply --check` with the
patch (if htere is no output, patch should apply cleanly).  
<!-- }}} -->
#### Applying a Patch with `am` <!-- {{{ -->
You can encaurage your contributors to use `format-patch` instead of
`diff` (because it produces more info)  

To apply a patch generated by `format-patch`, you use `git am` (am -
apply a series of patches from a mailbox)  

If someone has emailed you the patch properly using `git send-email`,
and you download that into an mbox format, then you can point `git am`
to that mbox file, and it will start applying all the patches it sees.
If you run a mail client that can save several email out in mbox format,
you can save entire patch series into a file and then use `git am`.  

_commit_ information indicates the person who applied the patch  
_authore_ information is the individual who originally created the patch  

if `git am` fails, it will ask you what you want to do. It will put
conflict markers in any files it has issues with, much like a conflicted
merge or rebase operation. You resolve the conflict and run `git am
-resolved` to continue to the next patch.  

To make git resolve more intelligently, you can pass  a `-3` option to
it, which makes Git attempt a three-way merge.  
<!-- }}} -->
<!-- }}} -->
### Checking Out Remote Branches <!-- {{{ -->
For instance, if Jessica sends you an email saying that she has a greate
new feature in the `ruby-client` branch of her repository, you can test
in by adding the remote and checking out that branch locally:  
```shell
$ git remote add jessica git://github.com/jessica/myproject.git
$ git fetch jessica
$ git checkout -b rubyclient jessica/ruby-client
```

If you aren't working with a person consistently but still want to pull
from them with respect of commit history, you can provide the URL of
the remote repository to the `git pull` command. This does a one-time
pull and doesn't save the URL as a remote reference:  
```shell
$ git pull https://github.com/onetimeguy/project
```

<!-- }}} -->
### Determining What Is Introduced <!-- {{{ -->
It's often helpful to get a review of all the commits that are in this
branch but that aren't in your `master` branch.  

For example, you create branch `contrib` and applied patches, you can
run this:
```shell
$ git log contrib --not master
<two commits there>...
```
you may also use `-p` option  

Direct diffing from master will show you misinformation (`$ git diff
master`). One solution is explicitly figuring out the common ancestor
and then running your diff on it:
```shell
$ git merge-base contrib master
367db....
$ git diff 36c7db
```
or, more concisely:
```shell
$ git diff $(git merge-base contrib master)
```
Git provides another shothand:
```shell
$ git diff master...contrib
```




<!-- }}} -->
### Integrating Contributed Work <!-- {{{ -->
#### Merging Workflows <!-- {{{ -->
One basic workflow is to simply merge all that work directly into your `master` branch.  
In this scenaria, you have a `master` branch that contains basically
stable code.  

 If you have a more important project, you might want to use a two-phase
 merge cycle. In this scenaria, you have two long-running branches,
 `master` and `develop`, in which you determine that `master` is updated
 only when a very stable release is cut and all new code is integrated
 into the `develop` branch. (you may also include `integrate` branch
 before `develope`).  
<!-- }}} -->
#### Large-Merging Workflows <!-- {{{ -->
The Git project has four long-running branches: `master`, `next`, and
`pu` (proposed updates) for new work, and `maint` for maintenance
backports.  

+ new work introduced by contributors is collected into topic branches
  in the maintainer's repository.  
    + if they're safe they're merged into `next` and that branch is pushed
  up so everyone can try the topics integrated together.  
    + if the topics still need work, they're merged into `pu` insted.
+ when it's determined that they're totally stable, the topics are
  re-merged into `master`. The `next` and `pu` branches are then rebuilt
  from the `master` (`master` almost always moves forward, `next` is
  rebased occasionally, `pu` is rebased even more often)  

The git project also has a `maint` branch that is forked off from the
last release to provide backported patches in case a maintenance release
is required.  

<!-- }}} -->
#### Rebasing and Cherry-Picking Workflows <!-- {{{ -->
Other maintainers prefer to rebase or charry-pick contributed work on
top of their `master` branch, rather than mergin it in, to keep a mostly
linear history. You can move to topic branch and run the rebase command
to rebuild the changes on top of your current `master` (or `develop` and
so on) branch. Then you can fast-forward your `master` branch.  

If you prefer to apply a single commit from another branch, you may
_cherry-pick_ it rather than run rebase:
```shell
$ git cherry-pick e43a6
```
it creates new SHA-1 value, because the date applied is different  
<!-- }}} -->
#### Rerere <!-- {{{ -->
If you're doing lots of merging and rebasing, you you're maintaining a
long-lived topic branch, Git has a feature called "rerere' that can
help".  

Rerere stands for "reuse recorded resolution" - it's a way of
shortcutting manual conflict resolution. When **rerere** is enabled, Git
will keep a set of pre- and post-images from successful merges, and if
it notices that there's a conflict that looks exatly like one you've
already fixed, it'll just use the fix from last time, without bothering
you with it.  
To enable:
```shell
$ git config --global rerere.enabled true
```
You can interact with the **rerere** cache using the `git rerere`
command. When it's invoked alone, Git checks its database of resolutions
and tries to find a match with any current merge conflicts and resolve
them.  
<!-- }}} -->
<!-- }}} -->
### Tagging Your Releases <!-- {{{ -->
**Exporting gpg keys and signed-tagging your releases**  
If you decide to sign the tag as the maintainer, the tagging may look
something like this:
```shell
$ git tag -s v1.5 -m 'my signed 1.5 tag'
You need a passphrase to unlock the secret key for
user: "Scott Chacon <schacon@gmail.com>"
1024-bit DSA key, ID F721C45A, created 2009-02-09
```
To unclude your public key as blob in the repository and then adding a
tag that points directly to that content. To do this, you can figure out
which key you want by running `gpg --list-keys`  

Then you can directly import the key into the Git database by exporting
it and piping that through `git hash-object`, which writes a new blob
with those contents into Git and gives you back the SHA-1 of the blob:
```shell
$ gpg -a --export F721C45A | git hash-object -w --stdin
```

Now you can create a tag that points directly to it by specifying the
new SHA-1 value that the `hash-boject` command gave you:
```shell
$ git tag -a maintainer-pgp-pub 659...
```

If you run `git push --tags`, the `maintainer-pgp-pub` tag will be
shared with everyone.  
If anyone wants to verify a tag, then can directly import your PGP key
by pulling the blob directly out of the database and importing it into
GPG
```shell
$ git show maintainer-pgp-pub | gpg --import
```
Also, if you include instructions in the tag message, running `git show
<tag>` will let you give the end user more specific instructions about
tag verification.  

<!-- }}} -->
### Generating a Build Number <!-- {{{ -->
If you want to have a human-readable name to go with a commit, you can
run `git describe` on that commit. In response, Git generates a string
consisting of:  

+ name of the most recent tag earlier than that commit  
+ number of commits since taht tag  
+ partial SHA-1 value (prefixed with the letter "g" meaning Git)  

```shell
$ git describe master
v1.6.2-rc1-20-g8c5b85c
```

By default, the `git describe` command requires annotated tags (tags
created with the `-a` or `-a` flag); if you want to take advantage of
lightweight tags, add `--tags` option. You can also use this string as
the target of a `git checkout` or `git show` command.  

<!-- }}} -->
### Preparing a Release <!-- {{{ -->
Now you want to release a build. One of the things you'll want to do is
create an archive of the latest snapshot of your code for those poor
sould who don't use Git. The command to do this is `git archive`:
```shell
$ git archive master --prefix='project/' | gzip > `git describe
master`.tar.gz
```

You can also create a zip archieve by passing the `--format=zip` option:
```shell
$ git archive master --prefix='project/' --format=zip > `git describe
master`.zip
```


<!-- }}} -->
### The Shortlog <!-- {{{ -->
Nice way of quickly getting a sort of changelog of what has been added
to your project since your last release or email is to use the `git
shortlog` command. If summarizes all the commits in the range you give
it;
```shell
$ git shortlog --no-merges master --not v1.0.1
Chris Wanstrath (6):
    ...
Top Preston-Werner (4):
    ...
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# GitHub <!-- {{{ -->
This chapter is about using GitHub effectively.  
If you are not interested in using GitHub, you can safely skip to `Git
Tools`.  

## Account Setup and Configuration <!-- {{{ -->
SSH Access - add on GitHub your `~/.ssh/id_rsa.pub` key.  
Two Factior Authentication.  
<!-- }}} -->
## Contributing to a Project <!-- {{{ -->
### Forking Projects <!-- {{{ -->
**Fork button** will create copy of repository in your namespace.  
<!-- }}} -->
### The GitHub Flow <!-- {{{ -->

1. Fork the project  
2. Create a topic branch from `master`  
3. Make some commits to improve the project  
4. Push this branch to your GitHub project  
5. Open a Pull Request on GitHub  
6. Discuss, and optionally continue committing  
7. The project owner merges or closes the Pull Request  
8. Sync the updated master back to your fork  

#### Creating a Pull Request <!-- {{{ -->
Just do what you know, but notice adding commits to an existing Pull
Request doesn't trigger a notification, so you want to leave a comment.  

Also GitHub checks to see if the Pull Request merges cleanly and
provides a button to do the merge for you on the server. If you click
button GitHub will perform a "non-fast-forward" merge, meaning that even
if the merge **could** be a fast-forward, it will still create a merge
commit.  

After merge, the Pull Request will automatically be closed.  

You can also open Pull Request between two branches in the same
repository (if you both ahve write access)
<!-- }}} -->
<!-- }}} -->
### Advanced Pull Requests <!-- {{{ -->
Lets cover a fiew interesting tips and tricks about PullRequests.  
#### Pull Requests as Patches <!-- {{{ -->
Think of patches as history of "why certain thing exist".
<!-- }}} -->
#### References <!-- {{{ -->
Simply put `#<issue id>` or `#<pull request id>`  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Maintaining a Project <!-- {{{ -->
### Pull Request Refs <!-- {{{ -->
Run `git ls-remote <remote>` and pseudo branches (_pull request_) will
have prefix _refs/pull/_. To fetch some, use `git fetch <remote>
refs/pull/<pr#>/head`  

To fetch all of the pull request automatically, modify your config file
as follows:
```txt
[remote "origin"]
    url = https://github.com/libgit2/libgit2
    fetch = +refs/heads/*:refs/remotes/origin/*
```
e.g. the things on the remote that are under _refs/heads_ should go in
my local repository under _refs/remotes/origin_.  
There's also a _refs/pull/#/merge_ ref on the GiHub side, which
represents the commit that would result if you push the "merge" button
on the site.  
<!-- }}} -->
### Email Notifications <!-- {{{ -->
There are a lot of useful information in e-mail metadata.  
<!-- }}} -->
### Special Files <!-- {{{ -->
README - lands on open page of repository.  
CONTRIBUTING - show it when anyone starts opening a Pull Request.  
<!-- }}} -->
<!-- }}} -->
## Scripting GitHub <!-- {{{ -->
### Services and Hooks <!-- {{{ -->
**Hooks** - you specify a URL and GitHub will post an HTTP payload to
that URL on any even you want.  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
# Git Tools <!-- {{{ -->
## Revision Selection <!-- {{{ -->
Git allows you to refer to a single commit, set of commits, or range of
commits in a number of ways. They aren't necessarily ovious but are
helpful to know.

### Single Revisions <!-- {{{ -->
You can refer with first few (unique) characters of the SHA-1 hash.
To list them use `git log --abbrev-commit`  
<!-- }}} -->
### Branch References <!-- {{{ -->
If commit is on top of some branch, you can simply use that branch name:
```shell
$ git shot topic1
```
To see SHA-1 hash to which top commit of branch points to use:
```shell
$ git rev-parse topic1
ca82a6dff...
```

<!-- }}} -->
### Reflog Shortnames <!-- {{{ -->
You can see reflog by using `git reflog`.  
```shell
$ git show HEAD@{5}
# another example
$ git show master@{yesterday}
```

Note: this nechnique only works for data that's still in your reflog, so
you can use it to look for commits older than a few months.  

To see reflog information formatted like the `git log`, you can run `git
log -g`  

<!-- }}} -->
### Ancestry References <!-- {{{ -->
If you place a `^` (caret) at the end of a reference, Git resolves it to
mean the parent of that commit. You can also specify a number after the
`^`to identify _which_ parent you want. The first parent of a merge
commit is from the branch you were on when you merged (frequently
`master`), while the _second_ parent - branch that was merged (say,
`topic`)  

If you place a `~` at the end, it will refer to the parent. Unlike `^`
when chaining, if will expand as "first parent of the first parent..."  
<!-- }}} -->
### Commit Ranges <!-- {{{ -->
#### Double Dot <!-- {{{ -->
This basically asks Git to resolve a range of commits that are reachable
from one commit but aren't reachable from another.  

`master..experiment` means "all commits reachable from `experiment` that
aren't reachable from `master`"  

Another frequent example is:
```shell
git log origin/master..HEAD
# or equivalent
git log origin/master..     # Git substitutes HEAD if one side is missing
```

<!-- }}} -->
#### Multiple Points <!-- {{{ -->
Git allow you to specify  other branches or commits by using either the
`^` character or `--not` before any reference from which you don't want
to see reachable commits. The following three commands are equivalent:
```shell
$ git log refA..refB
$ git log ^refA refB
$ git log refB --not refA
```
this is nice, because you can specify more than two references in your
query.  

<!-- }}} -->
#### Triple Dot <!-- {{{ -->
Specify the list of commits that are reachable by _either_ of two
references but not by both of them.  

`--left-right` opriont shows you which side of the range each commit is
in.
```shell
$ git log --left-right master...experiment
```

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Interactive Staging <!-- {{{ -->
If you run `git add` with the `-i` or `--interactive` option, Git enters
an interactive shell mode.  

### Staging and Unstaging Files <!-- {{{ -->
If you time `u` (for update), you're prompted for which files you want
to stage. Then you enter indexes of files (Git will mark selected files
with `*` next to each file). If you press Enter after typing nothing at
the propmpt, Git takes anything selected and stages it for you.  

To unstage you can use the `r` (for revert) option.  

To see the diff of what you've staged, you can use the `d` (for diff)
command (much like `git diff --cached`).  
<!-- }}} -->
### Staging Patches <!-- {{{ -->
It's also possible for Git to stage certain _parts_ of files and not the
rest.  

From same interactive prompt type `p` (for the patch). Then, after file
choosing, Git will display hunks of the file diff and ask if you would
like to stage them, one by one (at this point typing `?` shows a list of
what you can do)  

You can run described patch mode from shell by using `git add -p` or
`git add --patch`.  
You can use patch mode for:  

+ partially resetting files with the `git reset --patch`  
+ checking out parts of files with the `git checkout --patch` command  
+ stashing parts of files with the `git stach save --patch` command  
<!-- }}} -->
<!-- }}} -->
## Stashing and Cleaning <!-- {{{ -->
If you do not want to move to another branch, but don't
- commit of half-done work, command `git stash` helps you.  
Takes messy from your dir, saves it (staged and unstaged files) so you
may back to those changes later.  

### Stashing Your Work <!-- {{{ -->
In working directory type `git stash` or `git stash push`. Now your
working directory is clean.  
To see what you've stashed - `git stash list`.  

To **apply** most recent stash use `git stash apply` command.  
To apply more _older_ stashes use `git stash apply stash@{2}`  
The changes to your files were reapplied, but the file you staged before
wasn't restaged. To do that you mast pass `--index` option to `git stash
apply` command.  

After applying you still have that snapshot in stash list. To remove use
`git stash drop` command with the name of the stash to remove.  
<!-- }}} -->
### Creative Stashing <!-- {{{ -->
Common options that can be usefull:  

+ `--keep-index` - include all staged content and leave them in the
  index (changes will persist in directory)  
+ `--include-untracked` or `-u` - include untracked files in the stash
  being created.  
    - to include ignored files use `--all` or `-a`  
+ `--patch` - prompt you interactively which of the changes you would
  like to stach.  
<!-- }}} -->
### Creating a Branch from a Stash <!-- {{{ -->
If your stash doesn't applied cleanly, but you need to test some of
those, you may create branch from stashed itemes with `git stash branch
<new branchname>` and continue work there.  
This command will drop applyed stash if applying were sucessfull  
<!-- }}} -->
### Cleaning your Working Directory <!-- {{{ -->
Remove cruft files or clean your working directory:  

+ `git clean`  
+ `git clean -f -d` - remove all the untracked files (-f - force).  
+ `--dry-run`, or `-n` - do a dry run and tell me what you
  _would_ have removed.  

By default will only remove untracked untracked files that are not
ignored.  

+ `-x` - extend removing on untracked files from .gitignore  
+ `-i` - interactive mode  
+ `-f -f` - extra forceful  
<!-- }}} -->
<!-- }}} -->
## Signing Your Work <!-- {{{ -->
If you're taking work from others on the internet and want to verify
that commits are actually from a trusted source, Git has a few ways to
sign and verify work using GPG.

### GPG Introduction <!-- {{{ -->

+ `$ gpg --list-keys` - list installed keys  
+ `$ gpg --gen-key` - generate your key  
+ `$ git config --global user.signingkey <code>` now Git will use your
  key by default to sign tags and commits if you want.  
<!-- }}} -->
### Signing Tags <!-- {{{ -->
All you have to do is use `-s` instead of `-a`:
```shell
$ git tag -s v1.5 -m 'my signed 1.5 tag'
```
If you run `git show` on that tag, you can see your GPG signature
attached to it.  

<!-- }}} -->
### Verifying Tags <!-- {{{ -->
`git tag -v <tag-name>`. You need the signer's public key in your
keyring for this to work properly.  
<!-- }}} -->
### Signing Commits <!-- {{{ -->
All you need to do is add a `-S` to your `git commit` command.  

To see and verify these signatures, there is also a `--show-signature`
option to `git log`  
To configure `git log` to check any signatures - use `%G?` format.  

Also `git merge` and `git pull`can be told to inspect and reject when
merging a commit that does not carry a t rusted GPG signature with the
`--verify-signatures` command. If branch contains not signed and valid
commits the merge will not work.
```shell
$ git merge --verify-signatures non-verified-branch
fatal: Commit ab06180 does not have a GPG signature.
```
you can also add `-S` option to the `git merge` command to sign the
resulting merge commit.  

<!-- }}} -->
### Everyone Must Sign <!-- {{{ -->
Make sure you understand GPG and the benefits of signing things. And if
you choose to use, make sure all of your team will understands how to do
so.  
<!-- }}} -->
<!-- }}} -->
## Searching <!-- {{{ -->
You'll often need to find where a function is called or defined, or
display the history of a method.  

### Git Grep <!-- {{{ -->
By default, `git grep` will look through the files in your working
directory.  

+ You can use either of the `-n` or `--line-number` options to print out
the line numbers where Git has found matches:  
```shell
$ git grep -n gmtime_r
```
+ You can ask git to summorize output - how many entries in each file.
```shell
$ git grep --count gmtime_r
```
+ You can specify _context_ (pattern for searched files) with either of
the `-p` or `--show-function` options:
```shell
$ git grep -p gmtime_r *.c
```
+ You can combine expressions with `--and` flag, which ensures that
multiple matches must occur in the same line of text.  
Example: we'll look for any lines that define a constant whose name
contains either of the substrings "LINK" or "BUF_MAX", specifically in
an older version of the Git codebase represented by the tag `v1.8.0`
(we'll throw in the `--break` and `--heading` options which help split
up the output into a more readable format):
```shell
$ git grep --break --heading -n -e '#define' --and \( -e LINK -e \
BUF_MAX \) v1.8.0
```

<!-- }}} -->
### Git Log Searching <!-- {{{ -->
Would be usefull if you're looking not for _where_ a term exists, but
_when_ it existed or was introduced.  

+ `-S` option tells git log to output only those mathces that changed
  number of occurences.  
```shell
$ git log -S ZLIB_BUF_MAX --oneline
```
+ `-G` allows you to provide a regular expression to search.  

#### Line Log Search <!-- {{{ -->
`-L` option to `git log` command shows the history of a function or
line of code. It will figure out the bounds of passed
function name and then look through the history and show us every change
that was made to the function as a series of patches.  

```shell
$ git log -L :git_deflate_bound:zlib.c
```

If Git can't figure out how to match a function or method, you can
provide regular expression. For example above what be similar to:
```shell
$ git log -L '/unsigned long git deflate_bound/',/^}/:zlib.c
```

You could also give it a range of lines or a single line number.  

<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Rewriting History <!-- {{{ -->

+ Decide what files go into which commits right before you commit with
  the staging area  
+ that you didn't mean to be working on something yet with `git stash`  
+ refrite commits that already happened so they look like thay happened
  in a different way.  
    - changing order of the commits  
    - changing messages  
    - modifying files in a commit  
    - squashing together of splitting apart commits  
    - removing commits entirely  

_all before you share your work with others._  

One cardinal rule:
> Don't push your work until you're happy with it  

### Changing the Last Commit <!-- {{{ -->
If you simply want to modify your last commit message:
```shell
$ git commit --amend
```

If you want to change content, you should change, stage and you command
above.  

If you don't want to chagne message append `--no-edit` option  

<!-- }}} -->
### Changing Multiple commit Messages <!-- {{{ -->
Git doesn't provide any modify-hstory tool, but you can use the rebase
tool to rebase a series of commits onto the HEAD they were originally
based on instead of moving them to another one.  
With the interactive rebase tool you can:  

+ stop after each commit  
+ modify and chagne the message, add files, or do whatever you with  

You can run rebase by adding the `-i` option to `git rebase`.  
You must indicate how far back you want to rewrite commits by telling
the command which commit to rebase onto.  

For example, if you want to change last 3 commits (or any of those), you
supply as an argument to `git rebase -i` the parent of the last commit
you want to edit, which is `HEAD~2^` or `HEAD~3`.  

Commands above will open a list of commits in your text editor. The list
of commits is listed in the **opposite order**.  

Mark commits that you want to edit with `edit` instead of `pick`.  
Then Git will help you to do the rest.  
<!-- }}} -->
### Reordering Commits <!-- {{{ -->
To reorder open interactive rebase tool and simply remove lines with
commits you don't want to exist and reorder the rest lines in the way
you prefer (remember reverse order from `git log`)  
<!-- }}} -->
### Squashing Commits <!-- {{{ -->
Open interactive rebase tool and instead of "pick" or "edit" specify
"squash". Git applies both that change and the change directly before it
and makes you merge the commit messages together.  
So if you want to make a single commit from these three commits:
```txt
pick <SHA-1> <msg>
squash ....
squash ....
```

When you exit git will apply all three changes and then puts you back
into the editor to merge the three commit messages.  

<!-- }}} -->
### Splitting a Commit <!-- {{{ -->
Mark selected commits in interactive rebase tool with "pick" word. Then
in command-line this will help you:
```shell
$ git reset HEAD^   # undoes that commit and leaves the modified files
$ git add README
$ git commit -m 'updated README formatting'
$ git add lib/simplegit.rb
$ git commit -m 'added blame'
$ git rebase --continue
```

And your history looks like this:
```shell
$ git log -4 --pretty=format:"%h %s"
... added cat-file
... added blame
... updated README formatting
... changed my name a bit
```


<!-- }}} -->
### The Nuclear Option: filter-branch <!-- {{{ -->
Rewrite a larger number of commits in some scriptable way. The command is
`filter-branch`.

> `git filter-brach` has many pitfalls, and is no longer the recommended
> way to rewrite history. Instead, consider using `git-filter-repo`.  

#### Removing a File from Every Commit <!-- {{{ -->
For example, to remove a file named `passwords.txt` from your entire
history, you can use the `--tree-filter` option to `filter-branch`:
```shell
$ git filter-branch --tree-filter 'rm -f passwords.txt' HEAD
```

To run `filter-branch` on all branches, pass `--all` option.  

<!-- }}} -->
#### Making a Subdirectory the New Root <!-- {{{ -->
If you want to make the _trunk_ subdirectory be the new project root for
every commit, `filter-branch` can help you do that:
```shell
$ git filter-branch --subdirectory-filter trunk HEAD
```
Now your new project root is what was in the _trunk_ subdirectory each
time. Git will also automatically remove commits that did not affect the
subdirectory.  

<!-- }}} -->
#### Changing Email Addresses Globally <!-- {{{ -->
Use `--commit-filter`:
```shell
$ git filter-branch --commit-filter '
    if [ "$GIT_AUTHOR_EMAIL" = "schacon@localhost" ];
    then
        GIT_AUTHOR_NAME="Scott Chacon";
        GIT_AUTHOR_EMAIL="schacon@example.com";
        git commit-tree "$@";
    else
        git commit-tree "$@";
    fi' HEAD
```

<!-- }}} -->
<!-- }}} -->

<!-- }}} -->
## Reset Demystified <!-- {{{ -->
For Git commands `reset` and `checkout` it seems hard to actually
understand what they do. Buy check out a simple mataphor.  

### The Three Trees <!-- {{{ -->
If easier way is to consider of Git being a content manager of three
different trees. Git as a system manages and manipulates three trees in
its normal operation:  

+ **HEAD** - last commit snapshot, next parent  
+ **Index** - proposed next commit snapshot  
+ **Working Directory** - sandbox  

#### The HEAD <!-- {{{ -->
If fact, it's pretty easy to see what snapshot looks like. Here is an
example of getting the actual directory listing and SHA-1 checksums for
each file in the HEAD snapshot:
```shell
$ git cat-file -p HEAD
tree ...
author ...
committer ...

<commit_name>

$ git ls-tree -r HEAD
100644 blob ... README
100644 blob ... Rakefile
040000 tree ... lib
```

<!-- }}} -->
#### The Index <!-- {{{ -->
The _index_ is your **proposed next commit** ("Staging Area").  
```shell
$ git ls-files -s
```

<!-- }}} -->
#### The Working Directory <!-- {{{ -->
Think of the working directory as a **sandbox**, where you can try
changes out before committing them to your staging area (index) and then
to history
```shell
$ tree
    ....
```

<!-- }}} -->
<!-- }}} -->
### The Workflow <!-- {{{ -->
+ `git reset --soft HEAD~` - simply undoes last commit command (but
  don't remove this commit from history)  
+ `git reset [--mixed] HEAD~` - updates index to HEAD~  
+ `git reset --hard HEAD~` - updates your working directory  

You can call `git reset file.txt` (`git reset --mixed HEAD file.txt`)
so Git will ignore first step and execute other only for a file
(reverse for `git add`).  

It's the same as "pull the data from HEAD". Also we call
`git reset eb43bf file.txt` to be more precise.  

`git reset` (like `git add`) accept a `--patch` option to unstage
content on a hunk-by-hunk basis.  
<!-- }}} -->
### Squashing <!-- {{{ -->
If you have series of commits like: "oops.", "WIP", "forgot this file".
You can use `reset` to quickly and easily squash them into a single
commit:  
Suppose you want to keep your first commit (of three), then you run `git
reset --soft HEAD~2` (which only moves master pointer back two
commits). Then do `commit` and you're done. The history will look like
you create first commit, then in second commit you done all other
things.  
<!-- }}} -->
### Check It Out <!-- {{{ -->
What the difference between `checkout` and `reset`. Like `reset`,
`checkout` manipulates the three trees, and it is a bit different
depending on whether you give the command a file path or nor.  

#### Without Paths <!-- {{{ -->
Running `git checkout [branch]` is pretty similar to running `git reset
--hard [branch]`. But `checkout` is smarter. It will:  

+ check to make sure it's not blowing away files that have changes to
  them.  
+ try to do a trivial merge in the working directory, so all of the
  files you haven't changed will be updated.  

`checkout` will move HEAD itself to point to another branch.  
<!-- }}} -->
#### With Paths <!-- {{{ -->
It's like `git reset --hard [branch] file`. Also, like `git reset`
and `git add`, `checkout` will accept a `--patch` option to allow you to
selectively revert file contents on a hunk-by-hunk basis.  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Advanced Merging <!-- {{{ -->
If you watit too long to merge two branches that diverge quickly, you
can run into some issues.  

We'll go through possible issues and what tools does Git offers to solve
them. We'll also cover non-standard types of merges you can do, as well
as how to back out merges.  

### Merge Conflicts <!-- {{{ -->
They could be caused by different line endings.  
<!-- }}} -->
### Aborting a Merge <!-- {{{ -->
If you don't ready for the situation, run `git merge --abort`. The only
cases where it may not be able to do its job perfectly would be if you
had unstashed, uncommitted changes in your working directory.  
<!-- }}} -->
### Ignoring Whitespace <!-- {{{ -->
Git's `merge` command takes additional options related to whitespace
processing. Those are:  

+ `-Xignore-all-space` - ignores whitespace **completely** when
  comparing lines  
+ `-Xignore-space-change` - treats sequences of one or more whitespace
  characters as equivalent  

<!-- }}} -->
### Manual File Re-merging <!-- {{{ -->
There are other types of changes that perhaps Git can't handle
automatically, but are scriptable fixes. Let's pretend Git could not
handle the whitespace change and we needed to do it by hand.  

1. Get into merge conflict state:  
    + Get copies of our, their, and common versions of file.  
2. Fix either our or their side  
3. Re-try the merge again for just this single file  

Git stores all of these versions in the index under "stages" which each
have numbers associated with the. 1 - common acestor, 2 - your version,
3 - is from `MERGE_HEAD`, the version you're merging in ("theirs")  

You can extract a copy of each of these versions:
```shell
$ git show :1:hello.rb > hello.common.rb
$ git show :2:hello.rb > hello.ours.rb
$ git show :3:hello.rb > hello.theirs.rb
```

Then we want to correct their version and run `git merge-file` command:
```shell
$ dos2unix hello.theirs.rb
    ...
$ git merge-file -p \
    hello.ours.rb hello.common.rb hello.theirs.rb > hello.rb

$ git diff -b # prints summary of what introduced from both sides
```

To get information of what introduced from you:
```shell
$ git diff --ours
```

To see how result of the merge differed from what was on their side:
```shell
$ git diff --theirs -b
```
`-b` options strips out the whitespace  

Finally, you can see how the file has changed from both sides with:
```shell
$ git diff --base -b
```

At this point we can use the `git clean` command to clear out the extra
files we created to do the manual merge:
```shell
$ git clean -f
```





<!-- }}} -->
### Checking Out Conflicts <!-- {{{ -->
For example manual editing still didn't work and we need more context.  

Let's change up things a little bit. For this example, we have two
longer lived branches that each have a few commits in them but create a
legitimate content conflict when merged.  

`git checkout` with the `--conflict` option will re-checkout the file
again and replace the merge conflict markers (if you want to reset the
markers and try to resolve them again)  

You can pass `--conflict` either `diff3` or `merge` (which is default).
If you pass it `diff3`, Git will use a slightly different version of
conflict markers, not only giving you the "ours" and "theirs" versions,
but also the "base" version inline to give your more context.  

If you like this format, you can set it by default by setting the
`merge.conflictstyle` setting to `diff3`.
```shell
$ git config --global merge.conflictstyle diff3
```

The `git checkout` can also take `--ours` and `--theirs` options, which
can be really fast way of just choosing either one side or the other
without merging things at all (usefull for merging binaries, just choose
one side and commit the changes).  

<!-- }}} -->
### Merge Log <!-- {{{ -->
To get a full list of all of the unique commits that were included in
either branch involved in this merge, we can use the "triple dot"
syntax:
```shell
$ git log --oneline --left-right HEAD...MERGE_HEAD
< ... update README
< ... add a README
< ... update phrase to hola world
> ... add more tests
> ... add testing script
> ... changed text to hello mundo
```

if we add the `--merge` option, it will only show the commits in either
side of the merge that touch a file that's currently conflicted.
```shell
$ git log --oneline --left-right --merge
< ... update phrase to hola world
> ... changed text to hello mundo
```

<!-- }}} -->
### Combined Diff Format <!-- {{{ -->
When you run `git diff` directly after a merge conflict, it will give
you information in a rather unique diff output format. The format is
called "Combined Diff" giving you two columns of data next to each line.  

First column shows you if that line is different between the "ours"
branch and the file in your working directory.  
Second column does the same between the "theirs" branch and your working
directory copy.  

You can also get this from the `git log` for any merge with the `--cc`
option to a `git log -p`. Also you may use `git show` on a merge commit.  
```shell
$ git log --cc -p 1
```

<!-- }}} -->
### Undoing Merges <!-- {{{ -->
Assume we have `topic` branch, that we accidantly merged into `master`
branch.  

#### Fix the references <!-- {{{ -->
`git reset --hard HEAD~` will do the trick.  
To understand why, read `Reset Demystified`  
<!-- }}} -->
#### Reverse the commit <!-- {{{ -->
Git gives you the option of making a new commit which undoes all the
changes from an existing one. Git calls this operation a "revert".
```shell
$ git revert -m 1 HEAD
```
The `-m 1` flag indicates which parent is the "mainline" and should be
kept.  

If you want to undo the revert (e.g. un-revert the original merge):
```shell
$ git revert ^M
    ...
$ git merge topic
```

<!-- }}} -->
<!-- }}} -->
### Other Types of Merges <!-- {{{ -->
#### Our or Theirs Preference <!-- {{{ -->

We can also tell Git to favor one side or the other when it sees a
conflict.  

If you would prefer for Git to simply choose a specific side and ignore
the other side instead of letting you manually resolve the conflict, you
can pass the `merge` command either a `-Xours` or `-Xtheirs`.  

To pass this option to `merge-file` use `git merge-file --ours`.  

If you don't want Git to even try to merge changes from the other side,
there is a more draconian option. This will basically do a fake merge.
It will record a new merge commit with both branches as a parents, but
it will not even look at the branch you're merging in. It will simply
record as the result of the merge the exact code in your current branch.
```shell
$ git merge -s ours mundo
Mege made by the 'ours' strategy.
$ git diff HEAD HEAD~
$
```

This can be useful to basically trick Git into thinking that a branch is
already merged.  
For example you branched off a `release` branch. Do some work. In the
meantime some bugfix on `master` needs to be bacckported in to your
release branch. You can merge the bugfix into `release` branch and also
`merge -s ours` the same branch into your `master`, so when you later
merge the `release` branch again, there are no conflicts from the
bugfix.  

<!-- }}} -->
#### Subtree Merging <!-- {{{ -->
Suppose you want to add remote branch as one of the subdirectories:
```shell
$ git remote add rack_remote https://github.com/rack/rack
$ git fetch rack_remote --no-tags
    ...
$ git checkout -b rack_branch rack_remote/master
$ git checkout master
$ git read-tree --prefix=rack/ -u rack_branch
```
if the Rack project updates, we can pull in upstream changes by
switching to that branch and pulling:
```shell
$ git ckecout rack_branch
$ git pull
```

If you want to merge those changes back into our `master` branch. To
pull in the changes and prepopulate the commit message, use the
`--squash` option, as well as the recursive merge strategy's `-Xsubtree`
option
```shell
$ git checkout master
$ git merge --squash -s recursive -Xsubree=rack rack_branch
Squash commit --not updating HEAD
Automatic merge went well; stopped before committing as requested
```

If you have submodules structure, you cannot run normal `diff`. Instead
you must run `git diff-tree` with the branch you want to compare:
```shell
$ git diff-tree -p rack_branch
```
or
```shell
$ git diff-tree -p rack_remote/master
```



<!-- }}} -->

<!-- }}} -->
### Rerere <!-- {{{ -->
The name stands for "reuse recorded resolution" and, as the name
implies, it allows you to ask Git to remember how you've resolved a hunk
conflict so that next time it sees the same conflict, Git can resolve it
for you automatically.  

To enable `rerere` functionaliry:
```shell
$ git config --global rerere.enabled true
```

Use `git rerere status` to see what it has recorded the pre-merge state:
```shell
$ git rerere status
```

`git rerere diff` will show current state of the resolution

After you resolved conflict, it will be stored in `rerere cache`. And
each time Git sees same conflict, it will automatically resolve it.  
To inspect  conflicted file state use:
```shell
$ git checkout --conflict=merge hello.rb
$ cat hello.rb
    ....
```


<!-- }}} -->
<!-- }}} -->
## Debugging with Git <!-- {{{ -->
### File Annotation <!-- {{{ -->
If you need to see which commit and commiter is responsible for specific
changes in file, use `git blame`:
```shell
$ git blame -L 69,82 Makefile
```

`-C` option analyzes the file and lists all code movement.  

<!-- }}} -->
### Binary Search <!-- {{{ -->
Annotating a file helps if you know hwere the issue is to begin with.If
you don't, you'll likely turn to `git bisect` for help.  

Start `bisect` with:
```shell
$ git bisect start
```
Set end point and start point for binary search:
```shell
$ git bisect bad
$ git bisect good v1.0
```

Then for every commit type either `$ git bisect good` or `$ git bisect
bad`. After Git founds bad commit you will be given detailed information
about it.  

To reset HEAD type:
```shell
$ git bisect reset
```

If you have testing script that returns 0 if project is good and
non-zero if project is broken, if could automate `git bisect`:
```shell
$ git bisect start HEAD v1.0
$ git bisect run test-error.sh
```

<!-- }}} -->
<!-- }}} -->
## Submodules <!-- {{{ -->
Submodules allow you to keep a Git repository as a subdirectory of
another Git repository. This lets you clone another repository and keep
your commits separate.

### Starting with Submodules <!-- {{{ -->
To add new submodule you use the `git submodule add` command. You can
add different path at the end of the command if you want it to go
elsewhere.  

New file created is `.gitmodules`. This is a configuration file that
stores the mapping between the project's URL and hte local subdirectory:
```txt
[submodule "DbConnector"]
    path = DbConnector
    url = https://github.com/chaconinc/DbConnector
```
It's better to use public url in that file. To set private url locally
use `config submodule.DbConnector.url`.  

Git sees submodules simply as commit from specified git repository.  

The `160000` mode means you're recording a commit as a directory entry
rather than a subdirectory or a file.  

<!-- }}} -->
### Cloning a Project with Submodules <!-- {{{ -->
You get all of the directories but they're empty. You must run commands:
`git submodule init` to initialize your local configuration file, and
`git submodule update` to fetch all the data from that project and check
out the appropriate commit listed in your superproject.  

Do all in one step:
```shell
$ git clone --recurse-submodules https://github.com/chaconinc/MainProject
```

If you forgot `--recurse-submodules` option, you may run `git submodule
update --init`. to initialize, fetch and checkout any nested submodules,
you can use `git submodule update --init --recursive`  

<!-- }}} -->
### Working on a Project with Submodules <!-- {{{ -->
#### Pulling in Upstream Changes from the Submodule Remote <!-- {{{ -->
You can update Submodule by simple `cd` into that directory and running
usual Git commands. Afterwards you may go into main project and run `git
diff --submodule` to see commits that were added. If you don't want to
type `--submodule` every time, you can set it as the default format by
setting the `diff.submodule` config value to "log":
```shell
$ git config --global diff.submodule log
$ git diff
    ...
```

Other ways to automatically update:  

+ `git submodule update --remote` - updates all of the submodules  
+ `git submodule update --remote DbConnector`  
+ `git config -f .gitmodules submodule.DbConnector.branch stable` set
  branch for updates. `-f .gitmodules` shares this option.  

`status.submodulesummary` configuration variable tells Git to show you a
short summary of changes to your submodules:
```shell
$ git config status.submodulesummary 1
$ git status
    ...
```

Submodules with Git log: `git log -p --submodule`  


<!-- }}} -->
#### Pulling Upstream Changes from the Project Remote <!-- {{{ -->
Run:  

+ `git pull` fetches submodules but does not update  
+ `git submodule update --init --recursive` updates  

If you want to automate this process, you can add `--recurse-submodules`
flag to the `git pull`command (will run `submodule update` right after `pull`).
Moreover, if you want Git always pull such way, you can set the
configuration option `submodule.recurse` to true.  

If submodules' url changed you must pass `git submodule sync` command  
<!-- }}} -->
#### Working on a Submodule <!-- {{{ -->
If you want changes in submodule to be tracked:  

+ go into each submodule and check out a branch to work on  
```shell
$ cd DbConector/
$ git checkout stable
    ...
```
+ tell Git what to do if you have made chagnes  
    - after changes use `git submodule update --remote --rebase`  
    - if you forget it, just check out your branch again and merge or
  rebase manually
+ `git submodule update --remote`  
    - `--merge` can be usefull  
<!-- }}} -->
<!-- }}} -->
### Submodule Tips <!-- {{{ -->
#### Submodule Foreach <!-- {{{ -->
There's a `foreach` submodule command to run some arbitrary command in
each submodule.  

For example, let's say we want to start a new feature and we have work
going on in several submodules. We can easily stash all the work in all
our submodules:  
```shell
$ git submodule foreach 'git stash'
```

<!-- }}} -->
#### Useful Aliases <!-- {{{ -->
Usefull aliases for working with submodules:  

```shell
$ git config alias.sdiff '!'"git diff && git submodule foreach 'git diff'"
$ git config alias.spush 'push --recurse-submodules=on-demand'
$ git config alias.supdate 'submodule update --remote --merge'
```

<!-- }}} -->
<!-- }}} -->
### Issues with Submodules <!-- {{{ -->
#### Switching branches <!-- {{{ -->
If you init submodule in one branch and switch branches it could be
confusing that submodule still exists.  

Newer Git versions (Git >= 2.13) simplify all this by adding the
`--recurse-submodules` flag to the `git checkout` command.  

In older versions you have to run `git clean -ffdx` in branch without
sumbodule and `git submodule update --init` in branch containing
submodule  

Commits in submodules will be appeared as modified after each checkout
(because submodule state is by default not carried over when switching
branches). For older version you have to run `git submodule update
--init --recursive` every time to put the submodules in the right state.  

For newer versions (Git >= 2.14) to always use the `--recurse-submodules`
flag set configuration option `git config submodule.recurse true`  
<!-- }}} -->
#### Switching from subdirectories to submodules <!-- {{{ -->
First you have to remove directory from index, then you may run `git
submodule add <url>`  

If you checkout to branch that has that directory as well, git will give
you an error. You can force swith by `checkout -f`, but be carefull -
unsaved changes will bel ost.  

Then, if you switch bach, you get an empty directory and `git submodule
update` won't fix it. You may need to go into your submodule directory
and run a `git checkout .` to get all your files back (`submodule
foreach` can be helpfull)  
<!-- }}} -->
<!-- }}} -->
<!-- }}} -->
## Bundling <!-- {{{ -->
The `git bundle` command will package up everything that would normally
be pushed over the wire with a `git push` command into a binary file
that you can email to someone or put on a flash drive, then unbundle
into another repository.  

```shell
$ git bundle create repo.bundle HEAD master
```
now you have a file named `repo.bundle` that has all the data needed to
re-create the repository's `master` branch. With the `bundle` command
you need to list out every reference or specific range of commits that
you want to be included. If you intend for this to be cloned somewhere
else, you should add HEAD as a reference as well as we've done here.  

On the other side:
```shell
$ git clone repo.bundle repo
Cloning into 'repo'...
...
$ cd repo
$ git log --oneline
```

If you odn't include HEAD in the references, you have to also specify
`-b master` or whatever branch is included because otherwise it won't
know what branch to check out.  

Now let's say you do three commits on it and want to send the new
commits back via a bundle on a USB stick or email. First we need to
determine the range of commits we want to include in the bundle. To get
the three commits we can use something like:
```shell
$ git log --oneline master ^origin/master
```
Now we run `git bundle create` command, giving it a filename we want our
bundle to be and the range of commits we want to go into it
```shell
# last commit is origin/master commit
$ git bundle create commits.bundle master ^9a466c5
```

On the other side. `bundle verify` command will make sure the file is
actually a valid Git bundle and that you have all the necessary
ancestors to reconstitute it properly.
```shell
$ git bundle verify ../commits.bundle
```
If you want to see what branches are in the bundle that can be imported,
there is also a command to just list the heads:
```shell
$ git bundle list-heads ../commits.bundle
```
To actually pull or fetch you can use `fetch` or `pull` commands. Here
we'll fetch the `master` branch of the bundle to a branch named
`other-master`:
```shell
$ git fetch ../commits.bundle master:other-master
```

<!-- }}} -->
## Replace <!-- {{{ -->
The `replace` command lets you specify an object in Git and say "every
type you refer to _this_ object, pretend it's a _different_ object".  

Let's try split repository into two repositoryes: one recent and one
historical.  

We'll use a simple repository with five simple commits:
```shell
$ git log --oneline
ef989d8 fifth commit
c6e1e95 fourth commit
9c68fdc third commit
945704c second commit
c1822cf first commit
```
we want to break this up into two lines of history: one line goes from
commit one to commit four - historical one, second line will just be
commits four and five - that will be the recent history.

Creating history is easy:
```shell
# create branch
$ git branch history c6e1e95
# add remote containing history
$ git remote add project-history <url>
# push our history branch to theirs master
$ git push project-history history:master
```

To create smaller history we actually need the base, then rebase fourth
and fifth commits on top of it. Our base commit will be based on third
commit. To do that using `commit-tree` command, which just takes a tree
and will give us a brand new, parentless commit object SHA-1 back.
```shell
$ echo 'base commit message' | git commit-tree 9c68fdc^{tree}
622e88e9cdfbacfb85b5290245b8fb38dfea10cf
```
Ok, so now we have a base commit, we can rebase the rest of our history
on top of that with `git rebase --onto`. The `--onto` argument will be
the SHA-1 we just got back from `commit-tree` and rebase point will be
the third commits (the parent of the first commit we want to keep):
```shell
$ git rebase --onto 622e88 9c68fdc
First,rewinding head to replay your work on top of it...
Applying: fourth commit
Applying: fifth commit
```
Now we have re-written our recent history on top of a throw away base
commit that now has instructions in it on how to reconstitute the entire
history if we wanted to. From now we can push that new history to a new
project and now when people clone that repository, they will only see
the most recent two commits and then a base commit with instructions.  

On the other side. If we want entire history, one would have to add a
second remote for the historical repository and fetch:
```shell
$ git clone https://github.com/schacon/project
$ cd project

$ git log --oneline master
<truncated history>
$ git log --online project-history/master
<full history>
```

To combine them, you can simply call `git replace` with the commit you
want to replace and then the commit you want to replace it with. So we
want to replace the "fourth" commit in the `master` branch with the
"fourth" commit in the `project-history/master` branch:
```shell
$ git replace 81a708d c6e1e95
```

But remember, replaced commit SHA-1 will be still shown in log. Even
if `cat-file` will hsow you the replaced data. And it will be kept in
our references  




<!-- }}} -->
## Credential Storage <!-- {{{ -->
Instead of typing username and password everytime< Git has a few options
provided in the box:  

+ The default is not to cache at all  
+ The "cache" mode keeps credentials in memory for a certain period of
  time. None of the passwords are ever stored on disk, and they are
  purged from the cache after 15 minutes.  
    - accepts the `--timeout <seconds>` option - changes the amount of
  time its daemon is kept running (default "900" or 15 min.)  
+ The "store" mode saves the credentials to a plain-text file on disk,
  and they never expire. You will never have to enter you password.  
    - accepts the `--file <path>` argument, which customizes where the
  plain-text file is saved (default - _~/.git-credentials_)  
+ Mac and Windows has their own mechanism that help with this task.  

To choose one of these methods:
```shell
$ git config --global credential.helper cache
$ git config --global credential.helper 'store --file ~/.my-credentials'
```

Git can even choose possible solution. For example if you have a
credentials file on a thumb drive, but wanted to use thein-memory cache
to save some typing if the drive isn't plugged in:
```txt
[credential]
    helper = store --file /mnt/thumbdrive/.git-credentials
    helper = cache --timeout 30000
```

### Under the Hood <!-- {{{ -->
Root command is `git credential`, you give it all available info and it
prints what it's know about it. If it doesn't, it asks you to fill
fields by yourself.  

Then the credential system is actually invoking a program that's
separate from Git itself; which one and how depends on the
`credential.helper` configuration value. There are several forms it can
take (**configuration value** - **behavior**):  

+ `foo` - runs `git-credential-foo`  
+ `foo -a --opt=bcd` - runs `git-credential-foo -a --opt=bcd`  
+ `/absolute/path/foo -xyz`- runs `/absolute/path/foo -xyz`  
+ `!f() { echo "password=s3cre7"; }; f` - code after `!` evaluated in
  shell  

So the helpers are actually named `git-credential-cache`,
`git-credential-store`. They are take commands:  

+ `get` - is a request for a username/password pair  
+ `store` - is a request to save a set of credentials in this helper's
  memory  
+ `erase` - purge the credentials for the given properties from this
  helper's memory

```shell
$ git credential-store --file ~/git.store store
protocol=https
host=mygithost
username=bob
password=s3cre7
$ git credential-store --file ~/git.store get
protocol=https
host=mygithost

username=bob
password=s3cre7
```

Here's what the `~/git.store` file looks
```txt
https://bob:s3cre7@mygithost
```


<!-- }}} -->
### A Custom Credential Cache <!-- {{{ -->
Covered helpers proveded by Git cover many common use cases, but not
all. For example we need helper for team credentials that are shared
with the entire team, and they're changed often.  

There are sever key concepts:  

1. The only action we need to pay attention to is `get`; `store` and
   `erase` are write operations, so we'll just exit cleanly when they're
   received.  
2. The file format of the shared-credential file is the same as that
   used by `git-credential-store`  
3. The location of that file is fairly standard, but we should allow the
   user to pass a custom path just in case.  
<!-- }}} -->

<!-- }}} -->
<!-- }}} -->
# Customizing Git <!-- {{{ -->

+ introduce several important configuration settings  
+ hooks system  

## Git Configuration <!-- {{{ -->
### Basic Client Configuration <!-- {{{ -->
All git configuration options fall into two categories: cliend-side and
server-side. You can list all available options:
```shell
$ man git-config
```

`core.editor`  
By default, Git uses variables `VISUAL` or `EDITOR`, or else falls back
to the `vi` editor.  
```shell
$ git config --global core.editor emacs
```
Now, no matter what is set as your default shell editor, Git will fire
up Emacs to edit messages  

`commit.template`  
If you set this to the path of a file on your system, Git will use that
file as the fdefault initial message when you commit. The purse of this
file is to remind yourself (or others) of the proper format and style
when creating a commit message.  
For instance, consider a template file at `~/.gitmessage.txt` that looks
like this:
```txt
Subject line (try to keep under 50 characters)

Multi-line description of commit,
feel free to be detailed.

[Ticket: X]
```

`core.pager`  
This setting determines which pages is used when Git pages output such
as `log` and `diff`. You can turn it off by setting it to a blank
string:
```shell
$ git config --global core.pager ''
```

`user.signingkey`
If you're making signed annotated tags, setting your GPG signing key as
a configuration setting makes things easier.
```shell
$ git config --global user.signingkey <gpg-key-id>
```
Now, you can sign tags without having to specify your key every time
with the `git tag` command:
```shell
$ git tag -s <tag-name>
```

`core.excludesfile`  
Global filename patterns to ignore. For example `.DS_Store`
on Max, or `~` or `.swp`when developing in Emacs or in Vim.  
If you Create `~/.gitignore_global` file with these contents:
```txt
*~
.*.swp
.DS_Store
```
and you run `git config --global core.excludesfile ~/.gitignore_global`,
Git will never again bother you about those files  

`help.autocorrect`  
If you mistype a command, it shows you something like this:
```shell
$ git chekcout master
git: 'chekcout' is not a git command. See 'git --help'.

Did you mean this?
    checkout
```
If you set `help.autocorrect` to 1 (it's actually tenths of a seconds
for timeout before running corrected command), Git will
actually run this command for you:
```shell
$ git chekcout master
WARNING: You called a Git command named 'chekcout', which does not exist
Continuing under the assumption thatyou meant 'checkout'
in 0.1 seconds automatically...
```



<!-- }}} -->
### Colors in Git <!-- {{{ -->
A number of options can help you set the coloring you your preference:  

```txt
color.ui
```
To turn off all Git's colored terminal output, do this:
```shell
$ git config --global color.ui false
```
The default setting is `auto` - volotd output when it's going straight
to a terminal, but omits the color-control codes when the output is
redirected to a pipe or a file.  

`always` setting will ignore the difference between terminals and pipes.
You'll rarely want this; in most scenarios it's better to pass `--color`
flag to the Git command to force it to use color codes.  

```txt
color.*
```
If you want to be more specific about which commands are colored and
how, Git provides verb-specific coloring settings. Each of these can be
set to `true`, `false`, or `always`:
```txt
color.branch
color.diff
color.interactive
color.status
```
If addition, each of these has subsettings you can use to set specific
colors for parts of the ouput. For example, to set the meta information
in your diff output to blue foreground, black background, and bold text,
you can run:
```shell
$ git config --global color.diff.meta "blue black bold"
```

Possible color values: `normal`, `black`, `red`, `green`, `yellow`,
`blue`, `magenta`, `cyan`, or `white`. Decorate attribute can be set to:
`bold`, `dim`, `ul` (underline), `blink`, and `reverse` (swap foreground
and background).  

<!-- }}} -->
### External Merge and Diff Tools <!-- {{{ -->
<!-- TODO: stopped here -->
<!-- }}} -->

<!-- }}} -->
<!-- }}} -->
