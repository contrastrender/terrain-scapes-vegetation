import bpy
from ..ui.preset_manager import tsv_preset_manager
from ..utils.property_utils import property_exists
from ..utils.const_utils import ROOT_PACKAGE_NAME

class TSV_GROUP_preset_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(
        name='label',
        description='',
        default='',
        subtype='NONE',
        maxlen=0) # type: ignore
    
    inputs: bpy.props.StringProperty(
        name='Inputs',
        description='',
        default='',
        subtype='NONE',
        maxlen=0) #type: ignore

class TSV_GROUP_preset_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(
        name='label',
        description='',
        default='',
        subtype='NONE',
        maxlen=0
        ) # type: ignore
    
    tsv_preset_layers: bpy.props.CollectionProperty(
        name='TSV_preset_layers',
        description='',
        type=TSV_GROUP_preset_layer
        ) #type: ignore

class TSV_AddonPreferences(bpy.types.AddonPreferences):

    bl_idname = ROOT_PACKAGE_NAME #must match the root package name __package__
    sna_tsv_preset_groups: bpy.props.CollectionProperty(
        name='TSV_preset_groups',
        description='',
        type=TSV_GROUP_preset_group
        ) #type: ignore
    
    sna_tsv_preset_groups_index: bpy.props.IntProperty(
        name='TSV_preset_groups_index',
        description='',
        default=0,
        subtype='NONE'
        ) #type: ignore
 
    def draw(self, context):
        if not (False):
            layout = self.layout
            column = layout.column(heading='', align=False)
            if property_exists("bpy.context.preferences.filepaths.asset_libraries['Terrain Scapes Vegetation']", globals(), locals()):
                pass
            else:
                op = column.operator('sna.load_asset_library_db971', text='Load Asset Library', icon_value=0, emboss=True, depress=False)
            tsv_preset_manager(column, )

classes = [
    TSV_GROUP_preset_layer,
    TSV_GROUP_preset_group,
    TSV_AddonPreferences
]