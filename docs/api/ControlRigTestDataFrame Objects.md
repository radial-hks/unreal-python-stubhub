## ControlRigTestDataFrame Objects

```python
class ControlRigTestDataFrame(StructBase)
```

Control Rig Test Data Frame

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigTestData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_time`` (double):  [Read-Only]
- ``delta_time`` (double):  [Read-Only]
- ``pose`` (RigPose):  [Read-Only]
- ``variables`` (Array[ControlRigTestDataVariable]):  [Read-Only]

<a id="unreal.ControlRigTestDataFrame.__init__"></a>

#### __init__

```python
def __init__(absolute_time: float = 0.000000,
             delta_time: float = 0.000000,
             variables: Array[ControlRigTestDataVariable] = [],
             pose: RigPose = []) -> None
```

<a id="unreal.ControlRigTestDataFrame.absolute_time"></a>

#### absolute_time

```python
@property
def absolute_time() -> float
```

(double):  [Read-Only]

<a id="unreal.ControlRigTestDataFrame.delta_time"></a>

#### delta_time

```python
@property
def delta_time() -> float
```

(double):  [Read-Only]

<a id="unreal.ControlRigTestDataFrame.variables"></a>

#### variables

```python
@property
def variables() -> Array[ControlRigTestDataVariable]
```

(Array[ControlRigTestDataVariable]):  [Read-Only]

<a id="unreal.ControlRigTestDataFrame.pose"></a>

#### pose

```python
@property
def pose() -> RigPose
```

(RigPose):  [Read-Only]

<a id="unreal.RigPose"></a>