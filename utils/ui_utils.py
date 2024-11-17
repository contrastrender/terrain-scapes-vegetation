def sna_display_inputs_from_67553(layout_function, inputs, from_input):
    col_BB9D5 = layout_function.column(heading='', align=False)
    col_BB9D5.alert = False
    col_BB9D5.enabled = True
    col_BB9D5.active = True
    col_BB9D5.use_property_split = True
    col_BB9D5.use_property_decorate = False
    col_BB9D5.scale_x = 1.0
    col_BB9D5.scale_y = 1.0
    col_BB9D5.alignment = 'Expand'.upper()
    col_BB9D5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
    for i_1C254 in range(len(inputs)):
        if inputs[i_1C254].hide_value:
            pass
        else:
            if (i_1C254 >= from_input):
                col_BB9D5.prop(inputs[i_1C254], 'default_value', text=inputs[i_1C254].name, icon_value=0, emboss=True)

classes = [
    
]