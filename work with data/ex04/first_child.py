# ex04/first_child.py
import sys
import os
from random import randint

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
        def __init__(self, data):
            self.data = data
        
        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails
        
        def fractions(self, heads, tails):
            total = heads + tails
            head_percent = (heads / total) * 100
            tail_percent = (tails / total) * 100
            return head_percent, tail_percent

class Analytics(Research.Calculations):
    def __init__(self, data):
        super().__init__(data)
    
    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            prediction = randint(0, 1)
            predictions.append([prediction, 1 - prediction])
        return predictions
    
    def predict_last(self):
        return self.data[-1] if self.data else None

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python first_child.py <file_path>")
        sys.exit(1)
    
    try:
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)
        
        calculations = Research.Calculations(data)
        heads, tails = calculations.counts()
        print(heads, tails)
        
        head_percent, tail_percent = calculations.fractions(heads, tails)
        print(head_percent, tail_percent)
        
        analytics = Analytics(data)
        predictions = analytics.predict_random(3)
        print(predictions)
        
        last_prediction = analytics.predict_last()
        print(last_prediction)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)