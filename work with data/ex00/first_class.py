class must_read :
    with open("data.csv","r") as file_csv :
        content = file_csv.read()
        print(content)

if __name__ =='__main__' :
     must_read