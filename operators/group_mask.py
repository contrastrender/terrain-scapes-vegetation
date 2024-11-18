import bpy
import os

from .. utils.const_utils import ROOT_DIR

from .. utils.property_utils import property_exists

biome_density_mask__add = {'sna_masks': [], }
_icons = None

def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id

class TSV_OT_group_mask_add(bpy.types.Operator):
    bl_idname = "tsv.group_mask_add"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        """
        Add a new density mask to the vegetation system and update the node group structure.
        """
        # Get references to frequently used data
        scene = bpy.context.scene
        tsv_emitter = scene.tsv_emitter
        group_index = tsv_emitter.tsv_group_index
        group = tsv_emitter.tsv_groups[group_index]
        modifiers = tsv_emitter.modifiers
        vegetation_node_group = modifiers['vegetation'].node_group
        mask_name = scene.tsv_masks

        # Determine current and new density node identifiers
        current_density_index = len(group.density_masks)
        current_density_name = f"{group_index},{current_density_index}_density"
        new_density_name = f"{group_index},{current_density_index + 1}_density"

        # Rename the current density node
        vegetation_node_group.nodes[current_density_name].name = new_density_name

        # Create a new density node
        new_node = vegetation_node_group.nodes.new(type='GeometryNodeGroup')
        new_node.node_tree = bpy.data.node_groups[f".TSV_mask_{mask_name}"]
        new_node.name = current_density_name  # Assign the appropriate name for the new node

        # Create links between nodes
        previous_node = vegetation_node_group.nodes[f"{group_index},{current_density_index - 1}_density"]
        vegetation_node_group.links.new(
            input=vegetation_node_group.nodes[current_density_name].inputs[0],
            output=previous_node.outputs[0]
        )
        vegetation_node_group.links.new(
            input=vegetation_node_group.nodes[new_density_name].inputs[0],
            output=vegetation_node_group.nodes[current_density_name].outputs[0]
        )

        # Add a new density mask to the group
        new_mask = group.density_masks.add()
        new_mask.label = mask_name
        new_mask.texture = f".TSV_mask_{mask_name}"
    
        # Update the active density mask index
        group.density_mask_index = current_density_index
        
        return {"FINISHED"}


    def draw(self, context):
        layout = self.layout
        col_FC1B4 = layout.column(heading='', align=False)
        col_FC1B4.template_icon_view(bpy.context.scene, 'tsv_masks', show_labels=True, scale=8.0, scale_popup=5.0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

    
class TSV_OT_group_mask_remove(bpy.types.Operator):
    bl_idname = "tsv.group_mask_remove"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        """
        Remove a density mask and update the associated node group structure.
        """
        # Get references to frequently used data
        scene = bpy.context.scene
        tsv_emitter = scene.tsv_emitter
        group_index = tsv_emitter.tsv_group_index
        group = tsv_emitter.tsv_groups[group_index]
        modifiers = tsv_emitter.modifiers
        vegetation_node_group = modifiers['vegetation'].node_group
        density_masks = group.density_masks
        mask_index = group.density_mask_index

        # Ensure the property exists before proceeding
        if property_exists(
            f"bpy.context.scene.tsv_emitter.tsv_groups[{group_index}].density_masks[{mask_index}]",
            globals(), locals()
        ):
            # Remove the specified density node
            node_to_remove = vegetation_node_group.nodes[f"{group_index},{mask_index}_density"]
            vegetation_node_group.nodes.remove(node_to_remove)

            # Update subsequent node names
            for i in range(len(density_masks) - mask_index):
                current_index = mask_index + i + 1
                new_index = mask_index + i
                current_node_name = f"{group_index},{current_index}_density"
                new_node_name = f"{group_index},{new_index}_density"
                vegetation_node_group.nodes[current_node_name].name = new_node_name

            # Re-link nodes around the removed node
            if mask_index > 0:
                previous_node_name = f"{group_index},{mask_index - 1}_density"
                current_node_name = f"{group_index},{mask_index}_density"
                vegetation_node_group.links.new(
                    input=vegetation_node_group.nodes[current_node_name].inputs[0],
                    output=vegetation_node_group.nodes[previous_node_name].outputs[0]
                )

            # Remove the density mask from the group
            if mask_index < len(density_masks):
                density_masks.remove(mask_index)

            # Update the active mask index if necessary
            if mask_index == len(density_masks):
                group.density_mask_index = len(density_masks) - 1

        return {"FINISHED"}


    def invoke(self, context, event):
        return self.execute(context)

classes = [
    TSV_OT_group_mask_add,
    TSV_OT_group_mask_remove
]