import bpy

from .. utils.const_utils import ROOT_PACKAGE_NAME

from .. utils.property_utils import display_collection_id, property_exists

save_preset_group = {'sna_inputs': '', }

class TSV_OT_save_preset_group(bpy.types.Operator):
    bl_idname = "tsv.save_preset_group"
    bl_label = "Save Preset Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_index: bpy.props.IntProperty(name='index', description='', default=0, subtype='NONE') #type: ignore

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_save_preset_group_778E3(bpy.context.scene.tsv_emitter.tsv_groups[self.sna_index], self.sna_index)
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        col_9E3B3 = layout.column(heading='', align=False)
        col_9E3B3.template_list('SNA_UL_display_collection_list_55549', "", bpy.context.scene.tsv_emitter, 'tsv_groups', self, 'sna_index', rows=0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)


def sna_save_preset_group_778E3(group, group_index):
    if property_exists("group", globals(), locals()):
        # Create a new preset item
        item_0A881 = bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups.add()
        item_0A881.label = group.label
        
        for i_8EA76, layer in enumerate(group.layers):
            # Create a preset layer
            item_FD65E = item_0A881.tsv_preset_layers.add()
            item_FD65E.label = layer.label
            
            # Initialize the 'sna_inputs' string
            sna_inputs = ''
            
            # Access the node group and the current layer's node
            node_name = f"{group_index},{i_8EA76}_layer"
            node = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes.get(node_name)
            
            if node:
                # Loop through the node's inputs
                for i_A39E2, input_node in enumerate(node.inputs):
                    # Check if the default_value exists for the input
                    if property_exists(f"bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[{node_name}].inputs[{i_A39E2}].default_value", globals(), locals()):
                        input_value = input_node.default_value
                        input_type = input_node.type
                        
                        # Handle OBJECT type inputs
                        if input_type == 'OBJECT' and input_value:
                            input_name = input_value.name if property_exists(f"bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[{node_name}].inputs[{i_A39E2}].default_value.name", globals(), locals()) else 'None'
                        else:
                            input_name = str(input_value) if input_value else 'None'
                        
                        # Append the input type and value to the 'sna_inputs' string
                        sna_inputs += f"{input_type}|{input_name}{'||' if i_A39E2 < len(node.inputs) - 1 else ''}"
                    else:
                        # If no default_value, add 'None' to the 'sna_inputs'
                        sna_inputs += 'None|None' + ('||' if i_A39E2 < len(node.inputs) - 1 else '')
            
            # Assign the processed 'sna_inputs' string to the preset layer
            item_FD65E.inputs = sna_inputs

classes = [
    TSV_OT_save_preset_group
]