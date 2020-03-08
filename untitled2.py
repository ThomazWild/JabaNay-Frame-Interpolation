# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:20:02 2020

@author: JabaNay
"""

import subprocess

from subprocess import CREATE_NEW_CONSOLE


p = subprocess.Popen("start cmd /K excel",creationflags= CREATE_NEW_CONSOLE, shell=True)
p