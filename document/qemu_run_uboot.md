# Run u-boot in QEMU

- ### To make sure the buildroot be installed and compiled
- ### Run the following script to start `u-boot`
  ```bash
  $ cd linux_learning_environment
  $ ./script/qemu_uboot_start 
  ```
- ### The output of u-boot
  ```bash
  U-Boot 2018.09 (Jan 19 2019 - 21:46:35 +0800)
  
  DRAM:  512 MiB
  WARNING: Caches not enabled
  Flash: 128 MiB
  MMC:   MMC: 0
  *** Warning - bad CRC, using default environment
  
  In:    serial
  Out:   serial
  Err:   serial
  Net:   smc911x-0
  Hit any key to stop autoboot:  0 
  => 
  ```
