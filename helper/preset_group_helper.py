import json
import bpy
import os

from .. helper.get_prop_helper import tsv_get_geo_nodes, tsv_get_group, tsv_get_group_index, tsv_get_preset_group, tsv_get_preset_group_index, tsv_get_preset_groups
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
        preset_layer_item = preset_group_item.preset_layers.add()

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
                preset_layer_input_item.type = "VALUE" #define type
                preset_layer_input_item.value = f"{input.default_value}" #define value
            elif input.type == "INT":
                preset_layer_input_item.type = "INT" #define type
                preset_layer_input_item.value = f"{input.default_value}" #define value
            elif input.type == "BOOLEAN":
                preset_layer_input_item.type = "BOOLEAN" #define type
                preset_layer_input_item.value = f"{input.default_value}" #define value
            elif input.type == "MENU":
                preset_layer_input_item.type = "STRING" #define type
                preset_layer_input_item.value = f"{input.default_value}" #define value
            elif input.type == "OBJECT":
                preset_layer_input_item.type = "OBJECT" #define type
                preset_layer_input_item.value = f"{input.default_value.name}" #define value
            else:
                preset_layer_input_item.type = "" #define type
                preset_layer_input_item.value = "" #define value

def tsv_preset_group_remove():
    preset_group = tsv_get_preset_group()

    if preset_group is not None:
        preset_groups = tsv_get_preset_groups()
        preset_group_index = tsv_get_preset_group_index()
        preset_groups.remove(preset_group_index)

def tsv_preset_group_export_to_json(directory: str, json_file_name: str):


    file_path = os.path.join(directory, json_file_name)

    # Get the current preset group
    preset_group = tsv_get_preset_group()
    
    # Check if the group exists
    if preset_group is None:
        print("No preset group available to export.")
        return

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
    None

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
    None

def tsv_preset_group_move_down():
    None

def tsv_preset_group_load():
    None

    if property_exists("preset_group", globals(), locals()):
        if os.path.isdir(directory):
            if (name != ''):
                if property_exists("preset_group", globals(), locals()):
                    export_preset_group['sna_layers'] = ''
                    for i_AC223 in range(len(preset_group.tsv_preset_layers)):
                        export_preset_group['sna_layers'] = export_preset_group['sna_layers'] + preset_group.tsv_preset_layers[i_AC223].label + '|||' + preset_group.tsv_preset_layers[i_AC223].inputs + ('' if (int(len(preset_group.tsv_preset_layers) - 1.0) == i_AC223) else '||||')
                    if os.path.exists(os.path.join(directory,name) + '.txt'):
                        with open(os.path.join(directory,name) + '.txt', mode='w') as file_D3175:
                            file_D3175.seek(0)
                            file_D3175.write(preset_group.label + '|||||' + export_preset_group['sna_layers'])
                            file_D3175.truncate()
                    else:
                        with open(os.path.join(directory,name) + '.txt', mode='a') as file_7C20D:
                            file_7C20D.write(preset_group.label + '|||||' + export_preset_group['sna_layers'])