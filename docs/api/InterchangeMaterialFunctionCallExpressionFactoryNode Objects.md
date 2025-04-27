## InterchangeMaterialFunctionCallExpressionFactoryNode Objects

```python
class InterchangeMaterialFunctionCallExpressionFactoryNode(
        InterchangeMaterialExpressionFactoryNode)
```

Interchange Material Function Call Expression Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeMaterialFactoryNode.h

<a id="unreal.InterchangeMaterialFunctionCallExpressionFactoryNode.set_custom_material_function_dependency"></a>

#### set_custom_material_function_dependency

```python
def set_custom_material_function_dependency(attribute_value: str) -> bool
```

x.set_custom_material_function_dependency(attribute_value) -> bool
Set the unique ID of the material function that the function call expression
is referring to.
Note that a call to AddFactoryDependencyUid is made to guarantee that
the material function is created before the function call expression

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeMaterialFunctionCallExpressionFactoryNode.get_custom_material_function_dependency"></a>

#### get_custom_material_function_dependency

```python
def get_custom_material_function_dependency() -> Optional[str]
```

x.get_custom_material_function_dependency() -> str or None
Get Custom Material Function Dependency

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeMaterialFunctionFactoryNode"></a>