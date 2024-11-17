import bpy

from . import export_preset_group
from . import import_preset_group
from . import open_preset_manager
from . import remove_preset_group
from . import save_preset_group
from . import move_preset_group
from . import add_vegetation_geo_nodes
from . import remove_vegetation_geo_nodes
from . import add_group
from . import remove_group
from . import move_group_layer
from . import group_layer


from . import expand_ui #legacy

classes  =  []
classes += export_preset_group.classes
classes += import_preset_group.classes
classes += open_preset_manager.classes
classes += remove_preset_group.classes
classes += save_preset_group.classes
classes += move_preset_group.classes
classes += add_vegetation_geo_nodes.classes
classes += remove_vegetation_geo_nodes.classes
classes += add_group.classes
classes += remove_group.classes
classes += move_group_layer.classes
classes += group_layer.classes


classes += expand_ui.classes


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    return 


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return