import bpy

from .. const import PACKAGE

from .. utils.integer_utils import random_integer
from .. utils.color_utils import random_color
from .. helper.group_layer_helper import sna_append_low_poly_objects_8DF63
from .. utils.property_utils import property_exists

def sna_add_layer_31A03(label):
    node_BFB5F = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes.new(type='GeometryNodeGroup', )
    node_BFB5F.node_tree = bpy.data.node_groups['.TSV_layer']
    node_BFB5F.name = str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'
    material_72B75 = bpy.data.materials.new(name='.', )
    material_72B75.diffuse_color = (random_color(False, None, None)[0], random_color(False, None, None)[1], random_color(False, None, None)[2], 1.0)
    bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs['Solid Material'].default_value = material_72B75
    link_AC827 = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[0], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes['Group Input'].outputs[0], )
    link_8CA9C = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes['Join Geometry'].inputs[0], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].outputs[0], )
    link_21B4B = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[3], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + '_biome' + ''].outputs[1], )
    link_70E24 = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[4], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + '_biome' + ''].outputs[2], )
    link_3C430 = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[1], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].outputs[1], )
    link_B31C1 = bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[2], output=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].outputs[2], )
    bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers)) + '_layer'].inputs[8].default_value = random_integer(0.0, 10000.0, None)
    item_F1484 = bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers.add()
    item_F1484.label = label
    bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index = int(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) - 1.0)
    return str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(int(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) - 1.0)) + '_layer'


class TSV_OT_group_layer_add_from_selection(bpy.types.Operator):
    bl_idname = "tsv.group_layer_add_from_selection"
    bl_label = "Add From Selection"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        for i_C60DB in range(len(bpy.context.selected_objects)):
            node_0_6aca5 = sna_add_layer_31A03(bpy.context.selected_objects[i_C60DB].name)
            bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[node_0_6aca5].inputs[7].default_value = bpy.context.selected_objects[i_C60DB]
        sna_append_low_poly_objects_8DF63()
        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        col_0E2D5 = layout.column(heading='', align=True)
        col_0E2D5.alert = False
        col_0E2D5.enabled = True
        col_0E2D5.active = True
        col_0E2D5.use_property_split = True
        col_0E2D5.use_property_decorate = False
        col_0E2D5.scale_x = 1.0
        col_0E2D5.scale_y = 1.0
        col_0E2D5.alignment = 'Expand'.upper()
        col_0E2D5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        if (0 == len(bpy.context.selected_objects)):
            box_EFDD4 = col_0E2D5.box()
            box_EFDD4.alert = False
            box_EFDD4.enabled = True
            box_EFDD4.active = False
            box_EFDD4.use_property_split = False
            box_EFDD4.use_property_decorate = False
            box_EFDD4.alignment = 'Expand'.upper()
            box_EFDD4.scale_x = 1.0
            box_EFDD4.scale_y = 1.0
            if not True: box_EFDD4.operator_context = "EXEC_DEFAULT"
            box_EFDD4.label(text='No objects selected', icon_value=0)
        else:
            for i_C55A4 in range(len(bpy.context.selected_objects)):
                box_5BA78 = col_0E2D5.box()
                box_5BA78.alert = False
                box_5BA78.enabled = True
                box_5BA78.active = True
                box_5BA78.use_property_split = False
                box_5BA78.use_property_decorate = False
                box_5BA78.alignment = 'Expand'.upper()
                box_5BA78.scale_x = 1.0
                box_5BA78.scale_y = 1.0
                if not True: box_5BA78.operator_context = "EXEC_DEFAULT"
                box_5BA78.label(text=bpy.context.selected_objects[i_C55A4].name, icon_value=0)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=300)

class TSV_OT_group_layer_remove(bpy.types.Operator):
    bl_idname = "tsv.group_layer_remove"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_layer_3CD98(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def sna_remove_layer_3CD98(Index):
    if property_exists("bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers[bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index]", globals(), locals()):
        if (None != bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(Index) + '_layer'].inputs['Solid Material'].default_value):
            bpy.data.materials.remove(material=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(Index) + '_layer'].inputs['Solid Material'].default_value, )
        bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes.remove(node=bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(Index) + '_layer'], )
        for i_6362E in range(int(int(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) - Index) - 1.0)):
            bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(int(int(Index + i_6362E) + 1.0)) + '_layer'].name = str(bpy.context.scene.tsv_emitter.tsv_group_index) + ',' + str(int(Index + i_6362E)) + '_layer'
        if len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) > bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index:
            bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers.remove(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index)
        if (len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) == bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index):
            bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layer_index = int(len(bpy.context.scene.tsv_emitter.tsv_groups[bpy.context.scene.tsv_emitter.tsv_group_index].layers) - 1.0)

class TSV_OT_group_layer_add_from_asset_browser(bpy.types.Operator):
    bl_idname = "tsv.group_layer_add_from_asset_browser"
    bl_label = "Add from asset browser"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (None == bpy.context.asset):
            bpy.ops.sna.error_659d1('INVOKE_DEFAULT', sna_message='Select an asset')
        else:
            if ('OBJECT' != bpy.context.asset.id_type):
                bpy.ops.sna.error_659d1('INVOKE_DEFAULT', sna_message='Active asset is not an object')
            else:
                sna_append_objects_67667(bpy.context.asset.name, bpy.context.asset.full_library_path)
                sna_append_low_poly_objects_8DF63()
                node_0_d56bb = sna_add_layer_31A03(bpy.context.asset.name)
                bpy.context.scene.tsv_emitter.modifiers['vegetation'].node_group.nodes[node_0_d56bb].inputs[7].default_value = bpy.data.objects[bpy.context.asset.name]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
def sna_append_objects_67667(asset_name, asset_path):
    if property_exists("bpy.data.collections['vegetation_assets']", globals(), locals()):
        pass
    else:
        collection_FEE38 = bpy.data.collections.new(name='vegetation_assets', )
        bpy.context.scene.collection.children.link(child=collection_FEE38, )
        collection_FEE38.hide_render = True
        collection_FEE38.hide_viewport = True
    if property_exists("bpy.data.objects[asset_name]", globals(), locals()):
        pass
    else:
        before_data = list(bpy.data.objects)
        bpy.ops.wm.append(directory=asset_path + r'\Object', filename=asset_name, link=False)
        new_data = list(filter(lambda d: not d in before_data, list(bpy.data.objects)))
        appended_84AC8 = None if not new_data else new_data[0]
        for i_B3C5D in range(len(appended_84AC8.users_collection)):
            appended_84AC8.users_collection[i_B3C5D].objects.unlink(object=appended_84AC8, )
        bpy.data.collections['vegetation_assets'].objects.link(object=appended_84AC8, )


classes = [
    TSV_OT_group_layer_add_from_selection,
    TSV_OT_group_layer_remove,
    TSV_OT_group_layer_add_from_asset_browser
]