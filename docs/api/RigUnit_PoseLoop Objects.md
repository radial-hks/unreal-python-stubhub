## RigUnit_PoseLoop Objects

```python
class RigUnit_PoseLoop(RigUnit_HierarchyBaseMutable)
```

Given a pose, execute iteratively across all items in the pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``completed`` (ControlRigExecuteContext):  [Read-Write]
- ``count`` (int32):  [Read-Write]
- ``curve_value`` (float):  [Read-Write]
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``global_transform`` (Transform):  [Read-Write]
- ``index`` (int32):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``local_transform`` (Transform):  [Read-Write]
- ``pose`` (RigPose):  [Read-Write]
- ``ratio`` (float):  [Read-Write] Ranging from 0.0 (first item) and 1.0 (last item)
  This is useful to drive a consecutive node with a
  curve or an ease to distribute a value.

<a id="unreal.RigUnit_PoseLoop.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             pose: RigPose = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             global_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             curve_value: float = 0.000000,
             index: int = 0,
             count: int = 0,
             ratio: float = 0.000000,
             completed: ControlRigExecuteContext = []) -> None
```

<a id="unreal.RigUnit_PoseLoop.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseLoop.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseLoop.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.global_transform"></a>

#### global_transform

```python
@property
def global_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.curve_value"></a>

#### curve_value

```python
@property
def curve_value() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.count"></a>

#### count

```python
@property
def count() -> int
```

(int32):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Only] Ranging from 0.0 (first item) and 1.0 (last item)
This is useful to drive a consecutive node with a
curve or an ease to distribute a value.

<a id="unreal.RigUnit_PoseLoop.completed"></a>

#### completed

```python
@property
def completed() -> ControlRigExecuteContext
```

(ControlRigExecuteContext):  [Read-Only]

<a id="unreal.RigUnit_HierarchyCreatePoseItemArray_Entry"></a>