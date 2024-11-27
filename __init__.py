MODULE_NAMES = [
    "operators",
    "preferences",
    "ui",
    "properties",
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



def register():

    for m in MAIN_MODULES:
        m.register() 
    
    return None

def unregister():

    for m in reversed(MAIN_MODULES):
        m.unregister()

    # remove modules from sys.modules 
    cleanse_modules()

    return None