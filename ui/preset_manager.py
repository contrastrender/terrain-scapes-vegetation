import bpy

from .. helper.get_prop import get_preset_group_index, get_preset_groups
from .. utils.property_utils import *
from .. utils.const_utils import ROOT_PACKAGE_NAME

class TSV_UL_preset_groups(bpy.types.UIList):

    def draw_item(self, context, layout, data, item_AFE29, icon, active_data, active_propname, index_AFE29):
        row = layout
        layout.prop(item_AFE29, 'label', text='', icon_value=0, emboss=False)

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

def tsv_preset_manager(layout, ):

    preset_groups = get_preset_groups()
    preset_group_index = get_preset_group_index()

    column = layout.column(heading='', align=False)
    column.label(text='Preset Groups', icon_value=0)
    column.operator('tsv.export_preset_group', text='Export Preset', icon_value=707, emboss=True, depress=False)
    column.operator('tsv.import_preset_group', text='Import Preset', icon_value=706, emboss=True, depress=False)

    row = column.row(heading='', align=True)
    coll_id = display_collection_id('AFE29', locals())
    row.template_list('TSV_UL_preset_groups', coll_id, bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences, 'tsv_preset_groups', bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences, 'tsv_preset_group_index', rows=0)
    col_87264 = row.column(heading='', align=False)
    col_FB45C = col_87264.column(heading='', align=True)
    op = col_FB45C.operator('tsv.save_preset_group', text='', icon_value=31, emboss=True, depress=False)
    op.sna_index = 0
    op = col_FB45C.operator('tsv.remove_preset_group', text='', icon_value=32, emboss=True, depress=False)
    col_D13CF = col_87264.column(heading='', align=True)
    op = col_D13CF.operator('tsv.preset_group_move_up', text='', icon_value=7, emboss=True, depress=False)
    op = col_D13CF.operator('tsv.preset_group_move_down', text='', icon_value=5, emboss=True, depress=False)
    op = col_87264.operator('tsv.expand_preset_group', text='', icon_value=393, emboss=True, depress=bpy.context.scene.tsv_expand_preset_layers)
    if bpy.context.scene.tsv_expand_preset_layers:
        col_7ABF7 = column.column(heading='', align=False)
        col_7ABF7.label(text='Preset Group Layers', icon_value=0)
        if property_exists("bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_group_index]", globals(), locals()):
            if (len(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups_index].tsv_preset_layers) != 0):
                for i_702AC in range(len(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups_index].tsv_preset_layers)):
                    box_2E602 = col_7ABF7.box()
                    box_2E602.label(text=bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.tsv_preset_groups_index].tsv_preset_layers[i_702AC].label, icon_value=0)
            else:
                col_7ABF7.label(text="Preset doesn't contain any layers", icon_value=0)
        else:
            col_7ABF7.label(text='No Preset Selected', icon_value=0)
    col_2E96F = column.column(heading='', align=False)
    op = col_2E96F.operator('sna.load_preset_group_ea06e', text='Load Preset', icon_value=0, emboss=True, depress=False)

classes = [
    TSV_UL_preset_groups
]