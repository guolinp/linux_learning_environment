# smem memory reporting tool

## What is the smem?
- ### `smem` is a tool that can give numerous reports on memory usage on Linux systems.
- ### link: https://www.selenic.com/smem

## Install smem
- ### the `smem` is installed by default in script `script/setup_environment`
- ### if you have not installed it, run the script:
  ```bash
  $ ./script/__setup_smem
  ```
- ### the `smemcap` is ran on target board to collect board memory usage, the `smem` is a script ran on host to parse the report
  ```bash
  $ ls software/smem-1.4 
  COPYING  smem  smem.8  smemcap  smemcap.c
  ```
## Example
- Start linux in QEMU
   ```bash
   $ ./script/qemu_linux_start 
   ```
- Copy `smemcap` to guest linux
   ```bash
   $ ./script/copy_to_linux software/smem-1.4/smemcap
   #1# check the smemcap in current directory
   -rwxr-xr-x 1 guolinp platform 7716 Jan 28 13:00 software/smem-1.4/smemcap
   #2# start copy...
   #3# check the smemcap in guest /share/
   -rwx------    1 root     root          7716 Jan 29 00:59 /share/smemcap
   ```
- Run `smemcap` in guest linux
   ```bash
   $ ./script/login_linux 
   # cd /share
   # ./smemcap > capdata.gz
   # exit
   ```
- Copy `capdata.gz` to host
   ```bash
   $ ./script/copy_from_linux capdata.gz
   #1# check the capdata.gz in guest /share/
   -rw-r--r--    1 root     root        239616 Jan 29 01:00 /share/capdata.gz
   #2# start copy...
   #3# check the capdata.gz in current directory
   -rw-r--r-- 1 guolinp platform 239616 Jan 29 09:01 ./capdata.gz
   ```
- Generate report with `smem` in host, see help for more details
   ```bash
   $ ./software/smem-1.4/smem -S capdata.gz -s pid -t
     PID User     Command                         Swap      USS      PSS      RSS 
       1 0        init                               0       56      154      748 
     726 0        /sbin/syslogd -n                   0      116      237      884 
     729 0        /sbin/klogd -n                     0       48      169      816 
     778 0        udhcpc -R -n -p /var/run/ud        0      120      175      564 
     786 0        /usr/sbin/dropbear -R              0       36      194      672 
     787 0        /sbin/getty -L ttyAMA0 0 vt        0       60      161      768 
     794 0        /usr/sbin/dropbear -R              0       64      222      700 
     795 0        -sh                                0      132      254      904 
     797 0        ./smemcap                          0      108      155      524 
   -------------------------------------------------------------------------------
       9 1                                           0      740     1721     6580 
   ```

## Script `script/smem`
- It has most steps in above example
- Start linux in QEMU
   ```bash
   $ ./script/qemu_linux_start 
   ```
- Run `script/smem`
   ```bash
   $ ./script/smem 
   [smem] copy ....../linux_learning_environment/software/smem-1.4/smemcap to guest linux
   #1# check the smemcap in current directory
   -rwxr-xr-x 1 guolinp platform 7716 Jan 28 13:00 ....../linux_learning_environment/software/smem-1.4/smemcap
   #2# start copy...
   #3# check the smemcap in guest /share/
   -rwx------    1 root     root          7716 Jan 29 01:05 /share/smemcap
   [smem] start 'smemcap' in guest linux
   [smem] run 'ls -l /share/capdata.gz' in guest linux
   -rw-r--r--    1 root     root        225280 Jan 29 01:05 /share/capdata.gz
   [smem] copy '/share/capdata.gz' to here
   #1# check the capdata.gz in guest /share/
   -rw-r--r--    1 root     root        225280 Jan 29 01:05 /share/capdata.gz
   #2# start copy...
   #3# check the capdata.gz in current directory
   -rw-r--r-- 1 guolinp platform 225280 Jan 29 09:05 ./capdata.gz
   [smem] show report
   
     PID User     Command                         Swap      USS      PSS      RSS 
       1 0        init                               0       56      167      700 
     726 0        /sbin/syslogd -n                   0      116      271      884 
     728 0        /sbin/klogd -n                     0       48      203      816 
     777 0        udhcpc -R -n -p /var/run/ud        0      120      189      572 
     783 0        /usr/sbin/dropbear -R              0       36      206      676 
     784 0        /sbin/getty -L ttyAMA0 0 vt        0       60      172      708 
     791 0        /usr/sbin/dropbear -R              0       64      234      704 
     792 0        /share/smemcap                     0      108      154      464 
   -------------------------------------------------------------------------------
       8 1                                           0      608     1596     5524 
   
   Map                                       PIDs   AVGPSS      PSS 
   [sigpage]                                    8        0        0 
   [vdso]                                       8        0        0 
   [vectors]                                    8        0        0 
   [vvar]                                       8        0        0 
   /share/smemcap                               1       12       12 
   [stack]                                      8        7       60 
   /lib/ld-uClibc-1.0.30.so                     8       10       80 
   [heap]                                       7       18      128 
   <anonymous>                                  8       16      132 
   /usr/sbin/dropbear                           2      108      216 
   /lib/libuClibc-1.0.30.so                     8       55      447 
   /bin/busybox                                 5      104      521 
   
   User     Count     Swap      USS      PSS      RSS 
   0            8        0      608     1596     5524 
   
   Area                           Used      Cache   Noncache 
   firmware/hardware                 0          0          0 
   kernel image                      0          0          0 
   kernel dynamic memory         16572       7160       9412 
   userspace memory               1536       1104        432 
   free memory                  200188     200188          0 
   [smem] remove 'capdata.gz'
   ```

