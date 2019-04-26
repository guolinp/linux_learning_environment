# Run Linux in QEMU

- ### To make sure the buildroot be installed and compiled
- ### Run the following script to start `Linux`
  ```bash
  $ cd linux_learning_environment
  $ ./script/qemu_linux_start
  ```
- ### The output of `Linux`
  ```bash
  Booting Linux on physical CPU 0x0
  Linux version 4.16.7 (guolinp@FNSHA189) (gcc version 7.3.0 (Buildroot 2018.11.1-g91a13a6-dirty)) #1 SMP Mon Jan 21 10:54:47 CST 2019
  CPU: ARMv7 Processor [410fc090] revision 0 (ARMv7), cr=10c5387d
  CPU: PIPT / VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
  OF: fdt: Machine model: V2P-CA9
  Memory policy: Data cache writeback
  CPU: All CPU(s) started in SVC mode.
  ...
  
  adding dns 10.0.2.3
  OK
  No persistent location to store SSH host keys. New keys will be
  generated at each boot. Are you sure this is what you want to do?
  Starting dropbear sshd: OK
  
  Welcome to Buildroot
  buildroot login:
  ```
