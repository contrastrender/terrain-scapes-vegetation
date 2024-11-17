import bpy

from .. utils.property_utils import property_exists

def sna_remove_layer_3CD98(Index):
    if property_exists("bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index]", globals(), locals()):
        if (None != bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(Index) + '_layer'].inputs['Solid Material'].default_value):
            bpy.data.materials.remove(material=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(Index) + '_layer'].inputs['Solid Material'].default_value, )
        bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.remove(node=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(Index) + '_layer'], )
        for i_6362E in range(int(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers) - Index) - 1.0)):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(int(Index + i_6362E) + 1.0)) + '_layer'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(Index + i_6362E)) + '_layer'
        if len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers) > bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index:
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers.remove(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index)
        if (len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers) == bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index):
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index = int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers) - 1.0)


def sna_remove_biome_06ED5(Index):
    if property_exists("bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index]", globals(), locals()):
        bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.remove(node=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(Index) + '_biome'], )
        for i_40409 in range(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers)):
            sna_remove_layer_3CD98(0)
        for i_A1EA6 in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) + 2.0)):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.remove(node=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(Index) + ',' + str(int(i_A1EA6 - 1.0)) + '_density'], )
        for i_64844 in range(int(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) - Index) - 1.0)):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(int(i_64844 + Index) + 1.0)) + '_biome'].name = str(int(i_64844 + Index)) + '_biome'
            for i_8C52A in range(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(int(i_64844 + Index) + 1.0)].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(int(i_64844 + Index) + 1.0)) + ',' + str(i_8C52A) + '_layer'].name = str(int(i_64844 + Index)) + ',' + str(i_8C52A) + '_layer'
            for i_040CE in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(int(i_64844 + Index) + 1.0)].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(int(i_64844 + Index) + 1.0)) + ',' + str(int(i_040CE - 1.0)) + '_density'].name = str(int(i_64844 + Index)) + ',' + str(int(i_040CE - 1.0)) + '_density'
        bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'].name = str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) - 1.0)) + '_biome'
        link_C9799 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + '_biome'].outputs[0], )
        if len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) > bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index:
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers.remove(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index)
        if (len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) == bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index):
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index = int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) - 1.0)

class TSV_OT_remove_group(bpy.types.Operator):
    bl_idname = "tsv.remove_group"
    bl_label = "Remove"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_remove_biome_06ED5(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_remove_group
]