import contextlib
import typing
import stat
import tbot
from tbot.machine import board
from tbot.machine import linux


@tbot.testcase
def qemu_linux_file_create(
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

        f = lnx.workdir / "testfile"

        lnx.exec0("touch", f)
        assert f.exists()

        lnx.exec0("rm", "-f",  f)
        assert not f.exists()


@tbot.testcase
def qemu_linux_file_read_write(
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

        f = lnx.workdir / "testfile"

        lnx.exec0("touch", f)
        assert f.exists()

        lnx.exec0("echo", "Hello", stdout=f)
        out = lnx.exec0("cat", f)
        assert out == "Hello\n", repr(out)

        lnx.exec0("rm", "-f",  f)
        assert not f.exists()
