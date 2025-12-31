# SubGHz Files

This directory contains Sub-GHz radio signal files for Flipper Zero. These files can be used to capture, save, and transmit radio signals on frequencies below 1 GHz.

## ⚠️ IMPORTANT DISCLAIMER
These files are provided for **EDUCATIONAL PURPOSES ONLY**. Only transmit signals on devices you own or have explicit permission to test. Unauthorized transmission on certain frequencies may be illegal in your jurisdiction.

## Available Files

### 433mhz_test_signal.sub
- **Frequency**: 433.92 MHz
- **Protocol**: RAW
- **Description**: Test signal for 433 MHz devices
- **Use Case**: Testing SubGHz transmission

### garage_door_sample.sub
- **Frequency**: 315 MHz
- **Protocol**: Princeton
- **Description**: Sample garage door opener signal
- **Use Case**: Learning signal structure
- **Warning**: Only use on your own garage door

### car_keyfob_sample.sub
- **Frequency**: 433.92 MHz
- **Protocol**: Princeton
- **Description**: Generic car key fob signal structure
- **Use Case**: Educational reference only

## Common Frequencies

- **315 MHz**: Common in North America for garage doors, car keys
- **433.92 MHz**: Common worldwide for various remote controls
- **868 MHz**: Common in Europe for home automation
- **915 MHz**: ISM band, used for various applications

## How to Use

1. Copy the `.sub` file to your Flipper Zero's `subghz` folder on the SD card
2. Navigate to Sub-GHz in the Flipper menu
3. Select "Saved" and choose your file
4. You can read, transmit, or analyze the signal

## File Format

SubGHz files contain:
- `Frequency`: The radio frequency in Hz
- `Preset`: Modulation settings
- `Protocol`: Signal encoding (Princeton, RAW, etc.)
- `Key`: The actual data bits

## Safety Notes

- Always check local regulations before transmitting
- Test signals in a controlled environment
- Never transmit signals that could interfere with critical systems
- Be aware of rolling code systems (many modern devices use these for security)
