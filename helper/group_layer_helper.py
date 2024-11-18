import bpy
import os

from .. utils.const_utils import ROOT_DIR
from .. utils.blend_utils import get_blend_contents


def sna_append_low_poly_objects_8DF63():
    # Check if the collection already exists
    if bpy.data.collections.get('low_poly_objects') is None:
        # Create a new collection if it doesn't exist
        collection = bpy.data.collections.new(name='low_poly_objects')
        bpy.context.scene.collection.children.link(child=collection, )
        collection.hide_viewport = True
        collection.hide_render = True

        # Get the file path of the blend file
        blend_file_path = os.path.join(ROOT_DIR, 'assets', 'blends', 'low_poly_objects.blend')
        
        # Get object names from the blend file
        objects_to_append = get_blend_contents(blend_file_path, 'objects')
        blend_object_dir = os.path.join(blend_file_path, r'Object')

        # Append each object
        for object_name in objects_to_append:
            before_objects = set(bpy.data.objects)
            
            # Append the object
            bpy.ops.wm.append(
                directory=blend_object_dir, 
                filename=object_name, 
                link=False
            )
            
            # Identify the newly appended object
            new_objects = set(bpy.data.objects) - before_objects
            appended_object = next(iter(new_objects), None)

            if appended_object:
                # Unlink the object from all current collections
                for collection in list(appended_object.users_collection):
                    collection.objects.unlink(appended_object)
                
                # Link the object to the low_poly_objects collection
                bpy.data.collections['low_poly_objects'].objects.link(appended_object)


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