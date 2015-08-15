import re

templateDict = {
	"root": {
		"csharp": {
			"typeMap": {
				"bool": {
					"name": "bool",
					"defaultInit": "true"
				},
				"int": {
					"name": "int",
					"defaultInit": "0"
				},
				"double": {
					"name": "double",
					"defaultInit": "0.0"
				},
				"long": {
					"name": "long",
					"defaultInit": "0"
				},
				"float": {
					"name": "float",
					"defaultInit": "0.0"
				},
				"string": {
					"name": "string",
					"defaultInit": "string.Empty"
				},
				"date": {
					"name": "DateTime",
					"defaultInit": "DateTime.Now"
				},
				"object": {
					"name": "{{type_name}}",
					"defaultInit": "new {{type_name}}()"
				}
			},			
			"class": {
				"base": "public {{class_name}}{{optional_class_inherit}}\n{\n{{scaf_prop}}\n{{scaf_method}}}",
				"base_inherits": ": {{inherits}}",
				"prop": "\t{{prop_access}} {{prop_type}} {{prop_name}} { get; set; }\n",
				"method": "\t{{method_access}} {{method_return_type}} {{method_name}}({{scaf_param}})\n\t{\n\t\t\n\t}\n\n",
				"method_param_head": "{{param_type}} {{param_name}}",
				"method_param_tail": ", {{param_type}} {{param_name}}"
			},
			"enum": {
				"base": "{{enum_access}} enum {{enum_name}}\n{\n{{scaf_enum_options}}}\n",
				"option_no_value": "{{option_name}},\n",
				"option_with_value": "\t{{option_name}} = {{option_value}},\n"
			},
			"struct": {
				
			},
			"interface": {
				
			}
			
		},
		"python": {
			"class": {
				"base": "class {{class_name}}{{optional_class_inherit}}:\n\n\tdef __init__(self):\n{{scaf_prop}}\n{{scaf_method}}",
				"base_inherits": "({{inherits}})",
				"prop": "\t\tself.{{prop_name}} = None\n",
				"method": "\tdef {{method_name}}(self{{scaf_param}}):\n\t\tpass\n\n",
				"method_param_head": ", {{param_name}}",
				"method_param_tail": ", {{param_name}}"
			},
			"enum": {
				"base": "class {{enum_name}}(Enum):\n{{scaf_enum_options}}}\n",
				"option_no_value": "{{option_name}},\n",
				"option_with_value": "\t{{option_name}} = {{option_value}}\n"
			},
			"struct": {
			},
			"interface": {
			}
		},
		"php": {
		    "class": {
		        "base":"class {{class_name}}{{optional_class_inherit}}\n{\n{{scaf_prop}}\n{{scaf_method}}\n}",
		        "base_inherits":" extends {{inherits}}",
		        "prop":"\t{{prop_access}} ${{prop_name}} = {{prop_value}};\n",
		        "method":"\t{{method_access}} function {{method_name}}({{scaf_param}}) {\n\t\t\n\t}\n",
		        "method_param_head":"${{param_name}}",
		        "method_param_tail":", ${{param_name}}"
		    }
		},
		"objc": {
		    "typeMap": {
				"bool": {
					"name": "bool",
					"defaultInit": "YES"
				},
				"int": {
					"name": "NSNumber",
					"defaultInit": "0"
				},
				"double": {
					"name": "NSNumber",
					"defaultInit": "0.0"
				},
				"long": {
					"name": "NSNumber",
					"defaultInit": "0"
				},
				"float": {
					"name": "NSNumber",
					"defaultInit": "0.0"
				},
				"string": {
					"name": "NSString",
					"defaultInit": "string.Empty"
				},
				"date": {
					"name": "NSDate",
					"defaultInit": "DateTime.Now"
				},
				"object": {
					"name": "{{type_name}}",
					"defaultInit": "new {{type_name}}()"
				}
			},	
			"class": {
				"base": "@interface {{class_name}} : {{optional_class_inherit}} {\n\n}\n\n{{scaf_prop}}\n{{scaf_method}}\n\n@end\n",
				"base_inherits": "{{inherits}}",
				"prop": "@property (copy) {{prop_type}} *{{prop_name}};\n",
				"method": "-({{method_return_type}}*){{method_name}}{{scaf_param}};\n",
				"method_param_head": ": ({{param_type}}){{param_name}}",
				"method_param_tail": " {{param_name}}:({{param_type}}){{param_name}}"
			},
			"blah": {
				"base": "@implementation {{class_name}} {\n\n\tdef __init__(self):\n{{scaf_prop}}\n{{scaf_method}}",
				"base_inherits": "({{inherits}})",
				"prop": "\t\tself.{{prop_name}} = None\n",
				"method": "\tdef {{method_name}}(self{{scaf_param}}):\n\t\tpass\n\n",
				"method_param_head": ", {{param_name}}",
				"method_param_tail": ", {{param_name}}"
			},
			"enum": {
				"base": "typedef enum {{enum_name}} {\n{{scaf_enum_options}}} {{enum_name}};\n",
				"option_no_value": "k{{option_name}},\n",
				"option_with_value": "\tk{{option_name}} = {{option_value}}\n"
			},
			"struct": {
			},
			"interface": {
			}
		}
	}
}




meta = {
  "root": {
    "enum": {
      "access": "public",
      "name": "BodyTypes",
      "options": [
        {
          "name": "Small",
          "value": "0"
        },
        {
          "name": "Medium",
          "value": "1"
        },
        {
          "name": "Big",
          "value": "2"
        }
      ]
    },
    "interface": {
      "name": "IBusiness",
      "methods": [{
        "name": "CreateDumbThing",
        "access": "public",
        "returnType": "void",
        "parameters": [
          {
            "name": "dumbThing",
            "type": "int"
          },
          {
            "name": "dumbThing2",
            "type": "float"
          }
        ]
      }]
    },
    "class": {
      "name": "Bear",
      "inherits": "Animal",
      "properties": [
        {
          "name": "Height",
          "type": "int",
          "access": "public"
        },
        {
          "name": "Weight",
          "type": "string",
          "access": "public"
        }
      ],
      "methods": [
          {
        "access": "public",
        "name": "CreateBear",
        "static": "true",
        "returnType": "Bear",
        "parameters": [
          {
            "name": "bearsName",
            "type": "string"
          },
          {
            "name": "type",
            "type": "BearType"
          }
        ]
      }
      ]
    },
  }
}

def LoadTemplate(language, dict):
    if language in dict["root"]:
        return dict["root"][language]

#pseudo
#        self.class_t = "Class {{class_name}}\n-----------\n\n\tProperties:\n\t-----------\n{{scaf_prop}}\n\n\tMethods:\n\t-----------\n{{scaf_method}}"
#        self.prop_t = "\t- {{prop_name}}\n"
#        self.method_t = "\t- {{method_name}}\n"

        
#tokens = re.findall('{{.*?}}', text.class_t)

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

    method_text = BuildMethods(tmp, dict["methods"], typeMap)
    text = text.replace("{{scaf_method}}", method_text)

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
    
def BuildMethods(tmp, dict, typeTmp):
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














language = "objc"
result = ""

template = LoadTemplate(language, templateDict)

for objType in meta["root"]:
    objContents = meta["root"][objType]
    
    if objType == 'class':
        result += BuildClass(template, objContents)
#    elif objType == 'interface':
#        result += BuildInterface(template, objContents)
    elif objType == 'enum':
        result += BuildEnum(template, objContents)
        
    result += "\n"
        
print(result)

