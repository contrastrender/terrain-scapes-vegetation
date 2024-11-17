import bpy
import os
from .. utils.property_utils import property_exists

export_preset_group = {'sna_layers': '', }

class TSV_OT_export_preset_group(bpy.types.Operator):
    bl_idname = "tsv.export_preset_group"
    bl_label = "Export Preset Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_directory: bpy.props.StringProperty(name='directory', description='', default='', subtype='DIR_PATH', maxlen=0)
    sna_name: bpy.props.StringProperty(name='name', description='', default='', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_export_preset_group_4E077(self.sna_name, self.sna_directory, bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups[bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups_index])
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        col_35C43 = layout.column(heading='', align=False)
        col_35C43.alert = False
        col_35C43.enabled = True
        col_35C43.active = True
        col_35C43.use_property_split = True
        col_35C43.use_property_decorate = False
        col_35C43.scale_x = 1.0
        col_35C43.scale_y = 1.0
        col_35C43.alignment = 'Expand'.upper()
        col_35C43.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_35C43.prop(self, 'sna_directory', text='Directory', icon_value=0, emboss=True)
        col_35C43.prop(self, 'sna_name', text='Save As', icon_value=0, emboss=True)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)


def sna_export_preset_group_4E077(name, directory, preset_group):
    if property_exists("preset_group", globals(), locals()):
        if os.path.isdir(directory):
            if (name != ''):
                if property_exists("preset_group", globals(), locals()):
                    export_preset_group['sna_layers'] = ''
                    for i_AC223 in range(len(preset_group.tsv_preset_layers)):
                        export_preset_group['sna_layers'] = export_preset_group['sna_layers'] + preset_group.tsv_preset_layers[i_AC223].label + '|||' + preset_group.tsv_preset_layers[i_AC223].inputs + ('' if (int(len(preset_group.tsv_preset_layers) - 1.0) == i_AC223) else '||||')
                    if os.path.exists(os.path.join(directory,name) + '.txt'):
                        with open(os.path.join(directory,name) + '.txt', mode='w') as file_D3175:
                            file_D3175.seek(0)
                            file_D3175.write(preset_group.label + '|||||' + export_preset_group['sna_layers'])
                            file_D3175.truncate()
                    else:
                        with open(os.path.join(directory,name) + '.txt', mode='a') as file_7C20D:
                            file_7C20D.write(preset_group.label + '|||||' + export_preset_group['sna_layers'])

classes = [
    TSV_OT_export_preset_group
]