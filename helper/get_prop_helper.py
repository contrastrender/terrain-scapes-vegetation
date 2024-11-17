import bpy

from .. utils.const_utils import ROOT_PACKAGE_NAME

#preset groups

def get_preset_groups():
    return bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups

def get_preset_group_index():
    return bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_group_index

def get_preset_group(index: int):
    try:
        return bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups[index]
    except:
        return None

def get_ac_preset_group():
    preset_group_index = get_preset_group_index()
    return get_preset_group(preset_group_index)

#emitter

def get_emitter():
    return bpy.context.scene.tsv_emitter

def get_geo_node_prop():
    emitter = get_emitter()
    if emitter != None:
        return emitter.modifiers.get("vegetation")

#groups

def get_ac_group_index():
    emitter = get_emitter()
    if emitter != None:
        return emitter.tsv_group_index

def get_ac_group_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_ac_group_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + '_biome')
    
def get_group_node(index: int):
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        return geo_nodes.node_group.nodes.get(str(index) + '_biome')
    
#group_mask

def get_ac_group_ac_density_index():
    emitter = get_emitter()
    group_index = get_ac_group_index()
    try:
        return emitter.tsv_groups[group_index].density_index
    except:
        return None

def get_ac_group_ac_density_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_ac_group_index()
        group_density_index = get_ac_group_ac_density_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(group_density_index) + "_density")

def get_ac_group_density_node(density_index: int):
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_ac_group_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(density_index) + "_density")

def get_group_density_node(group_index: int, density_index: int):
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(density_index) + "_density")

#group_layer

def get_ac_group_ac_layer_index():
    emitter = get_emitter()
    group_index = get_ac_group_index()
    try:
        return emitter.tsv_groups[group_index].layer_index
    except:
        return None

def get_ac_group_ac_layer_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_ac_group_index()
        group_layer_index = get_ac_group_ac_layer_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(group_layer_index) + "_layer")

def get_ac_group_layer_node(layer_index: int):
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_ac_group_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(layer_index) + "_layer")

def get_group_layer_node(group_index: int, layer_index: int):
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        return geo_nodes.node_group.nodes.get(str(group_index) + "," + str(layer_index) + "_layer")