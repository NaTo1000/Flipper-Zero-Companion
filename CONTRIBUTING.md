# Contributing to Flipper Zero Companion

Thank you for your interest in contributing to Flipper Zero Companion! We welcome contributions from the community.

## 🎯 How to Contribute

### Types of Contributions

We accept the following types of contributions:

1. **New Scripts & Files**
   - BadUSB payloads
   - SubGHz captures
   - RFID/NFC dumps
   - Infrared remotes
   - iButton keys

2. **Documentation**
   - Improved README files
   - Usage guides
   - Tutorials

3. **Bug Fixes**
   - Corrections to existing files
   - Fixed file formats

4. **Improvements**
   - Better organization
   - Enhanced examples
   - Quality improvements

## 📋 Contribution Guidelines

### Before Contributing

1. **Check Legality**: Ensure your contribution doesn't include:
   - Real credentials or passwords
   - Actual access card data
   - Copyrighted content
   - Illegal signal captures

2. **Search First**: Check if similar files already exist

3. **Test Your Files**: Verify files work on Flipper Zero before submitting

### Making a Contribution

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Flipper-Zero-Companion.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Add Your Files**
   - Place files in appropriate directories
   - Use descriptive filenames
   - Follow existing naming conventions

4. **Add Documentation**
   - Include comments in files explaining what they do
   - Update README if adding new categories
   - Add usage instructions if needed

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add: descriptive commit message"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Submit a Pull Request**
   - Clearly describe what you're adding
   - Explain why it's useful
   - Include any relevant testing information

## ✅ File Requirements

### All Files Must Include

1. **Educational Purpose Statement**
   - Clear indication that files are for educational use
   - Appropriate warnings if applicable

2. **Proper Comments**
   - Description of what the file does
   - Author or source (if applicable)
   - Target device/OS (if applicable)

3. **Sample/Dummy Data Only**
   - No real credentials
   - No real card numbers
   - No actual access codes

### File Format Standards

#### BadUSB Scripts (.txt)
```
REM Description of script
REM Author: Your Name/Handle
REM Target: OS name
REM EDUCATIONAL PURPOSES ONLY

[Script content]
```

#### SubGHz Files (.sub)
```
Filetype: Flipper SubGhz Key File
Version: 1
Frequency: [frequency in Hz]
Preset: [preset name]
Protocol: [protocol name]
# Description and warnings
```

#### RFID/NFC Files (.rfid/.nfc)
```
Filetype: Flipper [RFID/NFC] device
[Format-specific headers]
# Description and educational purpose notice
```

#### Infrared Files (.ir)
```
Filetype: IR signals file
Version: 1
# Device: [Device name and model]
# Description
```

#### iButton Files (.ibtn)
```
Filetype: Flipper iButton key
Key type: [type]
# Description and educational purpose notice
```

## 🚫 What NOT to Contribute

**Do NOT submit:**
- Real access credentials
- Actual credit card data
- Real NFC/RFID card dumps with personal data
- Malicious or destructive payloads
- Illegal signal captures
- Copyrighted material
- Tools designed solely for illegal purposes

## 📝 Code of Conduct

### Our Standards

- **Be Respectful**: Treat all contributors with respect
- **Be Ethical**: Only contribute legal and ethical content
- **Be Helpful**: Help others learn and understand
- **Be Honest**: Don't misrepresent your contributions

### Unacceptable Behavior

- Harassment or discrimination
- Publishing others' private information
- Encouraging illegal activity
- Trolling or inflammatory comments

## 🔍 Review Process

1. **Initial Review**: Maintainers will review your PR for:
   - Legality and ethics
   - Code quality
   - Documentation completeness
   - File format correctness

2. **Feedback**: You may receive requests for changes

3. **Testing**: Files may be tested on actual Flipper Zero

4. **Merge**: Once approved, your contribution will be merged

## 💡 Contribution Ideas

### Needed Contributions

- More IR remote databases
- Additional BadUSB scripts for different OSes (Linux, macOS)
- Documentation improvements
- Usage tutorials
- SubGHz protocol examples
- Common RFID format examples

### Quality Over Quantity

We prefer:
- Well-documented files over many undocumented ones
- Tested files over untested ones
- Original creations over duplicates
- Clear explanations over minimal documentation

## 🆘 Getting Help

If you need help contributing:

1. Check existing issues and PRs
2. Read the documentation thoroughly
3. Open an issue describing your question
4. Join the Flipper Zero community forums

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

## 🙏 Thank You!

Every contribution makes this project better. Whether it's a single file or extensive documentation, we appreciate your effort!

---

**Remember: Contribute responsibly and ethically! 🐬**
