<!-- ended on https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs -->
<!-- header: Modifying the Journal Display -->
By default _journalctl_ will show logs in pager (_less_).  

+ `journalctl -b` - show info starting from boot  

Days are splitted by - `-- Reboot --` string  

+ `journalctl --list-boots`- shows boots, their ids and date  
    For instance, to see the journal from the previous boot, use `-1`
    relative pinter with the `-b` flag:  
    `journalctl -b -1`  
    `journalctl -b caf0524a1d394ce0bdbcff75b94444fe`  

Time Windows<!-- {{{ -->
============

You may use `--sunce` and `--until` options - after or beforethe given
time, respectively.  
**_Time values_** can come in a variety of formats.  

+ absolute time values: `YYYY-MM-DD HH:MM:SS`  
    * if left default values would be applied to commponents  
    * curent date if date is missing  
    * 00:00:00 if time is missing  
+ understands some relative vallues and named shortucts: yesterday,
  today, now, you do relative time by prepending "-" or "+"  
    `journalctl --since yesterday`  
    `journalctl --since 09:00 --until "1 hour ago"`  
<!-- }}} -->
Filtering by Message Interest<!-- {{{ -->
=============================
### By Unit<!-- {{{ -->

Use `-u` option to filter this way.  
To see all of the logs from an Ngingx unit:  
`journalctl -u nginx.service`  

You may merge the entries from both services in chonologival order:  
`journalctl -u nginx.service -u php-fpm.service --since today`  
<!-- }}} -->
### By Process, User, or Group ID<!-- {{{ -->

If you know PID of process you want to monitor. Use `_PID` option:  
`journalctl _PID=8088`  

If you know user id or user group: `_UID` or `_GID` options as above.  

The `-F` option shows all of the available values for a given journal
field.  
`journalctl -F _GID`  
<!-- }}} -->
### By Component Path <!-- {{{ -->
For instance, to find those entries that involve the `bash` executable,
you can type:  
`journalctl /usr/bin/bash`  
<!-- }}} -->
### Displaying Kernel Messages <!-- {{{ -->
Add `-k` or `--dmesg` flags to your command:  
`journalctl -k`  
By default this will display thekernel messages from thecurrent boot.  
<!-- }}} -->
### By Priority <!-- {{{ -->
You can use `journalctl` to display only messages of a specified
priority or above by using the `-p` option. This allows you to filter
out lower priority messages.  
For example, to show only entries logged at the error level or above,
type:  
`journalctl -p err -b`  

You can use either the priority name of its corresponding numeric value.
In order of highest to loves priority, these are:  

+ 0: emerg  
+ 1: alert  
+ 2: crit  
+ 3: err  
+ 4: warning  
+ 5: notice  
+ 6: info  
+ 7: debug  
<!-- }}} -->
### Help<!-- {{{ -->
You cann find out about all of the available journal fields by typing:  
`man systemd.journal-fields`  
<!-- }}} -->
<!-- }}} -->
