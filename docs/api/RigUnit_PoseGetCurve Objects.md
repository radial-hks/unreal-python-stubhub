## RigUnit_PoseGetCurve Objects

```python
class RigUnit_PoseGetCurve(RigUnit_HierarchyBase)
```

Returns the hierarchy's pose curve value

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Hierarchy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (Name):  [Read-Write]
- ``curve_value`` (float):  [Read-Write]
- ``pose`` (RigPose):  [Read-Write]
- ``valid`` (bool):  [Read-Write]

<a id="unreal.RigUnit_PoseGetCurve.__init__"></a>

#### __init__

```python
def __init__(pose: RigPose = [],
             curve: Name = "None",
             valid: bool = False,
             curve_value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_PoseGetCurve.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Write]

<a id="unreal.RigUnit_PoseGetCurve.pose"></a>

#### pose

```python
@pose.setter
def pose(value: RigPose) -> None
```

<a id="unreal.RigUnit_PoseGetCurve.curve"></a>

#### curve

```python
@property
def curve() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RigUnit_PoseGetCurve.curve"></a>

#### curve

```python
@curve.setter
def curve(value: Name) -> None
```

<a id="unreal.RigUnit_PoseGetCurve.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_PoseGetCurve.curve_value"></a>

#### curve_value

```python
@property
def curve_value() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_PoseLoop"></a>