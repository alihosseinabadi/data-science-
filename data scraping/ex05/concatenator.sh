#!/bin/sh


input_dir="partitions"
output_file="hh_concatenated.csv"

if [ ! -d "$input_dir" ]; then
    echo "Error: Input directory '$input_dir' not found!" >&2
    exit 1
fi

if [ -z "$(ls -A "$input_dir"/*.csv 2>/dev/null)" ]; then
    echo "Error: No CSV files found in '$input_dir'!" >&2
    exit 1
fi

first_file=$(ls "$input_dir"/*.csv | head -1)
header=$(head -1 "$first_file")

echo "$header" > "$output_file"

for file in "$input_dir"/*.csv; do
    tail -n +2 "$file" >> "$output_file"
done

echo "Concatenation complete. Output saved to '$output_file'."
echo "Number of lines in output file: $(wc -l < "$output_file")"
echo "Number of partition files processed: $(ls -1 "$input_dir"/*.csv | wc -l)"
