import subprocess
import os

def cmd(comando):
    subprocess.run(comando, shell=True)

# Obtener directorio actual
dirActual = os.getcwd()

# Nombre de la carpeta donde se encuentra el archivo blender.exe
blenderFolder = 'blender-3.1.2-windows-x64'

# Directorio desde el cual se ejecuta blender
dirBlender = '{}\\blender'.format(blenderFolder)

# Cambiar cmd a directorio actual
cmd('cd {}'.format(dirActual))

# Ejecutar script de python en blender
cmd('{} -b -P blenderControlador.py'.format(dirBlender))