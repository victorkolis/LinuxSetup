#!/usr/bin/env python3

import os
import sys
import time

# commands
install = 'sudo apt install {} -y'
upgrade = 'sudo apt upgrade -y'
clear = 'clear'


def _greeting():
    os.system(clear)
    message = 'Installing list of software...\n🐍'
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)


def _upgrade():
    os.system('')


software_list = [
    'ndcu', 'gimp', 'ranger', 'firefox'
]


def _install(program_list):
    _greeting()
    _upgrade()
    for software in program_list:
        os.system(install.format(software))
    _upgrade()


_install(software_list)
