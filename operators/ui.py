import bpy
from ..ui.preset_manager import tsv_preset_manager

class TSV_OT_open_preset_manager(bpy.types.Operator):
    bl_idname = "tsv.open_preset_manager"
    bl_label = "Preset Manager"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        tsv_preset_manager(self.layout)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
class TSV_OT_show_warning(bpy.types.Operator):
    bl_idname = "tsv.show_warning"
    bl_label = "Warning"

    text: bpy.props.StringProperty() #type: ignore

    def execute(self, context):
        return {"FINISHED"}

    def draw(self, context):
        box = self.layout.box()
        box.label(text=self.text, icon="ERROR")

    def invoke(self, context, event):
        return context.window_manager.invoke_popup(self, width=300)
    
classes = [
    TSV_OT_open_preset_manager,
    TSV_OT_show_warning
]