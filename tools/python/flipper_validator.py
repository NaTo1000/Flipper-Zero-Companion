#!/usr/bin/env python3
"""
Flipper Zero File Format Validator
Validates various Flipper Zero file formats for correctness.
"""

import sys
import os
import re
from pathlib import Path
from typing import Dict, List, Tuple


class FlipperValidator:
    """Validates Flipper Zero file formats."""
    
    VALID_FORMATS = {
        '.sub': 'SubGHz',
        '.rfid': 'RFID',
        '.nfc': 'NFC',
        '.ir': 'Infrared',
        '.ibtn': 'iButton',
        '.txt': 'BadUSB'
    }
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_file(self, filepath: str) -> Tuple[bool, List[str], List[str]]:
        """Validate a Flipper Zero file."""
        self.errors = []
        self.warnings = []
        
        path = Path(filepath)
        if not path.exists():
            self.errors.append(f"File not found: {filepath}")
            return False, self.errors, self.warnings
        
        extension = path.suffix.lower()
        if extension not in self.VALID_FORMATS:
            self.errors.append(f"Unknown file format: {extension}")
            return False, self.errors, self.warnings
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        file_type = self.VALID_FORMATS[extension]
        
        if file_type == 'SubGHz':
            self._validate_subghz(content, path.name)
        elif file_type == 'RFID':
            self._validate_rfid(content, path.name)
        elif file_type == 'NFC':
            self._validate_nfc(content, path.name)
        elif file_type == 'Infrared':
            self._validate_ir(content, path.name)
        elif file_type == 'iButton':
            self._validate_ibutton(content, path.name)
        elif file_type == 'BadUSB':
            self._validate_badusb(content, path.name)
        
        return len(self.errors) == 0, self.errors, self.warnings
    
    def _validate_subghz(self, content: str, filename: str):
        """Validate SubGHz file format."""
        if not content.startswith('Filetype:'):
            self.errors.append(f"{filename}: Missing 'Filetype:' header")
        
        if 'Frequency:' not in content:
            self.errors.append(f"{filename}: Missing 'Frequency:' field")
        else:
            freq_match = re.search(r'Frequency:\s*(\d+)', content)
            if freq_match:
                freq = int(freq_match.group(1))
                if freq < 300000000 or freq > 928000000:
                    self.warnings.append(f"{filename}: Frequency {freq} Hz may be outside typical range")
        
        if 'Preset:' not in content:
            self.warnings.append(f"{filename}: Missing 'Preset:' field")
        
        if 'Protocol:' not in content:
            self.errors.append(f"{filename}: Missing 'Protocol:' field")
    
    def _validate_rfid(self, content: str, filename: str):
        """Validate RFID file format."""
        if not content.startswith('Filetype:'):
            self.errors.append(f"{filename}: Missing 'Filetype:' header")
        
        if 'Key type:' not in content:
            self.errors.append(f"{filename}: Missing 'Key type:' field")
        
        if 'Data:' not in content:
            self.errors.append(f"{filename}: Missing 'Data:' field")
    
    def _validate_nfc(self, content: str, filename: str):
        """Validate NFC file format."""
        if not content.startswith('Filetype:'):
            self.errors.append(f"{filename}: Missing 'Filetype:' header")
        
        if 'Device type:' not in content:
            self.errors.append(f"{filename}: Missing 'Device type:' field")
        
        if 'UID:' not in content:
            self.errors.append(f"{filename}: Missing 'UID:' field")
    
    def _validate_ir(self, content: str, filename: str):
        """Validate Infrared file format."""
        if not content.startswith('Filetype:'):
            self.errors.append(f"{filename}: Missing 'Filetype:' header")
        
        if 'name:' not in content:
            self.warnings.append(f"{filename}: No signal definitions found")
        
        if 'protocol:' not in content and 'type:' not in content:
            self.warnings.append(f"{filename}: Missing protocol or type information")
    
    def _validate_ibutton(self, content: str, filename: str):
        """Validate iButton file format."""
        if not content.startswith('Filetype:'):
            self.errors.append(f"{filename}: Missing 'Filetype:' header")
        
        if 'Key type:' not in content:
            self.errors.append(f"{filename}: Missing 'Key type:' field")
        
        if 'Data:' not in content:
            self.errors.append(f"{filename}: Missing 'Data:' field")
    
    def _validate_badusb(self, content: str, filename: str):
        """Validate BadUSB script."""
        lines = content.split('\n')
        
        has_commands = False
        for line in lines:
            line = line.strip()
            if line and not line.startswith('REM'):
                has_commands = True
                break
        
        if not has_commands:
            self.warnings.append(f"{filename}: Script contains only comments")
        
        # Check for common commands
        valid_commands = ['DELAY', 'STRING', 'ENTER', 'GUI', 'CTRL', 'ALT', 'SHIFT', 'REM']
        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line and not line.startswith('REM'):
                cmd = line.split()[0] if line else ''
                if cmd and cmd not in valid_commands:
                    self.warnings.append(f"{filename}:{i}: Unknown command '{cmd}'")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Flipper Zero File Format Validator")
        print("Usage: python flipper_validator.py <file_or_directory>")
        print("\nSupported formats: .sub, .rfid, .nfc, .ir, .ibtn, .txt (BadUSB)")
        sys.exit(1)
    
    target = sys.argv[1]
    validator = FlipperValidator()
    
    files_to_check = []
    if os.path.isdir(target):
        for ext in validator.VALID_FORMATS.keys():
            files_to_check.extend(Path(target).rglob(f'*{ext}'))
    else:
        files_to_check = [Path(target)]
    
    total_files = 0
    valid_files = 0
    
    for filepath in files_to_check:
        total_files += 1
        print(f"\nValidating: {filepath}")
        
        is_valid, errors, warnings = validator.validate_file(str(filepath))
        
        if is_valid:
            valid_files += 1
            print("✓ Valid")
        else:
            print("✗ Invalid")
        
        for error in errors:
            print(f"  ERROR: {error}")
        
        for warning in warnings:
            print(f"  WARNING: {warning}")
    
    print(f"\n{'='*60}")
    print(f"Total files checked: {total_files}")
    print(f"Valid files: {valid_files}")
    print(f"Invalid files: {total_files - valid_files}")
    
    return 0 if valid_files == total_files else 1


if __name__ == '__main__':
    sys.exit(main())
