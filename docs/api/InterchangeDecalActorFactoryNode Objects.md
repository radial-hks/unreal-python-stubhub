## InterchangeDecalActorFactoryNode Objects

```python
class InterchangeDecalActorFactoryNode(InterchangeActorFactoryNode)
```

Interchange Decal Actor Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeDecalActorFactoryNode.h

<a id="unreal.InterchangeDecalActorFactoryNode.set_custom_sort_order"></a>

#### set\_custom\_sort\_order

```python
def set_custom_sort_order(attribute_value: int,
                          add_apply_delegate: bool = True) -> bool
```

x.set_custom_sort_order(attribute_value, add_apply_delegate=True) -> bool
Set Custom Sort Order

Args:
    attribute_value (int32): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeDecalActorFactoryNode.set_custom_decal_size"></a>

#### set\_custom\_decal\_size

```python
def set_custom_decal_size(attribute_value: Vector,
                          add_apply_delegate: bool = True) -> bool
```

x.set_custom_decal_size(attribute_value, add_apply_delegate=True) -> bool
Set Custom Decal Size

Args:
    attribute_value (Vector): 
    add_apply_delegate (bool): 

Returns:
    bool:

<a id="unreal.InterchangeDecalActorFactoryNode.set_custom_decal_material_path_name"></a>

#### set\_custom\_decal\_material\_path\_name

```python
def set_custom_decal_material_path_name(attribute_value: str) -> bool
```

x.set_custom_decal_material_path_name(attribute_value) -> bool
Set Custom Decal Material Path Name

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeDecalActorFactoryNode.get_object_class"></a>

#### get\_object\_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get Object Class

Returns:
    type(Class):

<a id="unreal.InterchangeDecalActorFactoryNode.get_custom_sort_order"></a>

#### get\_custom\_sort\_order

```python
def get_custom_sort_order() -> Optional[int]
```

x.get_custom_sort_order() -> int32 or None
Get Custom Sort Order

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeDecalActorFactoryNode.get_custom_decal_size"></a>

#### get\_custom\_decal\_size

```python
def get_custom_decal_size() -> Optional[Vector]
```

x.get_custom_decal_size() -> Vector or None
Get Custom Decal Size

Returns:
    Vector or None: 

    attribute_value (Vector):

<a id="unreal.InterchangeDecalActorFactoryNode.get_custom_decal_material_path_name"></a>

#### get\_custom\_decal\_material\_path\_name

```python
def get_custom_decal_material_path_name() -> Optional[str]
```

x.get_custom_decal_material_path_name() -> str or None
Get Custom Decal Material Path Name

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeBaseMaterialFactoryNode"></a>