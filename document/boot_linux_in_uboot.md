# Boot linux in uboot shell from SD

- ## Run uboot with QEMU
  ```bash
  $ ./script/qemu_uboot_start 
  U-Boot 2018.09 (Jan 21 2019 - 10:35:40 +0800)
  
  DRAM:  256 MiB
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

- ## Run below commands
  - The raw commands
    ```bash
    setenv bootargs 'root=/dev/mmcblk0 rw console=ttyAMA0 init=/linuxrc'
    ext2load mmc 0:0 0x60100000 /boot/uImage
    ext2load mmc 0:0 0x60600000 /boot/vexpress-v2p-ca9.dtb
    bootm 0x60100000 - 0x60600000
    ```
  - You can also use `run bootcmd`
  
- ## The boot logs
  ```bash
  => setenv bootargs 'root=/dev/mmcblk0 rw console=ttyAMA0 init=/linuxrc'
  => ext2load mmc 0:0 0x60100000 /boot/uImage
  3678472 bytes read in 1298 ms (2.7 MiB/s)
  => ext2load mmc 0:0 0x60600000 /boot/vexpress-v2p-ca9.dtb
  14457 bytes read in 126 ms (111.3 KiB/s)
  => bootm 0x60100000 - 0x60600000
  ## Booting kernel from Legacy Image at 60100000 ...
     Image Name:   Linux-4.16.7
     Image Type:   ARM Linux Kernel Image (uncompressed)
     Data Size:    3678408 Bytes = 3.5 MiB
     Load Address: 60100000
     Entry Point:  60100000
     Verifying Checksum ... OK
  ## Flattened Device Tree blob at 60600000
     Booting using the fdt blob at 0x60600000
     Loading Kernel Image ... OK
     Loading Device Tree to 6feee000, end 6fef4878 ... OK
  
  Starting kernel ...
  
  Booting Linux on physical CPU 0x0
  Linux version 4.16.7 (guolinp@FNSHA189) (gcc version 7.3.0 (Buildroot 2018.11.1-g91a13a6-dirty)) #1 SMP Thu Jan 24 16:05:30 CST 2019
  CPU: ARMv7 Processor [410fc090] revision 0 (ARMv7), cr=10c5387d
  CPU: PIPT / VIPT nonaliasing data cache, VIPT nonaliasing instruction cache
  
  ...
  
  Welcome to Buildroot
  buildroot login: root
  Password: 
  # 
  ```
