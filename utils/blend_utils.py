import bpy
import os

def tsv_list_blend_content(path: str, data_type: str):
    if os.path.exists(path):
        with bpy.data.libraries.load(path) as (data_from, data_to):
            return getattr(data_from, data_type)
    return []

def append_object(object_name: str, blend_file_path: str):
    bpy.ops.wm.append()