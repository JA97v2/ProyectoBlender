'''Nota soblre bpy!!!
    Incluso si bpy no se puede instalar desde pip, esete script se ejecuta
    desde blender, y blender si tiene el módulo bpy.
'''
import bpy
import os
import sys

# Añadir directorio actual a la lista de directorios de los módulos
sys.path.append('.')
''' NOTA!!!
    Este orden de importación es el único que ha permitido importar las clases
    desde el archivo blenderModelo.py
'''
from blenderModelo import Objeto, Escena


def main():

    bpy.data.objects['Cube'].select_set(True)           # Seleccionar cubo por defecto  
    bpy.ops.object.delete()                             # Eliminar cubo por defecto 

    obj = Objeto()

    # Crear cilindro
    obj.cilindro((0, 0, 0), (1, 1, 1), 1, 1)

    esc = Escena()
    ruta = os.getcwd() + '\\Renders\\render.png'
    esc.renderizar(ruta, 1920, 1080)

    # Guardar archivo en formato .blend
    #bpy.ops.wm.save_as_mainfile(filepath="C:\\Users\\ASUS\\Downloads\\test.blend")

main()