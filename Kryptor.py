import os
os.system("clear")
from hashlib import sha256
print('''
 /$$   /$$                                 /$$                        
| $$  /$$/                                | $$                        
| $$ /$$/   /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$$$$/   /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$  | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$| $$  \__/
| $$\  $$ | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$| $$      
| $$ \  $$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/| $$      
|__/  \__/|__/       \____  $$| $$____/    \___/   \______/ |__/      
                     /$$  | $$| $$                                    
                    |  $$$$$$/| $$                                    
                     \______/ |__/    
                     
                     
                     
                     ENCODE XOR                                
 /$$   /$$        /$$$$$$        /$$$$$$$                             
| $$  / $$       /$$__  $$      | $$__  $$                            
|  $$/ $$/      | $$  \ $$      | $$  \ $$                            
 \  $$$$/       | $$  | $$      | $$$$$$$/                            
  >$$  $$       | $$  | $$      | $$__  $$                            
 /$$/\  $$      | $$  | $$      | $$  \ $$                            
| $$  \ $$      |  $$$$$$/      | $$  | $$                            
|__/  |__/       \______/       |__/  |__/                            
                                               
                                                                      
██╗   ██╗ ██╗    ██████╗     ██████╗ ███████╗████████╗ █████╗ 
██║   ██║███║   ██╔═████╗    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
██║   ██║╚██║   ██║██╔██║    ██████╔╝█████╗     ██║   ███████║
╚██╗ ██╔╝ ██║   ████╔╝██║    ██╔══██╗██╔══╝     ██║   ██╔══██║
 ╚████╔╝  ██║██╗╚██████╔╝    ██████╔╝███████╗   ██║   ██║  ██║
  ╚═══╝   ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝
]|                                                              
||>>>>>>>>>>>>>>>>>>>>>           
||FurySec            ||
||By H-TechDev36     ||
||>>>>>>>>>>>>>>>>>>>>>
]|
.________________________.
| www.furysec7.webnode.fr| 
|.______________________.|
''')
entree = input("Name of file to Crypt/Uncrypt >>> ")
sortie = input("Final file : ")
key = input("Key  : ")
keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
 with open(sortie,'wb') as f_sortie:
  i = 0
  while f_entree.peek():
    c = ord(f_entree.read(1))
    j = i % len(keys)
    b = bytes([c^keys[j]])
    f_sortie.write(b)
    i = i + 1 
