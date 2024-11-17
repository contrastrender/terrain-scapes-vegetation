import bpy
import os

_item_map = dict()

biome_density_mask__add = {'sna_masks': [], }
load_preset_group = {'sna_missing_assets': [], 'sna_asset_libraries': [], }

def make_enum_item(_id, name, descr, preview_id, uid):
    lookup = str(_id)+"\0"+str(name)+"\0"+str(descr)+"\0"+str(preview_id)+"\0"+str(uid)
    if not lookup in _item_map:
        _item_map[lookup] = (_id, name, descr, preview_id, uid)
    return _item_map[lookup]

def load_preview_icon(path):
    global _icons
    if not path in _icons:
        if os.path.exists(path):
            _icons.load(path, path, "IMAGE")
        else:
            return 0
    return _icons[path].icon_id

def sna_tsv_masks_enum_items(self, context):
    enum_items = biome_density_mask__add['sna_masks']
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]

def sna_tsv_searchable_asset_libraries_enum_items(self, context):
    enum_items = load_preset_group['sna_asset_libraries']
    return [make_enum_item(item[0], item[1], item[2], item[3], 2**i) for i, item in enumerate(enum_items)]

def sna_tsv_layer_low_poly_objects_enum_items(self, context):
    enum_items = [['TSV_low_poly_object_1', 'TSV_low_poly_object_1', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_1.png'))], ['TSV_low_poly_object_2', 'TSV_low_poly_object_2', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_2.png'))], ['TSV_low_poly_object_3', 'TSV_low_poly_object_3', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_3.png'))], ['TSV_low_poly_object_4', 'TSV_low_poly_object_4', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_4.png'))], ['TSV_low_poly_object_5', 'TSV_low_poly_object_5', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_5.png'))], ['TSV_low_poly_object_6', 'TSV_low_poly_object_6', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_6.png'))], ['TSV_low_poly_object_7', 'TSV_low_poly_object_7', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_7.png'))], ['TSV_low_poly_object_8', 'TSV_low_poly_object_8', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_8.png'))], ['TSV_low_poly_object_9', 'TSV_low_poly_object_9', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_9.png'))], ['TSV_low_poly_object_10', 'TSV_low_poly_object_10', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_10.png'))], ['TSV_low_poly_object_11', 'TSV_low_poly_object_11', '', load_preview_icon(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__), 'assets', 'terrain_scapes_vegetation'),'low_poly_objects'),'TSV_low_poly_object_11.png'))]]
    return [make_enum_item(item[0], item[1], item[2], item[3], i) for i, item in enumerate(enum_items)]

def sna_update_viewport_display_516D8(self, context):
    sna_updated_prop = self.viewport_display
    bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index) + '_layer'].inputs[10].default_value = sna_updated_prop
    if (('' != bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index].low_poly_objects) and ('Low Poly' == sna_updated_prop)):
        bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index) + '_layer'].inputs[11].default_value = bpy.data.objects[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index].low_poly_objects]

def sna_update_low_poly_objects_4322F(self, context):
    sna_updated_prop = self.low_poly_objects
    bpy.context.scene.sna_tsv_emitter.modifiers['vegetation'].node_group.nodes[str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index) + ',' + str(bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layers[bpy.context.scene.sna_tsv_emitter.sna_tsv_group_layer_index].layer_index) + '_layer'].inputs[11].default_value = bpy.data.objects[sna_updated_prop]


class SNA_GROUP_sna_tsv_mask(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    texture: bpy.props.StringProperty(name='Texture', description='', default='', subtype='NONE', maxlen=0)


class SNA_GROUP_sna_tsv_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    viewport_display: bpy.props.EnumProperty(name='Viewport Display', description='', items=[('Bounding Box', 'Bounding Box', '', 0, 0), ('Object', 'Object', '', 0, 1), ('Low Poly', 'Low Poly', '', 0, 2)], update=sna_update_viewport_display_516D8)
    low_poly_objects: bpy.props.EnumProperty(name='Low Poly Objects', description='', items=sna_tsv_layer_low_poly_objects_enum_items, update=sna_update_low_poly_objects_4322F)

class SNA_GROUP_sna_tsv_group_layer(bpy.types.PropertyGroup):
    label: bpy.props.StringProperty(name='Label', description='', default='', subtype='NONE', maxlen=0)
    layers: bpy.props.CollectionProperty(name='Layers', description='', type=SNA_GROUP_sna_tsv_layer)
    layer_index: bpy.props.IntProperty(name='Layer Index', description='', default=0, subtype='NONE')
    density_masks: bpy.props.CollectionProperty(name='Density Masks', description='', type=SNA_GROUP_sna_tsv_mask)
    density_mask_index: bpy.props.IntProperty(name='Density Mask Index', description='', default=0, subtype='NONE')

#from . import module

classes  =  [
    SNA_GROUP_sna_tsv_mask,
    SNA_GROUP_sna_tsv_layer,
    SNA_GROUP_sna_tsv_group_layer
]
#classes += module.classes

def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.sna_tsv_emitter = bpy.props.PointerProperty(name='TSV_emitter', description='', type=bpy.types.Object)
    bpy.types.Object.sna_tsv_group_layers = bpy.props.CollectionProperty(name='TSV_group_layers', description='', type=SNA_GROUP_sna_tsv_group_layer)
    bpy.types.Object.sna_tsv_group_layer_index = bpy.props.IntProperty(name='TSV_group_layer_index', description='', default=0, subtype='NONE')
    bpy.types.Scene.sna_tsv_masks = bpy.props.EnumProperty(name='TSV_masks', description='', items=sna_tsv_masks_enum_items)
    bpy.types.Scene.sna_tsv_expand_density = bpy.props.BoolProperty(name='TSV_expand_density', description='', default=False)
    bpy.types.Scene.sna_tsv_expand_layers = bpy.props.BoolProperty(name='TSV_expand_layers', description='', default=False)
    bpy.types.Scene.sna_tsv_searchable_asset_libraries = bpy.props.EnumProperty(name='TSV_searchable_asset_libraries', description='', items=sna_tsv_searchable_asset_libraries_enum_items, options={'ENUM_FLAG'})
    bpy.types.Scene.sna_tsv_expand_preset_layers = bpy.props.BoolProperty(name='TSV_expand_preset_layers', description='', default=False)

    return 


def unregister():

    del bpy.types.Scene.sna_tsv_expand_preset_layers
    del bpy.types.Scene.sna_tsv_searchable_asset_libraries
    del bpy.types.Scene.sna_tsv_expand_layers
    del bpy.types.Scene.sna_tsv_expand_density
    del bpy.types.Scene.sna_tsv_masks
    del bpy.types.Object.sna_tsv_group_layer_index
    del bpy.types.Object.sna_tsv_group_layers
    del bpy.types.Scene.sna_tsv_emitter

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
        
    return