#!/bin/sh

query=$(echo '$1' | tr ' ' '+' )
url="https://api.hh.ru/vacancies?text=$query&per_page=20"

curl -s "$url" | jq  '.items[] | [.id, .name, .has_test]' > hh1.json

echo "we did it "