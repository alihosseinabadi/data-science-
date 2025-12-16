def convert_csv_to_tsv():
    with open('ds.csv', 'r', encoding='utf-8') as csv_file:
        with open('ds.tsv', 'w', encoding='utf-8') as tsv_file:
            for line in csv_file:
                
                parts = line.split('"')
                
                for i in range(len(parts)):
                    if i % 2 == 0:  
                        parts[i] = parts[i].replace(',', '\t')
                
                modified_line = '"'.join(parts)
                tsv_file.write(modified_line)

if __name__ == '__main__':
    convert_csv_to_tsv()