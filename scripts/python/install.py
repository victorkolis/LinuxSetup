#!/usr/bin/env python3

import os
import sys
import time

# commands
install = 'sudo apt install {} -y'
classic_install = 'sudo snap install --classic {}'
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
    'ndcu', 'gimp', 'ranger', 'firefox', 'git', '', '',
    ''
]

classic_snap_software = [
    'pycharm-community', 'ffmpeg', 'ffmpeg-integration-gplv3', 
    'ffmpeg-integration-lgpl'
]

def _install(apt_list, snap_list):
    _greeting()
    _upgrade()

    # Installing the apt software
    for software in apt_list:
        os.system(install.format(software))
    _upgrade()

    # Installing the snap software
    for software in snap_list:
        os.system(classic_install.format(software))
    _upgrade()


_install(software_list, classic_snap_software)

