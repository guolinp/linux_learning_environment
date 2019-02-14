from tbot.machine.linux import lab
from tbot.machine import linux

class LocalLabHost(lab.SSHLabHost):
    name     = "LocalLabHost"
    hostname = "localhost"
    username = "root"
    password = "root"

    @property
    def ignore_hostkey(self) -> bool:
        return True

    @property
    def authenticator(self) -> linux.auth.Authenticator:
        return linux.auth.PasswordAuthenticator(self.password)

    @property
    def workdir(self) -> "linux.Path[LabHost]":
        p = linux.Path(self, f"/")
        return p

LAB = LocalLabHost
