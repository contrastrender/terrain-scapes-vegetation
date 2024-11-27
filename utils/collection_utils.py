import bpy

def tsv_collection_move_up(collection_prop: bpy.types.CollectionProperty, index_prop: bpy.types.IntProperty):

    # Check if index is not first and index in collection
    if index_prop > 0 and tsv_index_in_collection(collection_prop, index_prop):
        collection_prop.move(index_prop, index_prop-1)
        index_prop -= 1

def tsv_collection_move_down(collection_prop: bpy.types.CollectionProperty, index_prop: bpy.types.IntProperty):
    # Check if index is not first and index in collection
    if index_prop < len(collection_prop) - 1:
        collection_prop.move(index_prop, index_prop + 1)
        index_prop += 1

def tsv_collection_remove(collection_prop: bpy.types.CollectionProperty, index_prop: bpy.types.IntProperty):

    # Check if index is in collection
    if tsv_index_in_collection(collection_prop, index_prop):
        collection_prop.remove(index_prop)
        if not tsv_index_in_collection(collection_prop, index_prop):
            index_prop -= 1

def tsv_collection_add(collection_prop: bpy.types.CollectionProperty, index_prop: bpy.types.IntProperty) -> bpy.types.PropertyGroup:
    collection_item = collection_prop.add()
    index_prop = len(collection_prop) - 1
    return collection_item

def tsv_index_in_collection(collection_prop: bpy.types.CollectionProperty, index_prop: bpy.types.IntProperty) -> bool:
    return len(collection_prop) > index_prop