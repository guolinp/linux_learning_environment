from tbot.machine.linux import lab
from tbot.machine import linux

import tc_config

class LabHost(lab.SSHLabHost):
    name     = "LabHost:%s@%s" % (tc_config.username, tc_config.hostname)
    hostname = tc_config.hostname
    username = tc_config.username
    password = tc_config.password

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

LAB = LabHost
