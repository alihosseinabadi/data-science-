#!/bin/bash


extract_position_level() {
    local name="$1"
    
    # Check if title contains any of the position levels
    if echo "$name" | grep -qiE "(junior|middle|senior)"; then
        # Extract all matching position levels (case insensitive)
        echo "$name" | grep -oiE "junior|middle|senior" | tr '\n' '/' | sed 's/\/$//' | tr '[:upper:]' '[:lower:]'
    else
        echo "-"
    fi
}
input="../ex02/hh_sorted.csv"
output="hh_positions.csv"

if [ ! -f "$input" ]; then
    echo "Error: Input file '$input' not found!"
    echo "Please make sure the file exists in the correct location."
    echo "Current directory: $(pwd)"
    echo "Looking for: $(readlink -f "$input" 2>/dev/null || echo "$input")"
    exit 1
fi

if [ ! -r "$input" ]; then
    echo "Error: Input file '$input' is not readable!"
    exit 1
fi

echo "Processing file: $input"
echo "Output will be saved to: $output"

temp_file=$(mktemp)
echo "Using temporary file: $temp_file"

{
   #it read each line for us 
    IFS= read -r header
    echo "${header},position_level"

 
    while IFS= read -r line; do
      
        position_name=$(echo "$line" | cut -d','  -f3| tr -d '"')

        
        position_level=$(extract_position_level "$position_name")

       
        echo "${line},${position_level}"
    done
} < "$input" > "$temp_file"

if [ $? -eq 0 ] && [ -s "$temp_file" ]; then
    mv "$temp_file" "$output"
    echo "Processing complete. Results saved to $output"
    echo "Number of lines processed: $(wc -l < "$output")"
else
    echo "Error: Processing failed!"
    rm -f "$temp_file"
    exit 1
fi
