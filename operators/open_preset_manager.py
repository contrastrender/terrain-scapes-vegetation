import bpy
from .. ui.preset_manager import tsv_preset_manager

class TSV_OT_open_preset_manager(bpy.types.Operator):
    bl_idname = "tsv.open_preset_manager"
    bl_label = "Preset Manager"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        layout_function = layout
        tsv_preset_manager(layout_function, )

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
classes = [
    TSV_OT_open_preset_manager
]