## RigUnit_GetControlFloat Objects

```python
class RigUnit_GetControlFloat(RigUnit)
```

GetControlFloat is used to retrieve a single Float from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the Float for.
- ``float_value`` (float):  [Read-Write] The current value of the control.
- ``maximum`` (float):  [Read-Write] The maximum value of the control.
- ``minimum`` (float):  [Read-Write] The minimum value of the control.

<a id="unreal.RigUnit_GetControlFloat.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             float_value: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000) -> None
```

<a id="unreal.RigUnit_GetControlFloat.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the Float for.

<a id="unreal.RigUnit_GetControlFloat.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlFloat.float_value"></a>

#### float_value

```python
@property
def float_value() -> float
```

(float):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlFloat.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(float):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlFloat.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(float):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetControlInteger"></a>