import bpy

from . import vegetation_panel
from . import group_panel
from . import group_masks_panel
from . import group_layers_panel
from . import preset_manager
from . import layer_add_asset_panel

classes  =  []
classes += vegetation_panel.classes
classes += group_panel.classes
classes += group_masks_panel.classes
classes += group_layers_panel.classes
classes += preset_manager.classes
classes += layer_add_asset_panel.classes


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    return 


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return