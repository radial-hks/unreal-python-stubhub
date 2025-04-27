## RigVMPinCategory Objects

```python
class RigVMPinCategory(StructBase)
```

Rig VMPin Category

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMNodeLayout.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``elements`` (Array[str]):  [Read-Only]
- ``expanded_by_default`` (bool):  [Read-Only]
- ``path`` (str):  [Read-Only]

<a id="unreal.RigVMPinCategory.__init__"></a>

#### __init__

```python
def __init__(path: str = "",
             elements: Array[str] = [],
             expanded_by_default: bool = False) -> None
```

<a id="unreal.RigVMPinCategory.path"></a>

#### path

```python
@property
def path() -> str
```

(str):  [Read-Only]

<a id="unreal.RigVMPinCategory.elements"></a>

#### elements

```python
@property
def elements() -> Array[str]
```

(Array[str]):  [Read-Only]

<a id="unreal.RigVMPinCategory.expanded_by_default"></a>

#### expanded_by_default

```python
@property
def expanded_by_default() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigVMGraphFunctionCategory"></a>