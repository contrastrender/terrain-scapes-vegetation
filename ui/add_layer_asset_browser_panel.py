import bpy

from .. utils.property_utils import property_exists

class TSV_PT_add_layer(bpy.types.Panel):
    bl_label = 'Add Asset Layer'
    bl_idname = 'TSV_PT_add_layer'
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOLS'
    bl_context = ''
    bl_category = 'Terrain Scapes'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (( not property_exists("bpy.context.asset.name", globals(), locals()) or  not property_exists("bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index]", globals(), locals()) or (None == bpy.context.asset) or ('OBJECT' != bpy.context.asset.id_type)))

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        box_E9848 = layout.box()
        box_E9848.alert = False
        box_E9848.enabled = True
        box_E9848.active = True
        box_E9848.use_property_split = False
        box_E9848.use_property_decorate = False
        box_E9848.alignment = 'Expand'.upper()
        box_E9848.scale_x = 1.0
        box_E9848.scale_y = 1.0
        if not True: box_E9848.operator_context = "EXEC_DEFAULT"
        row_1F69F = box_E9848.row(heading='', align=False)
        row_1F69F.alert = False
        row_1F69F.enabled = True
        row_1F69F.active = True
        row_1F69F.use_property_split = False
        row_1F69F.use_property_decorate = False
        row_1F69F.scale_x = 1.0
        row_1F69F.scale_y = 1.0
        row_1F69F.alignment = 'Expand'.upper()
        row_1F69F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_1F69F.label(text=bpy.context.asset.name, icon_value=0)
        op = row_1F69F.operator('tsv.group_layer_add_from_asset_browser', text='', icon_value=31, emboss=True, depress=False)

classes = [
    TSV_PT_add_layer
]