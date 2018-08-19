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
