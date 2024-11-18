import bpy

from .. utils.property_utils import property_exists

def sna_remove_group_layer(Index):
    """
    Removes a specific layer from the current TSV group and renames subsequent layers to maintain consistency.
    
    Parameters:
        Index (int): The index of the layer to be removed.
    """
    # References to frequently used data
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    vegetation_node_group = tsv_emitter.modifiers['vegetation'].node_group
    current_group = tsv_emitter.tsv_groups[tsv_emitter.tsv_group_index]

    # Check if the layer exists
    if property_exists(
        f"bpy.context.scene.tsv_emitter.tsv_groups[{tsv_emitter.tsv_group_index}].layers[{current_group.layer_index}]",
        globals(),
        locals(),
    ):
        # Retrieve the layer node
        layer_node_name = f"{tsv_emitter.tsv_group_index},{Index}_layer"
        layer_node = vegetation_node_group.nodes[layer_node_name]

        # Remove the associated material if it exists
        solid_material = layer_node.inputs["Solid Material"].default_value
        if solid_material is not None:
            bpy.data.materials.remove(material=solid_material)

        # Remove the layer node
        vegetation_node_group.nodes.remove(node=layer_node)

        # Rename subsequent layer nodes
        num_layers = len(current_group.layers)
        for i in range(Index + 1, num_layers):
            current_name = f"{tsv_emitter.tsv_group_index},{i}_layer"
            new_name = f"{tsv_emitter.tsv_group_index},{i - 1}_layer"
            vegetation_node_group.nodes[current_name].name = new_name

        # Remove the layer from the group
        if len(current_group.layers) > current_group.layer_index:
            current_group.layers.remove(current_group.layer_index)

        # Adjust the active layer index
        if len(current_group.layers) == current_group.layer_index:
            current_group.layer_index = len(current_group.layers) - 1

def tsv_remove_group(Index):
    """
    Removes a biome and its associated nodes, layers, and density masks from the TSV emitter system.
    
    Parameters:
        Index (int): The index of the biome to be removed.
    """
    # References to frequently used data
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    vegetation_node_group = tsv_emitter.modifiers['vegetation'].node_group

    # Check if the biome exists
    if property_exists(f"bpy.context.scene.tsv_emitter.tsv_groups[{tsv_emitter.tsv_group_index}]", globals(), locals()):
        # Remove the biome node
        biome_node_name = f"{Index}_biome"
        vegetation_node_group.nodes.remove(node=vegetation_node_group.nodes[biome_node_name])

        # Remove all layers associated with the biome
        for _ in range(len(tsv_emitter.tsv_groups[tsv_emitter.tsv_group_index].layers)):
            sna_remove_group_layer(0)

        # Remove all density mask nodes associated with the biome
        num_density_masks = len(tsv_emitter.tsv_groups[tsv_emitter.tsv_group_index].density_masks) + 2
        for i in range(num_density_masks):
            density_node_name = f"{Index},{int(i - 1)}_density"
            vegetation_node_group.nodes.remove(node=vegetation_node_group.nodes[density_node_name])

        # Rename nodes for subsequent biomes
        remaining_groups = int(len(tsv_emitter.tsv_groups) - Index - 1)
        for i in range(remaining_groups):
            current_index = Index + i + 1
            new_index = Index + i

            # Update biome node names
            vegetation_node_group.nodes[f"{current_index}_biome"].name = f"{new_index}_biome"

            # Update layer node names for the biome
            layers = tsv_emitter.tsv_groups[current_index].layers
            for j in range(len(layers)):
                old_layer_name = f"{current_index},{j}_layer"
                new_layer_name = f"{new_index},{j}_layer"
                vegetation_node_group.nodes[old_layer_name].name = new_layer_name

            # Update density mask node names for the biome
            num_density_masks = len(tsv_emitter.tsv_groups[current_index].density_masks) + 2
            for k in range(num_density_masks):
                old_density_name = f"{current_index},{int(k - 1)}_density"
                new_density_name = f"{new_index},{int(k - 1)}_density"
                vegetation_node_group.nodes[old_density_name].name = new_density_name

        # Update the name of the last biome node
        last_biome_node_name = f"{len(tsv_emitter.tsv_groups)}_biome"
        new_last_biome_name = f"{len(tsv_emitter.tsv_groups) - 1}_biome"
        vegetation_node_group.nodes[last_biome_node_name].name = new_last_biome_name

        # Reconnect the remaining biomes
        vegetation_node_group.links.new(
            input=vegetation_node_group.nodes[f"{tsv_emitter.tsv_group_index}_biome"].inputs[0],
            output=vegetation_node_group.nodes[f"{tsv_emitter.tsv_group_index - 1}_biome"].outputs[0]
        )

        # Remove the biome group from the list
        if len(tsv_emitter.tsv_groups) > tsv_emitter.tsv_group_index:
            tsv_emitter.tsv_groups.remove(tsv_emitter.tsv_group_index)

        # Update the active group index
        if len(tsv_emitter.tsv_groups) == tsv_emitter.tsv_group_index:
            tsv_emitter.tsv_group_index = len(tsv_emitter.tsv_groups) - 1


class TSV_OT_remove_group(bpy.types.Operator):
    bl_idname = "tsv.remove_group"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        tsv_remove_group(bpy.context.scene.tsv_emitter.tsv_group_index)

        #if no group exits, remove geo nodes modifier from emitter
        if len(bpy.context.scene.tsv_emitter.tsv_groups) is 0:
            bpy.ops.tsv.remove_vegetation_geo_nodes()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_remove_group
]