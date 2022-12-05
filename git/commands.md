# Dictionary

+ _Remote branch_: just pointer that tracks last commit on server  
+ _Tracking branch_: branch that compared to an _upstream branch_ (for example, initially, you master branch is _tracking_ remote branch _origin/master_ (it is upstream for your _master_ branch)). Running `git pull` git knows which remote and which brunch to merge  

# Remote branches

Remote branches is nothing but a pointer to last commit, pushed on remote  

+ `git push <remote> <localbranch>:<remotebranch>`: push localbranch and name it with another name on remote server  
+ `git fetch --all`: fetch all remotes, also fetches __pointers__ to branches on remote  
+ `git checkout <remotebranch>`
+ `git checkout -b <localbranch> <remote>/<remotebranch>`: create local copy from remote branch (because remote branch is just pointer, you can't just edit it). Automatically creates " _tracking branch_ " (the branch it tracks is called an " _upstream branch_ ")  
+ `git branch -u <remote>/<remotebranch>`: set _upstream_ branch  
+ `git merge @{u}`: merge _upstream_ branch into your current branch  
+ `git push <remote> --detele <remotebranch>`: delete branch from the server  

# Rebase

Use locally to ensure that you branch is perfectly applies to master branch. Create topic branch, add commits, rebase topic branch onto master branch so, when pushing, anyone can just fast-forward.  

+ `git rebase <branch>`: reapply all patches beginning from common ancestor on branch with current branch (all patches of current branch).  
+ `git rebase <target> <source>`: reapply all patches starting from common ancestor of `<target>` and `<source>` branches up to end of `<source>` branch.  
+ `git rebase --onto <branch> <firstbranch> <lastbranch>`: find the common ancestor of last two branches and reapply all patches up to `<lastbranch>` onto `<branch>`.  
+ `git pull --rebase`: reapply your changes from current branch on remote branch. For example: when you have master branch that is ahead two and behind one commit from _upstream_, you can do `git rebase <remote>/<remotebranch>` or `git rebase @{u}` and history will look like you wrote changes right on top of the master (so you don't need to do extra merge)  

`git config --global pull.rebase true` to make `git pull --rebase` default action while pulling.  
