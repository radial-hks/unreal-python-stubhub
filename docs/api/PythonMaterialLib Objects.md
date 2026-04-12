## PythonMaterialLib Objects

```python
class PythonMaterialLib(BlueprintFunctionLibrary)
```

USTRUCT(BlueprintType)
struct My
{
       GENERATED_USTRUCT_BODY()

               UPROPERTY()
               FString SourceName;

       UPROPERTY()
               TWeakObjectPtr<class UPaperTileSet> ImportedTileSet;

       UPROPERTY()
               TWeakObjectPtr<class UTexture> ImportedTexture;

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonMaterialLib.h

<a id="unreal.PythonMaterialLib.set_static_switch_parameter_value"></a>

#### set\_static\_switch\_parameter\_value

```python
@classmethod
def set_static_switch_parameter_value(
        cls,
        material_instance: MaterialInstanceConstant,
        switch_name: str,
        enabled: bool,
        update_static_permutation: bool = True) -> None
```

X.set_static_switch_parameter_value(material_instance, switch_name, enabled, update_static_permutation=True) -> None
Set the Static Switch Infos of material instance

Args:
    material_instance (MaterialInstanceConstant): 
    switch_name (str): The name of static switch.
    enabled (bool): Enabled the switch or not.
    update_static_permutation (bool): Update static permutation or not.

<a id="unreal.PythonMaterialLib.set_static_switch_parameters_values"></a>

#### set\_static\_switch\_parameters\_values

```python
@classmethod
def set_static_switch_parameters_values(
        cls, material_instance: MaterialInstanceConstant,
        switch_names: Array[str], values: Array[bool],
        overrides: Array[bool]) -> None
```

X.set_static_switch_parameters_values(material_instance, switch_names, values, overrides) -> None
Batch set the Static Switch's status of material instance.

Args:
    material_instance (MaterialInstanceConstant): 
    switch_names (Array[str]): The names of each static switches you want to set.
    values (Array[bool]): The bool values of each static switches.
    overrides (Array[bool]): The overrides bool values of each static switches.

<a id="unreal.PythonMaterialLib.set_shading_model"></a>

#### set\_shading\_model

```python
@classmethod
def set_shading_model(cls, material: Material,
                      shading_model_value: int) -> None
```

X.set_shading_model(material, shading_model_value) -> None
Set the shading model of the material, for the hidden shading model
note: added in v1.0.8

Args:
    material (Material): The source material
    shading_model_value (int32): The int value of the EMaterialShadingModel

<a id="unreal.PythonMaterialLib.log_mf"></a>

#### log\_mf

```python
@classmethod
def log_mf(cls, material_function: MaterialFunction) -> None
```

X.log_mf(material_function) -> None
Log out all the connections in the material function
note: added in v1.0.8

Args:
    material_function (MaterialFunction): The source material expression

<a id="unreal.PythonMaterialLib.log_mat_parameters"></a>

#### log\_mat\_parameters

```python
@classmethod
def log_mat_parameters(cls,
                       material_interface: MaterialInterface) -> Array[str]
```

X.log_mat_parameters(material_interface) -> Array[str]
Log Mat Parameters

Args:
    material_interface (MaterialInterface): 

Returns:
    Array[str]:

<a id="unreal.PythonMaterialLib.log_material_expression"></a>

#### log\_material\_expression

```python
@classmethod
def log_material_expression(cls,
                            material_expression: MaterialExpression) -> None
```

X.log_material_expression(material_expression) -> None
Log Detail information of the MaterialExpression, include inputs, outputs etc.
note: added in v1.0.8

Args:
    material_expression (MaterialExpression): The material expression you want to query.

<a id="unreal.PythonMaterialLib.log_mat_deep_first"></a>

#### log\_mat\_deep\_first

```python
@classmethod
def log_mat_deep_first(cls, material_interface: MaterialInterface) -> None
```

X.log_mat_deep_first(material_interface) -> None
Log Mat Deep First

Args:
    material_interface (MaterialInterface):

<a id="unreal.PythonMaterialLib.log_mat"></a>

#### log\_mat

```python
@classmethod
def log_mat(cls, material_interface: MaterialInterface) -> None
```

X.log_mat(material_interface) -> None
Log out all the connections in the material
note: added in v1.0.8

Args:
    material_interface (MaterialInterface): The source material

<a id="unreal.PythonMaterialLib.log_editing_nodes"></a>

#### log\_editing\_nodes

```python
@classmethod
def log_editing_nodes(cls, material_or_mf: Object) -> None
```

X.log_editing_nodes(material_or_mf) -> None
Log Detail information of the Material or Material Function
note: added in v1.0.8

Args:
    material_or_mf (Object): The material or material function you want to query.

<a id="unreal.PythonMaterialLib.get_static_switch_parameter_values"></a>

#### get\_static\_switch\_parameter\_values

```python
@classmethod
def get_static_switch_parameter_values(
        cls, material_interface: MaterialInterface) -> Array[StaticSwitchInfo]
```

X.get_static_switch_parameter_values(material_interface) -> Array[StaticSwitchInfo]
Get the Static Switch Infos of material instance

Args:
    material_interface (MaterialInterface): The material instance you want to query.

Returns:
    Array[StaticSwitchInfo]: 

    out_static_parameters (Array[StaticSwitchInfo]): The result of static switch infos, (StaticSwitchInfo: name, value, override).

<a id="unreal.PythonMaterialLib.get_static_parameters_summary"></a>

#### get\_static\_parameters\_summary

```python
@classmethod
def get_static_parameters_summary(
        cls,
        material_instance: MaterialInstance) -> Tuple[Array[int], Array[str]]
```

X.get_static_parameters_summary(material_instance) -> (out_parameters_count=Array[int32], out_info=Array[str])
Get the numbers of each StaticSwitchParameter of material instance.

Args:
    material_instance (MaterialInstance): 

Returns:
    tuple: 

    out_parameters_count (Array[int32]): The Count of each parameters: [StaticSwitchParameters, StaticComponentMaskParameters, TerrainLayerWeightParameters, MaterialLayersParameters]

    out_info (Array[str]): The name of each parameters.

<a id="unreal.PythonMaterialLib.get_shader_map_info"></a>

#### get\_shader\_map\_info

```python
@classmethod
def get_shader_map_info(cls,
                        material: Material,
                        platform_str: str,
                        detail: bool = False) -> str
```

X.get_shader_map_info(material, platform_str, detail=False) -> str
Get the ShaderMaps infos in string format.
note: added in v1.0.8

Args:
    material (Material): The material you want to query.
    platform_str (str): EShaderPlatform String: PCD3D_SM5, METAL, METAL_MRT, PCD3D_ES3_1, OPENGL_PCES3_1, METAL_SM5, VULKAN_PCES3_1, VULKAN_SM5, VULKAN_ES3_1_ANDROID, METAL_MACES3_1, OPENGL_ES3_1_ANDROID, METAL_MRT_MAC, METAL_TVOS, METAL_MRT_TVOS
    detail (bool): Log Detail ShaderMap or not

Returns:
    str: The ShaderMap info content as JSON

<a id="unreal.PythonMaterialLib.get_selected_nodes_in_material_editor"></a>

#### get\_selected\_nodes\_in\_material\_editor

```python
@classmethod
def get_selected_nodes_in_material_editor(
        cls, material_or_mf: Object) -> Array[MaterialExpression]
```

X.get_selected_nodes_in_material_editor(material_or_mf) -> Array[MaterialExpression]
Get the selected nodes in material editor.
note: The Material Root Node is not included.
note: added in v1.0.8

Args:
    material_or_mf (Object): The material or the material function you want to query.

Returns:
    Array[MaterialExpression]: The selected MaterialExpression nodes.

<a id="unreal.PythonMaterialLib.get_selected_material_nodes"></a>

#### get\_selected\_material\_nodes

```python
@classmethod
def get_selected_material_nodes(
        cls, material: Material) -> Array[MaterialExpression]
```

X.get_selected_material_nodes(material) -> Array[MaterialExpression]
Get the selected nodes in material editor.
note: Use this function in OnMaterialEditorMenu in MenuConfig.ini, the asset path of the material will be passed automatic.
note: For example: unreal.PythonMaterialLib.get_selected_nodes_in_material_editor(unreal.load_asset(%asset_paths[0]))
note: added in v1.0.8

Args:
    material (Material): The editing material

Returns:
    Array[MaterialExpression]: 

    out_expressions (Array[MaterialExpression]):

<a id="unreal.PythonMaterialLib.get_mf_static_switch_parameter"></a>

#### get\_mf\_static\_switch\_parameter

```python
@classmethod
def get_mf_static_switch_parameter(
        cls, material_function: MaterialFunction) -> Array[StaticSwitchInfo]
```

X.get_mf_static_switch_parameter(material_function) -> Array[StaticSwitchInfo]
Get the Static Switch Infos of material function.

Args:
    material_function (MaterialFunction): The material function you want to query.

Returns:
    Array[StaticSwitchInfo]: 

    out_static_parameters (Array[StaticSwitchInfo]): The result of static switch infos, (StaticSwitchInfo: name, value, override).

<a id="unreal.PythonMaterialLib.get_material_proper_str_from_guid"></a>

#### get\_material\_proper\_str\_from\_guid

```python
@classmethod
def get_material_proper_str_from_guid(cls, guid: Guid) -> str
```

X.get_material_proper_str_from_guid(guid) -> str
Get EMaterialProperty in string format from a guid
note: It's a python version of FMaterialAttributeDefinitionMap::GetProperty(guid)
note: added in v1.0.8

Args:
    guid (Guid): The Guid which used in AttributeGetTypes/AttributeSetTypes

Returns:
    str: EMaterialProperty value in string

<a id="unreal.PythonMaterialLib.get_material_function_output_expressions"></a>

#### get\_material\_function\_output\_expressions

```python
@classmethod
def get_material_function_output_expressions(
    cls, material_function: MaterialFunction
) -> Array[MaterialExpressionFunctionOutput]
```

X.get_material_function_output_expressions(material_function) -> Array[MaterialExpressionFunctionOutput]
Get all the output expressions in the Material Function
note: added in v1.0.8

Args:
    material_function (MaterialFunction): The source material expression

Returns:
    Array[MaterialExpressionFunctionOutput]: 

    output_expressions (Array[MaterialExpressionFunctionOutput]):

<a id="unreal.PythonMaterialLib.get_material_function_expressions"></a>

#### get\_material\_function\_expressions

```python
@classmethod
def get_material_function_expressions(
        cls,
        material_function: MaterialFunction,
        recursive: bool = False) -> Array[MaterialExpression]
```

X.get_material_function_expressions(material_function, recursive=False) -> Array[MaterialExpression]
Get all the expressions in the Material Function
note: added in v1.0.8

Args:
    material_function (MaterialFunction): The source material expression
    recursive (bool): Recursive or not

Returns:
    Array[MaterialExpression]: 

    out_expressions (Array[MaterialExpression]):

<a id="unreal.PythonMaterialLib.get_material_function_content"></a>

#### get\_material\_function\_content

```python
@classmethod
def get_material_function_content(cls,
                                  material_function: MaterialFunction,
                                  only_editable: bool = True,
                                  include_comments: bool = False) -> str
```

X.get_material_function_content(material_function, only_editable=True, include_comments=False) -> str
Get the material function's content in JSON Format
note: added in v1.0.8

Args:
    material_function (MaterialFunction): The material function you want to query.
    only_editable (bool): Get the Editable properties only or not.
    include_comments (bool): Include the Comments in Material Editor's graph or not.

Returns:
    str: The material's content in JSON Format

<a id="unreal.PythonMaterialLib.get_material_function_connections"></a>

#### get\_material\_function\_connections

```python
@classmethod
def get_material_function_connections(
        cls, material_function: MaterialFunction
) -> Array[TAPythonMaterialConnection]
```

X.get_material_function_connections(material_function) -> Array[TAPythonMaterialConnection]
Get all the connections in the material function
note: added in v1.0.8

Args:
    material_function (MaterialFunction): The source material function

Returns:
    Array[TAPythonMaterialConnection]: The connections

<a id="unreal.PythonMaterialLib.get_material_expressions"></a>

#### get\_material\_expressions

```python
@classmethod
def get_material_expressions(
        cls,
        material_interface: MaterialInterface) -> Array[MaterialExpression]
```

X.get_material_expressions(material_interface) -> Array[MaterialExpression]
Log out all the Material Expressions in the material
note: added in v1.0.8

Args:
    material_interface (MaterialInterface): The source material

Returns:
    Array[MaterialExpression]: 

    out_expressions (Array[MaterialExpression]):

<a id="unreal.PythonMaterialLib.get_material_expression_output_names"></a>

#### get\_material\_expression\_output\_names

```python
@classmethod
def get_material_expression_output_names(
        cls, expression: MaterialExpression) -> Array[str]
```

X.get_material_expression_output_names(expression) -> Array[str]
Get the output pin's names of the material expression
note: added in v1.0.8

Args:
    expression (MaterialExpression): The source material expression

Returns:
    Array[str]: The output pin's names in array

<a id="unreal.PythonMaterialLib.get_material_expression_input_names"></a>

#### get\_material\_expression\_input\_names

```python
@classmethod
def get_material_expression_input_names(cls,
                                        expression: MaterialExpression,
                                        raw_name: bool = False) -> Array[str]
```

X.get_material_expression_input_names(expression, raw_name=False) -> Array[str]
Get the input pin's names of the material expression
note: added in v1.0.8

Args:
    expression (MaterialExpression): The source material expression
    raw_name (bool): Set True will return the raw name that will not remove input type nor shorten the pin name. For instance the 'Input' will be none.

Returns:
    Array[str]: The input pin's names in array

<a id="unreal.PythonMaterialLib.get_material_expression_id"></a>

#### get\_material\_expression\_id

```python
@classmethod
def get_material_expression_id(cls, expression: MaterialExpression) -> Guid
```

X.get_material_expression_id(expression) -> Guid
Get the ParameterExpressionId of the material expression.
note: added in v1.0.8

Args:
    expression (MaterialExpression): The source expression material

Returns:
    Guid: The ParameterExpressionId

<a id="unreal.PythonMaterialLib.get_material_expression_captions"></a>

#### get\_material\_expression\_captions

```python
@classmethod
def get_material_expression_captions(
        cls, expression: MaterialExpression) -> Array[str]
```

X.get_material_expression_captions(expression) -> Array[str]
The captions of the material expression
note: added in v1.0.8

Args:
    expression (MaterialExpression): The source material expression

Returns:
    Array[str]: The captions in array

<a id="unreal.PythonMaterialLib.get_material_content"></a>

#### get\_material\_content

```python
@classmethod
def get_material_content(cls,
                         material: Material,
                         only_editable: bool = True,
                         include_comments: bool = False) -> str
```

X.get_material_content(material, only_editable=True, include_comments=False) -> str
Get the material's content in JSON Format
note: added in v1.0.8

Args:
    material (Material): The material you want to query.
    only_editable (bool): Get the Editable properties only or not.
    include_comments (bool): Include the Comments in Material Editor's graph or not.

Returns:
    str: The material's content in JSON Format

<a id="unreal.PythonMaterialLib.get_material_connections"></a>

#### get\_material\_connections

```python
@classmethod
def get_material_connections(
    cls, material_interface: MaterialInterface
) -> Array[TAPythonMaterialConnection]
```

X.get_material_connections(material_interface) -> Array[TAPythonMaterialConnection]
Get all the connections in the material
note: added in v1.0.8

Args:
    material_interface (MaterialInterface): The source material

Returns:
    Array[TAPythonMaterialConnection]: The connections

<a id="unreal.PythonMaterialLib.get_hlsl_code"></a>

#### get\_hlsl\_code

```python
@classmethod
def get_hlsl_code(cls, material_interface: MaterialInterface) -> Optional[str]
```

X.get_hlsl_code(material_interface) -> str or None
Get the HLSL code of the Material
note: The FeatureLevel if SM5
note: added in v1.0.8

Args:
    material_interface (MaterialInterface): The material you want to query.

Returns:
    str or None: None or the HLSL source code

    out_source (str):

<a id="unreal.PythonMaterialLib.get_editing_materials_from_mat"></a>

#### get\_editing\_materials\_from\_mat

```python
@classmethod
def get_editing_materials_from_mat(cls, object: Object) -> Array[Material]
```

X.get_editing_materials_from_mat(object) -> Array[Material]
Get the Editing Materials of the specified material in material editor.

Args:
    object (Object): 

Returns:
    Array[Material]: the being edited materials, include the temp material and the source material

<a id="unreal.PythonMaterialLib.get_all_referenced_expressions"></a>

#### get\_all\_referenced\_expressions

```python
@classmethod
def get_all_referenced_expressions(
        cls,
        material_interface: MaterialInterface,
        feature_level: int = 3) -> Array[MaterialExpression]
```

X.get_all_referenced_expressions(material_interface, feature_level=3) -> Array[MaterialExpression]
Get Material Expressions in the material with specified feature level
note: added in v1.0.8

Args:
    material_interface (MaterialInterface): The source material
    feature_level (int32): ERHIFeatureLevel value in integer. 0: ES2_REMOVED, 1: ES3_1, 2: SM4_REMOVED, 3: SM_5, 4: SM6. Default == 3(SM_5)

Returns:
    Array[MaterialExpression]: 

    out_expressions (Array[MaterialExpression]):

<a id="unreal.PythonMaterialLib.gen_guid_from_material_property_str"></a>

#### gen\_guid\_from\_material\_property\_str

```python
@classmethod
def gen_guid_from_material_property_str(cls, property_str: str) -> Guid
```

X.gen_guid_from_material_property_str(property_str) -> Guid
Generate a Guid from EMaterialProperty
note: It's a python version of FMaterialAttributeDefinitionMap::GetID(Property)
note: added in v1.0.8

Args:
    property_str (str): EMaterialProperty String: MP_BaseColor, MP_Metallic, MP_Specular, MP_Normal, MP_WorldPositionOffset, MP_CustomData0, MP_CustomizedUVs0 and so on

Returns:
    Guid: The new Guid

<a id="unreal.PythonMaterialLib.disconnect_material_property"></a>

#### disconnect\_material\_property

```python
@classmethod
def disconnect_material_property(cls, material: Material,
                                 material_property_str: str) -> bool
```

X.disconnect_material_property(material, material_property_str) -> bool
Disconnect the material property input
note: added in v1.0.8

Args:
    material (Material): The target material
    material_property_str (str): EMaterialProperty value in string from. So we can connect to the "Hidden" Property, for instance: MP_WorldPositionOffset, MP_CustomData0,  MP_CustomizedUVs0 and so on

Returns:
    bool: True if connected

<a id="unreal.PythonMaterialLib.disconnect_expression"></a>

#### disconnect\_expression

```python
@classmethod
def disconnect_expression(cls, expression: MaterialExpression,
                          input_name: str) -> bool
```

X.disconnect_expression(expression, input_name) -> bool
Disconnection the material expression's input
note: added in v1.0.8

Args:
    expression (MaterialExpression): Expression
    input_name (str): 

Returns:
    bool: True if disconnected

<a id="unreal.PythonMaterialLib.connect_material_property"></a>

#### connect\_material\_property

```python
@classmethod
def connect_material_property(cls, from_expression: MaterialExpression,
                              from_output_name: str,
                              material_property_str: str) -> bool
```

X.connect_material_property(from_expression, from_output_name, material_property_str) -> bool
Connect a material expression output to one of the material property inputs (e.g. diffuse color,  world position offset etc)
note: added in v1.0.8

Args:
    from_expression (MaterialExpression): Expression to make connection from
    from_output_name (str): Name of output of FromExpression to make connection from
    material_property_str (str): EMaterialProperty value in string from. So we can connect to the "Hidden" Property, for instance: MP_WorldPositionOffset, MP_CustomData0,  MP_CustomizedUVs0 and so on

Returns:
    bool: True if connected

<a id="unreal.PythonMaterialLib.connect_material_expressions"></a>

#### connect\_material\_expressions

```python
@classmethod
def connect_material_expressions(cls, from_expression: MaterialExpression,
                                 from_output_name: str,
                                 to_expression: MaterialExpression,
                                 to_input_name: str) -> bool
```

X.connect_material_expressions(from_expression, from_output_name, to_expression, to_input_name) -> bool
Create connection between two material expressions
note: Same as the function in UMaterialEditingLibrary, add extra log when failed.
note: added in v1.0.8

Args:
    from_expression (MaterialExpression): Expression to make connection from
    from_output_name (str): Name of output of FromExpression to make connection from. Leave empty to use first output.
    to_expression (MaterialExpression): Expression to make connection to
    to_input_name (str): Name of input of ToExpression to make connection to. Leave empty to use first input.

Returns:
    bool: True if connected

<a id="unreal.PythonMaterialLib.add_output_at_expression_get_material_attributes"></a>

#### add\_output\_at\_expression\_get\_material\_attributes

```python
@classmethod
def add_output_at_expression_get_material_attributes(
        cls, expression_get_material_attributes:
    MaterialExpressionGetMaterialAttributes, property_str: str) -> None
```

X.add_output_at_expression_get_material_attributes(expression_get_material_attributes, property_str) -> None
Add an Attribute Get Type pin for material expression "GetMaterialAttributes"
note: added in v1.0.8

Args:
    expression_get_material_attributes (MaterialExpressionGetMaterialAttributes): The target expression.
    property_str (str): EMaterialProperty String: MP_BaseColor, MP_Metallic, MP_Specular, MP_Normal, MP_WorldPositionOffset, MP_CustomData0, MP_CustomizedUVs0 and so on

<a id="unreal.PythonMaterialLib.add_input_at_expression_set_material_attributes"></a>

#### add\_input\_at\_expression\_set\_material\_attributes

```python
@classmethod
def add_input_at_expression_set_material_attributes(
        cls, expression_set_material_attributes:
    MaterialExpressionSetMaterialAttributes, property_str: str) -> None
```

X.add_input_at_expression_set_material_attributes(expression_set_material_attributes, property_str) -> None
Add an Attribute Get Type pin for material expression "GetMaterialAttributes"
note: added in v1.0.8

Args:
    expression_set_material_attributes (MaterialExpressionSetMaterialAttributes): The target expression.
    property_str (str): EMaterialProperty String: MP_BaseColor, MP_Metallic, MP_Specular, MP_Normal, MP_WorldPositionOffset, MP_CustomData0, MP_CustomizedUVs0 and so on

<a id="unreal.PythonMeshLib"></a>