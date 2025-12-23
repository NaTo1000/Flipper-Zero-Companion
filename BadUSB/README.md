# BadUSB Scripts

This directory contains BadUSB payloads for Flipper Zero. BadUSB allows the Flipper to emulate a USB keyboard and execute automated keystroke sequences.

## ⚠️ IMPORTANT DISCLAIMER
These scripts are provided for **EDUCATIONAL PURPOSES ONLY**. Only use them on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal.

## Available Scripts

### hello_world.txt
- **Description**: Basic demonstration script that opens Notepad and types a message
- **Target**: Windows
- **Difficulty**: Beginner
- **Use Case**: Testing BadUSB functionality

### wifi_password_grab.txt
- **Description**: Extracts saved WiFi passwords from a Windows system
- **Target**: Windows
- **Difficulty**: Intermediate
- **Use Case**: Security testing, password recovery on own systems
- **Warning**: Only use on systems you own

### rickroll.txt
- **Description**: Opens YouTube and plays the classic RickRoll video
- **Target**: Windows
- **Difficulty**: Beginner
- **Use Case**: Harmless prank

## How to Use

1. Copy the `.txt` file to your Flipper Zero's `badusb` folder on the SD card
2. Navigate to BadUSB in the Flipper menu
3. Select the script you want to run
4. Connect Flipper to target device via USB
5. Press the center button to execute

## Script Format

BadUSB scripts use Rubber Ducky syntax:
- `REM`: Comment line
- `DELAY`: Wait specified milliseconds
- `STRING`: Type the specified text
- `ENTER`: Press Enter key
- `GUI r`: Windows + R (Run dialog)
- And many more commands...

## Creating Your Own Scripts

Feel free to modify these scripts or create your own! Just follow the Rubber Ducky syntax and test on your own systems first.
