package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// SubGHzSignal represents a parsed SubGHz signal
type SubGHzSignal struct {
	Filetype  string
	Version   string
	Frequency int64
	Preset    string
	Protocol  string
	Key       string
	Bit       int
	TE        int
	RawData   []string
}

// SubGHzAnalyzer analyzes SubGHz signal files
type SubGHzAnalyzer struct {
	signal SubGHzSignal
}

// NewSubGHzAnalyzer creates a new analyzer instance
func NewSubGHzAnalyzer() *SubGHzAnalyzer {
	return &SubGHzAnalyzer{}
}

// ParseFile parses a SubGHz file
func (a *SubGHzAnalyzer) ParseFile(filename string) error {
	file, err := os.Open(filename)
	if err != nil {
		return fmt.Errorf("failed to open file: %w", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		
		if strings.HasPrefix(line, "#") || line == "" {
			continue
		}

		parts := strings.SplitN(line, ":", 2)
		if len(parts) != 2 {
			continue
		}

		key := strings.TrimSpace(parts[0])
		value := strings.TrimSpace(parts[1])

		switch key {
		case "Filetype":
			a.signal.Filetype = value
		case "Version":
			a.signal.Version = value
		case "Frequency":
			freq, _ := strconv.ParseInt(value, 10, 64)
			a.signal.Frequency = freq
		case "Preset":
			a.signal.Preset = value
		case "Protocol":
			a.signal.Protocol = value
		case "Key":
			a.signal.Key = value
		case "Bit":
			bit, _ := strconv.Atoi(value)
			a.signal.Bit = bit
		case "TE":
			te, _ := strconv.Atoi(value)
			a.signal.TE = te
		case "RAW_Data":
			a.signal.RawData = append(a.signal.RawData, value)
		}
	}

	if err := scanner.Err(); err != nil {
		return fmt.Errorf("error reading file: %w", err)
	}

	return nil
}

// Analyze performs analysis on the parsed signal
func (a *SubGHzAnalyzer) Analyze() {
	fmt.Println("\n╔════════════════════════════════════════════╗")
	fmt.Println("║     SubGHz Signal Analyzer                ║")
	fmt.Println("╚════════════════════════════════════════════╝\n")

	fmt.Println("Signal Information:")
	fmt.Println("==================")
	fmt.Printf("Filetype:  %s\n", a.signal.Filetype)
	fmt.Printf("Version:   %s\n", a.signal.Version)
	fmt.Printf("Frequency: %d Hz (%.2f MHz)\n", a.signal.Frequency, float64(a.signal.Frequency)/1000000.0)
	fmt.Printf("Preset:    %s\n", a.signal.Preset)
	fmt.Printf("Protocol:  %s\n", a.signal.Protocol)

	if a.signal.Key != "" {
		fmt.Printf("Key:       %s\n", a.signal.Key)
	}
	if a.signal.Bit > 0 {
		fmt.Printf("Bits:      %d\n", a.signal.Bit)
	}
	if a.signal.TE > 0 {
		fmt.Printf("TE:        %d\n", a.signal.TE)
	}

	fmt.Println("\nFrequency Analysis:")
	fmt.Println("===================")
	a.analyzeFrequency()

	fmt.Println("\nProtocol Analysis:")
	fmt.Println("==================")
	a.analyzeProtocol()

	if len(a.signal.RawData) > 0 {
		fmt.Println("\nRAW Data Analysis:")
		fmt.Println("==================")
		a.analyzeRawData()
	}
}

// analyzeFrequency provides information about the frequency
func (a *SubGHzAnalyzer) analyzeFrequency() {
	freq := a.signal.Frequency

	freqMHz := float64(freq) / 1000000.0

	fmt.Printf("Frequency: %.2f MHz\n", freqMHz)

	// Determine frequency band
	var band string
	var common string

	switch {
	case freq >= 300000000 && freq < 348000000:
		band = "300-348 MHz"
		common = "Older garage doors, wireless doorbells"
	case freq >= 387000000 && freq < 464000000:
		band = "387-464 MHz"
		if freq >= 433050000 && freq <= 434790000 {
			common = "ISM band - Very common for remotes, sensors"
		} else {
			common = "Various remote controls"
		}
	case freq >= 779000000 && freq < 928000000:
		band = "779-928 MHz"
		if freq >= 902000000 && freq <= 928000000 {
			common = "ISM band (US) - Garage doors, IoT devices"
		} else {
			common = "Various applications"
		}
	default:
		band = "Unknown"
		common = "Outside typical SubGHz range"
	}

	fmt.Printf("Band:      %s\n", band)
	fmt.Printf("Common:    %s\n", common)
}

// analyzeProtocol provides information about the protocol
func (a *SubGHzAnalyzer) analyzeProtocol() {
	protocol := a.signal.Protocol

	protocols := map[string]string{
		"Princeton":   "Fixed code protocol, common in garage doors and remotes",
		"RAW":         "Raw signal capture without decoding",
		"BinRAW":      "Binary raw signal data",
		"KeeLoq":      "Rolling code protocol, more secure than fixed codes",
		"Star_Line":   "Car alarm system protocol",
		"Came":        "Gate and garage door opener protocol",
		"Nice_Flo":    "Nice FLO protocol for gates",
		"Holtek":      "Common protocol for remotes",
		"Chamberlain": "Garage door opener with rolling codes",
	}

	description, found := protocols[protocol]
	if found {
		fmt.Printf("Protocol: %s\n", protocol)
		fmt.Printf("Description: %s\n", description)
	} else {
		fmt.Printf("Protocol: %s (Unknown/Custom)\n", protocol)
	}

	if a.signal.Bit > 0 {
		fmt.Printf("Data bits: %d (can encode %d unique codes)\n", a.signal.Bit, 1<<uint(a.signal.Bit))
	}
}

// analyzeRawData analyzes raw signal data
func (a *SubGHzAnalyzer) analyzeRawData() {
	totalSamples := 0
	for _, data := range a.signal.RawData {
		samples := strings.Fields(data)
		totalSamples += len(samples)
	}

	fmt.Printf("Raw data lines: %d\n", len(a.signal.RawData))
	fmt.Printf("Total samples:  %d\n", totalSamples)

	if totalSamples > 0 {
		fmt.Println("Note: RAW data contains timing information in microseconds")
		fmt.Println("      Positive values = signal high, Negative values = signal low")
	}
}

// ConvertKey converts a hex key to binary representation
func (a *SubGHzAnalyzer) ConvertKey() string {
	if a.signal.Key == "" {
		return ""
	}

	key := strings.ReplaceAll(a.signal.Key, " ", "")
	
	var binary strings.Builder
	for i := 0; i < len(key); i += 2 {
		if i+2 > len(key) {
			break
		}
		hex := key[i : i+2]
		val, err := strconv.ParseUint(hex, 16, 8)
		if err != nil {
			continue
		}
		binary.WriteString(fmt.Sprintf("%08b ", val))
	}

	return strings.TrimSpace(binary.String())
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("SubGHz Signal Analyzer for Flipper Zero")
		fmt.Println("\nUsage: subghz_analyzer <file.sub>")
		fmt.Println("\nAnalyzes SubGHz signal files and provides detailed information")
		fmt.Println("about frequency, protocol, and signal characteristics.")
		os.Exit(1)
	}

	filename := os.Args[1]

	analyzer := NewSubGHzAnalyzer()

	fmt.Printf("Loading file: %s\n", filename)

	err := analyzer.ParseFile(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	analyzer.Analyze()

	if analyzer.signal.Key != "" {
		fmt.Println("\nKey Conversion:")
		fmt.Println("===============")
		fmt.Printf("Hex:    %s\n", analyzer.signal.Key)
		fmt.Printf("Binary: %s\n", analyzer.ConvertKey())
	}

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("Analysis complete!")
}
