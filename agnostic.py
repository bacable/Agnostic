import sys, re, os, json, getopt

def LoadTemplate(jsonFile):
    with open(jsonFile) as data_file:
        data = json.load(data_file)
    return data
    
def LoadStructure(jsonFile):
    with open(jsonFile) as data_file:
        data = json.load(data_file)
    return data

def BuildClass(template, dict):
    if "class" not in template:
        return ""
        
    tmp = template["class"]
    
    SetTypeMap(template)

    text = tmp["base"].replace("{{class_name}}", dict["name"])
    
    inherit_text = tmp["base_inherits"].replace("{{inherits}}", dict["inherits"]) if "inherits" in dict else ""
    text = text.replace("{{optional_class_inherit}}", inherit_text)
    
    prop_text = BuildProperties(tmp, dict["properties"])
    text = text.replace("{{scaf_prop}}", prop_text)

    method_text = BuildMethods(tmp, dict["methods"])
    text = text.replace("{{scaf_method}}", method_text)

    return text

#Build and return struct string based on the template
def BuildStruct(template, dict):
    if "struct" not in template:
        return ""
        
    tmp = template["struct"]
    
    SetTypeMap(template)
    
    text = tmp["base"].replace("{{struct_access}}", dict["access"])
    text = text.replace("{{struct_name}}", dict["name"])
    
    prop_text = BuildProperties(tmp, dict["properties"])
    text = text.replace("{{scaf_struct_props}}", prop_text);
    
    return text
    
def BuildInterface(template, dict):
    if "interface" not in template:
        return ""
    
    tmp = template["interface"]
    
    SetTypeMap(template)
    
    text = tmp["base"].replace("{{interface_name}}", dict["name"])
    
    inherit_text = tmp["base_inherits"].replace("{{inherits}}", dict["inherits"]) if "inherits" in dict else ""

    prop_text = BuildProperties(tmp, dict["properties"]) if "properties" in dict else ""
    
    text = text.replace("{{scaf_interface_props}}", prop_text)
    
    method_text = BuildMethods(tmp, dict["methods"]) if "methods" in dict else ""
    
    text = text.replace("{{scaf_interface_methods}}", method_text)
    
    return text

def BuildProperties(tmp, dict):
    if "prop" not in tmp:
        return ""
    
    result = ""
    for prop in dict:
        text = tmp["prop"]
        text = text.replace("{{prop_access}}",prop["access"])
        
        propType = GetTypeProperty(prop["type"], "name")
        
        text = text.replace("{{prop_type}}", propType)
        text = text.replace("{{prop_name}}", prop["name"])
        result += text
    return result
    
def BuildMethods(tmp, dict):
    if "method" not in tmp:
        return ""
    
    result = ""
    for method in dict:
        text = tmp["method"]
        text = text.replace("{{method_access}}", method["access"])
        returnType = GetTypeProperty(method["returnType"], "name")
        text = text.replace("{{method_return_type}}", returnType)
        text = text.replace("{{method_name}}", method["name"])
        param_text = BuildMethodParams(tmp, method["parameters"])
        text = text.replace("{{scaf_param}}", param_text)
        result += text
    return result

def BuildMethodParams(tmp, dict):
    if "method_param_head" not in tmp or "method_param_tail" not in tmp:
        return ""
    
    result = ""
    first = True
    for param in dict:
        
        if first:
            first = False
            text = tmp["method_param_head"]
        else:
            text = tmp["method_param_tail"]
        
        paramType = GetTypeProperty(param["type"], "name")
        text = text.replace("{{param_type}}", paramType)
        text = text.replace("{{param_name}}", param["name"])
        result += text
        
    return result
    
def BuildEnum(template, dict):
    if "enum" not in template:
        return ""
    
    tmp = template["enum"]
        
    text = tmp["base"].replace("{{enum_access}}", dict["access"])
    text = text.replace("{{enum_name}}", dict["name"])
    enum_option_text = BuildEnumOptions(tmp, dict["options"])
    text = text.replace("{{scaf_enum_options}}", enum_option_text)
    return text

def BuildEnumOptions(tmp, dictOptions):
    if "option_no_value" not in tmp or "option_with_value" not in tmp:
        return ""
    
    result = ""
    for option in dictOptions:
        text = tmp["option_no_value"]
        if "value" in option:
            text = tmp["option_with_value"]
            text = text.replace("{{option_value}}", option["value"])
        text = text.replace("{{option_name}}", option["name"])
        result += text
    return result


typeMap = None
def SetTypeMap(template):
    if "typeMap" in template:
        typeMap = template["typeMap"]
    else:
        None
    

def GetTypeProperty(type, propertyName):

    global typeMap

    if typeMap is not None and type in typeMap:

        typeProps = typeMap[type]
        
        if propertyName in typeProps:
            
            return typeProps[propertyName]
    
    # if they wanted the name of the property, return
    # type, which is the default/most common value
    # otherwise, we don't want to display anything
    if propertyName == "name":
        return type
    else:
        return ""







class AgnosticScaffolder:
    
    def __init__(self, configfile, structurefile, templatefile, outputfolder):
        
        currentPath = os.path.dirname(os.path.abspath(__file__))

        structurePath = os.path.join(currentPath, "structure")
        structureFilename = os.path.join(structurePath, structurefile)
        structure = LoadStructure(structureFilename)

        templatePath = os.path.join(currentPath, "templates")
        templateFilename = os.path.join(templatePath, templatefile)
        template = LoadTemplate(templateFilename)

        result = ""

        for objType in structure["root"]:
            objContents = structure["root"][objType]
    
            if objType == 'class':
                result += BuildClass(template, objContents)
            elif objType == 'interface':
                result += BuildInterface(template, objContents)
            elif objType == 'enum':
                result += BuildEnum(template, objContents)
            elif objType == 'struct':
                result += BuildStruct(template, objContents)
            result += "\n"
        
        print(result)


def main(argv):
    structurefile = ""
    templatefile = ""
    configfile = ""
    outputfolder = ""
    
    try:
        opts, args = getopt.getopt(argv, "s:t:c:o:", ["structure", "template", "config", "ouput"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-s", "--structure"):
            structurefile = arg
        elif opt in ("-t", "--template"):
            templatefile = arg
        elif opt in ("-c", "--config"):
            configfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
            
    a = AgnosticScaffolder(configfile, structurefile, templatefile, outputfolder)
            
if __name__ == "__main__":
    main(sys.argv[1:])