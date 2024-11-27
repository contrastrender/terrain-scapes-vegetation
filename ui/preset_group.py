import bpy

from .. helper.get_prop_helper import tsv_get_preset_group

def tsv_display_preset_group(layout: bpy.types.UILayout):

    preset_group = tsv_get_preset_group()

    if preset_group is None:
        return None
    
    col = layout.column(align=True)

    for preset_group_layer in preset_group.layers:
        box = col.box()
        box.label(text=f"{preset_group_layer.label}")
    