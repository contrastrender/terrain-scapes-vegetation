import bpy

class TSV_OT_move_group_layer_up(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_up"
    bl_label = "Move Group"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (0 < bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].name = '-2_biome'
            for i_B84D5 in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(i_B84D5 - 1.0)) + '_density'].name = '-2' + ',' + str(int(i_B84D5 - 1.0)) + '_density'
            for i_F7112 in range(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(i_F7112) + '_layer'].name = '-2' + ',' + str(i_F7112) + '_layer'
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + '_biome'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'
            for i_D78FD in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + ',' + str(int(i_D78FD - 1.0)) + '_density'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(int(i_D78FD - 1.0)) + '_density'
            for i_13A14 in range(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + ',' + str(i_13A14) + '_layer'].name = str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(i_13A14) + '_layer'
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + '_biome'].name = str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + '_biome'
            for i_7827F in range(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + ',' + str(int(i_7827F - 1.0)) + '_density'].name = str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + ',' + str(int(i_7827F - 1.0)) + '_density'
            for i_B8E77 in range(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + ',' + str(i_B8E77) + '_layer'].name = str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + ',' + str(i_B8E77) + '_layer'
            if (bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index > 2):
                pass
            link_C37F3 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 2.0)) + '_biome'].outputs[0], )
            link_81D79 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)) + '_biome'].outputs[0], )
            link_DF050 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index + 1.0)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + '_biome'].outputs[0], )
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers.move(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index, int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0))
            item_3CFFF = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)]
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index = int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index - 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
class TSV_OT_move_group_layer_down(bpy.types.Operator):
    bl_idname = "tsv.move_group_layer_down"
    bl_label = "Move Biome"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (int(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers) - 1.0) > bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index):
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + '_biome'].name = '-2_Biome'
            for i_9DDDC in range(int(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + ',' + str(int(i_9DDDC - 1.0)) + '_density'].name = '-2' + ',' + str(int(i_9DDDC - 1.0)) + '_density'
            for i_152D6 in range(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + ',' + str(i_152D6) + '_layer'].name = '-2' + ',' + str(i_152D6) + '_layer'
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + '_biome'].name = str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + '_biome'
            for i_68B64 in range(int(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + ',' + str(int(i_68B64 - 1.0)) + '_density'].name = str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + ',' + str(int(i_68B64 - 1.0)) + '_density'
            for i_BC6CA in range(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + ',' + str(i_BC6CA) + '_layer'].name = str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + ',' + str(i_BC6CA) + '_layer'
            bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + '_biome'].name = str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + '_biome'
            for i_99B88 in range(int(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index].density_masks) + 2.0)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + ',' + str(int(i_99B88 - 1.0)) + '_density'].name = str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + ',' + str(int(i_99B88 - 1.0)) + '_density'
            for i_84A15 in range(len(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layers[bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index].layers)):
                bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['-2' + ',' + str(i_84A15) + '_layer'].name = str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + ',' + str(i_84A15) + '_layer'
            link_42708 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index - 1.0)) + '_biome'].outputs[0], )
            link_473C6 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index) + '_biome'].outputs[0], )
            link_96687 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 2.0)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(bpy.context.view_layer.objects.active.sna_tsv_group_layers.sna_tsv_group_layer_index + 1.0)) + '_biome'].outputs[0], )
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers.move(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index, int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index + 1.0))
            item_8FAB8 = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index + 1.0)]
            bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index = int(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index + 1.0)
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_move_group_layer_up,
    TSV_OT_move_group_layer_down
]