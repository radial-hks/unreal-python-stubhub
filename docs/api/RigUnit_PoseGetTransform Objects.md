## RigUnit_PoseGetTransform Objects

```python
class RigUnit_PoseGetTransform(RigUnit_HierarchyBase)
```

Returns the hierarchy's pose transform

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_value`` (float):  [Read-Write]
- ``item`` (RigElementKey):  [Read-Write]
- ``pose`` (RigPose):  [Read-Write]
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space
- ``transform`` (Transform):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.RigUnit_PoseGetTransform.__init__"></a>

#### __init__

```python
def __init__(pose: RigPose = [],
             item: RigElementKey = [RigElementType.NONE, "None"],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             valid: bool = False,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             curve_value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_PoseGetTransform.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetTransform.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetTransform.item"></a>

#### item

```python
@property
def item() -> RigElementKey
```

(RigElementKey):  [Read-Write]

<a id="unreal.RigUnit_PoseGetTransform.item"></a>

#### item

```python
@item.setter
def item(value: RigElementKey) -> None
```

<a id="unreal.RigUnit_PoseGetTransform.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space

<a id="unreal.RigUnit_PoseGetTransform.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_PoseGetTransform.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_PoseGetTransform.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Only]

<a id="unreal.RigUnit_PoseGetTransform.curve_value"></a>

#### curve_value

```python
@property
def curve_value() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_PoseGetTransformArray"></a>