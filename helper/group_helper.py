import bpy
import os

from .. helper.get_prop_helper import tsv_get_emitter, tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_groups
from .. const import __FILE__
from .. utils.property_utils import property_exists

def tsv_add_geo_nodes_modifier():
    if property_exists("bpy.data.node_groups['.TSV_vegetation']", globals(), locals()):
        pass
    else:
        before_data = list(bpy.data.node_groups)
        bpy.ops.wm.append(directory=os.path.join(os.path.dirname(__FILE__) ,"assets",'blends','vegetation.blend') + r'\NodeTree', filename='.TSV_vegetation', link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.node_groups)))
        appended_C10DA = None if not new_data else new_data[0]
        bpy.data.node_groups['.TSV_vegetation'].use_fake_user = True
    id_E5391 = bpy.data.node_groups['.TSV_vegetation'].copy()
    modifier_6E969 = bpy.context.scene.tsv_emitter.modifiers.new(name='vegetation', type='NODES', )
    modifier_6E969.node_group = id_E5391

def tsv_remove_geo_nodes_modifier():
    bpy.context.scene.tsv_emitter.tsv_groups.clear()
    bpy.context.scene.tsv_emitter.modifiers.remove(modifier=bpy.context.scene.tsv_emitter.modifiers['vegetation'], )

def tsv_group_move_up():
    None

def tsv_group_move_down():
    None

def tsv_group_add():
    # References to frequently used data
    emitter = tsv_get_emitter()
    vegetation_node_group = tsv_get_geo_nodes()
    groups_len = len(emitter.tsv_groups)

    # Add a new biome node
    group_node = vegetation_node_group.nodes.new(type='GeometryNodeGroup')
    group_node.node_tree = bpy.data.node_groups['.TSV_group'].copy()
    group_node.name = f"{groups_len}_group"

    # Link setting and group node
    settings_node = vegetation_node_group.nodes['settings']

    vegetation_node_group.links.new(
        input=group_node.inputs[0],
        output=settings_node.outputs[0]
    )
    vegetation_node_group.links.new(
        input=group_node.inputs[1],
        output=settings_node.outputs[1]
    )
    vegetation_node_group.links.new(
        input=group_node.inputs[2],
        output=settings_node.outputs[2]
    )
    vegetation_node_group.links.new(
        input=group_node.inputs[3],
        output=settings_node.outputs[3]
    )

    # Link group and combine_groups node

    combine_groups_node = vegetation_node_group.nodes["combine_groups"]

    vegetation_node_group.links.new(
        input=combine_groups_node.inputs[0],
        output=group_node.outputs[0]
    )

    # Add a new group to the TSV emitter
    new_group = emitter.tsv_groups.add()
    new_group.label = "group"

    # Update the active group index
    emitter.tsv_group_index = len(emitter.tsv_groups) - 1

def tsv_group_remove():
    # Checks if group exists
    if tsv_get_group() is None:
        return None

    # References to frequently used data
    emitter = tsv_get_emitter()
    geo_nodes = tsv_get_geo_nodes()
    group_index = tsv_get_group_index()

    # Remove the group node and its node tree
    group_node = geo_nodes.nodes[f"{group_index}_group"]
    bpy.data.node_groups.remove(group_node.node_tree)
    geo_nodes.nodes.remove(node=group_node)

    # Rename nodes for subsequent biomes
    remaining_groups = int(len(emitter.tsv_groups) - group_index - 1)
    for i in range(remaining_groups):
        geo_nodes.nodes[f"{group_index + i + 1}_group"].name = f"{group_index + i}_group"

    # Remove the biome group from the list
    if len(emitter.tsv_groups) > emitter.tsv_group_index:
        emitter.tsv_groups.remove(emitter.tsv_group_index)

    # Update the active group index
    if len(emitter.tsv_groups) == emitter.tsv_group_index:
        emitter.tsv_group_index = len(emitter.tsv_groups) - 1