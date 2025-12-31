# iButton Keys

This directory contains iButton key files for Flipper Zero. iButton (1-Wire) is a contact-based electronic key system commonly used for access control.

## ⚠️ IMPORTANT DISCLAIMER
These files are provided for **EDUCATIONAL PURPOSES ONLY**. Only clone or emulate keys you own or have explicit permission to use. Unauthorized access is illegal.

## Available Files

### dallas_sample.ibtn
- **Type**: Dallas (DS1990A)
- **Description**: Most common iButton format
- **Use Case**: Building access, lockers, timing systems
- **Protocol**: 1-Wire protocol with 64-bit unique ID

### cyfral_sample.ibtn
- **Type**: Cyfral
- **Description**: Common in Russian access control systems
- **Use Case**: Building access, apartment entry systems
- **Protocol**: Proprietary Russian format

## What is iButton?

iButton is a contact-based key technology:
- Small metal button contains a chip
- Requires physical contact with reader
- Very durable (can withstand harsh conditions)
- Uses 1-Wire communication protocol
- Each key has a unique ID

## Common iButton Types

- **Dallas DS1990A**: Standard read-only key
- **Cyfral**: Russian access control
- **Metakom**: Another Russian format
- **DS1992-DS1996**: Memory iButtons (store data)

## How to Use

### Reading iButton Keys
1. Go to iButton menu on Flipper
2. Select "Read"
3. Touch the key to Flipper's iButton contact (on top)
4. Key data will be displayed
5. Save if desired

### Emulating iButton Keys
1. Copy `.ibtn` files to `ibutton` folder on SD card
2. Go to iButton > Saved Keys
3. Select your key file
4. Choose "Emulate"
5. Touch Flipper's iButton contact to reader

### Writing to Blank Keys
1. Read or load a key file
2. Get a blank RW1990 or compatible key
3. Select "Write"
4. Touch blank key to Flipper
5. Key will be written (if compatible)

## iButton vs RFID

**iButton (Contact)**
- Requires physical touch
- More reliable in harsh conditions
- Harder to skim remotely
- Slower to use
- Very durable

**RFID (Contactless)**
- No physical contact needed
- Faster to use
- Can be read from distance
- More convenient
- Susceptible to damage

## Hardware Notes

- The iButton reader is the small metal circle on top of Flipper
- Make sure both contacts (center and outer ring) touch the key
- Clean contacts if having reading issues
- Some keys may be damaged or have weak signals

## Common Applications

- Building access control
- Apartment entry systems
- Locker systems
- Time and attendance systems
- Security checkpoints
- Tool control systems
- Vehicle immobilizers (some models)

## Blank Keys

You can write to blank iButton keys:
- **RW1990**: Rewritable Dallas-compatible keys
- **TM2004**: Writable Cyfral-compatible keys
- These can be purchased online inexpensively

## Legal Notes

- Only clone keys you own
- Respect access control systems
- Don't bypass security without authorization
- Be aware of local laws regarding key duplication
