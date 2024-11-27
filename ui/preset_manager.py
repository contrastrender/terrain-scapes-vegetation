import bpy

from ..helper.get_prop_helper import tsv_get_emitter, tsv_get_preferences, tsv_get_preset_group
from ..const import __PACKAGE__

class TSV_UL_preset_groups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.prop(item, 'label', text='', icon_value=0, emboss=False)

def tsv_preset_manager(layout, ):

    preferences = tsv_get_preferences()

    col = layout.column()
    col.label(text='Preset Groups', icon_value=0)
    col.operator('tsv.preset_group_export', text='Export Preset Group', icon = "EXPORT",)
    col.operator('tsv.preset_group_import', text='Import Preset Group', icon = "IMPORT",)
    col.separator()

    row = col.row()
    row.template_list('TSV_UL_preset_groups', "", preferences, 'preset_groups', preferences, 'preset_group_index')
    col_op = row.column()
    col_1 = col_op.column(heading='', align=True)
    col_1.operator('tsv.preset_group_add', text='', icon = "ADD")
    col_1.operator('tsv.preset_group_remove', text='', icon = "REMOVE")
    col_2 = col_op.column(heading='', align=True)
    col_2.operator('tsv.preset_group_move_up', text='', icon = "TRIA_UP")
    col_2.operator('tsv.preset_group_move_down', text='', icon = "TRIA_DOWN")

    emitter = tsv_get_emitter()
    preset_group = tsv_get_preset_group()

    if emitter is not None and preset_group is not None:
        col.separator()
        col.operator("tsv.preset_group_load", text = "Load Preset Group")

classes = [
    TSV_UL_preset_groups
]