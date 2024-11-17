import bpy

class TSV_OT_remove_vegetation_geo_nodes(bpy.types.Operator):
    bl_idname = "tsv.remove_vegetation_geo_nodes"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers.clear()
        bpy.context.scene.sna_tsv_emitter.modifiers.remove(modifier=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'], )
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
classes = [
    TSV_OT_remove_vegetation_geo_nodes
]