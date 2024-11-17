import bpy

from .. utils.const_utils import ROOT_PACKAGE_NAME

class TSV_OT_preset_group_move_up(bpy.types.Operator):
    bl_idname = "tsv.preset_group_move_up"
    bl_label = "Move Up"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (0 < bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index):
            bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups.move(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index, int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index - 1.0))
            item_4467A = bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index - 1.0)]
            bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index = int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index - 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class TSV_OT_preset_group_move_down(bpy.types.Operator):
    bl_idname = "tsv.preset_group_move_down"
    bl_label = "Move Down"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (len(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups) > int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index + 1.0)):
            bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups.move(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index, int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index + 1.0))
            item_86D49 = bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index + 1.0)]
            bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index = int(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index + 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_preset_group_move_up,
    TSV_OT_preset_group_move_down
]