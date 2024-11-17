import bpy
from .. utils.property_utils import *
from .. utils.const_utils import ROOT_PACKAGE_NAME

class SNA_UL_display_collection_list_AFE29(bpy.types.UIList):

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
    column = layout.column(heading='', align=False)
    column.label(text='Preset Groups', icon_value=0)
    column.operator('tsv.export_preset_group', text='Export Preset', icon_value=707, emboss=True, depress=False)
    column.operator('tsv.import_preset_group', text='Import Preset', icon_value=706, emboss=True, depress=False)

    row = column.row(heading='', align=True)
    coll_id = display_collection_id('AFE29', locals())
    row.template_list('SNA_UL_display_collection_list_AFE29', coll_id, bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences, 'sna_tsv_preset_groups', bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences, 'sna_tsv_preset_groups_index', rows=0)
    col_87264 = row.column(heading='', align=False)
    col_FB45C = col_87264.column(heading='', align=True)
    op = col_FB45C.operator('tsv.save_preset_group', text='', icon_value=31, emboss=True, depress=False)
    op.sna_index = 0
    op = col_FB45C.operator('tsv.remove_preset_group', text='', icon_value=32, emboss=True, depress=False)
    col_D13CF = col_87264.column(heading='', align=True)
    col_D13CF.alert = False
    col_D13CF.enabled = True
    col_D13CF.active = True
    col_D13CF.use_property_split = False
    col_D13CF.use_property_decorate = False
    col_D13CF.scale_x = 1.0
    col_D13CF.scale_y = 1.0
    col_D13CF.alignment = 'Expand'.upper()
    col_D13CF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    op = col_D13CF.operator('tsv.preset_group_move_up', text='', icon_value=7, emboss=True, depress=False)
    op = col_D13CF.operator('tsv.preset_group_move_down', text='', icon_value=5, emboss=True, depress=False)
    op = col_87264.operator('tsv.expand_preset_group', text='', icon_value=393, emboss=True, depress=bpy.context.scene.sna_tsv_expand_preset_layers)
    if bpy.context.scene.sna_tsv_expand_preset_layers:
        col_7ABF7 = column.column(heading='', align=False)
        col_7ABF7.alert = False
        col_7ABF7.enabled = True
        col_7ABF7.active = True
        col_7ABF7.use_property_split = False
        col_7ABF7.use_property_decorate = False
        col_7ABF7.scale_x = 1.0
        col_7ABF7.scale_y = 1.0
        col_7ABF7.alignment = 'Expand'.upper()
        col_7ABF7.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_7ABF7.label(text='Preset Group Layers', icon_value=0)
        if property_exists("bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index]", globals(), locals()):
            if (len(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index].tsv_preset_layers) != 0):
                for i_702AC in range(len(bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index].tsv_preset_layers)):
                    box_2E602 = col_7ABF7.box()
                    box_2E602.alert = False
                    box_2E602.enabled = True
                    box_2E602.active = True
                    box_2E602.use_property_split = False
                    box_2E602.use_property_decorate = False
                    box_2E602.alignment = 'Expand'.upper()
                    box_2E602.scale_x = 1.0
                    box_2E602.scale_y = 1.0
                    if not True: box_2E602.operator_context = "EXEC_DEFAULT"
                    box_2E602.label(text=bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[ROOT_PACKAGE_NAME].preferences.sna_tsv_preset_groups_index].tsv_preset_layers[i_702AC].label, icon_value=0)
            else:
                col_7ABF7.label(text="Preset doesn't contain any layers", icon_value=0)
        else:
            col_7ABF7.label(text='No Preset Selected', icon_value=0)
    col_2E96F = column.column(heading='', align=False)
    col_2E96F.alert = False
    col_2E96F.enabled = True
    col_2E96F.active = True
    col_2E96F.use_property_split = False
    col_2E96F.use_property_decorate = False
    col_2E96F.scale_x = 1.0
    col_2E96F.scale_y = 2.0
    col_2E96F.alignment = 'Expand'.upper()
    col_2E96F.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    op = col_2E96F.operator('sna.load_preset_group_ea06e', text='Load Preset', icon_value=0, emboss=True, depress=False)

classes = [
    SNA_UL_display_collection_list_AFE29
]