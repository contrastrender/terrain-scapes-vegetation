import bpy
import os

from .. const import __FILE__

icons = bpy.utils.previews.new()

def load_tsv_mask_items():
    path = os.path.join(os.path.dirname(__FILE__), "assets", "images", "masks")
    
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

class TSV_GROUP_mask(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty() #type: ignore
    texture: bpy.props.StringProperty() #type: ignore


class TSV_GROUP_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty() #type: ignore

class TSV_GROUP_group(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty() #type: ignore
    layers: bpy.props.CollectionProperty(type=TSV_GROUP_layer) #type: ignore
    layer_index: bpy.props.IntProperty() #type: ignore
    masks: bpy.props.CollectionProperty(type=TSV_GROUP_mask) #type: ignore
    mask_index: bpy.props.IntProperty() #type: ignore

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
        type=bpy.types.Object
    )
    
    bpy.types.Object.tsv_groups = bpy.props.CollectionProperty(
        type=TSV_GROUP_group
    )
    
    bpy.types.Object.tsv_group_index = bpy.props.IntProperty(
    )
    
    bpy.types.Scene.tsv_masks = bpy.props.EnumProperty(
        items=load_tsv_mask_items()
    )
    
    return None


def unregister():

    del bpy.types.Scene.tsv_masks
    del bpy.types.Object.tsv_group_index
    del bpy.types.Object.tsv_groups
    del bpy.types.Scene.tsv_emitter

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return None