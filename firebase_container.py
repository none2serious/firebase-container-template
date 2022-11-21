import numpy as np

def init_from_list(ilist:list, class_name="myclass")->str:
    class_name = "ematxt_user"
    pre = f"class {class_name}(object):\n\tdef__init__(\n\t\tself,\n"
    post = "\t):"
    mid = [f"\t\t{i},\n" for i in ilist]
    fullstr = pre+"".join(mid)+post
    return(fullstr)

def selfdot_from_list(ilist:list, class_name="myclass")->str:
    """
    using class init string, create the self.<var> = <var> 
    text and print it to stdout. cut and paste into __init__()
    """
    return_list = []
    for i in ilist:
        init = f"\t\tself.{i} = {i}\n"
        return_list.append(init)
    return("\n\n"+"".join(return_list))

def todict_from_list(ilist:list,class_name="myclass")->str:
    lines = []
    for i in ilist:
        line = f"'{i}': self.{i}"
        lines.append(line)
    pre = "\n\n\tdef to_dict(self):\n\t\toutdict = {"
    post = "\t\t\t}\n\n\t\treturn(outdict)"
    mid = [f"\t\t\t{line},\n" for line in lines]
    fullstr = pre+"".join(mid)+post
    return(fullstr)

def fromdict_from_list(ilist:list, class_name:str="my_class")->str:
    lines = []
    for i in ilist:
        line = f"\t{i}=source['{i}'],"
        lines.append(line)
    pre = f"\n\n\tdef from_dict(source:dict):\n\t\tnew_{class_name}"+" = {"
    post = "\t\t}\n\n\t\t"+f"return(new_{class_name})"
    mid = [f"\t\t{line}\n" for line in lines]
    fullstr = pre+"".join(mid)+post
    return(fullstr)

def container_class_from_list(varlist:list,
                              object_name="myclass",
                              save_dir=None,
                              usetabs=False,
                              num_spaces=4):
    res_list = []
    pipeline = [init_from_list,
                selfdot_from_list,
                todict_from_list,
                fromdict_from_list]
    for p in pipeline:
        res = p(varlist, class_name=class_name)
        res_list.append(res)
    fullstr = "".join(res_list)
    fullstr = fullstr.replace("{\t","{\n\t")
    
    if usetabs is False:
        fullstr = fullstr.replace('\t', " "*num_spaces)
    
    if save_dir is not None:
        outpath = f"{save_dir}/{object_name}.py"
        with open(outpath, 'w') as f:
            f.write(fullstr)
            print(f"saved class to: {outpath}")
    return(fullstr)