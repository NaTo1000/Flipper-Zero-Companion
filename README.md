# Flipper Zero Companion 🐬

A comprehensive collection of program designs, scripts, and files for the Flipper Zero multi-tool device. This repository contains various payloads, remote controls, card dumps, and other useful resources for security research, penetration testing, and hobbyist projects.

## ⚠️ IMPORTANT LEGAL DISCLAIMER

**All content in this repository is provided for EDUCATIONAL PURPOSES ONLY.**

- Only use these tools on systems, devices, and networks you own or have explicit written permission to test
- Unauthorized access to computer systems, networks, or devices is illegal
- Unauthorized transmission of radio signals may violate FCC regulations or equivalent laws in your jurisdiction
- Cloning access cards or keys without authorization is illegal
- The authors and contributors are not responsible for any misuse of this content
- Use at your own risk and responsibility

**Know your local laws and regulations before using any of these files.**

## 📁 Repository Structure

### [BadUSB/](BadUSB/)
USB Rubber Ducky-style keystroke injection payloads. Allows Flipper to act as a keyboard and execute automated commands.
- Windows scripts
- Password grabbers
- Pranks and demonstrations
- [Read More](BadUSB/README.md)

### [SubGHz/](SubGHz/)
Sub-GHz radio signal files for transmitting and receiving on frequencies below 1 GHz.
- Garage door remotes (315 MHz)
- Car key fobs (433.92 MHz)
- Generic remote controls
- [Read More](SubGHz/README.md)

### [RFID_NFC/](RFID_NFC/)
RFID (125 kHz) and NFC (13.56 MHz) card/tag files for reading and emulating contactless cards.
- EM4100 RFID tags
- HID Prox cards
- NTAG NFC tags
- [Read More](RFID_NFC/README.md)

### [Infrared/](Infrared/)
IR remote control files for TVs, air conditioners, and other infrared-controlled devices.
- Samsung TV remotes
- Sony TV remotes
- LG TV remotes
- [Read More](Infrared/README.md)

### [iButton/](iButton/)
iButton (1-Wire) contact key files for access control systems.
- Dallas keys
- Cyfral keys
- [Read More](iButton/README.md)

## 🚀 Getting Started

### Prerequisites
- Flipper Zero device with updated firmware
- MicroSD card (recommended for storing files)
- USB cable for connecting to computer

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/NaTo1000/Flipper-Zero-Companion.git
   ```

2. Connect your Flipper Zero to your computer via USB

3. Copy desired files to your Flipper's SD card in the appropriate folders:
   - BadUSB scripts → `/badusb/`
   - SubGHz files → `/subghz/`
   - RFID files → `/rfid/`
   - NFC files → `/nfc/`
   - Infrared files → `/infrared/`
   - iButton files → `/ibutton/`

4. Safely eject your Flipper or SD card

5. Use the Flipper Zero menu to navigate to the appropriate app and load your files

## 📖 How to Use

Each directory contains its own README with detailed instructions on how to use the files. Generally:

1. **Navigate** to the appropriate app on your Flipper Zero
2. **Select** "Saved" or "Saved Files"
3. **Choose** the file you want to use
4. **Execute** the action (Emulate, Transmit, Run, etc.)

## 🛠️ Creating Your Own Files

You can create your own files using:
- **Flipper Zero directly**: Most apps have "Read" or "Learn" modes
- **Computer tools**: Various tools exist for creating and editing Flipper files
- **Community resources**: Check the Flipper Zero forums and Discord

## 🤝 Contributing

Contributions are welcome! If you have cool designs or scripts:

1. Fork the repository
2. Create a feature branch
3. Add your files with appropriate documentation
4. Ensure all files include proper disclaimers
5. Submit a pull request

**Please ensure all contributions are legal and ethical.**

## 📚 Resources

### Official Resources
- [Flipper Zero Official Site](https://flipperzero.one/)
- [Flipper Zero Documentation](https://docs.flipperzero.one/)
- [Flipper Zero GitHub](https://github.com/flipperdevices)

### Community Resources
- [Awesome Flipper Zero](https://github.com/djsime1/awesome-flipperzero)
- Flipper Zero Discord Server
- r/flipperzero on Reddit

### Learning Resources
- Flipper Zero Official Lab
- Hak5 Rubber Ducky Documentation
- RFID/NFC technology guides
- Software Defined Radio basics

## ⚖️ License

This repository is provided for educational purposes. Individual files may have their own licenses. Check each file for specific license information.

## 🔒 Security & Privacy

- Never commit actual sensitive data (real card numbers, passwords, etc.)
- All sample files use dummy/example data
- Test in controlled environments only
- Respect others' privacy and property

## 📮 Contact & Support

For questions or issues:
- Open an issue in this repository
- Check existing issues for solutions
- Consult the Flipper Zero community forums

## 🌟 Acknowledgments

Thanks to:
- The Flipper Zero team for creating an amazing device
- The security research community
- All contributors to this repository
- The open-source community

---

**Remember: With great power comes great responsibility. Use wisely and legally! 🐬**