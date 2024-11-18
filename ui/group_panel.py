import bpy

from .. helper.get_prop_helper import get_emitter, get_geo_node_prop, get_group_node
from .. ui.vegetation_panel import TSV_PT_panel

class TSV_UL_groups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        emitter = get_emitter()
        group_node = get_group_node(index)

        row = layout
        layout.prop(item, 'label', text='', icon_value=0, emboss=False)
        row_FC6FF = layout.row(heading='', align=True)
        row_FC6FF.prop(group_node.inputs[7], 'default_value', text='', icon_value=(253 if group_node.inputs[7].default_value else 254), emboss=False)
        row_FC6FF.prop(group_node.inputs[8], 'default_value', text='', icon_value=(257 if group_node.inputs[8].default_value else 258), emboss=False)


class TSV_PT_groups(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_groups"
    bl_label = "Groups"
    bl_parent_id = "TSV_PT_vegetation_panel"

    @classmethod
    def poll(self, context):
        return bpy.context.scene.tsv_emitter

    def draw(self, context):

        emitter = get_emitter()

        layout = self.layout
        col_1689A = layout.column(heading='', align=False)
        col_1689A.scale_y = 2.0
        col_1689A.operator('tsv.open_preset_manager', text='Preset Manager', icon_value=0, emboss=True, depress=False)
        row_6C0C6 = layout.row(heading='', align=True)
        row_6C0C6.template_list('TSV_UL_groups', "", emitter, 'tsv_groups', emitter, 'tsv_group_index', rows=0)
        col_917D5 = row_6C0C6.column(heading='', align=False)
        col_A04CD = col_917D5.column(heading='', align=True)
        col_A04CD.operator('tsv.add_group', text='', icon_value=31, emboss=True, depress=False)
        col_A04CD.operator('tsv.remove_group', text='', icon_value=32, emboss=True, depress=False)
        col_DC67C = col_917D5.column(heading='', align=True)
        col_DC67C.operator('tsv.move_group_layer_up', text='', icon_value=7, emboss=True, depress=False)
        col_DC67C.operator('tsv.move_group_layer_down', text='', icon_value=5, emboss=True, depress=False)

classes = [
    TSV_PT_groups,
    TSV_UL_groups
]