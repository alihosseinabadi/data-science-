import sys
import os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
    
    def file_reader(self, has_header=True):
       
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File {self.file_path} not found")
    
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            
            if has_header:
                data_lines = lines[1:]
            else:
                data_lines = lines
            
            result = []
            for line in data_lines:
                values = line.strip().split(',')
                result.append([int(values[0]), int(values[1])])
            
            return result
    
    class Calculations:
       
        @staticmethod
        def counts(data):
           
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails
        
        @staticmethod
        def fractions(heads, tails):
           
            total = heads + tails
            if total == 0:
                return 0, 0  
            
            head_percent = (heads / total) * 100
            tail_percent = (tails / total) * 100
            return head_percent, tail_percent

if __name__ == '__main__':
 
    if len(sys.argv) != 2:
        print("Usage: python first_nest.py <file_path>")
        sys.exit(1)
    
    try:
        research = Research(sys.argv[1])
        
        data = research.file_reader()
        print(data)
        
        heads, tails = Research.Calculations.counts(data)
        print(heads, tails)
        
        head_percent, tail_percent = Research.Calculations.fractions(heads, tails)
        print(head_percent, tail_percent)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)