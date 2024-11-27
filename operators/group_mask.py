import bpy
import os

from .. helper.group_mask_helper import tsv_group_mask_add, tsv_group_mask_remove

class TSV_OT_group_mask_add(bpy.types.Operator):
    bl_idname = "tsv.group_mask_add"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        tsv_group_mask_add()
        
        return {"FINISHED"}


    def draw(self, context):
        self.layout.template_icon_view(bpy.context.scene, 'tsv_masks', show_labels=True, scale=10, scale_popup=5)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

    
class TSV_OT_group_mask_remove(bpy.types.Operator):
    bl_idname = "tsv.group_mask_remove"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        
        tsv_group_mask_remove()

        return {"FINISHED"}


    def invoke(self, context, event):
        return self.execute(context)

classes = [
    TSV_OT_group_mask_add,
    TSV_OT_group_mask_remove
]