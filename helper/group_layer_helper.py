import bpy
import os

from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_group_layer, tsv_get_group_layer_index, tsv_get_group_layers

from .. utils.color_utils import random_color
from .. utils.integer_utils import random_integer

from .. const import __FILE__

def tsv_group_layer_add():
    # Get references for better readability
    geo_nodes = tsv_get_geo_nodes()
    group_index = tsv_get_group_index()
    group = tsv_get_group()
    group_node = geo_nodes.nodes[f"{group_index}_group"]

    # Create a new Layer Node inside the group node
    layer_node_name = f"{len(group.layers)}_layer"
    
    layer_node = group_node.node_tree.nodes.new(type='GeometryNodeGroup')
    layer_node.node_tree = bpy.data.node_groups['.TSV_layer']
    layer_node.name = layer_node_name

    # Link layer and group-settings node
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes["group_settings"].outputs[0],
        input = layer_node.inputs[0]
    )
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes["group_settings"].outputs[1],
        input = layer_node.inputs[1]
    )
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes["group_settings"].outputs[2],
        input = layer_node.inputs[2]
    )
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes["group_settings"].outputs[3],
        input = layer_node.inputs[3]
    )

    # Link Layer and combine-layers node
    group_node.node_tree.links.new(
        output = layer_node.outputs[0],
        input = group_node.node_tree.nodes["combine_layers"].inputs[0]
    )
    
    # Set a random integer input value
    # Must match the seed input of the layer node
    layer_node.inputs[6].default_value = random_integer(0.0, 10000.0, None)

    # Create a new material with a random color
    # Must match the solid material input of the layer node
    solid_material = bpy.data.materials.new(name='Solid_Material')
    solid_material.diffuse_color = (*random_color(False, None, None)[0:3], 1.0)
    layer_node.inputs[7].default_value = solid_material
    
    # Add the layer to the TSV group and update the layer index
    new_layer = group.layers.add()
    new_layer.label = "layer"
    group.layer_index = len(group.layers) - 1  # Set to the last layer index

    return layer_node

def tsv_group_layer_remove():

    # Check if layer exists
    if tsv_get_group_layer() is None:
        return None

    # Get references
    geo_nodes = tsv_get_geo_nodes()
    group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
    layer_node = group_node.node_tree.nodes[f"{tsv_get_group_layer_index()}_layer"]

    # Remove Node
    group_node.node_tree.nodes.remove(layer_node)

    # Rename Nodes Above
    layer_index = tsv_get_group_layer_index()
    n_nodes_above = len(tsv_get_group_layers()) - (layer_index + 1)
    for node_above in range(n_nodes_above):
        group_node.node_tree.nodes[f"{node_above + layer_index + 1}_layer"].name = f"{node_above + layer_index}_layer"

    # Remove the biome group from the list
    group_layers = tsv_get_group_layers()
    group_layer_index = tsv_get_group_layer_index()

    group_layers.remove(group_layer_index)

    # Update the active group index
    if len(group_layers) == group_layer_index:
        group_layer_index = len(group_layers) - 1

def tsv_append_scattering_object(asset_name, asset_path):

    # Create collection for assets
    if bpy.data.collections.get("vegetation_assets") is None:
        collection = bpy.data.collections.new(name='vegetation_assets', )
        bpy.context.scene.collection.children.link(child=collection, )
        collection.hide_render = True
        collection.hide_viewport = True
    
    # Append asset if not in scene
    if bpy.data.objects.get(asset_name) is None:
        bpy.ops.wm.append(directory=os.path.join(asset_path, "Object"), filename=asset_name, link=False)

    # Unlink the appended object from current collections and link to correct collection
    appended_object = bpy.data.objects.get(asset_name)
    if appended_object is not None:

        for collection in appended_object.users_collection:
            collection.objects.unlink(appended_object)

        vegetation_assets_collection = bpy.data.collections.get('vegetation_assets')
        vegetation_assets_collection.objects.link(appended_object)
        return appended_object

def tsv_search_object_in_asset_libraries(object_name) -> str:
    asset_libraries = bpy.context.preferences.filepaths.asset_libraries
    for asset_library in asset_libraries:
        path = asset_library.path
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".blend"):
                    blend_file_path = os.path.join(root, file)
                    print(f"Checking {blend_file_path} for object '{object_name}'...")

                    # Check the blend file for the object
                    with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, _):
                        if object_name in data_from.objects:
                            print(f"Object '{object_name}' found in {blend_file_path}.")
                            return blend_file_path