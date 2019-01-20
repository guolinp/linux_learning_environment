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
