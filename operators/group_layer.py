import bpy

from .. const import PACKAGE

from .. utils.integer_utils import random_integer
from .. utils.color_utils import random_color
from .. helper.group_layer_helper import sna_append_low_poly_objects_8DF63
from .. utils.property_utils import property_exists

def add_group_layer(label):
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
    
    return node_BFB5F



class TSV_OT_group_layer_add_from_selection(bpy.types.Operator):
    bl_idname = "tsv.group_layer_add_from_selection"
    bl_label = "Add Layer"
    bl_description = "Adds scattering layer using the active object"
    bl_options = {"UNDO"}

    density_items = [
        ("","extremly low", "for large rock formations"),
        ("","low", ""),
        ("","mid", ""),
        ("","high", ""),
        ("","extremly high", ""),
    ]

    density_enum: bpy.props.EnumProperty(name='directory', description='', default='', items=density_items) #type: ignore

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        ac_ob = bpy.context.active_object

        if ac_ob is not None and ac_ob is not bpy.context.scene.tsv_emitter:
            layer_node = add_group_layer(ac_ob.name)
            layer_node.inputs[7].default_value = ac_ob
            sna_append_low_poly_objects_8DF63()

        return {"FINISHED"}

    def draw(self, context):
        col = self.layout.column()
        box = col.box()

        ac_ob = bpy.context.active_object
        if ac_ob is None:
            box.label(text = "No active object to scatter")
        elif ac_ob is bpy.context.scene.tsv_emitter:
            box.label(text = "Cant scatter emitter object")
        else:
            box.label(text = ac_ob.name)
            row = col.row()
            row.prop(self, "density_enum", expand=True)

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
                append_asset(bpy.context.asset.name, bpy.context.asset.full_library_path)
                sna_append_low_poly_objects_8DF63()
                layer_node = add_group_layer(bpy.context.asset.name)
                layer_node.inputs[7].default_value = bpy.data.objects[bpy.context.asset.name]
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)
    
def append_asset(asset_name, asset_path):
    if bpy.data.collections.get("vegetation_assets") is None:
        collection = bpy.data.collections.new(name='vegetation_assets', )
        bpy.context.scene.collection.children.link(child=collection, )
        collection.hide_render = True
        collection.hide_viewport = True
    
    if bpy.data.objects.get(asset_name) is None:
        existing_objects = list(bpy.data.objects)

        # Append the new asset
        bpy.ops.wm.append(directory=asset_path + r'\Object', filename=asset_name, link=False)

        # Determine which object was appended by filtering out the existing ones
        new_objects = [obj for obj in bpy.data.objects if obj not in existing_objects]
        appended_object = new_objects[0] if new_objects else None

        if appended_object:
            # Unlink the appended object from all its current collections
            for collection in appended_object.users_collection:
                collection.objects.unlink(appended_object)

            # Link the appended object to the 'vegetation_assets' collection
            vegetation_assets_collection = bpy.data.collections.get('vegetation_assets')
            if vegetation_assets_collection:
                vegetation_assets_collection.objects.link(appended_object)
            else:
                raise ValueError("Collection 'vegetation_assets' does not exist.")


classes = [
    TSV_OT_group_layer_add_from_selection,
    TSV_OT_group_layer_remove,
    TSV_OT_group_layer_add_from_asset_browser
]