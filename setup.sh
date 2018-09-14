#!/bin/sh

# Build apt package list
APT_PKGS="omxplayer python python-rpi.gpio python-pip dialog"

# Build PyPI package list
PIP_PKGS="python-uinput"

# Install apt packages
sudo apt-get update && sudo apt-get install -y ${APT_PKGS}

# Install PyPI packages
sudo pip install ${PIP_PKGS}

# Patch /etc/modules
# Add the following line
#uinput

# install gpio2kbd (fork of adafruit/retrogame)
# Website: https://github.com/opencardev/gpio2kbd
git submodule update --init
cd gpio2kbd
make && sudo make install
cd ..
sudo cp gpio2kbd.cfg /boot/
