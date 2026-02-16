#!/usr/bin/env bash

if [ $# -ne 1 ]; then
  echo "Input file not found!"
  echo "Usage: $0 <input_file>"
  exit 1
fi

INPUT_FILE=$1
OUTPUT_FILE="output.txt"

if [ ! -f "$INPUT_FILE" ]; then
  echo "File not found!"
  exit 1
fi

paste -d '\n' <(grep -w "frame.time" "$INPUT_FILE") <(grep -w "wlan.fc.type" "$INPUT_FILE") <(grep -w "wlan.fc.subtype" "$INPUT_FILE") > "$OUTPUT_FILE"
