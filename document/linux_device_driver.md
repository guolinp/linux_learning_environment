# Linux Device Driver

## Install
  ```bash
  $ cd linux_learning_environment
  $ ./script/__setup_project_linux_device_driver 
  clone 'linux_device_driver' project
  Cloning into 'linux_device_driver'...
  remote: Enumerating objects: 296, done.
  remote: Counting objects: 100% (296/296), done.
  remote: Compressing objects: 100% (185/185), done.
  remote: Total 296 (delta 103), reused 296 (delta 103)
  Receiving objects: 100% (296/296), 96.60 KiB | 0 bytes/s, done.
  Resolving deltas: 100% (103/103), done.
  ```

## Compile
  - compile one driver, for example `gfifo`
  ```bash
  $ ./script/compile_drv gfifo
  ```
  - compile all drivers
  ```bash
  $ ./script/compile_drv all
  ```
  - compile test applications
  ```bash
  $ ./script/compile_apps all
  ```
