#!/bin/sh


input="../ex03/hh_positions.csv"
output="hh_uniq_positions.csv"


if [ ! -f "$input" ]; then
    echo "Error: Input file '$input' not found!"
    exit 1
fi


tail -n +2 "$input" | awk -F, '{print $NF}' | \
sed 's/"//g' | sed 's/^[ \t]*//;s/[ \t]*$//' | \
grep -v "^-$" | grep -v "^$" | \
sort | uniq -c | \
sort -k1,1nr -k2,2 | \
awk '{printf "\"%s\",%d\n", $2, $1}' | \
awk 'BEGIN {print "\"name\",\"count\""} {print}' > "$output"

echo "Processing complete. Results saved to $output"
echo "Sample of results:"
head -n 5 "$output"
