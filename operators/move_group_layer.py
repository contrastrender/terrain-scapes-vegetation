import bpy

class TSV_OT_move_group_layer_up(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_up"
    bl_label = "Move Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        """
        Executes the reordering of TSV groups by moving the current group up in the hierarchy.
        This involves renaming nodes and relinking connections for consistency.
        """
        # References to frequently used data
        scene = bpy.context.scene
        tsv_emitter = scene.tsv_emitter
        vegetation_node_group = tsv_emitter.modifiers['vegetation'].node_group
        group_index = tsv_emitter.tsv_group_index

        # Ensure the group index is valid for reordering
        if group_index > 0:
            current_group = tsv_emitter.tsv_groups[group_index]
            previous_group_index = group_index - 1

            # Temporary renaming of current group's biome and density nodes
            vegetation_node_group.nodes[f"{group_index}_biome"].name = "-2_biome"
            for i in range(len(current_group.density_masks) + 2):
                vegetation_node_group.nodes[f"{group_index},{i - 1}_density"].name = f"-2,{i - 1}_density"
            for i in range(len(current_group.layers)):
                vegetation_node_group.nodes[f"{group_index},{i}_layer"].name = f"-2,{i}_layer"

            # Rename the previous group's nodes to occupy the current group's index
            vegetation_node_group.nodes[f"{previous_group_index}_biome"].name = f"{group_index}_biome"
            previous_group = tsv_emitter.tsv_groups[previous_group_index]
            for i in range(len(previous_group.density_masks) + 2):
                vegetation_node_group.nodes[f"{previous_group_index},{i - 1}_density"].name = f"{group_index},{i - 1}_density"
            for i in range(len(previous_group.layers)):
                vegetation_node_group.nodes[f"{previous_group_index},{i}_layer"].name = f"{group_index},{i}_layer"

            # Rename the temporary "-2" nodes back to the previous group's index
            vegetation_node_group.nodes["-2_biome"].name = f"{previous_group_index}_biome"
            for i in range(len(current_group.density_masks) + 2):
                vegetation_node_group.nodes[f"-2,{i - 1}_density"].name = f"{previous_group_index},{i - 1}_density"
            for i in range(len(current_group.layers)):
                vegetation_node_group.nodes[f"-2,{i}_layer"].name = f"{previous_group_index},{i}_layer"

            # Re-link biome nodes to maintain the connection structure
            if group_index >= 1:
                vegetation_node_group.links.new(
                    input=vegetation_node_group.nodes[f"{previous_group_index}_biome"].inputs[0],
                    output=vegetation_node_group.nodes[f"{previous_group_index - 1}_biome"].outputs[0],
                )
            vegetation_node_group.links.new(
                input=vegetation_node_group.nodes[f"{group_index}_biome"].inputs[0],
                output=vegetation_node_group.nodes[f"{previous_group_index}_biome"].outputs[0],
            )
            vegetation_node_group.links.new(
                input=vegetation_node_group.nodes[f"{group_index + 1}_biome"].inputs[0],
                output=vegetation_node_group.nodes[f"{group_index}_biome"].outputs[0],
            )

            # Move the current group in the TSV group list and update the index
            tsv_emitter.tsv_groups.move(group_index, previous_group_index)
            tsv_emitter.tsv_group_index = previous_group_index

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
class TSV_OT_move_group_layer_down(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_down"
    bl_label = "Move Biome"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        """
        Moves the current TSV group up in the index, renaming associated biome, density, and layer nodes.
        Updates connections between biome nodes and moves the group in the internal list.
        """

        # Get references to active scene and relevant attributes
        scene = bpy.context.scene
        tsv_emitter = scene.tsv_emitter
        vegetation_node_group = tsv_emitter.modifiers['vegetation'].node_group
        active_object = bpy.context.view_layer.objects.active

        # Check if the active object has tsv_groups
        if not hasattr(active_object, 'tsv_groups') or len(active_object.tsv_groups) == 0:
            self.report({'ERROR'}, "Active object does not have tsv_groups.")
            return {'CANCELLED'}

        # Check if tsv_group_index exists within the tsv_emitter or other context
        if not hasattr(tsv_emitter, 'tsv_group_index'):
            self.report({'ERROR'}, "tsv_group_index is not defined in tsv_emitter.")
            return {'CANCELLED'}

        # Retrieve the group index from tsv_emitter
        group_index = tsv_emitter.tsv_group_index

        # Ensure the index is valid
        if group_index < 0 or group_index >= len(active_object.tsv_groups):
            self.report({'ERROR'}, "Invalid TSV group index.")
            return {'CANCELLED'}

        # Check if the group is not the last one in the list
        if group_index < len(active_object.tsv_groups) - 1:
            current_group = active_object.tsv_groups[group_index]
            next_group_index = group_index + 1

            # Rename current group biome, density, and layer nodes to temporary names
            vegetation_node_group.nodes[f"{group_index}_biome"].name = "-2_Biome"
            for i in range(len(current_group.density_masks) + 2):
                vegetation_node_group.nodes[f"{group_index},{i - 1}_density"].name = f"-2,{i - 1}_density"
            for i in range(len(current_group.layers)):
                vegetation_node_group.nodes[f"{group_index},{i}_layer"].name = f"-2,{i}_layer"

            # Rename next group biome, density, and layer nodes to the current group's index
            next_group = active_object.tsv_groups[next_group_index]
            vegetation_node_group.nodes[f"{next_group_index}_biome"].name = f"{group_index}_biome"
            for i in range(len(next_group.density_masks) + 2):
                vegetation_node_group.nodes[f"{next_group_index},{i - 1}_density"].name = f"{group_index},{i - 1}_density"
            for i in range(len(next_group.layers)):
                vegetation_node_group.nodes[f"{next_group_index},{i}_layer"].name = f"{group_index},{i}_layer"

            # Rename the temporary nodes back to the next group's index
            vegetation_node_group.nodes["-2_Biome"].name = f"{next_group_index}_biome"
            for i in range(len(current_group.density_masks) + 2):
                vegetation_node_group.nodes[f"-2,{i - 1}_density"].name = f"{next_group_index},{i - 1}_density"
            for i in range(len(current_group.layers)):
                vegetation_node_group.nodes[f"-2,{i}_layer"].name = f"{next_group_index},{i}_layer"

            # Create links between biome nodes to preserve connections
            if group_index >= 0:
                vegetation_node_group.links.new(
                    input=vegetation_node_group.nodes[f"{group_index}_biome"].inputs[0],
                    output=vegetation_node_group.nodes[f"{group_index - 1}_biome"].outputs[0]
                )

            vegetation_node_group.links.new(
                input=vegetation_node_group.nodes[f"{next_group_index}_biome"].inputs[0],
                output=vegetation_node_group.nodes[f"{group_index}_biome"].outputs[0]
            )

            vegetation_node_group.links.new(
                input=vegetation_node_group.nodes[f"{next_group_index + 1}_biome"].inputs[0],
                output=vegetation_node_group.nodes[f"{next_group_index}_biome"].outputs[0]
            )

            # Move the current group to the next position in the list
            tsv_emitter.tsv_groups.move(group_index, next_group_index)
            tsv_emitter.tsv_group_index = next_group_index

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_move_group_layer_up,
    TSV_OT_move_group_layer_down
]