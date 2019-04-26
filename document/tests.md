# Tests Examples

## Install `tests` project
  ```bash
  $ cd linux_learning_environment
  $ ./script/__setup_project_tests
  ```

## Compile tests
  ```bash
  $ cd linux_learning_environment/project/tests
  $ ./build_tests.sh
  ```

## Valgrind test
  - copy test app to guest
  ```bash
  $ ./script/copy_to_linux project/tests/valgrind/test_memory_leak
  ```
  - in guest linux
  ```bash
  # cd /share/
  # valgrind --leak-check=yes ./test_memory_leak 

  ==1406== Invalid read of size 4
  ==1406==    at 0x4000F70: ??? (in /lib/ld-uClibc-1.0.30.so)
  ==1406==  Address 0x7d914c34 is on thread 1's stack
  ==1406==  20 bytes below stack pointer
  ==1406== 
  /share/test_memory_leak: can't resolve symbol '__libc_freeres'
  ==1406== 
  ==1406== HEAP SUMMARY:
  ==1406==     in use at exit: 32 bytes in 1 blocks
  ==1406==   total heap usage: 1 allocs, 0 frees, 32 bytes allocated
  ==1406== 
  ==1406== 32 bytes in 1 blocks are definitely lost in loss record 1 of 1
  ==1406==    at 0x482C83C: malloc (in /usr/lib/valgrind/vgpreload_memcheck-arm-linux.so)
  ==1406== 
  ==1406== LEAK SUMMARY:
  ==1406==    definitely lost: 32 bytes in 1 blocks
  ==1406==    indirectly lost: 0 bytes in 0 blocks
  ==1406==      possibly lost: 0 bytes in 0 blocks
  ==1406==    still reachable: 0 bytes in 0 blocks
  ==1406==         suppressed: 0 bytes in 0 blocks
  ==1406== 
  ==1406== For counts of detected and suppressed errors, rerun with: -v
  ==1406== ERROR SUMMARY: 49 errors from 5 contexts (suppressed: 0 from 0)
  ```

## Test-tlb
  - copy apps to guest linux
  ```bash
  $ ./script/copy_to_linux project/tests/testtlb/test.sh
  $ ./script/copy_to_linux project/tests/testtlb/test-tlb
  ```
  - in guest linux
  ```bash
  # cd /share/
  # ./test.sh 
  4k:
    7.52ns (~29.3 cycles)
    7.50ns (~29.2 cycles)
    7.51ns (~29.3 cycles)
    7.54ns (~29.4 cycles)
  8k:
    7.47ns (~29.1 cycles)
    7.49ns (~29.2 cycles)
    7.45ns (~29.1 cycles)
    7.47ns (~29.1 cycles)
  16k:
  ...
  ```
