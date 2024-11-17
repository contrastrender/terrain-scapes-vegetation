import bpy

from . import const_utils
from . import property_utils
from . import ui_utils

classes  =  []
classes += const_utils.classes
classes += property_utils.classes
classes += ui_utils.classes


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    return 


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return