import bpy
import os

from .. utils.const_utils import ROOT_DIR

from .. utils.property_utils import property_exists

class TSV_OT_add_vegetation_geo_nodes(bpy.types.Operator):
    bl_idname = "tsv.add_vegetation_geo_nodes"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):

        if property_exists("bpy.data.node_groups['.TSV_vegetation']", globals(), locals()):
            pass
        else:
            before_data = list(bpy.data.node_groups)
            bpy.ops.wm.append(directory=os.path.join(ROOT_DIR ,"assets",'blends','vegetation.blend') + r'\NodeTree', filename='.TSV_vegetation', link=False)
            new_data = list(filter(lambda d: not d in before_data, list(bpy.data.node_groups)))
            appended_C10DA = None if not new_data else new_data[0]
            bpy.data.node_groups['.TSV_vegetation'].use_fake_user = True
        id_E5391 = bpy.data.node_groups['.TSV_vegetation'].copy()
        modifier_6E969 = bpy.context.scene.tsv_emitter.modifiers.new(name='vegetation', type='NODES', )
        modifier_6E969.node_group = id_E5391
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_add_vegetation_geo_nodes
]