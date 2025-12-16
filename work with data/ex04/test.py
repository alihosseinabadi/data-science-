import os 
import sys

class read : 
     def __init__(self,path):
          self.path = path
     def check(self,has_head = True):
          if not os.path.exists(self.path):
               return f"basically you dont have a any file"
          #we here take validation of file content 
          with open(self.path,'r') as file :
               lines = file.readlines()
               if has_head :
                    new_data = lines[1:]
               else :
                    new_data = lines
                #in here we make result of our check head
               result = []
               for line in new_data :
                    value = line.strip().split(",")
                    result.append([int(value[0]),int(value[1])])

                    return result
     class calculation : 
          def __init__(self,data):
            self.data = data
          def count(self):
               for x in self.data :
                    head = sum(x[0])
                    tail = sum(x[1])
                    return head , tail
          def percantage(self,head ,tail):
                 total = heads + tails
                 head_percent = (heads / total) * 100
                 tail_percent = (tails / total) * 100
                 return head_percent, tail_percent
class dataanalyst(read.calculation):
     def __init__(self, data):
          super().__init__(data)
               
          