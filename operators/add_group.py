import bpy

def sna_add_group_46FA8(label):
    """
    Adds a new biome group to the TSV emitter system, updates node connections, 
    and sets up the necessary structures for the new group.
    """
    # References to frequently used data
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    modifiers = tsv_emitter.modifiers
    vegetation_node_group = modifiers['vegetation'].node_group
    num_groups = len(tsv_emitter.tsv_groups)

    # Update the name of the current biome node
    current_biome_node = vegetation_node_group.nodes[f"{num_groups}_biome"]
    current_biome_node.name = f"{num_groups + 1}_biome"

    # Add a new biome node
    new_biome_node = vegetation_node_group.nodes.new(type='GeometryNodeGroup')
    new_biome_node.node_tree = bpy.data.node_groups['.TSV_biome']
    new_biome_node.name = f"{num_groups}_biome"

    # Link the new biome node to the system and previous biome node
    vegetation_node_group.links.new(
        input=new_biome_node.inputs[1],
        output=vegetation_node_group.nodes['system'].outputs[0]
    )
    if num_groups > 0:
        previous_biome_node_name = f"{num_groups - 1}_biome"
        vegetation_node_group.links.new(
            input=new_biome_node.inputs[0],
            output=vegetation_node_group.nodes[previous_biome_node_name].outputs[0]
        )
    vegetation_node_group.links.new(
        input=vegetation_node_group.nodes[f"{num_groups + 1}_biome"].inputs[0],
        output=new_biome_node.outputs[0]
    )

    # Add a new density-related nodes
    value_node = vegetation_node_group.nodes.new(type='ShaderNodeValue')
    value_node.outputs[0].default_value = 1.0
    value_node.name = f"{num_groups},-1_density"

    reroute_node = vegetation_node_group.nodes.new(type='NodeReroute')
    reroute_node.name = f"{num_groups},0_density"

    # Link density-related nodes
    vegetation_node_group.links.new(
        input=reroute_node.inputs[0],
        output=value_node.outputs[0]
    )
    vegetation_node_group.links.new(
        input=new_biome_node.inputs[5],
        output=reroute_node.outputs[0]
    )

    # Add a new group to the TSV emitter
    new_group = tsv_emitter.tsv_groups.add()
    new_group.label = label

    # Update the active group index
    tsv_emitter.tsv_group_index = len(tsv_emitter.tsv_groups) - 1

class TSV_OT_add_group(bpy.types.Operator):
    bl_idname = "tsv.add_group"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_add_group_46FA8('group')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_add_group
]