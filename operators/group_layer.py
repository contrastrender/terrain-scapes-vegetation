import bpy

from .. const import PACKAGE

from .. utils.integer_utils import random_integer
from .. utils.color_utils import random_color
from .. helper.group_layer_helper import sna_append_low_poly_objects_8DF63
from .. utils.property_utils import property_exists

def sna_add_layer_31A03(label):
    # Get references for better readability
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    vegetation_node_group = tsv_emitter.modifiers['vegetation'].node_group
    group_index = tsv_emitter.tsv_group_index
    group = tsv_emitter.tsv_groups[group_index]

    # Create layer name based on the group index and number of layers
    layer_name = f"{group_index},{len(group.layers)}_layer"
    
    # Create a new Geometry Node
    node_BFB5F = vegetation_node_group.nodes.new(type='GeometryNodeGroup')
    node_BFB5F.node_tree = bpy.data.node_groups['.TSV_layer']
    node_BFB5F.name = layer_name
    
    # Create a new material with a random color
    material_72B75 = bpy.data.materials.new(name='Layer_Material')
    material_72B75.diffuse_color = (*random_color(False, None, None)[0:3], 1.0)  # Fix here, add arguments as in original code
    node_BFB5F.inputs['Solid Material'].default_value = material_72B75

    # Define node names for cleaner linking
    input_node = vegetation_node_group.nodes[layer_name]
    group_input_node = vegetation_node_group.nodes['Group Input']
    join_geometry_node = vegetation_node_group.nodes['Join Geometry']
    biome_node = vegetation_node_group.nodes[f"{group_index}_biome"]
    system_node = vegetation_node_group.nodes['system']
    
    # Link nodes
    vegetation_node_group.links.new(input=input_node.inputs[0], output=group_input_node.outputs[0])
    vegetation_node_group.links.new(input=join_geometry_node.inputs[0], output=input_node.outputs[0])
    vegetation_node_group.links.new(input=input_node.inputs[3], output=biome_node.outputs[1])
    vegetation_node_group.links.new(input=input_node.inputs[4], output=biome_node.outputs[2])
    vegetation_node_group.links.new(input=input_node.inputs[1], output=system_node.outputs[1])
    vegetation_node_group.links.new(input=input_node.inputs[2], output=system_node.outputs[2])
    
    # Set a random integer input value
    input_node.inputs[8].default_value = random_integer(0.0, 10000.0, None)
    
    # Add the layer to the TSV group and update the layer index
    new_layer = group.layers.add()
    new_layer.label = label
    group.layer_index = len(group.layers) - 1  # Set to the last layer index
    
    return layer_name



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
        if (0 == len(bpy.context.selected_objects)):
            box_EFDD4 = col_0E2D5.box()
            box_EFDD4.label(text='No objects selected', icon_value=0)
        else:
            for i_C55A4 in range(len(bpy.context.selected_objects)):
                box_5BA78 = col_0E2D5.box()
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
    # Get necessary references
    scene = bpy.context.scene
    tsv_emitter = scene.tsv_emitter
    node_group = tsv_emitter.modifiers['vegetation'].node_group
    group_index = tsv_emitter.tsv_group_index
    group = tsv_emitter.tsv_groups[group_index]
    
    # Generate the node name for the target layer
    layer_name = f"{group_index},{Index}_layer"
    
    # Check if the property exists before continuing
    if property_exists(f"bpy.context.scene.tsv_emitter.tsv_groups[{group_index}].layers[{group.layer_index}]", globals(), locals()):
        # Retrieve the node based on the generated name
        node = node_group.nodes.get(layer_name)
        
        if node:
            # Remove the material if it exists (only if the 'Solid Material' input is not None)
            solid_material = node.inputs.get('Solid Material')
            if solid_material and solid_material.default_value:
                bpy.data.materials.remove(solid_material.default_value)
            
            # Remove the node from the node group
            node_group.nodes.remove(node)
            
            # Shift the node names for the remaining layers
            for i in range(Index + 1, len(group.layers)):
                new_layer_name = f"{group_index},{i-1}_layer"
                node_to_rename = node_group.nodes.get(f"{group_index},{i}_layer")
                if node_to_rename:
                    node_to_rename.name = new_layer_name
            
            # Remove the layer from the group
            if len(group.layers) > group.layer_index:
                group.layers.remove(group.layer_index)
            
            # Update the layer_index if needed
            if len(group.layers) == group.layer_index:
                group.layer_index = len(group.layers) - 1



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