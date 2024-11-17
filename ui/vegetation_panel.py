import bpy

from .. utils.property_utils import property_exists

class TSV_PT_panel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Terrain Scapes"
    bl_options = {"DEFAULT_CLOSED"}
 
class TSV_PT_vegetation_panel(TSV_PT_panel, bpy.types.Panel):
    bl_idname = "TSV_PT_vegetation_panel"
    bl_label = "Vegetation"
 
    def draw(self, context):
        layout = self.layout
        col_CB6F2 = layout.column(heading='', align=False)
        col_CB6F2.prop(bpy.context.scene, 'sna_tsv_emitter', text='Emitter', icon_value=0, emboss=True)
        if (bpy.context.scene.sna_tsv_emitter != None):
            if property_exists("bpy.context.scene.sna_tsv_emitter.modifiers['vegetation']", globals(), locals()):
                col_B0A37 = col_CB6F2.column(heading='', align=False)
                op = col_B0A37.operator('tsv.remove_vegetation_geo_nodes', text='Remove', icon_value=0, emboss=True, depress=False)
                col_FC031 = col_B0A37.column(heading='', align=False)
                col_94805 = col_FC031.column(heading='', align=True)
                col_94805.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'], 'show_render', text='Show Render', icon_value=0, emboss=True)
                col_94805.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'], 'show_viewport', text='Show Viewport', icon_value=253, emboss=True)
                col_3A18C = col_FC031.column(heading='', align=True)
                col_3A18C.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[0], 'default_value', text='Render Scale', icon_value=0, emboss=True)
                col_3A18C.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[1], 'default_value', text='Viewport Scale', icon_value=0, emboss=True)
                col_FC031.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[2], 'default_value', text='Camera', icon_value=0, emboss=True)
                if (bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[2].default_value != None):
                    col_FC031.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[3], 'default_value', text='Camera-Culling', icon_value=0, emboss=True)
                if ((bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[2].default_value != None) and bool(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[3].default_value)):
                    col_31EF0 = col_FC031.column(heading='', align=True)
                    col_31EF0.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[4], 'default_value', text='Focal Length', icon_value=0, emboss=True)
                    col_31EF0.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[5], 'default_value', text='Width', icon_value=0, emboss=True)
                    col_31EF0.prop(bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].inputs[6], 'default_value', text='Height', icon_value=0, emboss=True)
                
            else:
                op = col_CB6F2.operator('tsv.add_vegetation_geo_nodes', text='Add', icon_value=0, emboss=True, depress=False)
        else:
            col_CB6F2.label(text='Select an emitter', icon_value=0)
 
classes = [
    TSV_PT_vegetation_panel
]
