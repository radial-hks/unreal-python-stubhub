## RigUnit_GetCurveValue Objects

```python
class RigUnit_GetCurveValue(RigUnit)
```

GetCurveValue is used to retrieve a single float from a Curve

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetCurveValue.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve`` (Name):  [Read-Write] The name of the Curve to retrieve the transform for.
- ``valid`` (bool):  [Read-Write]
- ``value`` (float):  [Read-Write] The current transform of the given Curve - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetCurveValue.__init__"></a>

#### __init__

```python
def __init__(curve: Name = "None",
             valid: bool = False,
             value: float = 0.000000) -> None
```

<a id="unreal.RigUnit_GetCurveValue.curve"></a>

#### curve

```python
@property
def curve() -> Name
```

(Name):  [Read-Write] The name of the Curve to retrieve the transform for.

<a id="unreal.RigUnit_GetCurveValue.curve"></a>

#### curve

```python
@curve.setter
def curve(value: Name) -> None
```

<a id="unreal.RigUnit_GetCurveValue.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Only]

<a id="unreal.RigUnit_GetCurveValue.value"></a>

#### value

```python
@property
def value() -> float
```

(float):  [Read-Only] The current transform of the given Curve - or identity in case it wasn't found.

<a id="unreal.RigUnit_GetInitialBoneTransform"></a>