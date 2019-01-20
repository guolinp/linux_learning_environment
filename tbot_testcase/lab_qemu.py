from tbot.machine.linux import lab
from tbot.machine import linux
import userconfig

# Let the PC of tbot_docker running on act the `SSHLabHost`
class LabQEMU(lab.SSHLabHost):
    name     = "SSH-LAB-QEMU"
    hostname = userconfig.hostname
    username = userconfig.username
    password = userconfig.password

    @property
    def ignore_hostkey(self) -> bool:
        return True

    @property
    def authenticator(self) -> linux.auth.Authenticator:
        return linux.auth.PasswordAuthenticator(self.password)

    @property
    def workdir(self) -> "linux.Path[LabQEMU]":
        p = linux.Path(self, f"/")
        return p

LAB = LabQEMU
