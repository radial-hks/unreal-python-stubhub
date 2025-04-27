## RigUnit_HierarchyCreatePoseItemArray Objects

```python
class RigUnit_HierarchyCreatePoseItemArray(RigUnit_HierarchyBase)
```

Creates the hierarchy's pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[RigUnit_HierarchyCreatePoseItemArray_Entry]):  [Read-Write] The entries to create
- ``pose`` (RigPose):  [Read-Write]

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray.__init__"></a>

#### __init__

```python
def __init__(entries: Array[RigUnit_HierarchyCreatePoseItemArray_Entry] = [],
             pose: RigPose = []) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray.entries"></a>

#### entries

```python
@property
def entries() -> Array[RigUnit_HierarchyCreatePoseItemArray_Entry]
```

(Array[RigUnit_HierarchyCreatePoseItemArray_Entry]):  [Read-Write] The entries to create

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[RigUnit_HierarchyCreatePoseItemArray_Entry]) -> None
```

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Only]

<a id="unreal.RigUnit_InteractionExecution"></a>