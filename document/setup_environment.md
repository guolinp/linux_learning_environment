# Setup `LLE`(linux learning environment)

- ### Assume that your work directory is `$work-dir`
- ### Run the following commands to make a full setup, this needs lots of minutes, you can take a cup of coffee now.
  ```bash
  $ cd $work-dir
  $ git clone https://gitee.com/guolinp/linux_learning_environment.git
  $ cd linux_learning_environment
  $ ./script/setup_environment
  ```
- ### you can also setup step by step by running below scripts, anyway the `buildroot` is a must.
  ```bash
  $ ./script/__setup_buildroot
  $ ./script/__setup_qemu
  $ ./script/__setup_sshpass
  ...
  ```
- ### if you encounter errors such as some packages missed in you host/pc, resolve it by yourself, sorry.
