import bpy

from .. ui.preset_group import tsv_display_preset_group

from .. const import __PACKAGE__
from ..ui.preset_manager import tsv_preset_manager

class TSV_GROUP_preset_group_layer_input(bpy.types.PropertyGroup):

    type: bpy.props.StringProperty() #type: ignore

    value: bpy.props.StringProperty() #type: ignore

class TSV_GROUP_preset_group_layer(bpy.types.PropertyGroup):

    label: bpy.props.StringProperty() # type: ignore

    inputs: bpy.props.CollectionProperty(
        type=TSV_GROUP_preset_group_layer_input
    ) #type: ignore

class TSV_GROUP_preset_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty() # type: ignore
    
    layers: bpy.props.CollectionProperty(
        type=TSV_GROUP_preset_group_layer
    ) #type: ignore

class TSV_AddonPreferences(bpy.types.AddonPreferences):

    bl_idname = __PACKAGE__

    preset_groups: bpy.props.CollectionProperty(
        type=TSV_GROUP_preset_group
    ) #type: ignore
    
    preset_group_index: bpy.props.IntProperty() #type: ignore
 
    def draw(self, context):
        layout = self.layout
        column = layout.column(heading='', align=False)
        tsv_preset_manager(column)
        tsv_display_preset_group(column)

classes = [
    TSV_GROUP_preset_group_layer_input,
    TSV_GROUP_preset_group_layer,
    TSV_GROUP_preset_group,
    TSV_AddonPreferences
]