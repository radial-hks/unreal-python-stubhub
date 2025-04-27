## RigSpace Objects

```python
class RigSpace(RigElement)
```

Rig Space

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigSpaceHierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``index`` (int32):  [Read-Only]
- ``initial_transform`` (Transform):  [Read-Write]
- ``local_transform`` (Transform):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``parent_index`` (int32):  [Read-Write]
- ``parent_name`` (Name):  [Read-Only]
- ``space_type`` (RigSpaceType):  [Read-Only]

<a id="unreal.RigSpace.__init__"></a>

#### __init__

```python
def __init__(
    name: Name = "None",
    index: int = 0,
    space_type: RigSpaceType = RigSpaceType.GLOBAL,
    parent_name: Name = "None",
    parent_index: int = 0,
    initial_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                    [-0.000000, 0.000000, 0.000000],
                                    [1.000000, 1.000000, 1.000000]],
    local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                  [-0.000000, 0.000000, 0.000000],
                                  [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.RigSpace.space_type"></a>

#### space_type

```python
@property
def space_type() -> RigSpaceType
```

(RigSpaceType):  [Read-Only]

<a id="unreal.RigSpace.parent_name"></a>

#### parent_name

```python
@property
def parent_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RigSpace.parent_index"></a>

#### parent_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigSpace.initial_transform"></a>

#### initial_transform

```python
@property
def initial_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigSpace.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigControlModifiedContext"></a>