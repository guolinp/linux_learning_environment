# TBOT test framework

## What is the tbot?
`tbot` is a testing/automation tool that is focused on usage in embedded development. At its core `tbot` just provides utilities for interaction with remote hosts/targets and an extensive library of routines that are common in embedded development/testing. `tbot` aims to be a support for the developer while working on a project and without much modification also allow running tests in an automated setting.

## What does in the framework?
- ### Some utility scripts were added to make test case be ran simplify with `tbot` , go to below directory to check.
  ```bash
  $ cd linux_learning_environment/tbot_testcase
  $ tree
  .
  ├── board.py
  ├── lab.py
  ├── ls_testcases
  ├── run_all_testcases
  ├── run_one_testcase
  ├── tc_config.py
  └── testcases
      ├── tc_qemu_linux_testcases.py
      └── tc_qemu_uboot_testcases.py
  ```
- ### Because the `tbot` installation is not easy, a docker image was introduced which contains all of `tbot` stuffs.
  - the `tbot` docker: https://github.com/guolinp/tbot_docker


## Run test case
- ### Get docker image, use `sudo` if need
  ```bash
  $ docker pull panguolin/tbot
  ```

- ### Config `tbot` settings in file `userconfig.py`
  ```bash
  # Host: ip, username, password
  hostname = "xxx.xxx.xxx.xxx"
  username = "xxxxxxxxxxxxxxx"
  password = "xxxxxxxxxxxxxxx"
  
  # This command will be ran in Host
  connect_board_command = "/path/to/linux_learning_environment/script/qemu_uboot_start"
  ```

- ### Start `tbot` docker container
  ```bash
  $ cd linux_learning_environment
  $ ./script/tbot_start_docker
  bash-4.4#
  ```

- ### In container shell
  - #### run tbot selftest
    ```bash
    bash-4.4# tbot selftest
    tbot starting ...
    ├─Calling selftest ...
    │   ├─Calling testsuite ...
    │   │   ├─Calling selftest_failing ...
    │   │   │   ├─Calling inner ...
    │   │   │   │   └─Fail. (0.000s)
    │   │   │   └─Done. (0.001s)
    │   │   ├─Calling selftest_uname ...
    │   │   │   └─Done. (0.002s)
    │   │   ├─Calling selftest_user ...
    │   │   │   └─Done. (0.001s)
    │   │   ├─Calling selftest_machine_reentrant ...
    │   │   │   └─Done. (0.001s)
    │   │   ├─Calling selftest_machine_labhost_shell ...
    │   │   │   ├─Calling selftest_machine_shell ...
    │   │   │   │   ├─Testing command output ...
    │   │   │   │   ├─Testing return codes ...
    │   │   │   │   ├─Testing env vars ...
    │   │   │   │   ├─Testing redirection (and weird paths) ...
    │   │   │   │   ├─Testing formatting ...
    │   │   │   │   ├─Testing subshell ...
    │   │   │   │   └─Done. (0.029s)
    │   │   │   ├─Calling selftest_machine_channel ...
    │   │   │   │   └─Done. (0.001s)
    ...
    ```
  - #### list existed user testcases
    ```bash
    bash-4.4# cd /tbot/testcases
    bash-4.4# ./ls_testcases 
    qemu_linux_testcases
    qemu_uboot_testcases
    ```
  
  - #### run existed user testcase
    ```bash
    bash-4.4# run_one_testcase qemu_linux_testcases
    tbot starting ...
    ├─Calling qemu_linux_testcases ...
    │   ├─POWERON (QemuBoard)
    │   ├─Not support 'poweron' command for QemuBoard
    │   ├─UBOOT (QemuBoard-uboot)
    │   ├─LINUX (QemuBoard-linux)
    │   ├─Calling testsuite ...
    │   │   ├─Calling linux_verify_uname ...
    │   │   │   └─Done. (0.054s)
    │   │   ├─Calling linux_regular_file_operations ...
    │   │   │   └─Done. (0.219s)
    │   │   ├─────────────────────────────────────────
    │   │   │ Success: 2/2 tests passed
    │   │   └─Done. (0.275s)
    │   ├─POWEROFF (QemuBoard)
    │   ├─Not support 'poweroff' command for QemuBoard
    │   └─Done. (21.685s)
    ├─────────────────────────────────────────
    ├─Log written to '/log/qemu_linux_testcases.log'
    └─SUCCESS (21.888s)
    ```
  
## Run all testcases
- ### In host, run `./script/tbot_run_testcase`
  ```bash
  $ cd linux_learning_environment
  $ ./script/tbot_run_testcase 
  tbot starting ...
  ├─Calling qemu_linux_testcases ...
  │   ├─POWERON (QemuBoard)
  │   ├─Not support 'poweron' command for QemuBoard
  │   ├─UBOOT (QemuBoard-uboot)
  │   ├─LINUX (QemuBoard-linux)
  │   ├─Calling testsuite ...
  │   │   ├─Calling linux_verify_uname ...
  │   │   │   └─Done. (0.054s)
  │   │   ├─Calling linux_regular_file_operations ...
  │   │   │   └─Done. (0.219s)
  │   │   ├─────────────────────────────────────────
  │   │   │ Success: 2/2 tests passed
  │   │   └─Done. (0.275s)
  │   ├─POWEROFF (QemuBoard)
  │   ├─Not support 'poweroff' command for QemuBoard
  │   └─Done. (21.685s)
  ├─────────────────────────────────────────
  ├─Log written to '/log/qemu_linux_testcases.log'
  └─SUCCESS (21.888s)
  tbot starting ...
  ├─Calling qemu_uboot_testcases ...
  │   ├─POWERON (QemuBoard)
  │   ├─Not support 'poweron' command for QemuBoard
  │   ├─UBOOT (QemuBoard-uboot)
  │   ├─Calling testsuite ...
  │   │   ├─Calling uboot_verify_version ...
  │   │   │   └─Done. (0.015s)
  │   │   ├─────────────────────────────────────────
  │   │   │ Success: 1/1 tests passed
  │   │   └─Done. (0.016s)
  │   ├─POWEROFF (QemuBoard)
  │   ├─Not support 'poweroff' command for QemuBoard
  │   └─Done. (0.605s)
  ├─────────────────────────────────────────
  ├─Log written to '/log/qemu_uboot_testcases.log'
  └─SUCCESS (0.810s)
  ```
