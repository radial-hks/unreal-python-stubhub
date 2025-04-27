## InterchangeFunctionCallShaderNode Objects

```python
class InterchangeFunctionCallShaderNode(InterchangeShaderNode)
```

A function call shader node has a named set of inputs and outputs which corresponds to the inputs and outputs of the shader function it instances.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeShaderGraphNode.h

<a id="unreal.InterchangeFunctionCallShaderNode.set_custom_material_function"></a>

#### set_custom_material_function

```python
def set_custom_material_function(attribute_value: str) -> bool
```

x.set_custom_material_function(attribute_value) -> bool
Set the unique id of the material function referenced by the function call expression.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeFunctionCallShaderNode.get_custom_material_function"></a>

#### get_custom_material_function

```python
def get_custom_material_function() -> Optional[str]
```

x.get_custom_material_function() -> str or None
Get Custom Material Function

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeShaderGraphNode"></a>