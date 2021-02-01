#!/usr/bin/python

import os
import time
import sys
import subprocess

if __name__ == "__main__":
    os.system('clear')
    directory = sys.argv[1]
    subprocess.run(["bash", "{0}/make.bash".format(directory)])
    time.sleep(0.01)
    subprocess.run(['python', '{0}/ManageDjango.py'.format(directory)])
