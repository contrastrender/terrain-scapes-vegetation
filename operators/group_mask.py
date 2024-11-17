import bpy
import os

from .. utils.property_utils import property_exists

biome_density_mask__add = {'sna_masks': [], }

def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id

class TSV_OT_group_mask_add(bpy.types.Operator):
    bl_idname = "tsv.group_mask_add"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        mask_name = bpy.context.scene.sna_tsv_masks
        bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks)) + '_density'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) + 1.0)) + '_density'
        node_FB024 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.new(type='GeometryNodeGroup', )
        node_FB024.node_tree = bpy.data.node_groups['.TSV_mask_' + mask_name]
        node_FB024.name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks)) + '_density'
        link_C4100 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks)) + '_density'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) - 1.0)) + '_density'].outputs[0], )
        link_D31DA = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) + 1.0)) + '_density'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks)) + '_density'].outputs[0], )
        item_43506 = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks.add()
        item_43506.label = mask_name
        item_43506.texture = '.TSV_mask_' + mask_name
        bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index = int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) - 1.0)

        return {"FINISHED"}

    def draw(self, context):
        layout = self.layout
        col_FC1B4 = layout.column(heading='', align=False)
        col_FC1B4.alert = False
        col_FC1B4.enabled = True
        col_FC1B4.active = True
        col_FC1B4.use_property_split = True
        col_FC1B4.use_property_decorate = False
        col_FC1B4.scale_x = 1.0
        col_FC1B4.scale_y = 1.0
        col_FC1B4.alignment = 'Expand'.upper()
        col_FC1B4.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        col_FC1B4.template_icon_view(bpy.context.scene, 'sna_tsv_masks', show_labels=True, scale=8.0, scale_popup=5.0)

    def invoke(self, context, event):
        biome_density_mask__add['sna_masks'] = []
        for i_895AA in range(len([os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f) for f in os.listdir(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks')) if os.path.isfile(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f))])):
            biome_density_mask__add['sna_masks'].append([os.path.basename([os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f) for f in os.listdir(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks')) if os.path.isfile(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f))][i_895AA]).replace('.png', ''), os.path.basename([os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f) for f in os.listdir(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks')) if os.path.isfile(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f))][i_895AA]).replace('.png', ''), '', load_preview_icon([os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f) for f in os.listdir(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks')) if os.path.isfile(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'masks'), f))][i_895AA])])

        return context.window_manager.invoke_props_dialog(self, width=300)
    
class TSV_OT_group_mask_remove(bpy.types.Operator):
    bl_idname = "tsv.group_mask_remove"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if property_exists("bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index]", globals(), locals()):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.remove(node=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(Index) + '_density'], )
            for i_A469F in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) - Index)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(int(i_A469F + Index) + 1.0)) + '_density'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(i_A469F + Index)) + '_density'
            link_53AC1 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(Index) + '_density'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(Index - 1.0)) + '_density'].outputs[0], )
            if len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) > bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index:
                bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks.remove(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index)
            if (len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) == bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index):
                bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_mask_index = int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) - 1.0)

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

classes = [
    TSV_OT_group_mask_add,
    TSV_OT_group_mask_remove
]