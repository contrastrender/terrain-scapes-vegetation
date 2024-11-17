import bpy

from .. utils.ui_utils import sna_display_inputs_from_67553
from .. utils.property_utils import display_collection_id, property_exists, property_existss
from .. ui.vegetation_panel import TSV_PT_panel

class TSV_UL_groups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item_8170E, icon, active_data, active_propname, index_8170E):
        row = layout
        layout.prop(item_8170E, 'label', text='', icon_value=0, emboss=False)
        row_FC6FF = layout.row(heading='', align=True)
        row_FC6FF.alert = False
        row_FC6FF.enabled = True
        row_FC6FF.active = True
        row_FC6FF.use_property_split = False
        row_FC6FF.use_property_decorate = False
        row_FC6FF.scale_x = 1.0
        row_FC6FF.scale_y = 1.0
        row_FC6FF.alignment = 'Expand'.upper()
        row_FC6FF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_FC6FF.prop(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(index_8170E) + '_biome'].inputs[7], 'default_value', text='', icon_value=(253 if bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(index_8170E) + '_biome'].inputs[7].default_value else 254), emboss=False)
        row_FC6FF.prop(bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(index_8170E) + '_biome'].inputs[8], 'default_value', text='', icon_value=(257 if bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(index_8170E) + '_biome'].inputs[8].default_value else 258), emboss=False)

    def filter_items(self, context, data, propname):
        flt_flags = []
        for item in getattr(data, propname):
            if not self.filter_name or self.filter_name.lower() in item.name.lower():
                if True:
                    flt_flags.append(self.bitflag_filter_item)
                else:
                    flt_flags.append(0)
            else:
                flt_flags.append(0)
        return flt_flags, []


def sna_biome_layers_95621(layout_function, ):
    layout = layout_function


class TSV_PT_groups(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_groups"
    bl_label = "Groups"
    bl_parent_id = "TSV_PT_vegetation_panel"

    @classmethod
    def poll(self, context):

        emitter = bpy.context.scene.tsv_emitter

        if (emitter != None and emitter.modifiers.get("vegetation") != None):
            return True
        else:
            return None

    def draw(self, context):
        layout = self.layout
        col_1689A = layout.column(heading='', align=False)
        col_1689A.scale_y = 2.0
        col_1689A.operator('tsv.open_preset_manager', text='Preset Manager', icon_value=0, emboss=True, depress=False)
        row_6C0C6 = layout.row(heading='', align=True)
        coll_id = display_collection_id('8170E', locals())
        row_6C0C6.template_list('TSV_UL_groups', coll_id, bpy.context.scene.tsv_emitter, 'tsv_groups', bpy.context.scene.tsv_emitter, 'tsv_group_index', rows=0)
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