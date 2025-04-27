## MaterialEditingLibrary Objects

```python
class MaterialEditingLibrary(BlueprintFunctionLibrary)
```

Blueprint library for creating/editing Materials

**C++ Source:**

- **Module**: MaterialEditor
- **File**: MaterialEditingLibrary.h

<a id="unreal.MaterialEditingLibrary.update_material_instance"></a>

#### update_material_instance

```python
@classmethod
def update_material_instance(cls, instance: MaterialInstanceConstant) -> None
```

X.update_material_instance(instance) -> None
Called after making modifications to a Material Instance to recompile shaders etc.

Args:
    instance (MaterialInstanceConstant):

<a id="unreal.MaterialEditingLibrary.update_material_function"></a>

#### update_material_function

```python
@classmethod
def update_material_function(cls,
                             material_function: MaterialFunctionInterface,
                             preview_material: Material = None) -> None
```

X.update_material_function(material_function, preview_material=None) -> None
Update a Material Function after edits have been made.
Will recompile any Materials that use the supplied Material Function.

Args:
    material_function (MaterialFunctionInterface): 
    preview_material (Material):

<a id="unreal.MaterialEditingLibrary.set_material_usage"></a>

#### set_material_usage

```python
@classmethod
def set_material_usage(cls, material: Material,
                       usage: MaterialUsage) -> Optional[bool]
```

X.set_material_usage(material, usage) -> bool or None
Enable a particular usage for the supplied material (e.g. SkeletalMesh, ParticleSprite etc)

Args:
    material (Material): Material to change usage for
    usage (MaterialUsage): New usage type to enable for this material

Returns:
    bool or None: 

    needs_recompile (bool): Returned to indicate if material needs recompiling after this change

<a id="unreal.MaterialEditingLibrary.set_material_instance_vector_parameter_value"></a>

#### set_material_instance_vector_parameter_value

```python
@classmethod
def set_material_instance_vector_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: LinearColor,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_vector_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the vector parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (LinearColor): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value"></a>

#### set_material_instance_texture_parameter_value

```python
@classmethod
def set_material_instance_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: Texture,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_texture_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the texture parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (Texture): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_static_switch_parameter_value"></a>

#### set_material_instance_static_switch_parameter_value

```python
@classmethod
def set_material_instance_static_switch_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: bool,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_static_switch_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the static switch parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (bool): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_sparse_volume_texture_parameter_value"></a>

#### set_material_instance_sparse_volume_texture_parameter_value

```python
@classmethod
def set_material_instance_sparse_volume_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: SparseVolumeTexture,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_sparse_volume_texture_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the texture parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (SparseVolumeTexture): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value"></a>

#### set_material_instance_scalar_parameter_value

```python
@classmethod
def set_material_instance_scalar_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: float,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_scalar_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the scalar (float) parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (float): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_runtime_virtual_texture_parameter_value"></a>

#### set_material_instance_runtime_virtual_texture_parameter_value

```python
@classmethod
def set_material_instance_runtime_virtual_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    value: RuntimeVirtualTexture,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.set_material_instance_runtime_virtual_texture_parameter_value(instance, parameter_name, value, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Set the texture parameter value for a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    value (RuntimeVirtualTexture): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.set_material_instance_parent"></a>

#### set_material_instance_parent

```python
@classmethod
def set_material_instance_parent(cls, instance: MaterialInstanceConstant,
                                 new_parent: MaterialInterface) -> None
```

X.set_material_instance_parent(instance, new_parent) -> None
Set the parent Material or Material Instance to use for this Material Instance

Args:
    instance (MaterialInstanceConstant): 
    new_parent (MaterialInterface):

<a id="unreal.MaterialEditingLibrary.recompile_material"></a>

#### recompile_material

```python
@classmethod
def recompile_material(cls, material: Material) -> None
```

X.recompile_material(material) -> None
Trigger a recompile of a material. Must be performed after making changes to the graph to have changes reflected.

Args:
    material (Material):

<a id="unreal.MaterialEditingLibrary.layout_material_function_expressions"></a>

#### layout_material_function_expressions

```python
@classmethod
def layout_material_function_expressions(
        cls, material_function: MaterialFunction) -> None
```

X.layout_material_function_expressions(material_function) -> None
Layouts the expressions in a grid pattern

Args:
    material_function (MaterialFunction):

<a id="unreal.MaterialEditingLibrary.layout_material_expressions"></a>

#### layout_material_expressions

```python
@classmethod
def layout_material_expressions(cls, material: Material) -> None
```

X.layout_material_expressions(material) -> None
Layouts the expressions in a grid pattern

Args:
    material (Material):

<a id="unreal.MaterialEditingLibrary.has_material_usage"></a>

#### has_material_usage

```python
@classmethod
def has_material_usage(cls, material: Material, usage: MaterialUsage) -> bool
```

X.has_material_usage(material, usage) -> bool
Check if a particular usage is enabled for the supplied material (e.g. SkeletalMesh, ParticleSprite etc)

Args:
    material (Material): Material to check usage for
    usage (MaterialUsage): Usage type to check for this material

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.get_vector_parameter_source"></a>

#### get_vector_parameter_source

```python
@classmethod
def get_vector_parameter_source(
        cls, material: MaterialInterface,
        parameter_name: Name) -> Optional[SoftObjectPath]
```

X.get_vector_parameter_source(material, parameter_name) -> SoftObjectPath or None
Returns the path of the asset where the parameter originated, as well as true/false if it was found

Args:
    material (MaterialInterface): The material or material instance you want to look up a parameter from
    parameter_name (Name): The parameter name

Returns:
    SoftObjectPath or None: Whether or not the parameter was found in this material

    parameter_source (SoftObjectPath): The soft object path of the asset the parameter originates in

<a id="unreal.MaterialEditingLibrary.get_vector_parameter_names"></a>

#### get_vector_parameter_names

```python
@classmethod
def get_vector_parameter_names(cls,
                               material: MaterialInterface) -> Array[Name]
```

X.get_vector_parameter_names(material) -> Array[Name]
Gets all vector parameter names

Args:
    material (MaterialInterface): 

Returns:
    Array[Name]: 

    parameter_names (Array[Name]):

<a id="unreal.MaterialEditingLibrary.get_used_textures"></a>

#### get_used_textures

```python
@classmethod
def get_used_textures(cls, material: Material) -> Array[Texture]
```

X.get_used_textures(material) -> Array[Texture]
Get the list of textures used by a material

Args:
    material (Material): 

Returns:
    Array[Texture]:

<a id="unreal.MaterialEditingLibrary.get_texture_parameter_source"></a>

#### get_texture_parameter_source

```python
@classmethod
def get_texture_parameter_source(
        cls, material: MaterialInterface,
        parameter_name: Name) -> Optional[SoftObjectPath]
```

X.get_texture_parameter_source(material, parameter_name) -> SoftObjectPath or None
Returns the path of the asset where the parameter originated, as well as true/false if it was found

Args:
    material (MaterialInterface): The material or material instance you want to look up a parameter from
    parameter_name (Name): The parameter name

Returns:
    SoftObjectPath or None: Whether or not the parameter was found in this material

    parameter_source (SoftObjectPath): The soft object path of the asset the parameter originates in

<a id="unreal.MaterialEditingLibrary.get_texture_parameter_names"></a>

#### get_texture_parameter_names

```python
@classmethod
def get_texture_parameter_names(cls,
                                material: MaterialInterface) -> Array[Name]
```

X.get_texture_parameter_names(material) -> Array[Name]
Gets all texture parameter names

Args:
    material (MaterialInterface): 

Returns:
    Array[Name]: 

    parameter_names (Array[Name]):

<a id="unreal.MaterialEditingLibrary.get_statistics"></a>

#### get_statistics

```python
@classmethod
def get_statistics(cls, material: MaterialInterface) -> MaterialStatistics
```

X.get_statistics(material) -> MaterialStatistics
Returns statistics about the given material

Args:
    material (MaterialInterface): 

Returns:
    MaterialStatistics:

<a id="unreal.MaterialEditingLibrary.get_static_switch_parameter_source"></a>

#### get_static_switch_parameter_source

```python
@classmethod
def get_static_switch_parameter_source(
        cls, material: MaterialInterface,
        parameter_name: Name) -> Optional[SoftObjectPath]
```

X.get_static_switch_parameter_source(material, parameter_name) -> SoftObjectPath or None
Returns the path of the asset where the parameter originated, as well as true/false if it was found

Args:
    material (MaterialInterface): The material or material instance you want to look up a parameter from
    parameter_name (Name): The parameter name

Returns:
    SoftObjectPath or None: Whether or not the parameter was found in this material

    parameter_source (SoftObjectPath): The soft object path of the asset the parameter originates in

<a id="unreal.MaterialEditingLibrary.get_static_switch_parameter_names"></a>

#### get_static_switch_parameter_names

```python
@classmethod
def get_static_switch_parameter_names(
        cls, material: MaterialInterface) -> Array[Name]
```

X.get_static_switch_parameter_names(material) -> Array[Name]
Gets all static switch parameter names

Args:
    material (MaterialInterface): 

Returns:
    Array[Name]: 

    parameter_names (Array[Name]):

<a id="unreal.MaterialEditingLibrary.get_scalar_parameter_source"></a>

#### get_scalar_parameter_source

```python
@classmethod
def get_scalar_parameter_source(
        cls, material: MaterialInterface,
        parameter_name: Name) -> Optional[SoftObjectPath]
```

X.get_scalar_parameter_source(material, parameter_name) -> SoftObjectPath or None
Returns the path of the asset where the parameter originated, as well as true/false if it was found

Args:
    material (MaterialInterface): The material or material instance you want to look up a parameter from
    parameter_name (Name): The parameter name

Returns:
    SoftObjectPath or None: Whether or not the parameter was found in this material

    parameter_source (SoftObjectPath): The soft object path of the asset the parameter originates in

<a id="unreal.MaterialEditingLibrary.get_scalar_parameter_names"></a>

#### get_scalar_parameter_names

```python
@classmethod
def get_scalar_parameter_names(cls,
                               material: MaterialInterface) -> Array[Name]
```

X.get_scalar_parameter_names(material) -> Array[Name]
Gets all scalar parameter names

Args:
    material (MaterialInterface): 

Returns:
    Array[Name]: 

    parameter_names (Array[Name]):

<a id="unreal.MaterialEditingLibrary.get_num_material_expressions_in_function"></a>

#### get_num_material_expressions_in_function

```python
@classmethod
def get_num_material_expressions_in_function(
        cls, material_function: MaterialFunction) -> int
```

X.get_num_material_expressions_in_function(material_function) -> int32
Returns number of material expressions in the supplied material

Args:
    material_function (MaterialFunction): 

Returns:
    int32:

<a id="unreal.MaterialEditingLibrary.get_num_material_expressions"></a>

#### get_num_material_expressions

```python
@classmethod
def get_num_material_expressions(cls, material: Material) -> int
```

X.get_num_material_expressions(material) -> int32
Returns number of material expressions in the supplied material

Args:
    material (Material): 

Returns:
    int32:

<a id="unreal.MaterialEditingLibrary.get_nanite_override_material"></a>

#### get_nanite_override_material

```python
@classmethod
def get_nanite_override_material(
        cls, material: MaterialInterface) -> MaterialInterface
```

X.get_nanite_override_material(material) -> MaterialInterface
Returns any nanite override material for the given material

Args:
    material (MaterialInterface): 

Returns:
    MaterialInterface:

<a id="unreal.MaterialEditingLibrary.get_material_selected_nodes"></a>

#### get_material_selected_nodes

```python
@classmethod
def get_material_selected_nodes(cls, material: Material) -> Set[Object]
```

X.get_material_selected_nodes(material) -> Set[Object]
Get the set of selected nodes from an active material editor

Args:
    material (Material): 

Returns:
    Set[Object]:

<a id="unreal.MaterialEditingLibrary.get_material_property_input_node_output_name"></a>

#### get_material_property_input_node_output_name

```python
@classmethod
def get_material_property_input_node_output_name(
        cls, material: Material, property_: MaterialProperty) -> str
```

X.get_material_property_input_node_output_name(material, property_) -> str
Get the node output name providing the output for a given material property from an active material editor

Args:
    material (Material): 
    property_ (MaterialProperty): 

Returns:
    str:

<a id="unreal.MaterialEditingLibrary.get_material_property_input_node"></a>

#### get_material_property_input_node

```python
@classmethod
def get_material_property_input_node(
        cls, material: Material,
        property_: MaterialProperty) -> MaterialExpression
```

X.get_material_property_input_node(material, property_) -> MaterialExpression
Get the node providing the output for a given material property from an active material editor

Args:
    material (Material): 
    property_ (MaterialProperty): 

Returns:
    MaterialExpression:

<a id="unreal.MaterialEditingLibrary.get_material_instance_vector_parameter_value"></a>

#### get_material_instance_vector_parameter_value

```python
@classmethod
def get_material_instance_vector_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> LinearColor
```

X.get_material_instance_vector_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> LinearColor
Get the current vector parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    LinearColor:

<a id="unreal.MaterialEditingLibrary.get_material_instance_texture_parameter_value"></a>

#### get_material_instance_texture_parameter_value

```python
@classmethod
def get_material_instance_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> Texture
```

X.get_material_instance_texture_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> Texture
Get the current texture parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    Texture:

<a id="unreal.MaterialEditingLibrary.get_material_instance_static_switch_parameter_value"></a>

#### get_material_instance_static_switch_parameter_value

```python
@classmethod
def get_material_instance_static_switch_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> bool
```

X.get_material_instance_static_switch_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> bool
Get the current static switch parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.get_material_instance_sparse_volume_texture_parameter_value"></a>

#### get_material_instance_sparse_volume_texture_parameter_value

```python
@classmethod
def get_material_instance_sparse_volume_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> SparseVolumeTexture
```

X.get_material_instance_sparse_volume_texture_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> SparseVolumeTexture
Get the current texture parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    SparseVolumeTexture:

<a id="unreal.MaterialEditingLibrary.get_material_instance_scalar_parameter_value"></a>

#### get_material_instance_scalar_parameter_value

```python
@classmethod
def get_material_instance_scalar_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> float
```

X.get_material_instance_scalar_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> float
Get the current scalar (float) parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    float:

<a id="unreal.MaterialEditingLibrary.get_material_instance_runtime_virtual_texture_parameter_value"></a>

#### get_material_instance_runtime_virtual_texture_parameter_value

```python
@classmethod
def get_material_instance_runtime_virtual_texture_parameter_value(
    cls,
    instance: MaterialInstanceConstant,
    parameter_name: Name,
    association: MaterialParameterAssociation = MaterialParameterAssociation.
    GLOBAL_PARAMETER
) -> RuntimeVirtualTexture
```

X.get_material_instance_runtime_virtual_texture_parameter_value(instance, parameter_name, association=MaterialParameterAssociation.GLOBAL_PARAMETER) -> RuntimeVirtualTexture
Get the current texture parameter value from a Material Instance

Args:
    instance (MaterialInstanceConstant): 
    parameter_name (Name): 
    association (MaterialParameterAssociation): 

Returns:
    RuntimeVirtualTexture:

<a id="unreal.MaterialEditingLibrary.get_material_expression_node_position"></a>

#### get_material_expression_node_position

```python
@classmethod
def get_material_expression_node_position(
        cls, material_expression: MaterialExpression) -> Tuple[int, int]
```

X.get_material_expression_node_position(material_expression) -> (node_pos_x=int32, node_pos_y=int32)
Get the position of the MaterialExpression node.

Args:
    material_expression (MaterialExpression): 

Returns:
    tuple: 

    node_pos_x (int32): 

    node_pos_y (int32):

<a id="unreal.MaterialEditingLibrary.get_material_expression_input_types"></a>

#### get_material_expression_input_types

```python
@classmethod
def get_material_expression_input_types(
        cls, material_expression: MaterialExpression) -> Array[int]
```

X.get_material_expression_input_types(material_expression) -> Array[int32]
Get the array of input pin types for a material expression

Args:
    material_expression (MaterialExpression): 

Returns:
    Array[int32]:

<a id="unreal.MaterialEditingLibrary.get_material_expression_input_names"></a>

#### get_material_expression_input_names

```python
@classmethod
def get_material_expression_input_names(
        cls, material_expression: MaterialExpression) -> Array[str]
```

X.get_material_expression_input_names(material_expression) -> Array[str]
Get the array of input pin names for a material expression

Args:
    material_expression (MaterialExpression): 

Returns:
    Array[str]:

<a id="unreal.MaterialEditingLibrary.get_material_default_vector_parameter_value"></a>

#### get_material_default_vector_parameter_value

```python
@classmethod
def get_material_default_vector_parameter_value(
        cls, material: Material, parameter_name: Name) -> LinearColor
```

X.get_material_default_vector_parameter_value(material, parameter_name) -> LinearColor
Get the default vector parameter value from a Material

Args:
    material (Material): 
    parameter_name (Name): 

Returns:
    LinearColor:

<a id="unreal.MaterialEditingLibrary.get_material_default_texture_parameter_value"></a>

#### get_material_default_texture_parameter_value

```python
@classmethod
def get_material_default_texture_parameter_value(
        cls, material: Material, parameter_name: Name) -> Texture
```

X.get_material_default_texture_parameter_value(material, parameter_name) -> Texture
Get the default texture parameter value from a Material

Args:
    material (Material): 
    parameter_name (Name): 

Returns:
    Texture:

<a id="unreal.MaterialEditingLibrary.get_material_default_static_switch_parameter_value"></a>

#### get_material_default_static_switch_parameter_value

```python
@classmethod
def get_material_default_static_switch_parameter_value(
        cls, material: Material, parameter_name: Name) -> bool
```

X.get_material_default_static_switch_parameter_value(material, parameter_name) -> bool
Get the default static switch parameter value from a Material

Args:
    material (Material): 
    parameter_name (Name): 

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.get_material_default_scalar_parameter_value"></a>

#### get_material_default_scalar_parameter_value

```python
@classmethod
def get_material_default_scalar_parameter_value(cls, material: Material,
                                                parameter_name: Name) -> float
```

X.get_material_default_scalar_parameter_value(material, parameter_name) -> float
Get the default scalar (float) parameter value from a Material

Args:
    material (Material): 
    parameter_name (Name): 

Returns:
    float:

<a id="unreal.MaterialEditingLibrary.get_inputs_for_material_expression"></a>

#### get_inputs_for_material_expression

```python
@classmethod
def get_inputs_for_material_expression(
        cls, material: Material,
        material_expression: MaterialExpression) -> Array[MaterialExpression]
```

X.get_inputs_for_material_expression(material, material_expression) -> Array[MaterialExpression]
Get the set of nodes acting as inputs to a node from an active material editor

Args:
    material (Material): 
    material_expression (MaterialExpression): 

Returns:
    Array[MaterialExpression]:

<a id="unreal.MaterialEditingLibrary.get_input_node_output_name_for_material_expression"></a>

#### get_input_node_output_name_for_material_expression

```python
@classmethod
def get_input_node_output_name_for_material_expression(
        cls, material_expression: MaterialExpression,
        input_node: MaterialExpression) -> Optional[str]
```

X.get_input_node_output_name_for_material_expression(material_expression, input_node) -> str or None
Get the output name of input node connected to MaterialExpression from an active material editor

Args:
    material_expression (MaterialExpression): 
    input_node (MaterialExpression): 

Returns:
    str or None: 

    output_name (str):

<a id="unreal.MaterialEditingLibrary.get_child_instances"></a>

#### get_child_instances

```python
@classmethod
def get_child_instances(cls, parent: MaterialInterface) -> Array[AssetData]
```

X.get_child_instances(parent) -> Array[AssetData]
Gets all direct child mat instances

Args:
    parent (MaterialInterface): 

Returns:
    Array[AssetData]: 

    child_instances (Array[AssetData]):

<a id="unreal.MaterialEditingLibrary.duplicate_material_expression"></a>

#### duplicate_material_expression

```python
@classmethod
def duplicate_material_expression(
        cls, material: Material, material_function: MaterialFunction,
        expression: MaterialExpression) -> MaterialExpression
```

X.duplicate_material_expression(material, material_function, expression) -> MaterialExpression
Duplicates the provided material expression adding it to the same material / material function, and copying parameters.
Note: Does not duplicate transient properties (Ex: GraphNode).

Args:
    material (Material): Material asset to add an expression to
    material_function (MaterialFunction): Specified if adding an expression to a MaterialFunction, used as Outer for new expression object
    expression (MaterialExpression): 

Returns:
    MaterialExpression:

<a id="unreal.MaterialEditingLibrary.delete_material_expression_in_function"></a>

#### delete_material_expression_in_function

```python
@classmethod
def delete_material_expression_in_function(
        cls, material_function: MaterialFunction,
        expression: MaterialExpression) -> None
```

X.delete_material_expression_in_function(material_function, expression) -> None
Delete a specific expression from a material function. Will disconnect from other expressions.

Args:
    material_function (MaterialFunction): 
    expression (MaterialExpression):

<a id="unreal.MaterialEditingLibrary.delete_material_expression"></a>

#### delete_material_expression

```python
@classmethod
def delete_material_expression(cls, material: Material,
                               expression: MaterialExpression) -> None
```

X.delete_material_expression(material, expression) -> None
Delete a specific expression from a material. Will disconnect from other expressions.

Args:
    material (Material): 
    expression (MaterialExpression):

<a id="unreal.MaterialEditingLibrary.delete_all_material_expressions_in_function"></a>

#### delete_all_material_expressions_in_function

```python
@classmethod
def delete_all_material_expressions_in_function(
        cls, material_function: MaterialFunction) -> None
```

X.delete_all_material_expressions_in_function(material_function) -> None
Delete all material expressions in the supplied material function

Args:
    material_function (MaterialFunction):

<a id="unreal.MaterialEditingLibrary.delete_all_material_expressions"></a>

#### delete_all_material_expressions

```python
@classmethod
def delete_all_material_expressions(cls, material: Material) -> None
```

X.delete_all_material_expressions(material) -> None
Delete all material expressions in the supplied material

Args:
    material (Material):

<a id="unreal.MaterialEditingLibrary.create_material_expression_in_function"></a>

#### create_material_expression_in_function

```python
@classmethod
def create_material_expression_in_function(
        cls,
        material_function: MaterialFunction,
        expression_class: Class,
        node_pos_x: int = 0,
        node_pos_y: int = 0) -> MaterialExpression
```

X.create_material_expression_in_function(material_function, expression_class, node_pos_x=0, node_pos_y=0) -> MaterialExpression
Create a new material expression node within the supplied material function

Args:
    material_function (MaterialFunction): Material function asset to add an expression to
    expression_class (type(Class)): Class of expression to add
    node_pos_x (int32): X position of new expression node
    node_pos_y (int32): Y position of new expression node

Returns:
    MaterialExpression:

<a id="unreal.MaterialEditingLibrary.create_material_expression"></a>

#### create_material_expression

```python
@classmethod
def create_material_expression(cls,
                               material: Material,
                               expression_class: Class,
                               node_pos_x: int = 0,
                               node_pos_y: int = 0) -> MaterialExpression
```

X.create_material_expression(material, expression_class, node_pos_x=0, node_pos_y=0) -> MaterialExpression
Create a new material expression node within the supplied material

Args:
    material (Material): Material asset to add an expression to
    expression_class (type(Class)): Class of expression to add
    node_pos_x (int32): X position of new expression node
    node_pos_y (int32): Y position of new expression node

Returns:
    MaterialExpression:

<a id="unreal.MaterialEditingLibrary.connect_material_property"></a>

#### connect_material_property

```python
@classmethod
def connect_material_property(cls, from_expression: MaterialExpression,
                              from_output_name: str,
                              property_: MaterialProperty) -> bool
```

X.connect_material_property(from_expression, from_output_name, property_) -> bool
Connect a material expression output to one of the material property inputs (e.g. diffuse color, opacity etc)

Args:
    from_expression (MaterialExpression): Expression to make connection from
    from_output_name (str): Name of output of FromExpression to make connection from
    property_ (MaterialProperty): Property input on material to make connection to

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.connect_material_expressions"></a>

#### connect_material_expressions

```python
@classmethod
def connect_material_expressions(cls, from_expression: MaterialExpression,
                                 from_output_name: str,
                                 to_expression: MaterialExpression,
                                 to_input_name: str) -> bool
```

X.connect_material_expressions(from_expression, from_output_name, to_expression, to_input_name) -> bool
Create connection between two material expressions

Args:
    from_expression (MaterialExpression): Expression to make connection from
    from_output_name (str): Name of output of FromExpression to make connection from. Leave empty to use first output.
    to_expression (MaterialExpression): Expression to make connection to
    to_input_name (str): Name of input of ToExpression to make connection to. Leave empty to use first input.

Returns:
    bool:

<a id="unreal.MaterialEditingLibrary.clear_all_material_instance_parameters"></a>

#### clear_all_material_instance_parameters

```python
@classmethod
def clear_all_material_instance_parameters(
        cls, instance: MaterialInstanceConstant) -> None
```

X.clear_all_material_instance_parameters(instance) -> None
Clears all material parameters set by this Material Instance

Args:
    instance (MaterialInstanceConstant):

<a id="unreal.RuntimeVirtualTextureFactory"></a>