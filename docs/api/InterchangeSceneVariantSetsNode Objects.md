## InterchangeSceneVariantSetsNode Objects

```python
class InterchangeSceneVariantSetsNode(InterchangeBaseNode)
```

Class to represent a set of VariantSet nodes

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeVariantSetNode.h

<a id="unreal.InterchangeSceneVariantSetsNode.remove_custom_variant_set_uid"></a>

#### remove_custom_variant_set_uid

```python
def remove_custom_variant_set_uid(variant_uid: str) -> bool
```

x.remove_custom_variant_set_uid(variant_uid) -> bool
Remove the specified VariantSet's unique id from this object.

Args:
    variant_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneVariantSetsNode.get_custom_variant_set_uids"></a>

#### get_custom_variant_set_uids

```python
def get_custom_variant_set_uids() -> Array[str]
```

x.get_custom_variant_set_uids() -> Array[str]
Retrieve all the VariantSets' unique ids for this object.

Returns:
    Array[str]: 

    out_variant_uids (Array[str]):

<a id="unreal.InterchangeSceneVariantSetsNode.get_custom_variant_set_uid_count"></a>

#### get_custom_variant_set_uid_count

```python
def get_custom_variant_set_uid_count() -> int
```

x.get_custom_variant_set_uid_count() -> int32
Retrieve the number of VariantSets for this object.

Returns:
    int32:

<a id="unreal.InterchangeSceneVariantSetsNode.get_custom_variant_set_uid"></a>

#### get_custom_variant_set_uid

```python
def get_custom_variant_set_uid(index: int) -> str
```

x.get_custom_variant_set_uid(index) -> str
Retrieve the specified VariantSet's unique id for this object.

Args:
    index (int32): 

Returns:
    str: 

    out_variant_uid (str):

<a id="unreal.InterchangeSceneVariantSetsNode.add_custom_variant_set_uid"></a>

#### add_custom_variant_set_uid

```python
def add_custom_variant_set_uid(variant_uid: str) -> bool
```

x.add_custom_variant_set_uid(variant_uid) -> bool
Add the specified VariantSet's unique id to this object.

Args:
    variant_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeVolumeTextureNode"></a>