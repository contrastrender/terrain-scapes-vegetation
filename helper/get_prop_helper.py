import bpy

from .. const import __PACKAGE__

# preferences

def tsv_get_preferences():
    return bpy.context.preferences.addons[__PACKAGE__].preferences

#preset groups

def tsv_get_preset_groups():
    preferences = tsv_get_preferences()
    return preferences.preset_groups

def tsv_get_preset_group_index():
    preferences = tsv_get_preferences()
    return preferences.preset_group_index

def tsv_get_preset_group():
    preset_groups = tsv_get_preset_groups()
    preset_group_index = tsv_get_preset_group_index()
    try:
        return preset_groups[preset_group_index]
    except:
        return None

#emitter

def tsv_get_emitter():
    return bpy.context.scene.tsv_emitter

def tsv_get_geo_nodes():
    emitter = tsv_get_emitter()
    if emitter is not None:
        return emitter.modifiers.get("vegetation").node_group

#groups

def tsv_get_groups():
    emitter = tsv_get_emitter()
    if emitter is not None:
        return emitter.tsv_groups

def tsv_get_group_index():
    emitter = tsv_get_emitter()
    if emitter is not None:
        return emitter.tsv_group_index
    
def tsv_get_group():
    groups = tsv_get_groups()
    group_index = tsv_get_group_index()
    try:
        return groups[group_index]
    except:
        return None
    
#group_mask

def tsv_get_group_mask_index():
    group = tsv_get_group()
    if group is not None:
        return group.mask_index

def tsv_get_group_masks():
    group = tsv_get_group()
    if group is not None:
        return group.masks
    
def tsv_get_group_mask():
    group_masks = tsv_get_group_masks()
    group_mask_index = tsv_get_group_mask_index()
    try:
        return group_masks[group_mask_index]
    except:
        return None

#group_layer

def tsv_get_group_layer_index():
    group = tsv_get_group()
    if group is not None:
        return group.layer_index

def tsv_get_group_layers():
    group = tsv_get_group()
    if group is not None:
        return group.layers
    
def tsv_get_group_layer():
    group_layers = tsv_get_group_layers()
    group_layer_index = tsv_get_group_layer_index()
    try:
        return group_layers[group_layer_index]
    except:
        return None