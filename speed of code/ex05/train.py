import timeit
import sys
import json

class EmailFilter:
    def __init__(self, emails):
        self.emails = emails
    
    def check(self):
        result = []
        for x in self.emails:
            if x.endswith('gmail.com') or x.endswith('yahoo.com'):
                result.append(x)
        return result
    
    def faster(self):
        return [x for x in self.emails if x.endswith('gmail.com') or x.endswith('yahoo.com')]
    
    def map_filter(self):
        return list(filter(lambda x: x.endswith('gmail.com') or x.endswith('yahoo.com'), self.emails))

if __name__ == '__main__':
    # Usage: python script.py "['test@gmail.com','test@yahoo.com','test@hotmail.com']"
    if len(sys.argv) > 1:
        try:
            # Parse string list from command line
            emails = eval(sys.argv[1])  # Be careful with eval in production!
        except:
            # Or use comma-separated values
            emails = sys.argv[1].split(',')
    else:
        # Default test data
        emails = ['test@gmail.com', 'test@yahoo.com', 'test@hotmail.com', 'user@gmail.com']
    
    email_filter = EmailFilter(emails)
    
    print("Testing email filtering methods:")
    print("Input emails:", emails)
    
    # Time the methods
    first = timeit.timeit(lambda: email_filter.check(), number=10000)
    second = timeit.timeit(lambda: email_filter.faster(), number=10000)
    third = timeit.timeit(lambda: email_filter.map_filter(), number=10000)
    
    print(f"\nTiming results (10,000 iterations):")
    print(f"Loop method: {first:.6f} seconds")
    print(f"List comprehension: {second:.6f} seconds")
    print(f"Map/filter: {third:.6f} seconds")
    
    # Compare performance
    if first > second and first > third:
        print("\nLoop method is the slowest")
    elif second < first and second < third:
        print("\nList comprehension is the fastest")
    else:
        print("\nMap/filter method is competitive")