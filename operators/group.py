import bpy

from .. helper.group_helper import tsv_add_geo_nodes_modifier, tsv_group_add, tsv_group_move_down, tsv_group_move_up, tsv_group_remove

class TSV_OT_move_group_layer_up(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_up"
    bl_label = "Move Group"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        
        tsv_group_move_up()

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
class TSV_OT_move_group_layer_down(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_down"
    bl_label = "Move Biome"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):

        tsv_group_move_down()

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class TSV_OT_remove_group(bpy.types.Operator):
    bl_idname = "tsv.remove_group"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        tsv_group_remove()

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class TSV_OT_add_group(bpy.types.Operator):
    bl_idname = "tsv.add_group"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        #adds geo nodes modifier if missing
        if bpy.context.scene.tsv_emitter.modifiers.get("vegetation") is None:
            tsv_add_geo_nodes_modifier()

        tsv_group_add()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

classes = [
    TSV_OT_move_group_layer_up,
    TSV_OT_move_group_layer_down,
    TSV_OT_remove_group,
    TSV_OT_add_group
]