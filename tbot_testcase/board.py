import typing
import tbot
from tbot.machine import board
from tbot.machine import channel
from tbot.machine import linux

import tc_config


class QemuBoard(board.Board):
    name = "QemuBoard"

    def poweron(self) -> None:
        # command to power on the board
        tbot.log.message(f"Not support 'poweron' command for {self.name}")

    def poweroff(self) -> None:
        # command to power off the board
        tbot.log.message(f"Not support 'poweroff' command for {self.name}")

    def connect(self) -> channel.Channel:
        channel = self.lh.new_channel(tc_config.connect_board_command)
        return channel


class QemuUBoot(board.UBootMachine[QemuBoard]):
    prompt = "=> "


class QemuLinux(board.LinuxWithUBootMachine[QemuBoard]):
    uboot    = QemuUBoot
    username = "root"
    password = "root"
    shell    = linux.shell.Bash 

    boot_commands = [
        ["run", "bootcmd"],
    ]


BOARD = QemuBoard
UBOOT = QemuUBoot
LINUX = QemuLinux
