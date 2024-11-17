import bpy

class TSV_OT_expand_preset_group(bpy.types.Operator):
    bl_idname = "tsv.expand_preset_group"
    bl_label = "Expand Preset Layers"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.tsv_expand_preset_layers =  not bpy.context.scene.tsv_expand_preset_layers
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)