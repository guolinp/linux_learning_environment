# Run uboot or linux with a pty

## install pty_connecter tool
```bash
$ cd linux_learning_environment
$ ./script/__setup_pty_connecter
```

## u-boot
- Run script `pty_run_uboot` to start in the first terminal. press `ctrl+c` to exit.
```bash
$ cd linux_learning_environment
$ ./script/pty_run_uboot 
create pty: ./script/board_uboot.tty --> /dev/pts/45
```
- In the second terminal, run script `pty_access_uboot` to access uboot. press `ctrl+c` to disconnect.
```bash
$ cd linux_learning_environment
$ ./script/pty_access_uboot
=> help
?       - alias for 'help'
base    - print or set address offset
bdinfo  - print Board Info structure
...
```

## linux
- Run script `pty_run_linux` to start in the first terminal. press `ctrl+c` to exit.
```bash
$ cd linux_learning_environment
$ ./script/pty_run_linux 
create pty: ./script/board_linux.tty --> /dev/pts/45
```
- In the second terminal, run script `pty_access_linux` to access linux. press `ctrl+c` to disconnect.
```bash
$ cd linux_learning_environment
$ ./script/pty_access_linux
...
Booting Linux on physical CPU 0x0
Linux version 4.16.7 (guolinp@FNSHA189) (gcc version 7.3.0 (Buildroot 2018.11.1-g91a13a6-dirty)) #1 SMP Mon Jan 21 10:54:47 CST 2019
...
```
