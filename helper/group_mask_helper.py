import bpy

from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_group_layers, tsv_get_group_mask, tsv_get_group_mask_index, tsv_get_group_masks

def tsv_group_mask_add():
    # Get references for better readability
    geo_nodes = tsv_get_geo_nodes()
    group_index = tsv_get_group_index()
    group = tsv_get_group()
    group_node = geo_nodes.nodes[f"{group_index}_group"]

    mask_enum = bpy.context.scene.tsv_masks

    #get mask node name
    mask_node_name = f"{len(group.masks)}_mask"

    # rename highest mask node name
    group_node.node_tree.nodes[mask_node_name].name = f"{len(group.masks) + 1}_mask"

    # Create a new Layer Node inside the group node
    mask_node = group_node.node_tree.nodes.new(type='GeometryNodeGroup')
    mask_node.node_tree = bpy.data.node_groups[f'.TSV_mask_{mask_enum}']
    mask_node.name = mask_node_name

    # Link Mask to the last masks
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes[f"{len(group.masks) - 1}_mask"].outputs[0],
        input = mask_node.inputs[0]
    )
    group_node.node_tree.links.new(
        output = mask_node.outputs[0],
        input = group_node.node_tree.nodes[f"{len(group.masks) + 1}_mask"].inputs[0]
    )
    
    # Add the layer to the TSV group and update the layer index
    mask_item = group.masks.add()
    mask_item.label = "layer"

    # Set index to the last item
    group.layer_index = len(group.layers) - 1

def tsv_group_mask_remove():
    
    # Check if layer exists
    if tsv_get_group_mask() is None:
        return None

    # Get references
    geo_nodes = tsv_get_geo_nodes()
    group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
    mask_node = group_node.node_tree.nodes[f"{tsv_get_group_mask_index()}_mask"]

    # Remove Node
    group_node.node_tree.nodes.remove(mask_node)

    # Rename Nodes Above
    mask_index = tsv_get_group_mask_index()
    n_nodes_above = len(tsv_get_group_masks()) - mask_index
    for node_above in range(n_nodes_above):
        group_node.node_tree.nodes[f"{node_above + mask_index + 1}_mask"].name = f"{node_above + mask_index}_mask"

    #relink the mask nodes
    group_node.node_tree.links.new(
        output = group_node.node_tree.nodes[f"{mask_index-1}_mask"].outputs[0],
        input = group_node.node_tree.nodes[f"{mask_index}_mask"].inputs[0]
    )

    # Remove the biome group from the list
    group_masks = tsv_get_group_masks()
    group_mask_index = tsv_get_group_mask_index()

    group_masks.remove(group_mask_index)

    # Update the active group index
    if len(group_masks) == group_mask_index:
        group_mask_index = len(group_masks) - 1