import bpy

from .. helper.get_prop_helper import tsv_get_emitter, tsv_get_geo_nodes

from .. panels.vegetation_panel import TSV_PT_panel

class TSV_UL_groups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{index}_group"].node_tree.nodes["group_settings"]

        row = layout
        layout.prop(item, 'label', text='', icon_value=0, emboss=False)
        row_FC6FF = layout.row(heading='', align=True)
        row_FC6FF.prop(group_node.inputs[5], 'default_value', text='', icon=("HIDE_OFF" if group_node.inputs[5].default_value else "HIDE_ON"), emboss=False)
        row_FC6FF.prop(group_node.inputs[6], 'default_value', text='', icon=("HIDE_OFF" if group_node.inputs[6].default_value else "HIDE_ON"), emboss=False)


class TSV_PT_groups(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_groups"
    bl_label = "Groups"
    bl_parent_id = "TSV_PT_vegetation_panel"

    @classmethod
    def poll(self, context):
        return bpy.context.scene.tsv_emitter

    def draw(self, context):

        emitter = tsv_get_emitter()

        layout = self.layout
        col = layout.column(heading='', align=False)
        col.scale_y = 2.0
        col.operator('tsv.open_preset_manager', text='Preset Groups', icon_value=0, emboss=True, depress=False)
        row = layout.row()
        row.template_list('TSV_UL_groups', "", emitter, 'tsv_groups', emitter, 'tsv_group_index', rows=0)
        col = row.column(heading='', align=False)
        col_1 = col.column(heading='', align=True)
        col_1.operator('tsv.add_group', text='', icon_value=31, emboss=True, depress=False)
        col_1.operator('tsv.remove_group', text='', icon_value=32, emboss=True, depress=False)
        col_2 = col.column(heading='', align=True)
        col_2.operator('tsv.move_group_layer_up', text='', icon_value=7, emboss=True, depress=False)
        col_2.operator('tsv.move_group_layer_down', text='', icon_value=5, emboss=True, depress=False)

classes = [
    TSV_PT_groups,
    TSV_UL_groups
]