import sys

def process_emails():
    # Check if filename is provided
    if len(sys.argv) != 2:
        print("Usage: python3 names_extractor.py <filename>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    
    try:
        # Read emails from file
        with open(input_filename, 'r', encoding='utf-8') as file:
            emails = file.read().splitlines()
        
        # Process each email and create TSV content
        tsv_lines = ["Name\tSurname\tEmail"]  # Header
        
        for email in emails:
            email = email.strip()
            if email and '@corp.com' in email:
                # Extract name and surname from email
                username = email.split('@')[0]
                
                if '.' in username:
                    name_part, surname_part = username.split('.', 1)
                    
                    # Capitalize first letter of each
                    name = name_part.capitalize()
                    surname = surname_part.capitalize()
                    
                    # Create TSV line
                    tsv_lines.append(f"{name}\t{surname}\t{email}")
        
        # Write to employees.tsv
        with open('employees.tsv', 'w', encoding='utf-8') as tsv_file:
            tsv_file.write('\n'.join(tsv_lines))
            
        print(f"Successfully processed {len(tsv_lines)-1} emails to employees.tsv")
        
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    process_emails()