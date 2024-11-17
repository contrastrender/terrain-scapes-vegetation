import bpy

def get_emitter():
    return bpy.context.scene.sna_tsv_emitter

def get_geo_node_prop():
    emitter = get_emitter()
    if emitter != None:
        return emitter.modifiers.get("vegetation")

def get_group_index():
    emitter = get_emitter()
    if emitter != None:
        return emitter.sna_tsv_group_layer_index

def get_group_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_group_index()
        return geo_nodes.node_group.nodes.get(str(group_index) + '_biome')
    
def get_group_density_index():
    emitter = get_emitter()
    group_index = get_group_index()
    try:
        return emitter.sna_tsv_group_layers[group_index].density_index # placeholder prop name
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
        return emitter.sna_tsv_group_layers[group_index].layer_index # placeholder prop name
    except:
        return None

def get_group_layer_node():
    geo_nodes = get_geo_node_prop()
    if geo_nodes != None:
        group_index = get_group_index()
        group_layer_index = get_group_layer_index()
        geo_nodes.node_group.nodes.get(str(group_index) + "," + str(group_layer_index) + "_layer")