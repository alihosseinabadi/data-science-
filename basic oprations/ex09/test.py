

class bank : 
    costumer = {}
    def  __init__(self,name: str , password : int , natniolity : str , id : int):
        self.name = name 
        self.password = password
        self.natniolity = natniolity
        bank.costumer[id] = self
    def ask(self):
        name = str(input("what is your name ? "))
        while True:
          natniolity = str(input("what is your natniolity"))
          password = int(input("write your password"))
          redline = ["isreal","saudi arabia", "turkey","africa"]
          for country in redline:
              if natniolity == country and len(password) < 6 :
                  print("sorry basically we cant help you for this condition")
              else:
                  break
          bank1 = bank(name,password,natniolity,id)

def main():
   bank2 = bank(name="erfan",password="1234567",natniolity="iran",id=1)  

if __name__ == "__main__ " : 
   main()

