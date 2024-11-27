import bpy

from .. helper.get_prop_helper import tsv_get_geo_nodes


class TSV_PT_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Terrain Scapes"
    bl_options = {"DEFAULT_CLOSED"}
 
class TSV_PT_vegetation_panel(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_vegetation_panel"
    bl_label = "Vegetation"
 
    def draw(self, context):

        geo_nodes = tsv_get_geo_nodes()

        col = self.layout.column()
        col.use_property_split = True
        col.use_property_decorate = False
        
        return

        col.prop(bpy.context.scene, 'tsv_emitter', text='Emitter', icon_value=0, emboss=True)
        if (bpy.context.scene.tsv_emitter is not None):
            if (geo_nodes is not None):
                system_node = geo_nodes.nodes.get("settings")
                col_B0A37 = col.column(heading='', align=False)
                col_FC031 = col_B0A37.column(heading='', align=False)
                col_94805 = col_FC031.column(heading='', align=True)
                col_94805.prop(geo_nodes, 'show_render', text='Show Render', icon_value=0, emboss=True)
                col_94805.prop(geo_nodes, 'show_viewport', text='Show Viewport', icon_value=253, emboss=True)
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
 
classes = [
    TSV_PT_vegetation_panel
]
