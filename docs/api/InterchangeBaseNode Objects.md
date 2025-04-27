## InterchangeBaseNode Objects

```python
class InterchangeBaseNode(Object)
```

This struct is used to store and retrieve key-value attributes. The attributes are stored in a generic FAttributeStorage that serializes the values in a TArray64<uint8>.
See UE::Interchange::EAttributeTypes to know the supported template types.
This is an abstract class. This is the base class of the interchange node graph format; all classes in this format should derive from this class.

**C++ Source:**

- **Module**: InterchangeCore
- **File**: InterchangeBaseNode.h

<a id="unreal.InterchangeBaseNode.set_parent_uid"></a>

#### set_parent_uid

```python
def set_parent_uid(parent_uid: str) -> bool
```

x.set_parent_uid(parent_uid) -> bool
Set Parent Uid

Args:
    parent_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.set_enabled"></a>

#### set_enabled

```python
def set_enabled(is_enabled: bool) -> bool
```

x.set_enabled(is_enabled) -> bool
Determine whether this node should be part of the import or export process.

Args:
    is_enabled (bool): If true, this node is imported or exported. If false, it is discarded.

Returns:
    bool: true if the attribute was set, or false otherwise.

<a id="unreal.InterchangeBaseNode.set_display_label"></a>

#### set_display_label

```python
def set_display_label(display_name: str) -> bool
```

x.set_display_label(display_name) -> bool
Change the display label.

Args:
    display_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.set_asset_name"></a>

#### set_asset_name

```python
def set_asset_name(asset_name: str) -> bool
```

x.set_asset_name(asset_name) -> bool
Set the name for the imported asset this node represents. The asset factory will call GetAssetName().

Args:
    asset_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.remove_target_node_uid"></a>

#### remove_target_node_uid

```python
def remove_target_node_uid(asset_uid: str) -> bool
```

x.remove_target_node_uid(asset_uid) -> bool
Remove an asset node UID relating to this object.

Args:
    asset_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.remove_attribute"></a>

#### remove_attribute

```python
def remove_attribute(node_attribute_key: str) -> bool
```

x.remove_attribute(node_attribute_key) -> bool
Remove the specified attribute from this node. Returns false if it could not be removed. If the attribute does not exist, returns true.

Args:
    node_attribute_key (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.is_enabled"></a>

#### is_enabled

```python
def is_enabled() -> bool
```

x.is_enabled() -> bool
If true, the node is imported or exported. If false, it is discarded.
Returns false if the node was disabled. Returns true if the attribute is not there or if it was enabled.

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.initialize_node"></a>

#### initialize_node

```python
def initialize_node(unique_id: str, display_label: str,
                    node_container_type: InterchangeNodeContainerType) -> None
```

x.initialize_node(unique_id, display_label, node_container_type) -> None
Initialize the base data of the node.

Args:
    unique_id (str): The unique ID for this node.
    display_label (str): The name of the node.
    node_container_type (InterchangeNodeContainerType):

<a id="unreal.InterchangeBaseNode.get_vector2_attribute"></a>

#### get_vector2_attribute

```python
def get_vector2_attribute(node_attribute_key: str) -> Optional[Vector2f]
```

x.get_vector2_attribute(node_attribute_key) -> Vector2f or None
Get a Vector2 attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    Vector2f or None: 

    out_value (Vector2f):

<a id="unreal.InterchangeBaseNode.get_unique_id"></a>

#### get_unique_id

```python
def get_unique_id() -> str
```

x.get_unique_id() -> str
Return the unique ID passed in the constructor.

Returns:
    str:

<a id="unreal.InterchangeBaseNode.get_target_node_uids"></a>

#### get_target_node_uids

```python
def get_target_node_uids() -> Array[str]
```

x.get_target_node_uids() -> Array[str]
Get the target assets relating to this object.

Returns:
    Array[str]: 

    out_target_assets (Array[str]):

<a id="unreal.InterchangeBaseNode.get_target_node_count"></a>

#### get_target_node_count

```python
def get_target_node_count() -> int
```

x.get_target_node_count() -> int32
Get the number of target assets relating to this object.

Returns:
    int32:

<a id="unreal.InterchangeBaseNode.get_string_attribute"></a>

#### get_string_attribute

```python
def get_string_attribute(node_attribute_key: str) -> Optional[str]
```

x.get_string_attribute(node_attribute_key) -> str or None
Get a string attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    str or None: 

    out_value (str):

<a id="unreal.InterchangeBaseNode.get_parent_uid"></a>

#### get_parent_uid

```python
def get_parent_uid() -> str
```

x.get_parent_uid() -> str
Return the parent unique ID. If the attribute does not exist, returns InvalidNodeUid().

Returns:
    str:

<a id="unreal.InterchangeBaseNode.get_node_container_type"></a>

#### get_node_container_type

```python
def get_node_container_type() -> InterchangeNodeContainerType
```

x.get_node_container_type() -> InterchangeNodeContainerType
Return the node container type that defines the purpose of the node (factory node, translated scene node, or translated asset node).

Returns:
    InterchangeNodeContainerType:

<a id="unreal.InterchangeBaseNode.get_linear_color_attribute"></a>

#### get_linear_color_attribute

```python
def get_linear_color_attribute(
        node_attribute_key: str) -> Optional[LinearColor]
```

x.get_linear_color_attribute(node_attribute_key) -> LinearColor or None
Get an FLinearColor attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    LinearColor or None: 

    out_value (LinearColor):

<a id="unreal.InterchangeBaseNode.get_int32_attribute"></a>

#### get_int32_attribute

```python
def get_int32_attribute(node_attribute_key: str) -> Optional[int]
```

x.get_int32_attribute(node_attribute_key) -> int32 or None
Get a int32 attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    int32 or None: 

    out_value (int32):

<a id="unreal.InterchangeBaseNode.get_guid_attribute"></a>

#### get_guid_attribute

```python
def get_guid_attribute(node_attribute_key: str) -> Optional[Guid]
```

x.get_guid_attribute(node_attribute_key) -> Guid or None
Get a GUID attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    Guid or None: 

    out_value (Guid):

<a id="unreal.InterchangeBaseNode.get_float_attribute"></a>

#### get_float_attribute

```python
def get_float_attribute(node_attribute_key: str) -> Optional[float]
```

x.get_float_attribute(node_attribute_key) -> float or None
Get a float attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    float or None: 

    out_value (float):

<a id="unreal.InterchangeBaseNode.get_double_attribute"></a>

#### get_double_attribute

```python
def get_double_attribute(node_attribute_key: str) -> Optional[float]
```

x.get_double_attribute(node_attribute_key) -> double or None
Get a double attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    double or None: 

    out_value (double):

<a id="unreal.InterchangeBaseNode.get_display_label"></a>

#### get_display_label

```python
def get_display_label() -> str
```

x.get_display_label() -> str
Return the display label.

Returns:
    str:

<a id="unreal.InterchangeBaseNode.get_boolean_attribute"></a>

#### get_boolean_attribute

```python
def get_boolean_attribute(node_attribute_key: str) -> Optional[bool]
```

x.get_boolean_attribute(node_attribute_key) -> bool or None
Get a Boolean attribute from this node. Returns false if the attribute does not exist.

Args:
    node_attribute_key (str): 

Returns:
    bool or None: 

    out_value (bool):

<a id="unreal.InterchangeBaseNode.get_asset_name"></a>

#### get_asset_name

```python
def get_asset_name() -> str
```

x.get_asset_name() -> str
Optional. Any node that can import or export an asset should set the desired name for the asset.
If the attribute was never set, returns GetDisplayLabel().

Returns:
    str:

<a id="unreal.InterchangeBaseNode.add_vector2_attribute"></a>

#### add_vector2_attribute

```python
def add_vector2_attribute(node_attribute_key: str, value: Vector2f) -> bool
```

x.add_vector2_attribute(node_attribute_key, value) -> bool
Add a Vector2 attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (Vector2f): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_target_node_uid"></a>

#### add_target_node_uid

```python
def add_target_node_uid(asset_uid: str) -> bool
```

x.add_target_node_uid(asset_uid) -> bool
Add an asset node UID relating to this object.

Args:
    asset_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_string_attribute"></a>

#### add_string_attribute

```python
def add_string_attribute(node_attribute_key: str, value: str) -> bool
```

x.add_string_attribute(node_attribute_key, value) -> bool
Add a string attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (str): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_linear_color_attribute"></a>

#### add_linear_color_attribute

```python
def add_linear_color_attribute(node_attribute_key: str,
                               value: LinearColor) -> bool
```

x.add_linear_color_attribute(node_attribute_key, value) -> bool
Add an FLinearColor attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (LinearColor): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_int32_attribute"></a>

#### add_int32_attribute

```python
def add_int32_attribute(node_attribute_key: str, value: int) -> bool
```

x.add_int32_attribute(node_attribute_key, value) -> bool
Add a int32 attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_guid_attribute"></a>

#### add_guid_attribute

```python
def add_guid_attribute(node_attribute_key: str, value: Guid) -> bool
```

x.add_guid_attribute(node_attribute_key, value) -> bool
Add a GUID attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (Guid): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_float_attribute"></a>

#### add_float_attribute

```python
def add_float_attribute(node_attribute_key: str, value: float) -> bool
```

x.add_float_attribute(node_attribute_key, value) -> bool
Add a float attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (float): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_double_attribute"></a>

#### add_double_attribute

```python
def add_double_attribute(node_attribute_key: str, value: float) -> bool
```

x.add_double_attribute(node_attribute_key, value) -> bool
Add a double attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (double): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNode.add_boolean_attribute"></a>

#### add_boolean_attribute

```python
def add_boolean_attribute(node_attribute_key: str, value: bool) -> bool
```

x.add_boolean_attribute(node_attribute_key, value) -> bool
Add a Boolean attribute to this node. Returns false if the attribute does not exist or if it cannot be added.

Args:
    node_attribute_key (str): 
    value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeBaseNodeContainer"></a>