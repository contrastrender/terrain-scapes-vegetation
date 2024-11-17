import bpy
import os

from .. utils.const_utils import ROOT_DIR

_item_map = dict()

biome_density_mask__add = {'sna_masks': [], }
load_preset_group = {'sna_missing_assets': [], 'sna_asset_libraries': [], }

def make_enum_item(_id, name, descr, preview_id, uid):
    lookup = str(_id)+"\0"+str(name)+"\0"+str(descr)+"\0"+str(preview_id)+"\0"+str(uid)
    if not lookup in _item_map:
        _item_map[lookup] = (_id, name, descr, preview_id, uid)
    return _item_map[lookup]

def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id

def tsv_masks_enum_items(self, context):
    enum_items = biome_density_mask__add['sna_masks']
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]

def tsv_searchable_asset_libraries_enum_items(self, context):
    enum_items = load_preset_group['sna_asset_libraries']
    return [make_enum_item(item[0], item[1], item[2], item[3], 2**i) for i, item in enumerate(enum_items)]

def sna_tsv_layer_low_poly_objects_enum_items(self, context):
    # Define the directory paths
    base_dir = os.path.dirname(__file__)
    assets_dir = os.path.join(ROOT_DIR, 'assets', 'low_poly_objects')
    
    # Define low poly objects with their corresponding icons
    object_names = [f'TSV_low_poly_object_{i}' for i in range(1, 12)]
    enum_items = [
        [
            obj_name,
            obj_name,
            '',
            load_preview_icon(os.path.join(assets_dir, f'{obj_name}.png'))
        ]
        for obj_name in object_names
    ]
    
    # Generate enum items
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]


def sna_update_viewport_display_516D8(self, context):
    """
    Update the viewport display settings for the vegetation system based on the
    selected layer and group configuration.
    """
    # Get the updated property value
    sna_updated_prop = self.viewport_display
    
    # Access key elements of the current context
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    group_index = tsv_emitter.tsv_group_index
    group = tsv_emitter.tsv_groups[group_index]
    layer_index = group.layer_index
    layer = group.layers[layer_index]
    
    # Construct the node identifier
    node_identifier = f"{group_index},{layer_index}_layer"
    node = tsv_emitter.modifiers['vegetation'].node_group.nodes[node_identifier]
    
    # Update the primary input value
    node.inputs[10].default_value = sna_updated_prop
    
    # Check conditions for updating the low poly object input
    if layer.low_poly_objects and sna_updated_prop == 'Low Poly':
        low_poly_object = bpy.data.objects[layer.low_poly_objects]
        node.inputs[11].default_value = low_poly_object

def sna_update_low_poly_objects_4322F(self, context):
    sna_updated_prop = self.low_poly_objects
    bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index) + '_layer'].inputs[11].default_value = bpy.data.objects[sna_updated_prop]


class TSV_GROUP_mask(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    texture: bpy.props.StringProperty(name='Texture', description='', default='', subtype='NONE', maxlen=0)


class TSV_GROUP_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    viewport_display: bpy.props.EnumProperty(name='Viewport Display', description='', items=[('Bounding Box', 'Bounding Box', '', 0, 0), ('Object', 'Object', '', 0, 1), ('Low Poly', 'Low Poly', '', 0, 2)], update=sna_update_viewport_display_516D8)
    low_poly_objects: bpy.props.EnumProperty(name='Low Poly Objects', description='', items=sna_tsv_layer_low_poly_objects_enum_items, update=sna_update_low_poly_objects_4322F)

class TSV_GROUP_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    layers: bpy.props.CollectionProperty(name='Layers', description='', type=TSV_GROUP_layer)
    layer_index: bpy.props.IntProperty(name='Layer Index', description='', default=0, subtype='NONE')
    density_masks: bpy.props.CollectionProperty(name='Density Masks', description='', type=TSV_GROUP_mask)
    density_mask_index: bpy.props.IntProperty(name='Density Mask Index', description='', default=0, subtype='NONE')

#from . import module

classes  =  [
    TSV_GROUP_mask,
    TSV_GROUP_layer,
    TSV_GROUP_group
]
#classes += module.classes

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.tsv_emitter = bpy.props.PointerProperty(name='TSV_emitter', description='', type=bpy.types.Object)
    bpy.types.Object.tsv_groups = bpy.props.CollectionProperty(name='TSV_group_layers', description='', type=TSV_GROUP_group)
    bpy.types.Object.tsv_group_index = bpy.props.IntProperty(name='TSV_group_layer_index', description='', default=0, subtype='NONE')
    bpy.types.Scene.tsv_masks = bpy.props.EnumProperty(name='TSV_masks', description='', items=tsv_masks_enum_items)
    bpy.types.Scene.tsv_searchable_asset_libraries = bpy.props.EnumProperty(name='TSV_searchable_asset_libraries', description='', items=tsv_searchable_asset_libraries_enum_items, options={'ENUM_FLAG'})
    bpy.types.Scene.tsv_expand_preset_layers = bpy.props.BoolProperty(name='TSV_expand_preset_layers', description='', default=False)

    return 


def unregister():

    del bpy.types.Scene.tsv_expand_preset_layers
    del bpy.types.Scene.tsv_searchable_asset_libraries
    del bpy.types.Scene.tsv_masks
    del bpy.types.Object.tsv_group_index
    del bpy.types.Object.tsv_groups
    del bpy.types.Scene.tsv_emitter

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return