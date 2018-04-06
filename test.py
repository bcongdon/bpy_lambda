from bpy_lambda import bpy


def handler(event, context):
    bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
    cube = bpy.context.scene.objects.active
    cube.scale = (1, 2, 3)
    return {'status': 'ok'}
