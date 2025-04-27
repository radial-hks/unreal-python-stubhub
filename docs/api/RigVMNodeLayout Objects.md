## RigVMNodeLayout Objects

```python
class RigVMNodeLayout(StructBase)
```

Rig VMNode Layout

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMNodeLayout.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``categories`` (Array[RigVMPinCategory]):  [Read-Only]
- ``display_names`` (Map[str, str]):  [Read-Only]
- ``pin_index_in_category`` (Map[str, int32]):  [Read-Only]

<a id="unreal.RigVMNodeLayout.__init__"></a>

#### __init__

```python
def __init__(categories: Array[RigVMPinCategory] = [],
             pin_index_in_category: Map[str, int] = {},
             display_names: Map[str, str] = {}) -> None
```

<a id="unreal.RigVMNodeLayout.categories"></a>

#### categories

```python
@property
def categories() -> Array[RigVMPinCategory]
```

(Array[RigVMPinCategory]):  [Read-Only]

<a id="unreal.RigVMNodeLayout.pin_index_in_category"></a>

#### pin_index_in_category

```python
@property
def pin_index_in_category() -> Map[str, int]
```

(Map[str, int32]):  [Read-Only]

<a id="unreal.RigVMNodeLayout.display_names"></a>

#### display_names

```python
@property
def display_names() -> Map[str, str]
```

(Map[str, str]):  [Read-Only]

<a id="unreal.RigVMGraphFunctionLayout"></a>