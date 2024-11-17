import bpy

from .. utils.property_utils import property_exists

class TSV_OT_remove_preset_group(bpy.types.Operator):
    bl_idname = "tsv.remove_preset_group"
    bl_label = "Remove Preset Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if property_exists("bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups_index]", globals(), locals()):
            if len(bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups) > bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups_index:
                bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups.remove(bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups_index)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_remove_preset_group
]