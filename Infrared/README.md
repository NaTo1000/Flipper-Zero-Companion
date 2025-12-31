# Infrared Remote Files

This directory contains IR (Infrared) signal files for Flipper Zero. These files allow your Flipper to act as a universal remote control for TVs, air conditioners, and other IR-controlled devices.

## ⚠️ IMPORTANT DISCLAIMER
These files are provided for **EDUCATIONAL and CONVENIENCE PURPOSES**. Use responsibly and don't disrupt others' devices without permission.

## Available Files

### Samsung_TV.ir
- **Device**: Samsung Television
- **Protocol**: Samsung32
- **Buttons**: Power, Volume Up/Down, Channel Next/Previous, Mute
- **Description**: Common Samsung TV remote commands

### Sony_TV.ir
- **Device**: Sony Television
- **Protocol**: SIRC (Sony Infrared Remote Control)
- **Buttons**: Power, Volume Up/Down, Channel Next/Previous, Mute
- **Description**: Common Sony TV remote commands

### LG_TV.ir
- **Device**: LG Television
- **Protocol**: NEC
- **Buttons**: Power, Volume Up/Down, Channel Next/Previous, Mute
- **Description**: Common LG TV remote commands

## Common IR Protocols

- **NEC**: Very common, used by many manufacturers
- **Samsung32**: Samsung's proprietary protocol
- **SIRC**: Sony's infrared protocol
- **RC5/RC6**: Philips protocols
- **RAW**: Direct IR signal capture for unsupported protocols

## How to Use

### Using Saved Remotes
1. Copy `.ir` files to the `infrared` folder on your Flipper's SD card
2. Navigate to Infrared menu on Flipper
3. Select "Saved Remotes"
4. Choose your device file
5. Point Flipper at device and select command to send

### Learning New Signals
1. Go to Infrared > Learn New Remote
2. Point your original remote at Flipper's IR receiver
3. Press buttons to learn them
4. Save the learned remote

### Universal Remote Mode
Flipper also has a built-in universal remote database for common devices!
1. Go to Infrared > Universal Remotes
2. Select device type (TV, AC, etc.)
3. Try different brands until you find one that works

## IR Signal Characteristics

- **Frequency**: Most IR remotes use 38 kHz carrier frequency
- **Range**: Typically 5-10 meters
- **Line of Sight**: IR requires direct line of sight
- **One-Way**: IR is transmit-only, no feedback from device

## Creating Your Own Remotes

You can create comprehensive remote files by:
1. Learning each button from your original remote
2. Organizing them in a single `.ir` file
3. Adding descriptive names for each button

## Tips

- Make sure IR LEDs on Flipper are clean
- Point directly at device's IR receiver
- Some devices may not respond to all commands
- Modern devices may use RF instead of IR
- You can combine multiple device controls in one file

## Compatible Devices

- TVs (most brands)
- Air conditioners
- Set-top boxes
- DVD/Blu-ray players
- Projectors
- Audio systems
- Fans
- LED light strips
- And many more IR-controlled devices!
