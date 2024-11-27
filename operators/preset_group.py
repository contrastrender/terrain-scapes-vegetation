import bpy

from .. helper.get_prop_helper import tsv_get_emitter
from .. const import __PACKAGE__
from .. helper.preset_group_helper import tsv_preset_group_add, tsv_preset_group_export_to_json, tsv_preset_group_import_from_json, tsv_preset_group_load, tsv_preset_group_move_down, tsv_preset_group_move_up, tsv_preset_group_remove

class TSV_OT_preset_group_export(bpy.types.Operator):
    bl_idname = "tsv.preset_group_export"
    bl_label = "Export Preset Group"
    bl_description = ""
    bl_options = {"UNDO"}

    directory: bpy.props.StringProperty(
        subtype='DIR_PATH'
    ) #type: ignore
    
    json_file_name: bpy.props.StringProperty() #type: ignore

    def execute(self, context):
        tsv_preset_group_export_to_json(self.directory, self.json_file_name)
        return {"FINISHED"}

    def draw(self, context):
        col = self.layout.column()
        col.prop(self, 'directory', text='Directory')
        col.prop(self, 'json_file_name', text='Save As')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)
    
class TSV_OT_preset_group_import(bpy.types.Operator):
    bl_idname = "tsv.preset_group_import"
    bl_label = "Import Preset Group"
    bl_description = ""
    bl_options = {"UNDO"}

    preset_group_json_file_path: bpy.props.StringProperty(
        subtype='FILE_PATH'
    ) #type: ignore

    def execute(self, context):
        tsv_preset_group_import_from_json(self.preset_group_json_file_path)
        return {"FINISHED"}

    def draw(self, context):
        self.layout.prop(self, 'preset_group_json_file_path', text='Preset Group')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

class TSV_OT_preset_group_add(bpy.types.Operator):
    bl_idname = "tsv.preset_group_add"
    bl_label = "Add Preset Group"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        tsv_preset_group_add()
        return {"FINISHED"}

    def draw(self, context):
        emitter = tsv_get_emitter()
        self.layout.template_list('TSV_UL_groups', "", emitter, 'tsv_groups', emitter, 'tsv_group_index')

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

class TSV_OT_preset_group_remove(bpy.types.Operator):
    bl_idname = "tsv.preset_group_remove"
    bl_label = "Remove Preset Group"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        tsv_preset_group_remove()
        return {"FINISHED"}
    
    def draw(self, context):
        None

    def invoke(self, context, event):
        return context.window_manager.invoke_confirm(self, event)

class TSV_OT_preset_group_move_up(bpy.types.Operator):
    bl_idname = "tsv.preset_group_move_up"
    bl_label = "Move Up"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        tsv_preset_group_move_up()
        return {"FINISHED"}

class TSV_OT_preset_group_move_down(bpy.types.Operator):
    bl_idname = "tsv.preset_group_move_down"
    bl_label = "Move Down"
    bl_description = ""
    bl_options = {"UNDO"}

    def execute(self, context):
        tsv_preset_group_move_down()
        return {"FINISHED"}

class TSV_OT_preset_group_load(bpy.types.Operator):
    bl_idname = "tsv.preset_group_load"
    bl_label = "Load"
    bl_description = "Loads selected preset group to the emitter"
    bl_options = {"UNDO"}

    def execute(self, context):
        tsv_preset_group_load()
        return {"FINISHED"}

classes = [
    TSV_OT_preset_group_export,
    TSV_OT_preset_group_import,
    TSV_OT_preset_group_add,
    TSV_OT_preset_group_remove,
    TSV_OT_preset_group_move_up,
    TSV_OT_preset_group_move_down,
    TSV_OT_preset_group_load
]