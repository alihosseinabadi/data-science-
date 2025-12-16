#!/bin/sh


INPUT_FILE="../ex01/hh.csv"
OUTPUT_FILE="hh_sorted.csv"


if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file $INPUT_FILE not found." >&2
    exit 1
fi


head -n 1 "$INPUT_FILE" > "$OUTPUT_FILE"


tail -n +2 "$INPUT_FILE" | sort -t',' -k2,2 -k1,1n >> "$OUTPUT_FILE"

echo "Success! Sorted data saved to $OUTPUT_FILE"
