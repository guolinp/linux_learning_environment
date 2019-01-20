# Run Linux in QEMU

- ### To make sure the buildroot be installed and compiled
- ### Run the following script to start `Linux`
  ```bash
  $ cd linux_learning_environment
  $ ./script/qemu_linux_start
  ```
- ### The output of `Linux`
  ```bash
  ===================================
  ====  QEMU: Linux is starting  ====
  ====  Press Ctrl+A+X to exit   ====
  ===================================
  
  pulseaudio: set_sink_input_volume() failed
  pulseaudio: Reason: Invalid argument
  pulseaudio: set_sink_input_mute() failed
  pulseaudio: Reason: Invalid argument
  Booting Linux on physical CPU 0x0
  Linux version 4.16.7 (panguolin@panguolin-vm) (gcc version 7.3.0 (Buildroot 2018.11.1)) #1 SMP Sat Jan 19 21:50:29 CST 2019
  CPU: ARMv7 Processor [410fc090] revision 0 (ARMv7), cr=10c5387d
  CPU: PIPT / VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
  OF: fdt: Machine model: V2P-CA9
  
  ...
  
  adding dns 10.0.2.3
  OK
  No persistent location to store SSH host keys. New keys will be
  generated at each boot. Are you sure this is what you want to do?
  Starting dropbear sshd: OK
  
  Welcome to Buildroot
  buildroot login:
  ```
  
- ### SSH login `Linux`, in a new terminal
  ```bash
  $ cd linux_learning_environment
  $ ./script/login_linux
  # uname -a
  Linux buildroot 4.16.7 #1 SMP Sat Jan 19 21:50:29 CST 2019 armv7l GNU/Linux
  ```
  
- ### Copy a file to the dir `/share/` in guest
  ```bash
  $ cd linux_learning_environment
  $ ./script/copy_to_linux testfile
  
  #1# check the testfile in current directory
  -rw-rw-r-- 1 panguolin panguolin 0 1月  20 14:10 ./testfile
  #2# start copy...
  #3# check the testfile in guest /share/
  -rw-------    1 root  root  0 Jan 20 06:18 /share/testfile
  ```

- ### Copy a file from the dir `/share/` in guest to host current dir
  ```bash
  $ cd linux_learning_environment
  $ ./script/copy_from_linux testfile
  
  #1# check the testfile in guest /share/
  -rw-------    1 root  root  0 Jan 20 06:18 /share/testfile
  #2# start copy...
  #3# check the testfile in current directory
  -rw-rw-r-- 1 panguolin panguolin 0 1月  20 14:18 ./testfile
  ```
