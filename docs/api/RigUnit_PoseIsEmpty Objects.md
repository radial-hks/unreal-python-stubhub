## RigUnit_PoseIsEmpty Objects

```python
class RigUnit_PoseIsEmpty(RigUnit_HierarchyBase)
```

Returns true if the hierarchy pose is empty (has no items)

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_empty`` (bool):  [Read-Write]
- ``pose`` (RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseIsEmpty.__init__"></a>

#### __init__

```python
def __init__(pose: RigPose = [], is_empty: bool = False) -> None
```

<a id="unreal.RigUnit_PoseIsEmpty.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseIsEmpty.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseIsEmpty.is_empty"></a>

#### is_empty

```python
@property
def is_empty() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_PoseGetItems"></a>