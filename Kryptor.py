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
                     
                     
                     
                     ENCODE XOR AND cesar CHRF                        
 /$$   /$$        /$$$$$$        /$$$$$$$                             
| $$  / $$       /$$__  $$      | $$__  $$                            
|  $$/ $$/      | $$  \ $$      | $$  \ $$                            
 \  $$$$/       | $$  | $$      | $$$$$$$/                            
  >$$  $$       | $$  | $$      | $$__  $$                            
 /$$/\  $$      | $$  | $$      | $$  \ $$                            
| $$  \ $$      |  $$$$$$/      | $$  | $$                            
|__/  |__/       \______/       |__/  |__/                            
                                        __       
                                       /%/                               
██╗   ██╗ ██╗    ██████╗     ██████╗ ███████╗████████╗ █████╗ 
██║   ██║███║   ██╔═████╗    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
██║   ██║╚██║   ██║██╔██║    ██████╔╝█████╗     ██║   ███████║
╚██╗ ██╔╝ ██║   ████╔╝██║    ██╔══██╗██╔══╝     ██║   ██╔══██║
 ╚████╔╝  ██║██╗╚██████╔╝    ██████╔╝███████╗   ██║   ██║  ██║
  ╚═══╝   ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝

XOR IS ONLY FOR LINUX !
]|                                                              
||>>>>>>>>>>>>>>>>>>>>>           
||FurySec            ||
||By H-TechDev36     ||
||>>>>>>>>>>>>>>>>>>>>>
]|
.________________________.
| www.furysec.webnode.fr | 
|.______________________.|
DO NOT USE XOR ON WINDOWS !
:-++===[Use it on windows at  your own risks]===++-:
on windows Kryptor do not crypt the file HE DESTROY IT !
''')
print("3 to decrypt Cersar [words]")
mode = int(input("Cesar = 1 [words] |   XOR = 2 [files]>>> "))
if mode ==2:
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
else:
  Messageacrypter= input("Words to be crypted >>> ")
  cle=24 

  acrypter=Messageacrypter.upper()
  lg=len(acrypter)
  MessageCrypte=""

  for i in range(lg):
      if acrypter[i]==' ':
        MessageCrypte+=' '
      else:
          asc=ord(acrypter[i])+cle
          MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

          print(MessageCrypte)
