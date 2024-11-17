import bpy

from . import group_layer_helper

classes  =  []
classes += group_layer_helper.classes


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    return 


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return