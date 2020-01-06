from bpy_lambda import bpy


def handler(event, context):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    bpy.ops.mesh.primitive_uv_sphere_add()
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].octree_depth = 1
    bpy.context.object.modifiers["Remesh"].scale = 0.9
    bpy.context.object.modifiers["Remesh"].threshold = 1
    bpy.context.object.modifiers["Remesh"].sharpness = 0
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
    # Test REMESH operation
    assert(len(bpy.context.object.data.vertices) == 8)
    return {'status': 'ok'}
