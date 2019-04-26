# Move file between host and guest linux

- ### start `Linux` in QEMU
  ```bash
  $ cd linux_learning_environment
  $ ./script/qemu_linux_start
  ```

- ### copy a file to the dir `/share/` in guest
  ```bash
  $ cd linux_learning_environment
  $ ./script/copy_to_linux testfile
  
  #1# check the testfile in current directory
  -rw-rw-r-- 1 panguolin panguolin 0 1月  20 14:10 ./testfile
  #2# start copy...
  #3# check the testfile in guest /share/
  -rw-------    1 root  root  0 Jan 20 06:18 /share/testfile
  ```

- ### copy a file from the dir `/share/` in guest to host current dir
  ```bash
  $ cd linux_learning_environment
  $ ./script/copy_from_linux testfile
  
  #1# check the testfile in guest /share/
  -rw-------    1 root  root  0 Jan 20 06:18 /share/testfile
  #2# start copy...
  #3# check the testfile in current directory
  -rw-rw-r-- 1 panguolin panguolin 0 1月  20 14:18 ./testfile
  ```
