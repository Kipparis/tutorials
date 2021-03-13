Overall:

+ `fsck` - fixes filesystem, input/output errors.  
+ `chroot` - allows you to change login into mounted system and update
  system from within.  
+ `/etc/fstab` - entries shows what system sees when booting  
+ `fdisk -l`, `blkid` - shows mounted drives  
+ `lsusb` - shows what in usb (if you doesn't see with previous)  

full upgrade pacman and it's mirrors:
```shell

# pacman-mirrors -f && sudo pacman -Syyu
```




### Failed to start file system and dependency failed /home
Mount from live cd and:  

+ check matching entries in `/etc/fstab` and from command `blkid`  
+ `fdisk -l` will give you additional info on what to google  
+ `fsck -y /dev/<broken_partition>` **must fix problem**  


### Can't boot, `<important.so>` not fount
Mount from live cd then:  

+ `chroot` into broken partition  
+ `"update mirrors" && pacman -Syyu` - full system update **must fix
  problem**  


### Hard drive cannot be mounted but seen with `lsusb`
Not enough power to transfer info.  
