#!/bin/sh


input_file="../ex03/hh_positions.csv"
output_dir="partitions"

if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found!" >&2
    exit 1
fi

mkdir -p "$output_dir"

header=$(head -1 "$input_file")

tail -n +2 "$input_file" | while IFS= read -r line; do
    date=$(echo "$line" | cut -d',' -f2 | cut -d'T' -f1 | tr -d '"')
    
    if ! echo "$date" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$'; then
        echo "Warning: Invalid date format in line: $line" >&2
        continue
    fi
    
    output_file="$output_dir/$date.csv"
    if [ ! -f "$output_file" ]; then
        echo "$header" > "$output_file"
    fi
    
    echo "$line" >> "$output_file"
done

echo "Partitioning complete. Files created in '$output_dir/' directory."
echo "Number of partition files created: $(ls -1 "$output_dir"/*.csv 2>/dev/null | wc -l)"
