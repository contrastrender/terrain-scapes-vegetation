import bpy


def tsv_display_input(layout: bpy.types.UILayout, input):
    col = layout.column()
    col.use_property_split = True
    col.use_property_decorate = False
    if not input.hide_value:
        col.prop(text=input.name, data=input, property="default_value")

def tsv_display_inputs(layout: bpy.types.UILayout, inputs: bpy.types.NodeInputs):
    col = layout.column()
    col.use_property_split = True
    col.use_property_decorate = False
    for input in inputs:
        if not input.hide_value:
            col.prop(text=input.name, data=input, property="default_value")

def tsv_display_inputs_in_range(layout: bpy.types.UILayout, inputs: bpy.types.NodeInputs, min: int, max: int = (2**31 - 1)):
    col = layout.column()
    col.use_property_split = True
    col.use_property_decorate = False
    for i, input in enumerate(inputs):
        if not input.hide_value and min <= i <= max:
            col.prop(text=input.name, data=input, property="default_value")

def tsv_display_warning(layout: bpy.types.UILayout, message: str):
    box = layout.box()
    row = box.row()
    row.label(text=message, icon="ERROR")
