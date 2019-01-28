import contextlib
import typing
import stat
import tbot
from tbot.machine import board
from tbot.machine import linux


@tbot.testcase
def linux_verify_uname(
    lnx: typing.Optional[linux.LinuxMachine]
) -> None:
    out = lnx.exec0("uname", "-n").strip()
    assert out == "buildroot", repr(out)


@tbot.testcase
def linux_regular_file_operations(
    lnx: typing.Optional[linux.LinuxMachine]
) -> None:
    # create 'testfile'
    f = lnx.workdir / "testfile"
    lnx.exec0("touch", f)
    assert f.exists()

    # write and read
    lnx.exec0("echo", "Hello", stdout=f)
    out = lnx.exec0("cat", f)
    assert out == "Hello\n", repr(out)

    # remove 'testfile'
    lnx.exec0("rm", "-f",  f)
    assert not f.exists()


# testsuite
@tbot.testcase
def qemu_linux_testcases(
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

        tbot.tc.testsuite(
            linux_verify_uname,
            linux_regular_file_operations,
            lnx=lnx,
        )
