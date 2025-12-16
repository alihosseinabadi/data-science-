import sys

def generate_welcome_letter():
    # Check if email is provided
    if len(sys.argv) != 2:
        print("Usage: python3 letter_starter.py <email>")
        sys.exit(1)
    
    email = sys.argv[1].strip()
    
    try:
        # Read the TSV file
        with open('employees.tsv', 'r', encoding='utf-8') as tsv_file:
            lines = tsv_file.read().splitlines()
        
        # Skip header and search for the email
        found = False
        for line in lines[1:]:  # Skip header line
            parts = line.split('\t')
            if len(parts) >= 3:
                stored_email = parts[2]
                if stored_email == email:
                    name = parts[0]
                    welcome_message = f"Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. That's a precondition for the professionals that our company hires."
                    print(welcome_message)
                    found = True
                    break
        
        if not found:
            print(f"No employee found with email: {email}")
            
    except FileNotFoundError:
        print("Error: employees.tsv file not found. Run names_extractor.py first.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    generate_welcome_letter()