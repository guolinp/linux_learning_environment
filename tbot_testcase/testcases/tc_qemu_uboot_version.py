import contextlib
import typing
import tbot
from tbot.machine import board


@tbot.testcase
def qemu_uboot_version(
    lab: typing.Optional[tbot.selectable.LabHost] = None
) -> None:
    with contextlib.ExitStack() as cx:
        lh = cx.enter_context(lab or tbot.acquire_lab())
        try:
            b = cx.enter_context(tbot.acquire_board(lh))
            ub = cx.enter_context(tbot.acquire_uboot(b))
        except NotImplementedError:
            b = cx.enter_context(QemuBoard(lh))
            ub = cx.enter_context(QemuUBoot(b))

        out = ub.exec0("version")
        print("u-boot version: %s" % out)
