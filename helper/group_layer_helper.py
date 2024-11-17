import bpy
import os

from .. utils.blend_utils import get_blend_contents
from .. utils.property_utils import property_exists


def sna_append_low_poly_objects_8DF63():
    if property_exists("bpy.data.collections['low_poly_objects']", globals(), locals()):
        pass
    else:
        collection_85E6C = bpy.data.collections.new(name='low_poly_objects', )
        collection_85E6C.hide_viewport = True
        collection_85E6C.hide_render = True
        bpy.context.collection.children.link(child=collection_85E6C, )
        for i_EEF75 in range(len(get_blend_contents(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'blends','low_poly_objects.blend'), 'objects'))):
            before_data = list(bpy.data.objects)
            bpy.ops.wm.append(directory=os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'blends','low_poly_objects.blend') + r'\Object', filename=get_blend_contents(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'blends','low_poly_objects.blend'), 'objects')[i_EEF75], link=False)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
            appended_A634A = None if not new_data else new_data[0]
            for i_5BF01 in range(len(appended_A634A.users_collection)):
                appended_A634A.users_collection[i_5BF01].objects.unlink(object=appended_A634A, )
            bpy.data.collections['low_poly_objects'].objects.link(object=appended_A634A, )

class TSV_OT_open_asset_browser(bpy.types.Operator):
    bl_idname = "tsv.open_asset_browser"
    bl_label = "open_asset_browser"
    bl_description = "Open Asset Browser"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.ops.wm.window_new('INVOKE_DEFAULT', )
        bpy.context.area.ui_type = 'ASSETS'
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

classes = [
    TSV_OT_open_asset_browser
]