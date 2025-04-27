## InterchangeShaderNode Objects

```python
class InterchangeShaderNode(InterchangeBaseNode)
```

A shader node is a named set of inputs and outputs. It can be connected to other shader nodes and finally to a shader graph input.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeShaderGraphNode.h

<a id="unreal.InterchangeShaderNode.set_custom_shader_type"></a>

#### set_custom_shader_type

```python
def set_custom_shader_type(attribute_value: str) -> bool
```

x.set_custom_shader_type(attribute_value) -> bool
Sets which type of shader this nodes represents. Can be arbitrary or one of the predefined shader types.
The material pipeline handling the shader node should be aware of the shader type that is being set here.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeShaderNode.get_custom_shader_type"></a>

#### get_custom_shader_type

```python
def get_custom_shader_type() -> Optional[str]
```

x.get_custom_shader_type() -> str or None
Get Custom Shader Type

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeShaderNode.add_string_input"></a>

#### add_string_input

```python
def add_string_input(input_name: str,
                     attribute_value: str,
                     is_a_parameter: bool = False) -> bool
```

x.add_string_input(input_name, attribute_value, is_a_parameter=False) -> bool
Set the String Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a overridable Texture
or else it should be treated as a LUT Texture.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

Args:
    input_name (str): 
    attribute_value (str): 
    is_a_parameter (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderNode.add_linear_color_input"></a>

#### add_linear_color_input

```python
def add_linear_color_input(input_name: str,
                           attribute_value: LinearColor,
                           is_a_parameter: bool = False) -> bool
```

x.add_linear_color_input(input_name, attribute_value, is_a_parameter=False) -> bool
Set the Linear Color Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a VectorParameter
when the Material Pipeline creates the materials. Otherwise it would be a constant 3 vector expression in the shader graph.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

Args:
    input_name (str): 
    attribute_value (LinearColor): 
    is_a_parameter (bool): 

Returns:
    bool:

<a id="unreal.InterchangeShaderNode.add_float_input"></a>

#### add_float_input

```python
def add_float_input(input_name: str,
                    attribute_value: float,
                    is_a_parameter: bool = False) -> bool
```

x.add_float_input(input_name, attribute_value, is_a_parameter=False) -> bool
Set the Float Attribute on the Shader Node. If bIsAParameter is set to true, it would be treated as a ScalarParameter
when the Material Pipeline creates the materials. Otherwise it would be a constant expression in the shader graph.
Note: It is assumed that the input name would be the parameter name when bIsAParameter is true.

Args:
    input_name (str): 
    attribute_value (float): 
    is_a_parameter (bool): 

Returns:
    bool:

<a id="unreal.InterchangeDecalMaterialNode"></a>