# Flipper Zero Companion Tools

This directory contains utility programs written in various programming languages to help manage, validate, and work with Flipper Zero files.

## 🛠️ Available Tools

### 1. Python - File Format Validator
**Location:** `python/flipper_validator.py`

Validates Flipper Zero file formats for correctness.

**Features:**
- Validates SubGHz, RFID, NFC, Infrared, iButton, and BadUSB files
- Checks for required headers and fields
- Provides detailed error and warning messages
- Can validate single files or entire directories

**Usage:**
```bash
python3 python/flipper_validator.py <file_or_directory>
```

**Examples:**
```bash
# Validate a single file
python3 python/flipper_validator.py ../SubGHz/garage_door_sample.sub

# Validate entire BadUSB directory
python3 python/flipper_validator.py ../BadUSB/
```

---

### 2. JavaScript - BadUSB Script Generator
**Location:** `javascript/badusb_generator.js`

Generates BadUSB scripts from templates and user input.

**Features:**
- Interactive mode for easy script creation
- Command-line mode for automation
- Multiple built-in templates (Hello World, Open URL, Run Command, etc.)
- Supports both Windows and Linux targets

**Usage:**
```bash
# Interactive mode
node javascript/badusb_generator.js

# List templates
node javascript/badusb_generator.js --list

# Generate from template
node javascript/badusb_generator.js hello_world --message "Hello!" --output hello.txt
```

**Examples:**
```bash
# Create a URL opener script
node javascript/badusb_generator.js open_url --url "https://github.com" --output github.txt

# Create a command runner
node javascript/badusb_generator.js run_command --terminal "powershell" --command "Get-Process" --output processes.txt
```

---

### 3. Go - SubGHz Signal Analyzer
**Location:** `go/subghz_analyzer.go`

Analyzes SubGHz signal files and provides detailed information.

**Features:**
- Parses SubGHz file format
- Frequency band analysis with common usage information
- Protocol identification and description
- RAW data statistics
- Hex to binary key conversion

**Usage:**
```bash
# First, compile the program
go build -o subghz_analyzer go/subghz_analyzer.go

# Then run it
./subghz_analyzer <file.sub>
```

**Examples:**
```bash
./subghz_analyzer ../SubGHz/garage_door_sample.sub
./subghz_analyzer ../SubGHz/car_keyfob_sample.sub
```

---

### 4. Rust - RFID/NFC Card Data Converter
**Location:** `rust/rfid_converter.rs`

Converts and analyzes RFID/NFC card data with format conversions.

**Features:**
- Parses RFID and NFC file formats
- Converts between hex, binary, and decimal representations
- Calculates checksums
- Provides detailed information about card types
- Exports to CSV format

**Usage:**
```bash
# First, compile the program
rustc rust/rfid_converter.rs -o rfid_converter

# Or use cargo (if you have a Cargo.toml)
cargo build --release

# Then run it
./rfid_converter <file.rfid|file.nfc> [options]
```

**Examples:**
```bash
# Analyze a card file
./rfid_converter ../RFID_NFC/em4100_sample.rfid

# Export to CSV
./rfid_converter ../RFID_NFC/ntag215_sample.nfc --export-csv card_data.csv
```

---

### 5. Ruby - IR Remote Signal Database Manager
**Location:** `ruby/ir_database_manager.rb`

Manages and merges IR remote signal databases.

**Features:**
- Parses IR signal files
- Protocol analysis with detailed descriptions
- Search functionality for finding specific signals
- Merge multiple IR databases
- Export to JSON and text formats
- Generate new IR files from merged databases

**Usage:**
```bash
ruby ruby/ir_database_manager.rb <file.ir> [options]
```

**Examples:**
```bash
# Analyze an IR file
ruby ruby/ir_database_manager.rb ../Infrared/Samsung_TV.ir

# Search for specific signals
ruby ruby/ir_database_manager.rb ../Infrared/LG_TV.ir --search "power"

# Merge two IR databases
ruby ruby/ir_database_manager.rb ../Infrared/Samsung_TV.ir --merge ../Infrared/Sony_TV.ir --output merged_tv.ir

# Export to JSON
ruby ruby/ir_database_manager.rb ../Infrared/DVD_Player.ir --export-json dvd.json
```

---

## 📋 Requirements

### Python Tool
- Python 3.6 or higher
- No external dependencies (uses standard library only)

### JavaScript Tool
- Node.js 12 or higher
- No external dependencies (uses Node.js standard library only)

### Go Tool
- Go 1.16 or higher
- No external dependencies (uses Go standard library only)

### Rust Tool
- Rust 1.50 or higher (with rustc or cargo)
- No external dependencies (uses Rust standard library only)

### Ruby Tool
- Ruby 2.5 or higher
- No external dependencies (uses Ruby standard library only)

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NaTo1000/Flipper-Zero-Companion.git
   cd Flipper-Zero-Companion/tools
   ```

2. **Choose a tool based on your needs:**
   - Need to validate files? → Python validator
   - Need to create BadUSB scripts? → JavaScript generator
   - Need to analyze SubGHz signals? → Go analyzer
   - Need to convert RFID/NFC data? → Rust converter
   - Need to manage IR databases? → Ruby manager

3. **Follow the specific tool's usage instructions above**

---

## 🔧 Building Compiled Tools

### Go (SubGHz Analyzer)
```bash
cd tools/go
go build -o subghz_analyzer subghz_analyzer.go
```

### Rust (RFID Converter)
```bash
cd tools/rust
rustc rfid_converter.rs -o rfid_converter

# Or with optimizations
rustc -O rfid_converter.rs -o rfid_converter
```

---

## 💡 Use Cases

### Workflow 1: Validate All Files
```bash
# Validate your entire Flipper Zero file collection
python3 tools/python/flipper_validator.py .
```

### Workflow 2: Create and Test BadUSB Scripts
```bash
# Generate a script
node tools/javascript/badusb_generator.js hello_world --message "Test" --output test.txt

# Validate it
python3 tools/python/flipper_validator.py test.txt

# Copy to Flipper Zero
cp test.txt /path/to/flipper/sdcard/badusb/
```

### Workflow 3: Analyze SubGHz Captures
```bash
# Analyze a captured signal
./tools/go/subghz_analyzer SubGHz/captured_signal.sub
```

### Workflow 4: Merge IR Remote Databases
```bash
# Combine multiple TV remotes into one
ruby tools/ruby/ir_database_manager.rb Infrared/Samsung_TV.ir \
  --merge Infrared/LG_TV.ir \
  --merge Infrared/Sony_TV.ir \
  --output Infrared/all_tvs.ir
```

---

## 🤝 Contributing

These tools are designed to be simple, dependency-free, and easy to extend. Feel free to:
- Add new features to existing tools
- Create tools in additional languages
- Improve error handling and user experience
- Add more templates to the BadUSB generator
- Extend protocol support in analyzers

See the main [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## 📄 License

These tools are provided under the same MIT License as the main repository. See [LICENSE](../LICENSE) for details.

---

## ⚠️ Disclaimer

These tools are provided for educational purposes to help manage and understand Flipper Zero files. Always ensure your use complies with local laws and regulations.
