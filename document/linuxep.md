# Linuxep

## What is the Linuxep?
- ### see page: https://github.com/linuxep/linuxep
- ### `lepd` is application ran in target board, it collects board usage
- ### `lepv` is a client interactives with `lepd`, it may be a web page

## Run `lepd` in qemu board
- ### install the linuxep project, the following script will clone and compile `lepd`
  ```bash
  $ cd linux_learning_environment
  $ $ ./script/__setup_project_linuxep                                    
  clone 'lepd' project
  Cloning into 'lepd'...
  remote: Enumerating objects: 3, done.
  remote: Counting objects: 100% (3/3), done.
  remote: Compressing objects: 100% (3/3), done.
  remote: Total 724 (delta 0), reused 2 (delta 0), pack-reused 721
  Receiving objects: 100% (724/724), 5.49 MiB | 302.00 KiB/s, done.
  Resolving deltas: 100% (373/373), done.
  mkdir -p /repo/guolinp/xLab189/linux_learning_environment/project/lepd/.objs
  mkdir -p /repo/guolinp/xLab189/linux_learning_environment/project/lepd/libs
  ...
  ```

- ### Start linux with QEMU in the first terminal
  ```bash
  $ cd linux_learning_environment
  $ ./script/qemu_linux_start 
  ```

- ### Start `lepd` on qemu board in the second terminal
  ```bash
  $ cd linux_learning_environment
  $ ./script/lepd start
  [lepd] copy /repo/guolinp/xLab189/linux_learning_environment/project/lepd/lepd to guest linux
  #1# check the lepd in current directory
  -rwxr-xr-x 1 guolinp platform 413068 Jan 25 12:58 /repo/guolinp/xLab189/linux_learning_environment/project/lepd/lepd
  #2# start copy...
  #3# check the lepd in guest /share/
  -rwx------    1 root     root        413068 Jan 25 05:01 /share/lepd
  [lepd] start 'lepd' in guest linux
  [lepd] run 'ps' in guest linux
    793 root     /share/lepd
  ```

- ### Test `ledp`
  - note that the `ledp` as a server monitors the tcp port `12307` in guest by default, our qemu start script maps it to host tcp port `22080`
  - use `nc` tool to test, you need to install it in your host
  - run below command in host to get all methods `ledp` supported
  ```bash
  $ echo "{\"method\":\"ListAllMethod\"}"  | nc localhost 22080
  {
          "result":       "SayHello ListAllMethod GetProcMeminfo GetProcLoadavg GetProcVmstat GetProcZoneinfo GetProcBuddyinfo GetProcCpuinfo GetProcSlabinfo GetProcSwaps GetProcInterrupts GetProcSoftirqs GetProcDiskstats GetProcVersion GetProcStat GetProcModules GetCmdIotop GetCmdFree GetCmdProcrank GetCmdIostat GetCmdTop GetCmdDmesg GetCmdDf GetCpuInfo GetCmdMpstat GetCmdMpstat-I GetCmdIrqInfo GetCmdCgtop GetCmdPerfFaults GetCmdPerfCpuclock GetCmdPerfFlame lepdendstring"
  }
  ```
  - run below command in host to get guest memory info
  ```bash
  $ echo "{\"method\":\"GetProcMeminfo\"}" | nc localhost 22080
  {
          "result":       "MemTotal:         218296 kB\nMemFree:          199712 kB\nMemAvailable:     202256 kB\nBuffers:             268 kB\nCached:             1932 kB\nSwapCached:            0 kB\nActive:             2088 kB\nInactive:            524 kB\nActive(anon):        436 kB\nInactive(anon):       24 kB\nActive(file):       1652 kB\nInactive(file):      500 kB\nUnevictable:           0 kB\nMlocked:               0 kB\nSwapTotal:             0 kB\nSwapFree:              0 kB\nDirty:                 0 kB\nWriteback:             0 kB\nAnonPages:           412 kB\nMapped:             1264 kB\nShmem:                48 kB\nSlab:              10256 kB\nSReclaimable:       6588 kB\nSUnreclaim:         3668 kB\nKernelStack:         384 kB\nPageTables:           84 kB\nNFS_Unstable:          0 kB\nBounce:                0 kB\nWritebackTmp:          0 kB\nCommitLimit:      109148 kB\nCommitted_AS:       2128 kB\nVmallocTotal:    1851392 kB\nVmallocUsed:           0 kB\nVmallocChunk:          0 kB\nCmaTotal:              0 kB\nCmaFree:               0 kB\nlepdendstring"
  }
  ```
