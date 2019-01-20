import typing
import tbot
from tbot.machine import board
from tbot.machine import channel
from tbot.machine import linux
import userconfig


class QemuBoard(board.Board):
    name = "Qemu-Board"

    def poweron(self) -> None:
        # command to power on the board
        tbot.log.message(f"Not support 'poweron' command for {self.name}")

    def poweroff(self) -> None:
        # command to power off the board
        tbot.log.message(f"Not support 'poweroff' command for {self.name}")

    def connect(self) -> channel.Channel:
        sshlogin_board_command = userconfig.sshlogin_board_command
        channel = self.lh.new_channel(sshlogin_board_command)
        return channel


class QemuBoard_Linux(board.LinuxMachine[board.Board]):
    username = "root"
    password = "root"
    shell    = linux.shell.Bash

    def __init__(self, b: QemuBoard) -> None:  # noqa: D107
        super().__init__(b)

        if self.board.channel is not None:
            self.channel = self.board.channel
        else:
            raise RuntimeError("{board!r} does not support current connection!")

        with tbot.log.EventIO(
            ["board", "linux", self.board.name],
            tbot.log.c("LINUX").bold + f" ({self.name})",
            verbosity=tbot.log.Verbosity.QUIET,
        ) as ev:
            ev.prefix = "   <> "
            ev.verbosity = tbot.log.Verbosity.STDOUT
            ev.data["output"] = "Skip call: self.boot_to_shell(ev)"

        self.channel.initialize(sh=self.shell)

    def destroy(self) -> None:  # noqa: D102
        self.channel.close()

    def _obtain_channel(self) -> channel.Channel:
        return self.channel


BOARD = QemuBoard
LINUX = QemuBoard_Linux
