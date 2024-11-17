import bpy

from .. helper.get_prop import get_geo_node_prop


class TSV_PT_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Terrain Scapes"
    bl_options = {"DEFAULT_CLOSED"}
 
class TSV_PT_vegetation_panel(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_vegetation_panel"
    bl_label = "Vegetation"
 
    def draw(self, context):

        veg_geo_nodes = get_geo_node_prop()

        layout = self.layout
        col_CB6F2 = layout.column(heading='', align=False)
        col_CB6F2.prop(bpy.context.scene, 'tsv_emitter', text='Emitter', icon_value=0, emboss=True)
        if (bpy.context.scene.tsv_emitter != None):
            if (veg_geo_nodes != None):
                system_node = veg_geo_nodes.node_group.nodes.get("system")
                col_B0A37 = col_CB6F2.column(heading='', align=False)
                op = col_B0A37.operator('tsv.remove_vegetation_geo_nodes', text='Remove', icon_value=0, emboss=True, depress=False)
                col_FC031 = col_B0A37.column(heading='', align=False)
                col_94805 = col_FC031.column(heading='', align=True)
                col_94805.prop(veg_geo_nodes, 'show_render', text='Show Render', icon_value=0, emboss=True)
                col_94805.prop(veg_geo_nodes, 'show_viewport', text='Show Viewport', icon_value=253, emboss=True)
                col_3A18C = col_FC031.column(heading='', align=True)
                col_3A18C.prop(system_node.inputs[0], 'default_value', text='Render Scale', icon_value=0, emboss=True)
                col_3A18C.prop(system_node.inputs[1], 'default_value', text='Viewport Scale', icon_value=0, emboss=True)
                col_FC031.prop(system_node.inputs[2], 'default_value', text='Camera', icon_value=0, emboss=True)
                if (system_node.inputs[2].default_value != None):
                    col_FC031.prop(system_node.inputs[3], 'default_value', text='Camera-Culling', icon_value=0, emboss=True)
                if ((system_node.inputs[2].default_value != None) and bool(system_node.inputs[3].default_value)):
                    col_31EF0 = col_FC031.column(heading='', align=True)
                    col_31EF0.prop(system_node.inputs[4], 'default_value', text='Focal Length', icon_value=0, emboss=True)
                    col_31EF0.prop(system_node.inputs[5], 'default_value', text='Width', icon_value=0, emboss=True)
                    col_31EF0.prop(system_node.inputs[6], 'default_value', text='Height', icon_value=0, emboss=True)
                
            else:
                op = col_CB6F2.operator('tsv.add_vegetation_geo_nodes', text='Add', icon_value=0, emboss=True, depress=False)
        else:
            col_CB6F2.label(text='Select an emitter', icon_value=0)
 
classes = [
    TSV_PT_vegetation_panel
]
