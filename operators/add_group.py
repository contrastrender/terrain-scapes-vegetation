import bpy

def sna_add_group_46FA8(label):
    bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'].name = str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) + 1.0)) + '_biome'
    node_F3D6B = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.new(type='GeometryNodeGroup', )
    node_F3D6B.node_tree = bpy.data.node_groups['.TSV_biome']
    node_F3D6B.name = str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'
    link_18D60 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'].inputs[1], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes['system'].outputs[0], )
    link_94E16 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) - 1.0)) + '_biome'].outputs[0], )
    link_5498A = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) + 1.0)) + '_biome'].inputs[0], output=bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + '_biome'].outputs[0], )
    node_7F85E = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.new(type='ShaderNodeValue', )
    node_7F85E.outputs[0].default_value = 1.0
    node_7F85E.name = str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + ',-1' + '_density'
    node_C629E = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes.new(type='NodeReroute', )
    node_C629E.name = str(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers)) + ',0' + '_density'
    link_79980 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=node_C629E.inputs[0], output=node_7F85E.outputs[0], )
    link_9D209 = bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.links.new(input=node_F3D6B.inputs[5], output=node_C629E.outputs[0], )
    item_6D1A0 = bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers.add()
    item_6D1A0.label = label
    bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index = int(len(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers) - 1.0)

class TSV_OT_add_group(bpy.types.Operator):
    bl_idname = "tsv.add_group"
    bl_label = "Add"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        sna_add_group_46FA8('group')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
classes = [
    TSV_OT_add_group
]