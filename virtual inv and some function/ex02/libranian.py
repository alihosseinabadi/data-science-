import subprocess
import sys
import os

def main():
    name_env  = "unellase"
    path_env = os.environ.get('VIRTUAL_ENV')
    
    if not path_env or name_env not in path_env : 
        raise Exception(f"error must run from {name_env}virtual enviroment")
    
    print("installing all library in requirments.txt")
    subprocess.run([sys.executable, "-m" , "pip" , "install", "-r","requirements.txt"],check=True)

    print("we installed the package ")
    
    result = subprocess.run([sys.executable,"-m","pip", "freeze"],capture_output=True, text=True,check=True)
    installed_packages =result.stdout
    print(installed_packages)

    with open('requirements.txt', 'w') as f:
        f.write(installed_packages)
    print("\nSaved to requirements.txt")

if __name__ == '__main__':
    main()