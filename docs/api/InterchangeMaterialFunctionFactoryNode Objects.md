## InterchangeMaterialFunctionFactoryNode Objects

```python
class InterchangeMaterialFunctionFactoryNode(InterchangeBaseMaterialFactoryNode
                                             )
```

Interchange Material Function Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeMaterialFactoryNode.h

<a id="unreal.InterchangeMaterialFunctionFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get Object Class

Returns:
    type(Class):

<a id="unreal.InterchangeMaterialFunctionFactoryNode.get_input_connection"></a>

#### get_input_connection

```python
def get_input_connection(input_name: str) -> Optional[Tuple[str, str]]
```

x.get_input_connection(input_name) -> (expression_node_uid=str, output_name=str) or None
Get Input Connection

Args:
    input_name (str): 

Returns:
    tuple or None: 

    expression_node_uid (str): 

    output_name (str):

<a id="unreal.InterchangeMeshActorFactoryNode"></a>