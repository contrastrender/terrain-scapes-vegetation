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
        col_9E3B3.alert = False
        col_9E3B3.enabled = True
        col_9E3B3.active = True
        col_9E3B3.use_property_split = False
        col_9E3B3.use_property_decorate = False
        col_9E3B3.scale_x = 1.0
        col_9E3B3.scale_y = 1.0
        col_9E3B3.alignment = 'Expand'.upper()
        col_9E3B3.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        coll_id = display_collection_id('55549', locals())
        col_9E3B3.template_list('SNA_UL_display_collection_list_55549', coll_id, bpy.context.scene.tsv_emitter, 'tsv_groups', self, 'sna_index', rows=0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)


def sna_save_preset_group_778E3(group, group_index):
    if property_exists("group", globals(), locals()):
        item_0A881 = bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups.add()
        item_0A881.label = group.label
        for i_8EA76 in range(len(group.layers)):
            item_FD65E = item_0A881.tsv_preset_layers.add()
            item_FD65E.label = group.layers[i_8EA76].label
            save_preset_group['sna_inputs'] = ''
            for i_A39E2 in range(len(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs)):
                if property_exists("bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].default_value", globals(), locals()):
                    if ('OBJECT' == bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].type):
                        save_preset_group['sna_inputs'] = save_preset_group['sna_inputs'] + bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].type + '|' + (bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].default_value.name if property_exists("bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].default_value.name", globals(), locals()) else 'None') + ('' if (float(len(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs) - 1.0) == i_A39E2) else '||')
                    else:
                        save_preset_group['sna_inputs'] = save_preset_group['sna_inputs'] + bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].type + '|' + str(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs[i_A39E2].default_value) + ('' if (float(len(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs) - 1.0) == i_A39E2) else '||')
                else:
                    save_preset_group['sna_inputs'] = save_preset_group['sna_inputs'] + 'None' + '|' + 'None' + ('' if (float(len(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(group_index) + ',' + str(i_8EA76) + '_layer'].inputs) - 1.0) == i_A39E2) else '||')
            item_FD65E.inputs = save_preset_group['sna_inputs']

classes = [
    TSV_OT_save_preset_group
]