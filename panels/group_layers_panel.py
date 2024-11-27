import bpy

from .. utils.ui_utils import tsv_display_input
from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_group_layer, tsv_get_group_layer_index
from .. panels.vegetation_panel import TSV_PT_panel

class TSV_UL_group_layers(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        geo_nodex = tsv_get_geo_nodes()
        group_index = tsv_get_group_index()

        layer_node = geo_nodex.nodes[f"{group_index}_group"].node_tree.nodes[f"{index}_layer"]

        row_1 = layout.row(heading='', align=False)
        row_1.prop(layer_node.inputs[7].default_value, 'diffuse_color', text='')
        row_1.prop(item, 'label', text = "", emboss = False)

        row_2 = layout.row(heading='', align=True)
        row_2.prop(layer_node.inputs[4], 'default_value', text='', icon=("HIDE_OFF" if layer_node.inputs[4].default_value else "HIDE_ON"), emboss=False)
        row_2.prop(layer_node.inputs[5], 'default_value', text='', icon=("HIDE_OFF" if layer_node.inputs[5].default_value else "HIDE_ON"), emboss=False)


class TSV_PT_group_layers(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layers"
    bl_label = "Layers"
    bl_parent_id = "TSV_PT_groups"

    @classmethod
    def poll(self, context):
        return tsv_get_group()

    def draw(self, context):

        group = tsv_get_group()

        row = self.layout.row()
        row.template_list('TSV_UL_group_layers', "", group, 'layers', group, 'layer_index', rows=0)
        col = row.column(heading='', align=True)
        col.operator('tsv.group_layer_add_from_selection', text='', icon = "ADD")
        col.operator('tsv.group_layer_remove', text='', icon = "REMOVE")
        

class TSV_PT_group_layer_viewport_display(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layer_viewport_display"
    bl_label = "Viewport Display"
    bl_parent_id = "TSV_PT_group_layers"

    @classmethod
    def poll(self, context):
        return tsv_get_group_layer()
    
    def draw(self, context):
        col = self.layout.column()
        col.use_property_decorate = False
        col.use_property_split = True

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        layer_node = group_node.node_tree.nodes[f"{tsv_get_group_layer_index()}_layer"]

        row = col.row()
        tsv_display_input(col, layer_node.inputs[9])

        if layer_node.inputs[9].default_value == "Placeholder":
            tsv_display_input(col, layer_node.inputs[10])
        
        tsv_display_input(col, layer_node.inputs[11])

class TSV_PT_group_layer_scale(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layer_scale"
    bl_label = "Scale"
    bl_parent_id = "TSV_PT_group_layers"

    @classmethod
    def poll(self, context):
        return tsv_get_group_layer()
    
    def draw(self, context):
        col = self.layout.column()
        col.use_property_decorate = False
        col.use_property_split = True

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        layer_node = group_node.node_tree.nodes[f"{tsv_get_group_layer_index()}_layer"]

        
        tsv_display_input(col, layer_node.inputs[12])
        tsv_display_input(col, layer_node.inputs[13])
        tsv_display_input(col, layer_node.inputs[14])

        if layer_node.inputs[14].default_value:
            tsv_display_input(col, layer_node.inputs[15])
            tsv_display_input(col, layer_node.inputs[16])
            tsv_display_input(col, layer_node.inputs[17])

            if layer_node.inputs[17].default_value:
                tsv_display_input(col, layer_node.inputs[18])
                tsv_display_input(col, layer_node.inputs[19])
                tsv_display_input(col, layer_node.inputs[20])
                tsv_display_input(col, layer_node.inputs[21])

class TSV_PT_group_layer_density(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layer_density"
    bl_label = "Density"
    bl_parent_id = "TSV_PT_group_layers"

    @classmethod
    def poll(self, context):
        return tsv_get_group_layer()
    
    def draw(self, context):
        col = self.layout.column()
        col.use_property_decorate = False
        col.use_property_split = True

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        layer_node = group_node.node_tree.nodes[f"{tsv_get_group_layer_index()}_layer"]

        tsv_display_input(col, layer_node.inputs[22])
        tsv_display_input(col, layer_node.inputs[23])

        if layer_node.inputs[23].default_value:
            tsv_display_input(col, layer_node.inputs[24])
            tsv_display_input(col, layer_node.inputs[25])
            tsv_display_input(col, layer_node.inputs[26])
            tsv_display_input(col, layer_node.inputs[27])

class TSV_PT_group_layer_wind(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_group_layer_wind"
    bl_label = "Wind"
    bl_parent_id = "TSV_PT_group_layers"

    @classmethod
    def poll(self, context):
        return tsv_get_group_layer()
    
    def draw(self, context):
        col = self.layout.column()
        col.use_property_decorate = False
        col.use_property_split = True

        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        layer_node = group_node.node_tree.nodes[f"{tsv_get_group_layer_index()}_layer"]

        tsv_display_input(col, layer_node.inputs[28])
        tsv_display_input(col, layer_node.inputs[29])
        tsv_display_input(col, layer_node.inputs[30])

classes = [
    TSV_PT_group_layers,
    TSV_UL_group_layers,
    TSV_PT_group_layer_viewport_display,
    TSV_PT_group_layer_scale,
    TSV_PT_group_layer_density,
    TSV_PT_group_layer_wind
]