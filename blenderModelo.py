'''Nota soblre bpy!!!
    Incluso si bpy no se puede instalar desde pip, esete script se ejecuta
    desde blender, y blender si tiene el módulo bpy.
'''
import bpy
import subprocess
import os



# Definir clase para crear objetos
class Objeto:
    def cubo(self, size: float, location: tuple, scale: tuple):
        return bpy.ops.mesh.primitive_cube_add(
            size=size, enter_editmode=False, 
            align='WORLD', location=location, scale=scale
        )

    def cilindro(self, location: tuple, scale: tuple, radius: float, height: float):
        return bpy.ops.mesh.primitive_cylinder_add(
            location=location, scale=scale, 
            radius=radius, depth=height, end_fill_type="NOTHING"
        )

    def esfera(self, location: tuple, scale: tuple, radius: float):
        return bpy.ops.mesh.primitive_uv_sphere_add(
            location=location, scale=scale, 
            size=radius
        )

# Definir clase para organizar escena
class Escena:
    def renderizar(self, filepath: str, ancho: int, alto: int):
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.filepath = filepath
        bpy.context.scene.render.resolution_x = ancho
        bpy.context.scene.render.resolution_y = alto
        bpy.ops.render.render(write_still = 1)