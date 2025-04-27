## RigUnit_SetControlInteger Objects

```python
class RigUnit_SetControlInteger(RigUnitMutable)
```

SetControlInteger is used to perform a change in the hierarchy by setting a single control's int32 value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``integer_value`` (int32):  [Read-Write] The transform value to set for the given Control.
- ``weight`` (int32):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlInteger.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             control: Name = "None",
             weight: int = 0,
             integer_value: int = 0) -> None
```

<a id="unreal.RigUnit_SetControlInteger.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlInteger.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlInteger.weight"></a>

#### weight

```python
@property
def weight() -> int
```

(int32):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlInteger.weight"></a>

#### weight

```python
@weight.setter
def weight(value: int) -> None
```

<a id="unreal.RigUnit_SetControlInteger.integer_value"></a>

#### integer_value

```python
@property
def integer_value() -> int
```

(int32):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetControlInteger.integer_value"></a>

#### integer_value

```python
@integer_value.setter
def integer_value(value: int) -> None
```

<a id="unreal.RigUnit_SetMultiControlInteger_Entry"></a>