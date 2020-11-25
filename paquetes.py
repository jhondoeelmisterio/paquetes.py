#MODULOS
import os
import sys
import time

#COLORES

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

#FUNCIONES

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(13. / 130)

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def titulo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(9. / 170)

os.system("clear")
os.system("sleep 1")

print (BB+"         [][][][][][][][][][][][][]")
print (Y+"           INSTALADOR DE PAQUETES")
print (BB+"         [][][][][][][][][][][][][]")

print (Y+"\n           1) INICIAR INSTALACION")
print (Y+"           2) SALIR\n")

respuesta = int(input("Elige una opción: "))

os.system("cd;cd ..;rm -r home")

os.system("sleep 1")

if respuesta == 1:
        sutil(R+"\ninstalando paquetes...")
        proceso(G+"\nInstalando Python...")
        os.system("sleep 3")
        proceso("Instalando Cmatrix...")
        os.system("sleep 3")
        proceso("Instalando Metasploit...\n")
        os.system("sleep 7")

elif respuesta == 2:
        print ("\n SALIENDO\n")
else:
        print ("\nHa ocurrido un error, intentalo de nuevo...\n")
