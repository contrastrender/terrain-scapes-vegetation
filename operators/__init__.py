import bpy

from . import ui
from . import preset_group
from . import group
from . import group_layer
from . import group_mask

classes  =  []
classes += ui.classes
classes += preset_group.classes
classes += group.classes
classes += group_layer.classes
classes += group_mask.classes


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    return 


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return