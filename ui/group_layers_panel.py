import bpy

from .. utils.collection_utils import index_in_col
from .. utils.ui_utils import sna_display_inputs_from_67553
from .. utils.property_utils import display_collection_id, property_exists
from .. ui.vegetation_panel import TSV_PT_panel

class TSV_UL_group_layers(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        cur_node = (bpy.context.scene
                    .sna_tsv_emitter.modifiers['vegetation']
                    .node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(index) + '_layer'])

        solid_material = (cur_node.inputs['Solid Material'].default_value)
        
        hide_viewport = (cur_node.inputs[5])
        
        hide_render = (cur_node.inputs[6])

        row = layout.row(heading='', align=True)
        row_1 = row.row(heading='', align=True)
        row_1.prop(solid_material, 'diffuse_color', text='', icon_value=0, emboss=True)
        row.prop(item, 'label', text='', icon_value=0, emboss=False)
        row_2 = layout.row(heading='', align=True)
        row_2.prop(hide_viewport, 'default_value', text='', icon_value=(253 if hide_viewport.default_value else 254), emboss=False)
        row_2.prop(hide_render, 'default_value', text='', icon_value=(257 if hide_render.default_value else 258), emboss=False)


class TSV_PT_group_layers(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layers"
    bl_label = "Layers"
    bl_parent_id = "TSV_PT_groups"

    @classmethod
    def poll(self, context):
        emitter = bpy.context.scene.sna_tsv_emitter
        if (index_in_col(emitter.sna_tsv_group_layers, emitter.sna_tsv_group_layer_index)):
            return True
        else:
            return None

    def draw(self, context):

        group_index = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index
        group_layer = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[group_index]

        col_3D419 = self.layout.column(heading='', align=True)
        box_C1BA5 = col_3D419.box()
        row_69993 = box_C1BA5.row(heading='', align=True)
        coll_id = display_collection_id('E36A2', locals())
        row_69993.template_list('TSV_UL_group_layers', coll_id, group_layer, 'layers', group_layer, 'layer_index', rows=0)
        col_76FCC = row_69993.column(heading='', align=False)
        col_69EE6 = col_76FCC.column(heading='', align=True)
        op = col_69EE6.operator('tsv.group_layer_add_from_selection', text='', icon_value=31, emboss=True, depress=False)
        op = col_69EE6.operator('tsv.group_layer_remove', text='', icon_value=32, emboss=True, depress=False)
        op = col_76FCC.operator('tsv.open_asset_browser', text='', icon_value=250, emboss=True, depress=False)

        cur_node = (bpy.context.scene
                    .sna_tsv_emitter.modifiers['vegetation']
                    .node_group.nodes[str(group_index) + ',' + str(group_layer.layer_index) + '_layer'])

        if (
            bpy.context.scene
            .sna_tsv_emitter
            .sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index]
            .layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index]
            ) != None:

            col_B146C = col_3D419.column(heading='', align=True)
            box_21F69 = col_B146C.box()
            col_2C638 = box_21F69.column(heading='', align=True)
            col_2C638.prop(cur_node.inputs[7], 'default_value', text='Object', icon_value=0, emboss=True, expand=True)
            box_52123 = col_B146C.box()
            col_9DC6A = box_52123.column(heading='', align=True)
            col_9DC6A.label(text='Viewport Display', icon_value=0)
            col_9DC6A.prop(cur_node.inputs[12], 'default_value', text='Max Instances', icon_value=0, emboss=True, expand=True)
            row_A0D0F = col_9DC6A.row(heading='', align=False)
            row_A0D0F.prop(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index], 'viewport_display', text=bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index].viewport_display, icon_value=0, emboss=True, expand=True)

            if (bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index].viewport_display == 'Low Poly'):
                col_9DC6A.template_icon_view(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index], 'low_poly_objects', show_labels=False, scale=8.0, scale_popup=5.0)
            box_5DF65 = col_B146C.box()
            col_01A02 = box_5DF65.column(heading='', align=True)
            col_01A02.label(text='Scale', icon_value=0)
            col_01A02.prop(cur_node.inputs[13], 'default_value', text='Instance Scale', icon_value=0, emboss=True, expand=True)
            col_01A02.prop(cur_node.inputs[14], 'default_value', text='Scale', icon_value=0, emboss=True, expand=True)
            col_01A02.prop(cur_node.inputs[15], 'default_value', text='Random', icon_value=0, emboss=True, expand=True)
            if cur_node.inputs[15].default_value:
                col_4A0D0 = col_01A02.column(heading='', align=True)
                col_4A0D0.prop(cur_node.inputs[16], 'default_value', text='Min', icon_value=0, emboss=True, expand=True)
                col_4A0D0.prop(cur_node.inputs[17], 'default_value', text='Max', icon_value=0, emboss=True, expand=True)
                col_4A0D0.prop(cur_node.inputs[18], 'default_value', text='Noise', icon_value=0, emboss=True, expand=True)
                if cur_node.inputs[18].default_value:
                    col_A6D64 = col_4A0D0.column(heading='', align=True)
                    col_A6D64.prop(cur_node.inputs[19], 'default_value', text='Scale', icon_value=0, emboss=True, expand=True)
                    col_A6D64.prop(cur_node.inputs[20], 'default_value', text='Contrast', icon_value=0, emboss=True, expand=True)
                    col_A6D64.prop(cur_node.inputs[21], 'default_value', text='Value', icon_value=0, emboss=True, expand=True)
                    col_A6D64.prop(cur_node.inputs[22], 'default_value', text='Seed', icon_value=0, emboss=True, expand=True)
            box_63018 = col_B146C.box()
            col_398E4 = box_63018.column(heading='', align=True)
            col_398E4.label(text='Density', icon_value=0)
            col_398E4.prop(cur_node.inputs[23], 'default_value', text='Densiy', icon_value=0, emboss=True, expand=True)
            col_398E4.prop(cur_node.inputs[24], 'default_value', text='Noise', icon_value=0, emboss=True, expand=True)
            if cur_node.inputs[24].default_value:
                col_E09D3 = col_398E4.column(heading='', align=True)
                col_E09D3.prop(cur_node.inputs[25], 'default_value', text='Scale', icon_value=0, emboss=True, expand=True)
                col_E09D3.prop(cur_node.inputs[26], 'default_value', text='Contrast', icon_value=0, emboss=True, expand=True)
                col_E09D3.prop(cur_node.inputs[27], 'default_value', text='Value', icon_value=0, emboss=True, expand=True)
                col_E09D3.prop(cur_node.inputs[28], 'default_value', text='Seed', icon_value=0, emboss=True, expand=True)
            box_742AD = col_B146C.box()
            col_BE11C = box_742AD.column(heading='', align=True)
            col_BE11C.label(text='Wind', icon_value=0)
            col_BE11C.prop(cur_node.inputs[29], 'default_value', text='Intensiy', icon_value=0, emboss=True, expand=True)
            col_BE11C.prop(cur_node.inputs[30], 'default_value', text='Speed', icon_value=0, emboss=True, expand=True)
            col_BE11C.prop(cur_node.inputs[31], 'default_value', text='Frequenzy', icon_value=0, emboss=True, expand=True)
            box_444B5 = col_B146C.box()
            col_6D1CB = box_444B5.column(heading='', align=True)
            col_6D1CB.label(text='Materials', icon_value=0)
            coll_id = display_collection_id('31907', locals())
            col_6D1CB.template_list('SNA_UL_display_collection_list_31907', coll_id, cur_node.inputs[7].default_value, 'material_slots', cur_node.inputs[7].default_value, 'active_material_index', rows=0)
            if property_exists("cur_node.inputs[7].default_value.material_slots[cur_node.inputs[7].default_value.active_material_index].material.node_tree.nodes['inputs'].inputs", globals(), locals()):
                layout_function = col_6D1CB
                sna_display_inputs_from_67553(layout_function, cur_node.inputs[7].default_value.material_slots[cur_node.inputs[7].default_value.active_material_index].material.node_tree.nodes['inputs'].inputs, 0)
            else:
                col_6D1CB.label(text='this material has not input node', icon_value=2)

classes = [
    TSV_PT_group_layers,
    TSV_UL_group_layers
]