from typing import Iterable
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

icons = bpy.utils.previews.new()

def load_tsv_mask_items():
    path = os.path.join(ROOT_DIR, "assets", "images", "masks")
    
    # Get icon names dynamically from the directory
    icon_names = [
        os.path.splitext(file_name)[0] 
        for file_name in os.listdir(path) 
        if file_name.endswith('.png')
    ]
    
    # Load all icons iteratively
    for name in icon_names:
        icons.load(
            name=name,
            path=os.path.join(path, f"{name}.png"),
            path_type='IMAGE'
        )
    
    # Create the return list iteratively
    return [
        (name, name, '', icons[name].icon_id, idx) 
        for idx, name in enumerate(icon_names)
    ]


def tsv_searchable_asset_libraries_enum_items(self, context):
    enum_items = load_preset_group['sna_asset_libraries']
    return [make_enum_item(item[0], item[1], item[2], item[3], 2**i) for i, item in enumerate(enum_items)]

def load_tsv_low_poly_objects_items():
    path = os.path.join(ROOT_DIR, "assets", "images", "low_poly_objects")
    
    # Get icon names dynamically from the directory
    icon_names = [
        os.path.splitext(file_name)[0] 
        for file_name in os.listdir(path) 
        if file_name.endswith('.png')
    ]
    
    # Load all icons iteratively
    for name in icon_names:
        icons.load(
            name=name,
            path=os.path.join(path, f"{name}.png"),
            path_type='IMAGE'
        )
    
    # Create the return list iteratively
    return [
        (name, name, '', icons[name].icon_id, idx) 
        for idx, name in enumerate(icon_names)
    ]


def update_viewport_display(self, context):
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

def update_low_poly_objects(self, context):
    sna_updated_prop = self.low_poly_objects
    scene = bpy.context.scene
    emitter = scene.tsv_emitter
    group_index = emitter.tsv_group_index
    layer_index = emitter.tsv_groups[group_index].layer_index
    node_name = f"{group_index},{layer_index}_layer"
    
    modifier = emitter.modifiers['vegetation']
    node_group = modifier.node_group
    node = node_group.nodes[node_name]
    
    # Update the input value
    node.inputs[11].default_value = bpy.data.objects[sna_updated_prop]


class TSV_GROUP_mask(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0) #type: ignore
    texture: bpy.props.StringProperty(name='Texture', description='', default='', subtype='NONE', maxlen=0) #type: ignore


class TSV_GROUP_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(
        name='Label', 
        description='', 
        default='', 
        subtype='NONE', 
        maxlen=0
        ) #type: ignore
    
    viewport_display: bpy.props.EnumProperty(
        name='Viewport Display', 
        description='', 
        items=[
            ('Bounding Box', 'Bounding Box', '', 0, 0), 
            ('Object', 'Object', '', 0, 1), 
            ('Low Poly', 'Low Poly', '', 0, 2)
        ], 
        update=update_viewport_display
        ) #type: ignore
    
    low_poly_objects: bpy.props.EnumProperty(
        name = 'Low Poly Objects', description='',
        items = load_tsv_low_poly_objects_items(), 
        update = update_low_poly_objects
        ) #type: ignore

class TSV_GROUP_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0) #type: ignore
    layers: bpy.props.CollectionProperty(name='Layers', description='', type=TSV_GROUP_layer) #type: ignore
    layer_index: bpy.props.IntProperty(name='Layer Index', description='', default=0, subtype='NONE') #type: ignore
    density_masks: bpy.props.CollectionProperty(name='Density Masks', description='', type=TSV_GROUP_mask) #type: ignore
    density_mask_index: bpy.props.IntProperty(name='Density Mask Index', description='', default=0, subtype='NONE') #type: ignore

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

    bpy.types.Scene.tsv_emitter = bpy.props.PointerProperty(
        name='TSV_emitter',
        description='', 
        type=bpy.types.Object
        )
    
    bpy.types.Object.tsv_groups = bpy.props.CollectionProperty(
        name='TSV_group_layers',
        description='', 
        type=TSV_GROUP_group
        )
    
    bpy.types.Object.tsv_group_index = bpy.props.IntProperty(
        name='TSV_group_layer_index',
        description='', 
        default=0, 
        subtype='NONE'
        )
    
    bpy.types.Scene.tsv_masks = bpy.props.EnumProperty(
        name='TSV_masks',
        description='',
        items=load_tsv_mask_items()
        )
    
    bpy.types.Scene.tsv_searchable_asset_libraries = bpy.props.EnumProperty(
        name='TSV_searchable_asset_libraries',
        description='', 
        items=tsv_searchable_asset_libraries_enum_items, 
        options={'ENUM_FLAG'}
        )
    
    bpy.types.Scene.tsv_expand_preset_layers = bpy.props.BoolProperty(
        name='TSV_expand_preset_layers',
        description='', 
        default=False
        )
    
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