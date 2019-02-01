import typing
import tbot
from tbot.machine import board
from tbot.machine import channel
from tbot.machine import linux
import userconfig


class QemuBoard(board.Board):
    name = "QemuBoard"

    def poweron(self) -> None:
        # command to power on the board
        tbot.log.message(f"Not support 'poweron' command for {self.name}")

    def poweroff(self) -> None:
        # command to power off the board
        tbot.log.message(f"Not support 'poweroff' command for {self.name}")

    def connect(self) -> channel.Channel:
        channel = self.lh.new_channel(userconfig.uboot_connection_command)
        return channel


class QemuUBoot(board.UBootMachine[QemuBoard]):
    prompt = "=> "


class QemuLinux(board.LinuxWithUBootMachine[QemuBoard]):
    uboot    = QemuUBoot
    username = "root"
    password = "root"
    shell    = linux.shell.Bash 

    boot_commands = [
        ["setenv", "bootargs", "'root=/dev/mmcblk0 rw console=ttyAMA0 init=/linuxrc'"],
        ["ext2load", "mmc", "0x60100000", "/boot/uImage"],
        ["ext2load", "mmc", "0x60600000", "/boot/vexpress-v2p-ca9.dtb"],
        ["bootm", "0x60100000", "-", "0x60600000"],
    ]


BOARD = QemuBoard
UBOOT = QemuUBoot
LINUX = QemuLinux
