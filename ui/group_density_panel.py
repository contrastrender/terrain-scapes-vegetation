import bpy

from .. utils.collection_utils import index_in_col
from .. utils.property_utils import display_collection_id, property_exists
from .. utils.ui_utils import sna_display_inputs_from_67553
from .. ui.vegetation_panel import TSV_PT_panel


class TSV_PT_group_density(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_density"
    bl_label = "Density"
    bl_parent_id = "TSV_PT_groups"

    @classmethod
    def poll(self, context):
        emitter = bpy.context.scene.sna_tsv_emitter
        if (index_in_col(emitter.sna_tsv_group_layers, emitter.sna_tsv_group_layer_index)):
            return True
        else:
            return None

    def draw(self, context):
        layout = self.layout
        col_73F61 = layout.column(heading='', align=True)
        box_AA695 = col_73F61.box()
        col_5B709 = box_AA695.column(heading='', align=True)
        col_5B709.prop(bpy.context.scene
                       .sna_tsv_emitter
                       .modifiers['vegetation']
                       .node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome']
                       .inputs[6],
                         'default_value', text='Density', icon_value=0, emboss=True)
        
        if (bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[2].default_value != None):
            col_5B709.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[2], 'default_value', text='Distance Culling', icon_value=0, emboss=True)
        if (bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[2].default_value and (bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[2].default_value != None)):
            col_5B709.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[3], 'default_value', text='Distance', icon_value=0, emboss=True)
        col_5B709.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[4], 'default_value', text='Avoid Biome Intersection', icon_value=0, emboss=True)
        box_04AEA = col_73F61.box()
        row_3956F = box_04AEA.row(heading='', align=True)
        coll_id = display_collection_id('80CA4', locals())
        row_3956F.template_list('SNA_UL_display_collection_list001_80CA4', coll_id, bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index], 'density_masks', bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index], 'density_mask_index', rows=0)
        col_8F69F = row_3956F.column(heading='', align=True)
        op = col_8F69F.operator('sna.add_d6bc2', text='', icon_value=31, emboss=True, depress=False)
        op = col_8F69F.operator('sna.remove_d46d0', text='', icon_value=32, emboss=True, depress=False)
        if property_exists("bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index]", globals(), locals()):
            box_4C49E = col_73F61.box()
            col_4A9BE = box_4C49E.column(heading='', align=False)
            layout_function = col_4A9BE
            sna_display_inputs_from_67553(layout_function, bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index) + '_density'].inputs, 1)


classes = [
    TSV_PT_group_density
]