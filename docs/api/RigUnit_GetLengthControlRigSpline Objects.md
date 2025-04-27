## RigUnit_GetLengthControlRigSpline Objects

```python
class RigUnit_GetLengthControlRigSpline(RigUnit)
```

* Retrieves the length from a given Splin

**C++ Source:**

- **Plugin**: ControlRigSpline
- **Module**: ControlRigSpline
- **File**: ControlRigSplineUnits.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``length`` (float):  [Read-Write]
- ``spline`` (ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_GetLengthControlRigSpline.__init__"></a>

#### __init__

```python
def __init__(spline: ControlRigSpline = [], length: float = 0.000000) -> None
```

<a id="unreal.RigUnit_GetLengthControlRigSpline.spline"></a>

#### spline

```python
@property
def spline() -> ControlRigSpline
```

(ControlRigSpline):  [Read-Write]

<a id="unreal.RigUnit_GetLengthControlRigSpline.spline"></a>

#### spline

```python
@spline.setter
def spline(value: ControlRigSpline) -> None
```

<a id="unreal.RigUnit_GetLengthControlRigSpline.length"></a>

#### length

```python
@property
def length() -> float
```

(float):  [Read-Only]

<a id="unreal.RigUnit_GetLengthAtParamControlRigSpline"></a>