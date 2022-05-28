# Standard Python Imports
import logging
from subprocess import Popen, PIPE


class ADBTools:
    '''Standard ADB Tools'''

    def __init__(self, adb_command, device_serial):
        self.adb_command = adb_command
        self.device_serial = device_serial

    def root_device(self):
        '''Root Device'''

        proc = Popen(["adb", "-s", self.device_serial, 'shell'], stdout=PIPE)
        p = proc.communicate()
        logging.info(f"Communicate: {p}")



if __name__ == "__main__":
    a = ADBTools('root', '375010008142000055')
    a.root_device()