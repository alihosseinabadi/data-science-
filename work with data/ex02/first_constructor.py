import sys
import os

class search: 
    def __init__(self, file_path):
        self.file_path = file_path
    def file_reader(Self):
        if not  os.path.exists(Self.file_path):
            raise Exception("file not find")
        with open(Self.file_path, "r") as file : 
            lines = file.readlines()

            header = lines[0].strip().split(',')
            if len(header) !=2:
                raise Exception("invalid headers")
            for i , lines in enumerate(lines[1:],1):
                value = lines.strip().split(',')
                if len(value) != 2 :
                       raise Exception(f"Invalid data format on line {i+1}")
                if value[0] not in ['0', '1'] or value[1] not in ['0', '1']:
                    raise Exception(f"Invalid values on line {i+1}")
                if value[0] == value[1]:
                    raise Exception(f"Both values are same on line {i+1}")
        with open(Self.file_path, 'r') as file:
               return file.read()
            
if  __name__ == '__main__':
    if len(sys.argv) != 2 : 
        print(" usage : file path pls")
        sys.exit(1)
    search1 = search(sys.argv[1])
    print(search1.file_reader())