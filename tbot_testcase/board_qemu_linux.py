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
        channel = self.lh.new_channel(userconfig.linux_connection_command)
        return channel


class QemuBoard_Linux(board.LinuxStandaloneMachine[board.Board]):
    username = "root"
    password = "root"
    shell    = linux.shell.Bash


BOARD = QemuBoard
LINUX = QemuBoard_Linux
