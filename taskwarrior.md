# Recurring tasks

+ `task add ... recur:[weekly|daily|monthly|yearly]` - create recurring task  
+ `task all +PARENT` - check existing  
+ `task delete <id>` - delete recurring (or not) task from above list  

[recurring tasks docs](https://taskwarrior.org/docs/durations.html)  

# More info on tasks

+ `task ID modify project:Home` - assign a project  
+ `task ID modify +problem +house` - add tags  
+ `task ID modify depends:OTHER_ID` - add dependency  
