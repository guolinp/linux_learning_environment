# TBOT test framework

## What is the tbot?
`tbot` is a testing/automation tool that is focused on usage in embedded development. At its core `tbot` just provides utilities for interaction with remote hosts/targets and an extensive library of routines that are common in embedded development/testing. `tbot` aims to be a support for the developer while working on a project and without much modification also allow running tests in an automated setting.

## What does in the framework?
- ### Some utility scripts were added to make test case be ran simplify with `tbot` , go to below directory to check.
  ```bash
  $ cd linux_learning_environment/tbot_testcase
  $ tree
  .
  ├── board_qemu.py
  ├── lab_qemu.py
  ├── ls_testcases
  ├── run_all_testcases
  ├── run_one_testcase
  ├── testcases
  │   ├── tc_qemu_linux_file_operation.py
  │   |── tc_qemu_linux_uname.py
  │   └── tc_qemu_uboot_version.py
  └── userconfig.py
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
  # the host IP where tbot-docker running
  # should NOT use loopback IP
  hostname = "xxx.xxx.xxx.xxx"
  
  # the user name to ssh login host
  username = "your_login_username"
  
  # the password of username
  password = "******"
  
  # commands/script from your host
  uboot_connection_command = "/path/to/linux_learning_environment/script/qemu_uboot_start"
  linux_connection_command = "/path/to/linux_learning_environment/script/qemu_linux_start"
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
    qemu_linux_file_create
    qemu_linux_file_read_write
    qemu_linux_uname
    qemu_uboot_version
    ```
  
  - #### run existed user test cases
    ```bash
    bash-4.4# ./run_one_testcase qemu_linux_uname
    tbot starting ...
    ├─Calling qemu_linux_uname ...
    │   ├─POWERON (Qemu-Board)
    │   ├─Not support 'poweron' command for Qemu-Board
    │   ├─LINUX (Qemu-Board-linux)
    the output of 'uname -n' on board:  buildroot
    
    │   ├─POWEROFF (Qemu-Board)
    │   ├─Not support 'poweroff' command for Qemu-Board
    │   └─Done. (12.830s)
    ├─────────────────────────────────────────
    ├─Log written to '/tbot/tbot-testcases/log/lab_qemu-board_qemu-0001.json'
    └─SUCCESS (13.031s)
    ```
  
## Create your test case, for example show free memory
  - ### go to dir `/tbot/testcases/testcases`
  - ### copy `tc_qemu_linux_uname.py` to `tc_qemu_linux_show_free_memory.py`
      ```python
      import contextlib
      import typing
      import tbot
      from tbot.machine import board
      
      @tbot.testcase
      def qemu_linux_uname(
          lab: typing.Optional[tbot.selectable.LabHost] = None,
          board_linux: typing.Optional[board.LinuxMachine] = None,
      ) -> None:
          with contextlib.ExitStack() as cx:
              lh = cx.enter_context(lab or tbot.acquire_lab())
              if board_linux is not None:
                  lnx = board_linux
              else:
                  b = cx.enter_context(tbot.acquire_board(lh))
                  lnx = cx.enter_context(tbot.acquire_linux(b))
      
            out = lnx.exec0("uname", "-n")
            print("the output of 'uname -n' on board: ", out)
      ```
  - ### change the test name from `qemu_linux_uname` to `qemu_linux_show_free_memory`
  - ### modify the last two lines to:
      ```python
      out = lnx.exec0("free", "-m")
      print("the output of 'free -m' on board: ", out)
      ```
  - ### then, run it with command
    ```bash
    bash-4.4# ./run_one_testcase qemu_linux_show_free_memory
    ```
    
## Run all test cases
- ### In host, run `./script/tbot_run_testcase`
  ```bash
  $ cd linux_learning_environment
  $ ./script/tbot_run_testcase 
  tbot starting ...
  ├─Calling qemu_linux_file_create ...
  │   ├─POWERON (Qemu-Board)
  │   ├─Not support 'poweron' command for Qemu-Board
  │   ├─LINUX (Qemu-Board-linux)
  │   ├─POWEROFF (Qemu-Board)
  │   ├─Not support 'poweroff' command for Qemu-Board
  │   └─Done. (1.031s)
  ├─────────────────────────────────────────
  ├─Log written to '/tbot/log/lab_qemu-board_qemu-0001.json'
  └─SUCCESS (1.262s)
  tbot starting ...
  ├─Calling qemu_linux_file_read_write ...
  │   ├─POWERON (Qemu-Board)
  │   ├─Not support 'poweron' command for Qemu-Board
  │   ├─LINUX (Qemu-Board-linux)
  │   ├─POWEROFF (Qemu-Board)
  │   ├─Not support 'poweroff' command for Qemu-Board
  │   └─Done. (1.074s)
  ├─────────────────────────────────────────
  ├─Log written to '/tbot/log/lab_qemu-board_qemu-0002.json'
  └─SUCCESS (1.273s)
  tbot starting ...
  ├─Calling qemu_linux_uname ...
  │   ├─POWERON (Qemu-Board)
  │   ├─Not support 'poweron' command for Qemu-Board
  │   ├─LINUX (Qemu-Board-linux)
  the output of 'uname -n' on board:  buildroot
  
  │   ├─POWEROFF (Qemu-Board)
  │   ├─Not support 'poweroff' command for Qemu-Board
  │   └─Done. (0.944s)
  ├─────────────────────────────────────────
  ├─Log written to '/tbot/log/lab_qemu-board_qemu-0003.json'
  └─SUCCESS (1.150s)
  ```

