use std::env;
use std::fs;
use std::io::{self, Write};
use std::path::Path;

/// Represents an RFID/NFC card data structure
#[derive(Debug, Clone)]
struct CardData {
    file_type: String,
    format: CardFormat,
    uid: Option<String>,
    data: Option<String>,
    key_type: Option<String>,
}

#[derive(Debug, Clone, PartialEq)]
enum CardFormat {
    RFID,
    NFC,
    Unknown,
}

/// RFID/NFC Card Data Converter
struct CardConverter {
    card: CardData,
}

impl CardConverter {
    fn new() -> Self {
        CardConverter {
            card: CardData {
                file_type: String::new(),
                format: CardFormat::Unknown,
                uid: None,
                data: None,
                key_type: None,
            },
        }
    }

    /// Parse a Flipper Zero RFID/NFC file
    fn parse_file(&mut self, filename: &str) -> io::Result<()> {
        let content = fs::read_to_string(filename)?;
        
        for line in content.lines() {
            let line = line.trim();
            
            if line.starts_with('#') || line.is_empty() {
                continue;
            }

            if let Some((key, value)) = line.split_once(':') {
                let key = key.trim();
                let value = value.trim();

                match key {
                    "Filetype" => {
                        self.card.file_type = value.to_string();
                        self.card.format = if value.contains("RFID") {
                            CardFormat::RFID
                        } else if value.contains("NFC") {
                            CardFormat::NFC
                        } else {
                            CardFormat::Unknown
                        };
                    }
                    "UID" => self.card.uid = Some(value.to_string()),
                    "Data" => self.card.data = Some(value.to_string()),
                    "Key type" => self.card.key_type = Some(value.to_string()),
                    _ => {}
                }
            }
        }

        Ok(())
    }

    /// Convert hex string to binary representation
    fn hex_to_binary(&self, hex: &str) -> String {
        hex.split_whitespace()
            .filter_map(|byte| u8::from_str_radix(byte, 16).ok())
            .map(|b| format!("{:08b}", b))
            .collect::<Vec<_>>()
            .join(" ")
    }

    /// Convert hex string to decimal representation
    fn hex_to_decimal(&self, hex: &str) -> Vec<u8> {
        hex.split_whitespace()
            .filter_map(|byte| u8::from_str_radix(byte, 16).ok())
            .collect()
    }

    /// Calculate checksum for RFID data
    fn calculate_checksum(&self, data: &[u8]) -> u8 {
        data.iter().fold(0u8, |acc, &x| acc ^ x)
    }

    /// Display card information
    fn display_info(&self) {
        println!("\n╔════════════════════════════════════════════╗");
        println!("║   RFID/NFC Card Data Converter            ║");
        println!("╚════════════════════════════════════════════╝\n");

        println!("Card Information:");
        println!("=================");
        println!("File Type: {}", self.card.file_type);
        println!("Format:    {:?}", self.card.format);

        if let Some(ref key_type) = self.card.key_type {
            println!("Key Type:  {}", key_type);
            self.display_key_type_info(key_type);
        }

        if let Some(ref uid) = self.card.uid {
            println!("\nUID (Unique Identifier):");
            println!("========================");
            println!("Hex:     {}", uid);
            println!("Binary:  {}", self.hex_to_binary(uid));
            println!("Decimal: {:?}", self.hex_to_decimal(uid));
            println!("Length:  {} bytes", uid.split_whitespace().count());
        }

        if let Some(ref data) = self.card.data {
            println!("\nData:");
            println!("=====");
            println!("Hex:     {}", data);
            println!("Binary:  {}", self.hex_to_binary(data));
            println!("Decimal: {:?}", self.hex_to_decimal(data));
            
            let data_bytes = self.hex_to_decimal(data);
            if !data_bytes.is_empty() {
                let checksum = self.calculate_checksum(&data_bytes);
                println!("XOR Checksum: 0x{:02X}", checksum);
            }
        }
    }

    /// Display information about specific key types
    fn display_key_type_info(&self, key_type: &str) {
        println!("\nKey Type Information:");
        println!("=====================");
        
        match key_type {
            "EM4100" => {
                println!("EM4100 (EM Marine):");
                println!("  - Read-only 125kHz RFID tag");
                println!("  - Common in access control, animal tags");
                println!("  - 40-bit unique ID (5 bytes)");
                println!("  - Manchester encoded");
            }
            "HIDProx" | "HID Prox" => {
                println!("HID Proximity:");
                println!("  - Corporate access control standard");
                println!("  - 125kHz frequency");
                println!("  - Various formats (26-bit, 35-bit, etc.)");
                println!("  - Used in building access systems");
            }
            "NTAG215" => {
                println!("NTAG215:");
                println!("  - NFC Type 2 tag");
                println!("  - 13.56 MHz frequency");
                println!("  - 504 bytes user memory");
                println!("  - Used in amiibo, smart posters");
            }
            "Dallas" | "DS1990A" => {
                println!("Dallas iButton:");
                println!("  - 1-Wire protocol");
                println!("  - 64-bit unique ID");
                println!("  - Contact-based (not RFID)");
                println!("  - Very durable");
            }
            "Cyfral" => {
                println!("Cyfral:");
                println!("  - Russian access control system");
                println!("  - Proprietary protocol");
                println!("  - Common in apartment buildings");
            }
            _ => {
                println!("Custom or unknown key type");
            }
        }
    }

    /// Export to different format
    fn export_csv(&self, output_file: &str) -> io::Result<()> {
        let mut file = fs::File::create(output_file)?;
        
        writeln!(file, "Field,Hex,Binary,Decimal")?;
        
        if let Some(ref uid) = self.card.uid {
            let decimal = self.hex_to_decimal(uid);
            writeln!(
                file,
                "UID,{},{},{:?}",
                uid,
                self.hex_to_binary(uid),
                decimal
            )?;
        }
        
        if let Some(ref data) = self.card.data {
            let decimal = self.hex_to_decimal(data);
            writeln!(
                file,
                "Data,{},{},{:?}",
                data,
                self.hex_to_binary(data),
                decimal
            )?;
        }
        
        println!("\n✓ Exported to CSV: {}", output_file);
        Ok(())
    }
}

fn print_usage() {
    println!("RFID/NFC Card Data Converter for Flipper Zero");
    println!("\nUsage:");
    println!("  rfid_converter <file.rfid|file.nfc> [options]");
    println!("\nOptions:");
    println!("  --export-csv <output.csv>  Export data to CSV format");
    println!("  --help                     Show this help message");
    println!("\nExamples:");
    println!("  rfid_converter card.rfid");
    println!("  rfid_converter card.nfc --export-csv output.csv");
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 || args.contains(&"--help".to_string()) {
        print_usage();
        return;
    }

    let filename = &args[1];

    if !Path::new(filename).exists() {
        eprintln!("Error: File '{}' not found", filename);
        std::process::exit(1);
    }

    let mut converter = CardConverter::new();

    match converter.parse_file(filename) {
        Ok(_) => {
            converter.display_info();

            // Check for export option
            if let Some(pos) = args.iter().position(|arg| arg == "--export-csv") {
                if let Some(output_file) = args.get(pos + 1) {
                    if let Err(e) = converter.export_csv(output_file) {
                        eprintln!("Error exporting to CSV: {}", e);
                    }
                }
            }

            println!("\n{}", "=".repeat(50));
            println!("Conversion complete!");
        }
        Err(e) => {
            eprintln!("Error parsing file: {}", e);
            std::process::exit(1);
        }
    }
}
