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
        channel.send("\n")
        channel.send("reset\n")
        return channel


class QemuUBoot(board.UBootMachine[QemuBoard]):
    prompt = "=> "
    autoboot_prompt = None


class QemuLinux(board.LinuxWithUBootMachine[QemuBoard]):
    uboot    = QemuUBoot
    username = "root"
    password = "root"
    shell    = linux.shell.Bash 

    #boot_commands = [
    #    ["setenv", "serverip", "192.168.1.1"],
    #    ["setenv", "netmask", "255.255.0.0"],
    #    ["setenv", "ipaddr", "192.168.20.95"],
    #    ["mw", "0x81000000", "0", "0x4000"],
    #    ["tftp", "0x81000000", "bbb/tbot/env.txt"],
    #    ["env", "import", "-t", "0x81000000"],
    #    ["setenv", "rootpath", "/opt/..."],
    #    ["run", "netnfsboot"],
    #]


BOARD = QemuBoard
UBOOT = QemuUBoot
LINUX = QemuLinux
