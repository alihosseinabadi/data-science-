import sys

def caesar_cipher():
    if len(sys.argv) != 4:
        raise Exception("Usage: python3 caesar.py <encode|decode> <text> <shift>")
    
    operation = sys.argv[1]
    text = sys.argv[2]
    
    try:
        shift = int(sys.argv[3])
    except ValueError:
        raise Exception("Shift must be an integer")
    
    for char in text:
        if '\u0400' <= char <= '\u04FF':  
            raise Exception("The script does not support your language yet.")
    
    result = ""
    
    if operation == "encode":
        result = encode(text, shift)
    elif operation == "decode":
        result = decode(text, shift)
    else:
        raise Exception("Operation must be 'encode' or 'decode'")
    
    print(result)

def encode(text, shift):
    """Encode text using Caesar cipher"""
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)

def decode(text, shift):
    """Decode text using Caesar cipher (encode with negative shift)"""
    return encode(text, -shift)

if __name__ == '__main__':
    caesar_cipher()