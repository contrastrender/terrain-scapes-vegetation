import json
import bpy
import os

from .. helper.group_layer_helper import tsv_group_layer_add, tsv_search_object_in_asset_libraries
from .. helper.group_helper import tsv_group_add
from .. utils.collection_utils import tsv_collection_move_down, tsv_collection_move_up
from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_group_layer_index, tsv_get_preset_group, tsv_get_preset_group_index, tsv_get_preset_groups
from .. const import __PACKAGE__

def tsv_preset_group_add():

    group = tsv_get_group()

    # Check if active group even exists
    if group is None:
        return None

    # Add preset group item
    preset_groups = tsv_get_preset_groups()
    preset_group_item = preset_groups.add()

    # Set label
    preset_group_item.label = group.label

    # Add Layers
    for i, layer in enumerate(group.layers):
        preset_layer_item = preset_group_item.layers.add()

        # Set layer label
        preset_layer_item.label = layer.label

        # Get Layer Node
        geo_nodes = tsv_get_geo_nodes()
        group_node = geo_nodes.nodes[f"{tsv_get_group_index()}_group"]
        layer_node = group_node.node_tree.nodes[f"{i}_layer"]

        # Add layer inputs
        for input in layer_node.inputs:
            preset_layer_input_item = preset_layer_item.inputs.add()

            # Set inputs depending on their type
            if input.type == "VALUE":
                preset_layer_input_item.type = "VALUE"
                preset_layer_input_item.value = f"{input.default_value}"
            elif input.type == "INT":
                preset_layer_input_item.type = "INT"
                preset_layer_input_item.value = f"{input.default_value}"
            elif input.type == "BOOLEAN":
                preset_layer_input_item.type = "BOOLEAN"
                preset_layer_input_item.value = f"{input.default_value}"
            elif input.type == "MENU":
                preset_layer_input_item.type = "MENU"
                preset_layer_input_item.value = f"{input.default_value}"
            elif input.type == "OBJECT":
                preset_layer_input_item.type = "OBJECT"

                # Check if object even exists
                if input.default_value is not None:
                    preset_layer_input_item.value = f"{input.default_value.name}"
                else:
                    preset_layer_input_item.value = f""

            else:
                preset_layer_input_item.type = ""
                preset_layer_input_item.value = ""

def tsv_preset_group_remove():
    preset_group = tsv_get_preset_group()

    if preset_group is not None:
        preset_groups = tsv_get_preset_groups()
        preset_group_index = tsv_get_preset_group_index()
        preset_groups.remove(preset_group_index)

def tsv_preset_group_export_to_json(directory: str, json_file_name: str):

    # Check if the group exists
    if preset_group is None:
        print("No preset group available to export.")
        return None
    
    if not os.path.exists(directory):
        print("Directory not found")
        return None

    file_path = os.path.join(directory, f"{json_file_name}.json")

    # Get the current preset group
    preset_group = tsv_get_preset_group()

    # Serialize the preset group
    preset_group_json = {
        "label": preset_group.label,
        "preset_layers": []
    }

    for preset_layer_item in preset_group.preset_layers:
        preset_group_layer_json = {
            "label": preset_layer_item.label,
            "inputs": []
        }

        for input_item in preset_layer_item.inputs:
            preset_group_layer_json["inputs"].append({
                "type": input_item.type,
                "value": input_item.value
            })

        preset_group_json["preset_layers"].append(preset_group_layer_json)

    # Write to JSON file
    try:
        with open(file_path, 'w') as json_file:
            json.dump(preset_group_json, json_file, indent=4)
        print(f"Preset group successfully exported to {file_path}")
    except Exception as e:
        print(f"Failed to export preset group: {e}")

def tsv_preset_group_import_from_json(json_preset_group_file_path: str):
    try:
        # Read the JSON file
        with open(json_preset_group_file_path, 'r') as json_file:
            json_preset_group = json.load(json_file)

        # Create a new preset group
        preset_groups = tsv_get_preset_groups()
        preset_group = preset_groups.add()

        # Set group label
        preset_group.label = json_preset_group.get("label", "Unnamed Group")

        # Add layers
        for layer_data in json_preset_group.get("preset_layers", []):
            layer = preset_group.preset_layers.add()
            layer.label = layer_data.get("label", "Unnamed Layer")

            # Add inputs
            for input_data in layer_data.get("inputs", []):
                input = layer.inputs.add()
                input.type = input_data.get("type", "")
                input.value = input_data.get("value", "")

        print(f"Preset group imported successfully from {json_preset_group_file_path}")
        return preset_group

    except FileNotFoundError:
        print(f"File not found: {json_preset_group_file_path}")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in file: {json_preset_group_file_path}")
    except Exception as e:
        print(f"An error occurred during import: {e}")
    None

def tsv_preset_group_move_up():
    preset_groups = tsv_get_preset_groups()
    preset_group_index = tsv_get_preset_group_index()
    tsv_collection_move_up(preset_groups, preset_group_index)

def tsv_preset_group_move_down():
    preset_groups = tsv_get_preset_groups()
    preset_group_index = tsv_get_preset_group_index()
    tsv_collection_move_down(preset_groups, preset_group_index)

def tsv_preset_group_load():

    geo_nodes = tsv_get_geo_nodes()
    preset_group = tsv_get_preset_group()
    
    tsv_group_add()
    group_node = geo_nodes.nodes.get(f"{tsv_get_group_index()}_group")

    for preset_group_layer in preset_group.layers:

        tsv_group_layer_add()
        layer_node = group_node.node_tree.nodes.get(f"{tsv_get_group_layer_index()}_layer")

        for i, preset_group_layer_input in enumerate(preset_group_layer.inputs):

            if preset_group_layer_input.type == "INT":
                layer_node.inputs[i].default_value = int(preset_group_layer_input.value)
            elif preset_group_layer_input.type == "VALUE":
                layer_node.inputs[i].default_value = float(preset_group_layer_input.value)
            elif preset_group_layer_input.type == "BOOLEAN":
                layer_node.inputs[i].default_value = bool(preset_group_layer_input.value)
            elif preset_group_layer_input.type == "MENU":
                layer_node.inputs[i].default_value = str(preset_group_layer_input.value)
            elif preset_group_layer_input.type == "OBJECT":

                object_name = preset_group_layer_input.value
                # Check if object name was saved
                if object_name != "":
                    object = tsv_search_object_in_asset_libraries(object_name)
                    layer_node.inputs[i].default_value = object

            elif preset_group_layer_input.type == "":
                None
