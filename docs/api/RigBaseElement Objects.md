## RigBaseElement Objects

```python
class RigBaseElement(StructBase)
```

Rig Base Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``selected`` (bool):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigBaseElement.__init__"></a>

#### __init__

```python
def __init__(key: RigElementKey = [RigElementType.NONE, "None"],
             index: int = 0,
             sub_index: int = 0,
             created_at_instruction_index: int = 0,
             selected: bool = False) -> None
```

<a id="unreal.RigBaseElement.key"></a>

#### key

```python
@property
def key() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigBaseElement.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigBaseElement.sub_index"></a>

#### sub_index

```python
@property
def sub_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigBaseElement.created_at_instruction_index"></a>

#### created_at_instruction_index

```python
@property
def created_at_instruction_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigBaseElement.selected"></a>

#### selected

```python
@property
def selected() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigTransformElement"></a>