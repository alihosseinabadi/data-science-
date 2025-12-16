#!/bin/sh

q=$(echo "$1" | tr ' ' '+')
URL="https://api.hh.ru/vacancies?text=$q&per_page=100"
curl -s "$URL" | jq '.' > hh.json
echo "JSON file has been created: hh.json"
