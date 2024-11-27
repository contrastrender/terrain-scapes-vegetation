import bpy

from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_group_mask, tsv_get_group_mask_index
from .. utils.ui_utils import tsv_display_inputs
from .. ui.vegetation_panel import TSV_PT_panel

class TSV_UL_group_masks(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        geo_nodex = tsv_get_geo_nodes()
        group_index = tsv_get_group_index()

        mask_node = geo_nodex.nodes[f"{group_index}_group"].node_tree.nodes[f"{index}_mask"]

        layout.prop(item, 'label', text = "", emboss = False)
        layout.prop(mask_node, 'mute', text='', icon=("HIDE_ON" if mask_node.mute else "HIDE_OFF"), emboss=False)

class TSV_PT_group_masks(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_masks"
    bl_label = "Masks"
    bl_parent_id = "TSV_PT_groups"

    @classmethod
    def poll(self, context):
        return tsv_get_group()

    def draw(self, context):

        group = tsv_get_group()

        col = self.layout.column()
        row = col.row()

        row.template_list('TSV_UL_group_masks', "", group, "masks", group, "mask_index")

        col_1 = row.column(align= True)

        col_1.operator('tsv.group_mask_add', text='', icon = "ADD")
        col_1.operator('tsv.group_mask_remove', text='', icon = "REMOVE")

        if not tsv_get_group_mask():
            return None

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        mask_node = group_node.node_tree.nodes[f"{tsv_get_group_mask_index()}_mask"]

        tsv_display_inputs(col, mask_node.inputs)

classes = [
    TSV_UL_group_masks,
    TSV_PT_group_masks
]