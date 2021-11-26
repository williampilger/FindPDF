# By: will.i.am
# 2021.11.25
# 𝅘𝅥𝅮  Heathens (Twenty One Pilots)

import os
import platform

eh_windows = platform.system() == "Windows"
eh_linux = platform.system() == "Linux"

def restart_program():
    if(eh_windows):
        os.system(f"python \"main.py\"")
    elif(eh_linux):
        os.system(f"python3 \"main.py\"")
    quit()
    
def install_lib(lib):
    print(f"\nINSTALANDO BIBLIOTECA NECESSÁRIA, AGUARDE!\n(CONEXÃO COM INTERNET NECESSÁRIA)\n{lib}")
    if(eh_windows):
        os.system(f"pip install --upgrade {lib}")
    elif(eh_linux):
        os.system(f"pip3 install --upgrade {lib}")

def limpar_terminal():
    if(eh_windows):
        os.system("cls")
    elif(eh_linux):
        os.system("clear")
    return

#cria um diretório
def mkdir(dir):
    if(eh_windows or eh_linux):
        os.system(f"mkdir {dir}")

#Remove (forçado) um diretório
def rmdir(dir):
    if(eh_windows):
        os.system(f"rmdir /s /q {dir}")
    if(eh_linux):
        os.system(f"rm -r -f {dir}")

#excluir arquivo
def delfile(file):
    if(eh_windows):
        os.system(f"del /q {file}")
    elif(eh_linux):
        os.system(f"rm -f {file}")

def dirConvert(dirstring):
    if(eh_windows):
        return dirstring.replace("/","\\")
    elif(eh_linux):
        return dirstring.replace("\\","/")
if(eh_linux):
    dirSep = "/"
elif(eh_windows):
    dirSep = "\\"

#Iniciar um arquivo
def startfile(fileName):
    if(eh_linux):
        pass
    if(eh_windows):
        os.system(f"start \"{fileName}\"")