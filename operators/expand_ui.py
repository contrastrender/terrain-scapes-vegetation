import bpy

class SNA_OT_Expand_Density_076E3(bpy.types.Operator):
    bl_idname = "sna.expand_density_076e3"
    bl_label = "expand_density"
    bl_description = "Open/Close this panel"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_tsv_expand_density =  not bpy.context.scene.sna_tsv_expand_density
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
class SNA_OT_Expand_Layers_9D965(bpy.types.Operator):
    bl_idname = "sna.expand_layers_9d965"
    bl_label = "expand_layers"
    bl_description = "Open/Close this panel"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_tsv_expand_layers =  not bpy.context.scene.sna_tsv_expand_layers
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    SNA_OT_Expand_Density_076E3,
    SNA_OT_Expand_Layers_9D965
]