import os
import bpy

from .. helper.group_layer_helper import tsv_append_scattering_object, tsv_group_layer_add, tsv_group_layer_remove, tsv_search_object_in_asset_libraries

class TSV_OT_group_layer_add_from_selection(bpy.types.Operator):
    bl_idname = "tsv.group_layer_add_from_selection"
    bl_label = "Add Layer"
    bl_description = "Adds scattering layer using the active object"
    bl_options = {"UNDO"}

    density_items = [
        ("LOW","Low (Trees)", ""),
        ("MID","Mid (Bushes)", ""),
        ("HIGH","High (Grass)", ""),
    ]

    density_enum: bpy.props.EnumProperty(items=density_items) #type: ignore

    def execute(self, context):
        #tsv_search_object_in_asset_libraries("Ash_1")
        #return

        ac_ob = bpy.context.active_object
        if ac_ob is not None:
            layer_node = tsv_group_layer_add()
            layer_node.inputs[8].default_value = ac_ob

            if self.density_enum is not None:
                if self.density_enum == "LOW":
                    layer_node.inputs["Density"].default_value = .1
                elif self.density_enum == "MID":
                    layer_node.inputs["Density"].default_value = 1
                elif self.density_enum == "HIGH":
                    layer_node.inputs["Density"].default_value = 10

        return {"FINISHED"}

    def draw(self, context):
        col = self.layout.column()
        col.use_property_split = True
        col.use_property_decorate = False
        box = col.box()

        ac_ob = bpy.context.active_object
        if ac_ob is None:
            box.label(text = "No active object to scatter")
        elif ac_ob is bpy.context.scene.tsv_emitter:
            box.label(text = "Cant scatter emitter object")
        else:
            box.label(text = ac_ob.name)
            col.prop(self, "density_enum", expand=True, text="Density")

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
        tsv_group_layer_remove()
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)

class TSV_OT_group_layer_add_from_asset_browser(bpy.types.Operator):
    bl_idname = "tsv.group_layer_add_from_asset_browser"
    bl_label = "Add from asset browser"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    asset_full_library_path: bpy.props.StringProperty() #type: ignore

    asset_name: bpy.props.StringProperty() #type: ignore

    def execute(self, context):
        appended_asset = tsv_append_scattering_object(self.asset_name, self.asset_full_library_path)
        layer_node = tsv_group_layer_add()
        layer_node.inputs[8].default_value = appended_asset

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


classes = [
    TSV_OT_group_layer_add_from_selection,
    TSV_OT_group_layer_remove,
    TSV_OT_group_layer_add_from_asset_browser
]