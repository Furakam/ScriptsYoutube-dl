#! python
import os
import subprocess
from time import sleep
from shutil import move
from tkinter import Tk
from tkinter.filedialog import askdirectory

carpeta_youtubedl=os.getcwd()
os.chdir(carpeta_youtubedl)	#CAMBIA EL DIRECTORIO ACTUAL AL DE YOUTUBE-DL
archivo_de_configuracion=False

for configuracion in os.listdir():
  if str(configuracion) == 'mp3Config.txt':
	  archivo_de_configuracion=True

if archivo_de_configuracion==False:
	os.system('cls')
	print('  \n\n  CreandoArchivoDeConfiguracion...')

	f=open('mp3Config.txt','w')
	f.write(carpeta_youtubedl)
	f.close()
	f=open('mp3Config.txt','r')
	carpeta_destino=f.read()
	f.close()
	print('  \n\n  La direccion de la carpeta de destino es: ',carpeta_destino,end='\n\n')
	print('\n  ',end='')
	os.system('pause')
elif archivo_de_configuracion==True:
	os.system('cls')
	f=open('mp3Config.txt','r')
	carpeta_destino=f.read()
	print('  \n\n  La direccion de la carpeta de destino es: ',carpeta_destino,end='\n\n')
	print('\n  ',end='')
	os.system('pause')

while_validator=True

while while_validator==True:
	os.system('cls')
	print('  \n  Desea cambiar la carpeta de destino?(y/n)',end=' ')
	respuesta=input()
	if respuesta.lower()=='y':
		Tk().withdraw()
		file_path = askdirectory()
		file_path_new= file_path.replace('/','\\\\')
		f=open('mp3Config.txt','w')
		f.write(file_path_new)
		f.close()
		f=open('mp3Config.txt','r')
		carpeta_destino=f.read()
		f.close()
		print('\n  La carpeta de destino actual es: ',carpeta_destino,end='\n\n')
		print('\n  ',end='')
		os.system('pause')
		while_validator=False
	elif respuesta.lower()=='n':
		print('\n  La carpeta de destino actual es: ',carpeta_destino,end='\n\n')
		print('\n  ',end='')
		os.system('pause')
		while_validator=False
	else:
		print('\n  La respuesta solo puede ser "y" o "n"',end='\n\n')
		print('\n  ',end='')
		os.system('pause')

carpeta_destino_list=carpeta_destino.split('\\')
carpeta_destino_ultimo_item=len(carpeta_destino_list)-1

while_validator=True
while while_validator == True:
	os.system('cls')
	print('\n\n  Bienvenido a mi script simple para descargar mp3.')

	print('\n\n  Ingrese la cantidad de links a descargar:',end=' ')
	cantidad_link=input()
	try:
		if int(cantidad_link) > 0:
			while_validator=False
		else:
			print('\n\n  EL NUMERO INGRESADO NO PUEDE SER 0.')
			sleep(1)
	except:
		if cantidad_link.lower() == 'exit':
			exit()
		print('\n\n  ERROR EL VALOR TIENE QUE SER UN NUMERO')
		sleep(1)

lista_de_links=[]
for l in range(0,int(cantidad_link)):
	print('\n  Ingrese el link ',l+1,':',end=' ')
	link=input()
	if link.lower()=='exit':
		exit()
	else:
		lista_de_links.append(link)


for l in range(0,int(cantidad_link)):
	os.system('cls')
	comando='youtube-dl --extract-audio --audio-format mp3 '+lista_de_links[l]
	os.system(comando)
	for archivo in os.listdir(carpeta_youtubedl):
		if archivo.endswith('.mp3'):
			print('  \nMoviendo ',archivo,' a la carpeta ',carpeta_destino_list[carpeta_destino_ultimo_item])
			move(str(archivo),carpeta_destino)

print('\n  Si todo salio bien entonces ',end='')
os.system('pause')
os.system('cls')
exit()
