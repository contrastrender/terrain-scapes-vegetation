import bpy

from .. utils.const_utils import ROOT_PACKAGE_NAME

def get_preset_groups():
    return bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups

def get_preset_group_index():
    return bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_group_index

def get_emitter():
    return bpy.context.scene.tsv_emitter

def get_geo_node_prop():
    emitter = get_emitter()
    if emitter != None:
        return emitter.modifiers.get("vegetation")

def get_group_index():
    emitter = get_emitter()
    if emitter != None:
        return emitter.tsv_group_index

def get_group_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_group_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + '_biome')
    
def get_group_density_index():
    emitter = get_emitter()
    group_index = get_group_index()
    try:
        return emitter.tsv_groups[group_index].density_index # placeholder prop name
    except:
        return None

def get_group_density_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_group_index()
        group_density_index = get_group_density_index()
        geo_nodes.node_group.nodes.get(str(group_index) + "," + str(group_density_index) + "_density")

def get_group_layer_index():
    emitter = get_emitter()
    group_index = get_group_index()
    try:
        return emitter.tsv_groups[group_index].layer_index # placeholder prop name
    except:
        return None

def get_group_layer_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_group_index()
        group_layer_index = get_group_layer_index()
        geo_nodes.node_group.nodes.get(str(group_index) + "," + str(group_layer_index) + "_layer")