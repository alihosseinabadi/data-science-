class must_read:
    def file_reader(self):
        with open('data.csv','r') as file_csv :
            content = file_csv.read()
            return content
        
if __name__ == '__main__' :
     search  = must_read()
     print(search.file_reader())