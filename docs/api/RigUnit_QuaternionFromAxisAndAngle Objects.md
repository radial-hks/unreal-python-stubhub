## RigUnit_QuaternionFromAxisAndAngle Objects

```python
class RigUnit_QuaternionFromAxisAndAngle(RigUnit)
```

Rig Unit Quaternion from Axis and Angle

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_Quaternion.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write]
- ``axis`` (Vector):  [Read-Write]
- ``result`` (Quat):  [Read-Write]

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.__init__"></a>

#### __init__

```python
def __init__(axis: Vector = [0.000000, 0.000000, 0.000000],
             angle: float = 0.000000,
             result: Quat = [0.000000, 0.000000, 0.000000, 1.000000]) -> None
```

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.axis"></a>

#### axis

```python
@property
def axis() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.axis"></a>

#### axis

```python
@axis.setter
def axis(value: Vector) -> None
```

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write]

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.RigUnit_QuaternionFromAxisAndAngle.result"></a>

#### result

```python
@property
def result() -> Quat
```

(Quat):  [Read-Only]

<a id="unreal.RigUnit_QuaternionToAngle"></a>