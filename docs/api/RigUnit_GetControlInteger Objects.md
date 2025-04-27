## RigUnit_GetControlInteger Objects

```python
class RigUnit_GetControlInteger(RigUnit)
```

GetControlFloat is used to retrieve a single Integer from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the Integer for.
- ``integer_value`` (int32):  [Read-Write] The current value of the control.
- ``maximum`` (int32):  [Read-Write] The maximum value of the control.
- ``minimum`` (int32):  [Read-Write] The minimum value of the control.

<a id="unreal.RigUnit_GetControlInteger.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             integer_value: int = 0,
             minimum: int = 0,
             maximum: int = 0) -> None
```

<a id="unreal.RigUnit_GetControlInteger.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the Integer for.

<a id="unreal.RigUnit_GetControlInteger.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlInteger.integer_value"></a>

#### integer_value

```python
@property
def integer_value() -> int
```

(int32):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlInteger.minimum"></a>

#### minimum

```python
@property
def minimum() -> int
```

(int32):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlInteger.maximum"></a>

#### maximum

```python
@property
def maximum() -> int
```

(int32):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetControlVector2D"></a>