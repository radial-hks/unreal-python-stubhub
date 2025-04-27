## RigUnit_PoseGetTransformArray Objects

```python
class RigUnit_PoseGetTransformArray(RigUnit_HierarchyBase)
```

Returns an array of transforms from a given hierarchy pose

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``pose`` (RigPose):  [Read-Write]
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space
- ``transforms`` (Array[Transform]):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.RigUnit_PoseGetTransformArray.__init__"></a>

#### __init__

```python
def __init__(pose: RigPose = [],
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             valid: bool = False,
             transforms: Array[Transform] = []) -> None
```

<a id="unreal.RigUnit_PoseGetTransformArray.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetTransformArray.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetTransformArray.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the transform should be retrieved in local or global space

<a id="unreal.RigUnit_PoseGetTransformArray.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_PoseGetTransformArray.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_PoseGetTransformArray.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Only]

<a id="unreal.RigUnit_PoseGetCurve"></a>