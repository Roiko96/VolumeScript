# Volume Script

A simple Python script that lets you control your system volume on Windows using the numeric keypad.<br>
**Just run the EXE file, and enjoy!**
**Press the plus (`+`) key on the numpad to increase the volume**,<br>
**and the minus (`-`) key to decrease it.** <br> 
**Press `LEFT SHIFT + ESC` to exit the script gracefully.**

-------

## Features

- Increase or decrease the volume in 2 dB steps.
- Print the current volume level to the console.
- Exit gracefully by pressing `LEFT SHIFT + ESC`, which displays a Windows message box with an exit message.

-------

## Requirements

- **Windows** operating system
- **Python 3.7+** (3.10 or 3.11 recommended)
- **Installed libraries**:
  - [pycaw](https://github.com/AndreMiras/pycaw)
  - [keyboard](https://github.com/boppreh/keyboard)
  - [comtypes](https://pypi.org/project/comtypes/)

-------

## Installation

1. Make sure you have Python installed and added to your system PATH.
2. Install the required libraries:
   ```bash
   pip install pycaw keyboard comtypes
