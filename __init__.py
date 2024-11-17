MODULE_NAMES = [
    "operators",
    "preferences",
    "ui",
    "properties",
    "utils",
    "helper"
    ]

# Import the modules dynamically
import importlib
MAIN_MODULES = []
for module_name in MODULE_NAMES:
    module = importlib.import_module("." + module_name, __package__)
    MAIN_MODULES.append(module)
    continue

# remove all plugin modules from sys.modules, will load them again, creating an effective hit-reload soluton
def cleanse_modules():
    import sys
    all_modules = sys.modules 
    all_modules = dict(sorted(all_modules.items(),key= lambda x:x[0])) #sort them
    
    for k,v in all_modules.items():
        if k.startswith(__name__):
            del sys.modules[k]

    return None

print(__package__)

#import bpy
#class TSV_AddonPreferences(bpy.types.AddonPreferences):
#    bl_idname = __package__
# 
#    def draw(self, context):
#        self.layout.operator("mesh.add_cube_sample", icon='MESH_CUBE', text="Add Cube")


def register():

    #bpy.utils.register_class(TSV_AddonPreferences)

    try:
        for m in MAIN_MODULES:
            m.register()
            
    # very common user report, previously failed register, then user try to register again, and stumble into the first already registered class
    # we don't want them to report this specific error, it' useless and don't indicate the original error, most of the time we gently ask them to restart their session
    # Note that we could skip a class register if the class is already registered, however the initial activation process shouldn't be faulty at the first place
    
    except Exception as e:        
        if ("register_class(...): already registered as a subclass 'SCATTER5_OT_print_icon_id'" in str(e)):
            raise Exception("\n\nDear User,\nAre you using the correct version of blender with our plugin?\nAn error occured during this activation, it seems that a previous activation failed\nPlease restart blender\n\n")
        raise e
    
    return None

def unregister():

    #bpy.utils.unregister_class(TSV_AddonPreferences)

    for m in reversed(MAIN_MODULES):
        m.unregister()

    # final step, remove modules from sys.modules 
    cleanse_modules()

    return None


if __name__ == "__main__":
    register()