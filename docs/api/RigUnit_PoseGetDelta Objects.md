## RigUnit_PoseGetDelta Objects

```python
class RigUnit_PoseGetDelta(RigUnit_HierarchyBase)
```

Compares two pose caches and compares their values.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_threshold`` (float):  [Read-Write] The delta threshold for curve value difference. 0.0 disables curve differences.
- ``element_type`` (RigElementType):  [Read-Write]
- ``items_to_compare`` (RigElementKeyCollection):  [Read-Write] An optional list of items to compare
- ``items_with_delta`` (RigElementKeyCollection):  [Read-Write]
- ``pose_a`` (RigPose):  [Read-Write]
- ``pose_b`` (RigPose):  [Read-Write]
- ``poses_are_equal`` (bool):  [Read-Write]
- ``position_threshold`` (float):  [Read-Write] The delta threshold for a translation / position difference. 0.0 disables position differences.
- ``rotation_threshold`` (float):  [Read-Write] The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences.
- ``scale_threshold`` (float):  [Read-Write] The delta threshold for a scale difference. 0.0 disables scale differences.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines in which space transform deltas should be computed

<a id="unreal.RigUnit_PoseGetDelta.__init__"></a>

#### __init__

```python
def __init__(pose_a: RigPose = [],
             pose_b: RigPose = [],
             position_threshold: float = 0.000000,
             rotation_threshold: float = 0.000000,
             scale_threshold: float = 0.000000,
             curve_threshold: float = 0.000000,
             element_type: RigElementType = RigElementType.NONE,
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             items_to_compare: RigElementKeyCollection = [[]],
             poses_are_equal: bool = False,
             items_with_delta: RigElementKeyCollection = [[]]) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.pose_a"></a>

#### pose_a

```python
@property
def pose_a() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetDelta.pose_a"></a>

#### pose_a

```python
@pose_a.setter
def pose_a(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.pose_b"></a>

#### pose_b

```python
@property
def pose_b() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetDelta.pose_b"></a>

#### pose_b

```python
@pose_b.setter
def pose_b(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.position_threshold"></a>

#### position_threshold

```python
@property
def position_threshold() -> float
```

(float):  [Read-Write] The delta threshold for a translation / position difference. 0.0 disables position differences.

<a id="unreal.RigUnit_PoseGetDelta.position_threshold"></a>

#### position_threshold

```python
@position_threshold.setter
def position_threshold(value: float) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.rotation_threshold"></a>

#### rotation_threshold

```python
@property
def rotation_threshold() -> float
```

(float):  [Read-Write] The delta threshold for a rotation difference (in degrees). 0.0 disables rotation differences.

<a id="unreal.RigUnit_PoseGetDelta.rotation_threshold"></a>

#### rotation_threshold

```python
@rotation_threshold.setter
def rotation_threshold(value: float) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.scale_threshold"></a>

#### scale_threshold

```python
@property
def scale_threshold() -> float
```

(float):  [Read-Write] The delta threshold for a scale difference. 0.0 disables scale differences.

<a id="unreal.RigUnit_PoseGetDelta.scale_threshold"></a>

#### scale_threshold

```python
@scale_threshold.setter
def scale_threshold(value: float) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.curve_threshold"></a>

#### curve_threshold

```python
@property
def curve_threshold() -> float
```

(float):  [Read-Write] The delta threshold for curve value difference. 0.0 disables curve differences.

<a id="unreal.RigUnit_PoseGetDelta.curve_threshold"></a>

#### curve_threshold

```python
@curve_threshold.setter
def curve_threshold(value: float) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.element_type"></a>

#### element_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write]

<a id="unreal.RigUnit_PoseGetDelta.element_type"></a>

#### element_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines in which space transform deltas should be computed

<a id="unreal.RigUnit_PoseGetDelta.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.items_to_compare"></a>

#### items_to_compare

```python
@property
def items_to_compare() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] An optional list of items to compare

<a id="unreal.RigUnit_PoseGetDelta.items_to_compare"></a>

#### items_to_compare

```python
@items_to_compare.setter
def items_to_compare(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_PoseGetDelta.poses_are_equal"></a>

#### poses_are_equal

```python
@property
def poses_are_equal() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_PoseGetDelta.items_with_delta"></a>

#### items_with_delta

```python
@property
def items_with_delta() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Only]

<a id="unreal.RigUnit_PoseGetTransform"></a>