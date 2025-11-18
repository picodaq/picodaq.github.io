import matplotlib.pyplot as plt
import inspect
plt.ion()
from picodaq.errors import DeviceError
    
def showandsave(name, obj):
    savecode(name, obj)
    
    runcode(name, obj)

        
def runcode(name, obj):
    f = plt.figure(figsize=[5, 3])
    f.clf()
    try:
        obj()
    except DeviceError as e:
        print(e)
        plt.close(f)
        return
    
    if f.axes:
        if len(f.axes)==1:
            f.axes[0].set_position([.2,.15, .78, .83])
        f.savefig(f"source/_static/imgs/cookbook/{name}.png", dpi=200)
    else:
        plt.close(f)

        
def savecode(name, obj):      
    src = inspect.getsource(obj)
    lines = src.split("\n")[1:] # split into lines and drop "def" line
    src = "\n".join(line[4:] for line in lines) # remove 4 spaces from start
    src = src.strip() + "\n" # ensure exactly one newline at end
    src = src.replace("##importall", "from picodaq import *")
    with open(f"source/_static/code/cookbook/{name}.py", "w") as fd:
        fd.write(src)
        

def showall(varlist):
    plt.close('all')
    vv = {k: v for k, v in varlist.items()}
    for name, obj in vv.items():
        if name.startswith("recipe_") and callable(obj):
            showandsave(name, obj)
           
