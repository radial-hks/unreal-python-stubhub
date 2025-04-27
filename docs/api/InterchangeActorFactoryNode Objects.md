## InterchangeActorFactoryNode Objects

```python
class InterchangeActorFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Actor Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeActorFactoryNode.h

<a id="unreal.InterchangeActorFactoryNode.set_custom_mobility"></a>

#### set_custom_mobility

```python
def set_custom_mobility(attribute_value: int,
                        add_apply_delegate: bool = True) -> bool
```

x.set_custom_mobility(attribute_value, add_apply_delegate=True) -> bool
Set Custom Mobility

Args:
    attribute_value (uint8): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeActorFactoryNode.set_custom_local_transform"></a>

#### set_custom_local_transform

```python
def set_custom_local_transform(attribute_value: Transform,
                               add_apply_delegate: bool = True) -> bool
```

x.set_custom_local_transform(attribute_value, add_apply_delegate=True) -> bool
Set Custom Local Transform

Args:
    attribute_value (Transform): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeActorFactoryNode.set_custom_global_transform"></a>

#### set_custom_global_transform

```python
def set_custom_global_transform(attribute_value: Transform,
                                add_apply_delegate: bool = True) -> bool
```

x.set_custom_global_transform(attribute_value, add_apply_delegate=True) -> bool
Set Custom Global Transform

Args:
    attribute_value (Transform): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeActorFactoryNode.set_custom_actor_class_name"></a>

#### set_custom_actor_class_name

```python
def set_custom_actor_class_name(attribute_value: str) -> bool
```

x.set_custom_actor_class_name(attribute_value) -> bool
Set Custom Actor Class Name

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeActorFactoryNode.get_custom_mobility"></a>

#### get_custom_mobility

```python
def get_custom_mobility() -> Optional[int]
```

x.get_custom_mobility() -> uint8 or None
Get Custom Mobility

Returns:
    uint8 or None: 

    attribute_value (uint8):

<a id="unreal.InterchangeActorFactoryNode.get_custom_local_transform"></a>

#### get_custom_local_transform

```python
def get_custom_local_transform() -> Optional[Transform]
```

x.get_custom_local_transform() -> Transform or None
Get Custom Local Transform

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeActorFactoryNode.get_custom_global_transform"></a>

#### get_custom_global_transform

```python
def get_custom_global_transform() -> Optional[Transform]
```

x.get_custom_global_transform() -> Transform or None
Get Custom Global Transform

Returns:
    Transform or None: 

    attribute_value (Transform):

<a id="unreal.InterchangeActorFactoryNode.get_custom_actor_class_name"></a>

#### get_custom_actor_class_name

```python
def get_custom_actor_class_name() -> Optional[str]
```

x.get_custom_actor_class_name() -> str or None
Get Custom Actor Class Name

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangePhysicalCameraFactoryNode"></a>