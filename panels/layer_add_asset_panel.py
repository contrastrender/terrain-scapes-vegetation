import bpy

from .. helper.get_prop_helper import tsv_get_group

class TSV_PT_add_layer(bpy.types.Panel):
    bl_label = 'Add Asset Layer'
    bl_idname = 'TSV_PT_add_layer'
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'TOOLS'
    bl_category = 'Terrain Scapes'

    @classmethod
    def poll(self, context):
        return tsv_get_group()

    def draw(self, context):
        col = self.layout.column()
        for asset in context.selected_assets:
            if asset.id_type == "OBJECT":
                op = col.operator(operator=f"tsv.group_layer_add_from_asset_browser", text=asset.name, icon="ADD")
                op.asset_full_library_path = asset.full_library_path
                op.asset_name = asset.name

classes = [
    TSV_PT_add_layer
]