import os
import sys
import subprocess
import socket

class Shell:
    def close():
        sys.exit()
    
    def clear():
        os.system('cls')
      
    def update():
        try:
            subprocess.check_call(['git', 'pull'])
            print('Script updated successfully. Please restart the shell.')
            sys.exit()
        except subprocess.CalledProcessError as e:
            print(f'Failed to update script: {e}')
            sys.exit()

class IP:
    def config():
        ip=subprocess.getoutput('ipconfig')
        return ip
