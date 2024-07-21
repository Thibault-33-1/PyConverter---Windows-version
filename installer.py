#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

def install_dependencies():

    os.system("REG ADD HKEY_CURRENT_USER\\Environment /v Path /d C:\\Python27 /f")

    os.system("MKDIR C:\\ffmpeg\\")
    os.system("MKDIR C:\\ffmpeg\\bin\\")
    os.system("MKDIR C:\\ffmpeg\\doc\\")
    os.system("MKDIR C:\\ffmpeg\\presets\\")

    os.system("COPY C:\\Users\\Thibault\\Desktop\\PyConverter\\dependence\\ffmpeg\\ C:\\ffmpeg\\")
    os.system("COPY C:\\Users\\Thibault\\Desktop\\PyConverter\\dependence\\ffmpeg\\bin\\ C:\\ffmpeg\\bin\\")
    os.system("COPY C:\\Users\\Thibault\\Desktop\\PyConverter\\dependence\\ffmpeg\\doc\\ C:\\ffmpeg\\doc\\")
    os.system("COPY C:\\Users\\Thibault\\Desktop\\PyConverter\\dependence\\ffmpeg\\presets\\ C:\\ffmpeg\\presets\\")

    os.system("REG ADD HKEY_CURRENT_USER\\Environment /v Path /d C:\\ffmpeg\\bin\\ /f")

    #subprocess.call("Python\\python-2.7.15.amd64.msi", shell=True)
    #subprocess.call("Python\\python-3.7.1.exe", shell=True)

    #os.system("REG ADD HKEY_CURRENT_USER\\Environment /v Path /d C:\\Python37 /f")

    subprocess.call("python get-pip.py", shell=True)

    subprocess.call("python -m pip install --upgrade pip", shell=True)

    #os.system("REG ADD HKEY_CURRENT_USER\\Environment /v Path /d C:\\Python27\\Scripts /f")
    #os.system("REG ADD HKEY_CURRENT_USER\\Environment /v Path /d C:\\Python37\\Scripts /f")

    subprocess.call("dependence\\ActiveTcl-8.6.8.0-MSWin32-x64.exe", shell=True)

    subprocess.call("dependence\\Pillow-2.5.3.win-amd64-py2.7.exe", shell=True)

    subprocess.call("shutdown -r -t 8", shell=True)

install_dependencies()
