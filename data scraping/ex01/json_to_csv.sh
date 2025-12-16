#!/bin/sh


INPUT_FILE="../ex00/hh.json"
OUTPUT_FILE="hh.csv"
FILTER_FILE="filter.jq"

#see if we have this file in general or nooo
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: Input file $INPUT_FILE not found." >&2
    exit 1
fi


if [ ! -f "$FILTER_FILE" ]; then
    echo "Error: Filter file $FILTER_FILE not found." >&2
    exit 1
fi

jq -r -f "$FILTER_FILE" "$INPUT_FILE" > "$OUTPUT_FILE"

#if proccess was satisfy 
if [ $? -eq 0 ]; then
    echo "Success! CSV data saved to $OUTPUT_FILE"
else
    echo "Error: jq command failed." >&2
    exit 1
fi
