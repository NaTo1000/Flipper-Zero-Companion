# RFID & NFC Files

This directory contains RFID and NFC card/tag files for Flipper Zero. These can be used to read, emulate, and store various contactless card formats.

## ⚠️ IMPORTANT DISCLAIMER
These files are provided for **EDUCATIONAL PURPOSES ONLY**. Only clone or emulate cards you own or have explicit permission to use. Unauthorized cloning or use of access cards may be illegal.

## Available Files

### RFID Files (.rfid)

#### em4100_sample.rfid
- **Type**: EM4100
- **Frequency**: 125 kHz
- **Description**: Common RFID tag format
- **Use Case**: Basic access control, animal tags

#### hidprox_sample.rfid
- **Type**: HID Prox
- **Frequency**: 125 kHz
- **Description**: Common corporate access control format
- **Use Case**: Building access cards

### NFC Files (.nfc)

#### ntag215_sample.nfc
- **Type**: NTAG215
- **Frequency**: 13.56 MHz
- **Description**: NFC tag commonly used for amiibo
- **Use Case**: Gaming, smart posters, NFC applications

## RFID vs NFC

**RFID (125 kHz)**
- Lower frequency
- Longer read range
- Simpler data storage
- Common in older access control systems

**NFC (13.56 MHz)**
- Higher frequency
- Shorter read range
- More data storage
- Common in modern applications (payments, smart cards)

## How to Use

### Reading Cards
1. Go to RFID/NFC menu on Flipper
2. Select "Read"
3. Hold card close to Flipper's back
4. Card data will be displayed and can be saved

### Emulating Cards
1. Copy card files to appropriate folder on SD card
2. Navigate to RFID or NFC menu
3. Select "Saved" and choose your file
4. Select "Emulate"
5. Hold Flipper close to reader

## Common Card Types

- **EM4100**: Simple 125kHz tags, easy to clone
- **HID Prox**: Corporate access control
- **T5577**: Rewritable RFID tags
- **NTAG**: NFC tags (various sizes)
- **Mifare Classic**: Common smart cards (some security issues)
- **Mifare Ultralight**: Ticket systems, simple NFC
- **Mifare DESFire**: Secure smart cards

## Legal and Ethical Notes

- Only clone cards you own
- Respect access control systems
- Don't bypass security without authorization
- Many cards have security features that can't be easily cloned
