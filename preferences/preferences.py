import bpy

from .. const import __PACKAGE__
from .. ui.preset_manager import tsv_preset_manager
from .. utils.property_utils import property_exists

class TSV_GROUP_preset_layer_input(bpy.types.PropertyGroup):

    type: bpy.props.StringProperty() #type: ignore

    value: bpy.props.StringProperty() #type: ignore

class TSV_GROUP_preset_layer(bpy.types.PropertyGroup):

    label: bpy.props.StringProperty() # type: ignore

    inputs: bpy.props.CollectionProperty(
        type=TSV_GROUP_preset_layer_input
    ) #type: ignore

class TSV_GROUP_preset_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty() # type: ignore
    
    preset_layers: bpy.props.CollectionProperty(
        type=TSV_GROUP_preset_layer
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
        if property_exists("bpy.context.preferences.filepaths.asset_libraries['Terrain Scapes Vegetation']", globals(), locals()):
            pass
        else:
            op = column.operator('sna.load_asset_library_db971', text='Load Asset Library', icon_value=0, emboss=True, depress=False)
        tsv_preset_manager(column, )

classes = [
    TSV_GROUP_preset_layer_input,
    TSV_GROUP_preset_layer,
    TSV_GROUP_preset_group,
    TSV_AddonPreferences
]