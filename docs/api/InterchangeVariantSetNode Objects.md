## InterchangeVariantSetNode Objects

```python
class InterchangeVariantSetNode(InterchangeBaseNode)
```

Class to represent a set of variants.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeVariantSetNode.h

<a id="unreal.InterchangeVariantSetNode.set_custom_variants_payload_key"></a>

#### set_custom_variants_payload_key

```python
def set_custom_variants_payload_key(payload_key: str) -> bool
```

x.set_custom_variants_payload_key(payload_key) -> bool
Set the payload key needed to retrieve the variants for this VariantSet.

Args:
    payload_key (str): 

Returns:
    bool:

<a id="unreal.InterchangeVariantSetNode.set_custom_display_text"></a>

#### set_custom_display_text

```python
def set_custom_display_text(attribute_value: str) -> bool
```

x.set_custom_display_text(attribute_value) -> bool
Set the text to be displayed in the UI for this VariantSet.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeVariantSetNode.remove_custom_dependency_uid"></a>

#### remove_custom_dependency_uid

```python
def remove_custom_dependency_uid(dependency_uid: str) -> bool
```

x.remove_custom_dependency_uid(dependency_uid) -> bool
Remove the specified translated node's unique ID from this VariantSet.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeVariantSetNode.get_custom_variants_payload_key"></a>

#### get_custom_variants_payload_key

```python
def get_custom_variants_payload_key() -> Optional[str]
```

x.get_custom_variants_payload_key() -> str or None
Get the payload key needed to retrieve the variants for this VariantSet.

Returns:
    str or None: 

    payload_key (str):

<a id="unreal.InterchangeVariantSetNode.get_custom_display_text"></a>

#### get_custom_display_text

```python
def get_custom_display_text() -> Optional[str]
```

x.get_custom_display_text() -> str or None
Retrieve the text that is displayed in the UI for this VariantSet.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeVariantSetNode.get_custom_dependency_uids"></a>

#### get_custom_dependency_uids

```python
def get_custom_dependency_uids() -> Array[str]
```

x.get_custom_dependency_uids() -> Array[str]
Retrieve all the translated node's unique IDs for this VariantSet.

Returns:
    Array[str]: 

    out_dependency_uids (Array[str]):

<a id="unreal.InterchangeVariantSetNode.get_custom_dependency_uid_count"></a>

#### get_custom_dependency_uid_count

```python
def get_custom_dependency_uid_count() -> int
```

x.get_custom_dependency_uid_count() -> int32
Retrieve the number of translated node's unique IDs for this VariantSet.

Returns:
    int32:

<a id="unreal.InterchangeVariantSetNode.get_custom_dependency_uid"></a>

#### get_custom_dependency_uid

```python
def get_custom_dependency_uid(index: int) -> str
```

x.get_custom_dependency_uid(index) -> str
Retrieve the specified translated node's unique ID for this VariantSet.

Args:
    index (int32): 

Returns:
    str: 

    out_dependency_uid (str):

<a id="unreal.InterchangeVariantSetNode.add_custom_dependency_uid"></a>

#### add_custom_dependency_uid

```python
def add_custom_dependency_uid(dependency_uid: str) -> bool
```

x.add_custom_dependency_uid(dependency_uid) -> bool
Add the specified translated node's unique ID to this VariantSet.

Args:
    dependency_uid (str): 

Returns:
    bool:

<a id="unreal.InterchangeSceneVariantSetsNode"></a>