import bpy
import os

class TSV_OT_import_preset_group(bpy.types.Operator):
    bl_idname = "tsv.import_preset_group"
    bl_label = "Import Preset Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_preset_group: bpy.props.StringProperty(name='preset_group', description='', default='', subtype='FILE_PATH', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_import_preset_group_AB955(self.sna_preset_group)
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        col_87E33 = layout.column(heading='', align=False)
        col_87E33.prop(self, 'sna_preset_group', text='Preset Group', icon_value=0, emboss=True)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

def sna_import_preset_group_AB955(path):
    if os.path.exists(path):
        if (os.path.splitext(path)[1] == '.txt'):
            text_9F810 = ""
            lines_9F810 = []
            if os.path.exists(path):
                with open(path, "r") as file_9F810:
                    lines_9F810 = list(map(lambda l: l.strip(), file_9F810.readlines()))
                    text_9F810 = "\n".join(lines_9F810)
            item_A0B3C = bpy.context.preferences.addons[__package__].preferences.sna_tsv_preset_groups.add()
            item_A0B3C.label = text_9F810.split('|||||')[0]
            for i_04DED in range(len(text_9F810.split('|||||')[1].split('||||'))):
                item_97DCD = item_A0B3C.tsv_preset_layers.add()
                item_97DCD.label = text_9F810.split('|||||')[1].split('||||')[i_04DED].split('|||')[0]
                item_97DCD.inputs = text_9F810.split('|||||')[1].split('||||')[i_04DED].split('|||')[1]
        else:
            bpy.ops.sna.error_659d1('INVOKE_DEFAULT', sna_message='File Extension must be .txt')
    else:
        bpy.ops.sna.error_659d1('INVOKE_DEFAULT', sna_message="Path Doesn't Exists")

classes = [
    TSV_OT_import_preset_group
]