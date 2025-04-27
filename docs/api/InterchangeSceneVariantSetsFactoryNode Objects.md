## InterchangeSceneVariantSetsFactoryNode Objects

```python
class InterchangeSceneVariantSetsFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Scene Variant Sets Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeSceneVariantSetsFactoryNode.h

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.remove_custom_variant_set_uid"></a>

#### remove_custom_variant_set_uid

```python
def remove_custom_variant_set_uid(variant_uid: str) -> bool
```

x.remove_custom_variant_set_uid(variant_uid) -> bool
Remove the specified unique ID of a translated VariantSet from this object.

Args:
    variant_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uids"></a>

#### get_custom_variant_set_uids

```python
def get_custom_variant_set_uids() -> Array[str]
```

x.get_custom_variant_set_uids() -> Array[str]
Retrieve the unique IDs of all translated VariantSets for this object.

Returns:
    Array[str]: 

    out_variant_uids (Array[str]):

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uid_count"></a>

#### get_custom_variant_set_uid_count

```python
def get_custom_variant_set_uid_count() -> int
```

x.get_custom_variant_set_uid_count() -> int32
Retrieve the number of unique IDs of all translated VariantSets for this object.

Returns:
    int32:

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.get_custom_variant_set_uid"></a>

#### get_custom_variant_set_uid

```python
def get_custom_variant_set_uid(index: int) -> str
```

x.get_custom_variant_set_uid(index) -> str
Retrieve the UID of the VariantSet with the specified index.

Args:
    index (int32): 

Returns:
    str: 

    out_variant_uid (str):

<a id="unreal.InterchangeSceneVariantSetsFactoryNode.add_custom_variant_set_uid"></a>

#### add_custom_variant_set_uid

```python
def add_custom_variant_set_uid(variant_uid: str) -> bool
```

x.add_custom_variant_set_uid(variant_uid) -> bool
Add a unique id of a translated VariantSet for this object.

Args:
    variant_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSkeletonFactoryNode"></a>