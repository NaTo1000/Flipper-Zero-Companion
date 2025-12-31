#!/usr/bin/env ruby
# frozen_string_literal: true

require 'json'
require 'optparse'

# IR Remote Signal Database Manager for Flipper Zero
class IRDatabaseManager
  def initialize
    @signals = []
    @device_name = ''
    @device_type = ''
  end

  # Parse an IR file
  def parse_file(filename)
    unless File.exist?(filename)
      raise "File not found: #{filename}"
    end

    current_signal = nil

    File.readlines(filename).each do |line|
      line = line.strip

      next if line.empty? || line.start_with?('#')

      if line.start_with?('Filetype:')
        @filetype = line.split(':', 2)[1].strip
      elsif line.start_with?('Version:')
        @version = line.split(':', 2)[1].strip
      elsif line.start_with?('# Device:')
        @device_name = line.sub('# Device:', '').strip
      elsif line.start_with?('name:')
        current_signal = { name: line.split(':', 2)[1].strip }
        @signals << current_signal
      elsif current_signal && line.include?(':')
        key, value = line.split(':', 2).map(&:strip)
        current_signal[key.to_sym] = value
      end
    end

    self
  end

  # Display database information
  def display_info
    puts "\n╔════════════════════════════════════════════╗"
    puts "║   IR Remote Signal Database Manager       ║"
    puts "╚════════════════════════════════════════════╝\n"

    puts "Device Information:"
    puts "==================="
    puts "Device: #{@device_name}" unless @device_name.empty?
    puts "Signals: #{@signals.length}"
    puts

    puts "Available Signals:"
    puts "=================="
    
    @signals.each_with_index do |signal, index|
      puts "\n#{index + 1}. #{signal[:name]}"
      puts "   Protocol: #{signal[:protocol]}" if signal[:protocol]
      puts "   Type: #{signal[:type]}" if signal[:type]
      puts "   Address: #{signal[:address]}" if signal[:address]
      puts "   Command: #{signal[:command]}" if signal[:command]
    end

    analyze_protocols
  end

  # Analyze protocols used
  def analyze_protocols
    puts "\nProtocol Analysis:"
    puts "=================="

    protocols = @signals.map { |s| s[:protocol] }.compact.uniq

    protocols.each do |protocol|
      count = @signals.count { |s| s[:protocol] == protocol }
      puts "#{protocol}: #{count} signal(s)"
      puts "  #{get_protocol_info(protocol)}"
    end
  end

  # Get information about a protocol
  def get_protocol_info(protocol)
    protocols = {
      'NEC' => 'Common in many devices, 32-bit protocol',
      'Samsung32' => 'Samsung proprietary 32-bit protocol',
      'SIRC' => 'Sony Infrared Remote Control, 12-20 bit',
      'RC5' => 'Philips protocol, used in many European devices',
      'RC6' => 'Enhanced RC5, used in modern devices',
      'RAW' => 'Raw signal timing data'
    }

    protocols[protocol] || 'Custom or unknown protocol'
  end

  # Search for signals by name
  def search(query)
    results = @signals.select do |signal|
      signal[:name].downcase.include?(query.downcase)
    end

    puts "\nSearch Results for '#{query}':"
    puts "==============================="

    if results.empty?
      puts "No signals found"
    else
      results.each do |signal|
        puts "- #{signal[:name]}"
      end
    end

    results
  end

  # Export to JSON format
  def export_json(output_file)
    data = {
      device: @device_name,
      filetype: @filetype,
      version: @version,
      signals: @signals
    }

    File.write(output_file, JSON.pretty_generate(data))
    puts "\n✓ Exported to JSON: #{output_file}"
  end

  # Export to human-readable text
  def export_text(output_file)
    File.open(output_file, 'w') do |file|
      file.puts "IR Remote Database Export"
      file.puts "=" * 50
      file.puts
      file.puts "Device: #{@device_name}"
      file.puts "Total Signals: #{@signals.length}"
      file.puts
      file.puts "Signals:"
      file.puts "-" * 50

      @signals.each_with_index do |signal, index|
        file.puts
        file.puts "#{index + 1}. #{signal[:name]}"
        signal.each do |key, value|
          next if key == :name
          file.puts "   #{key}: #{value}"
        end
      end
    end

    puts "\n✓ Exported to text: #{output_file}"
  end

  # Merge with another IR database
  def merge(other_manager)
    before_count = @signals.length
    
    other_manager.signals.each do |signal|
      # Check if signal already exists
      unless @signals.any? { |s| s[:name] == signal[:name] }
        @signals << signal
      end
    end

    after_count = @signals.length
    added = after_count - before_count

    puts "\n✓ Merged databases:"
    puts "  Original signals: #{before_count}"
    puts "  New signals added: #{added}"
    puts "  Total signals: #{after_count}"

    self
  end

  # Generate a new IR file
  def generate_file(output_file)
    File.open(output_file, 'w') do |file|
      file.puts "Filetype: IR signals file"
      file.puts "Version: 1"
      file.puts "# Device: #{@device_name}"

      @signals.each do |signal|
        file.puts "name: #{signal[:name]}"
        signal.each do |key, value|
          next if key == :name
          file.puts "#{key}: #{value}"
        end
      end
    end

    puts "\n✓ Generated IR file: #{output_file}"
  end

  # List all signal names
  def list_signals
    @signals.map { |s| s[:name] }
  end

  attr_reader :signals
end

# Command-line interface
def main
  options = {}
  
  parser = OptionParser.new do |opts|
    opts.banner = "IR Remote Signal Database Manager for Flipper Zero\n\n"
    opts.banner += "Usage: ruby ir_database_manager.rb <file.ir> [options]\n\n"

    opts.on('-s', '--search QUERY', 'Search for signals by name') do |query|
      options[:search] = query
    end

    opts.on('-j', '--export-json FILE', 'Export to JSON format') do |file|
      options[:export_json] = file
    end

    opts.on('-t', '--export-text FILE', 'Export to text format') do |file|
      options[:export_text] = file
    end

    opts.on('-m', '--merge FILE', 'Merge with another IR file') do |file|
      options[:merge] = file
    end

    opts.on('-o', '--output FILE', 'Output file for merged database') do |file|
      options[:output] = file
    end

    opts.on('-h', '--help', 'Show this help message') do
      puts opts
      exit
    end
  end

  parser.parse!

  if ARGV.empty?
    puts "Error: No input file specified\n\n"
    puts parser
    exit 1
  end

  filename = ARGV[0]

  begin
    manager = IRDatabaseManager.new
    manager.parse_file(filename)
    manager.display_info

    # Handle search
    if options[:search]
      manager.search(options[:search])
    end

    # Handle merge
    if options[:merge]
      other_manager = IRDatabaseManager.new
      other_manager.parse_file(options[:merge])
      manager.merge(other_manager)

      if options[:output]
        manager.generate_file(options[:output])
      end
    end

    # Handle exports
    if options[:export_json]
      manager.export_json(options[:export_json])
    end

    if options[:export_text]
      manager.export_text(options[:export_text])
    end

    puts "\n#{'=' * 50}"
    puts "Processing complete!"

  rescue StandardError => e
    puts "Error: #{e.message}"
    exit 1
  end
end

main if __FILE__ == $PROGRAM_NAME
