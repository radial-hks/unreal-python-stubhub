## RigUnit_GetControlRotator Objects

```python
class RigUnit_GetControlRotator(RigUnit)
```

GetControlRotator is used to retrieve a single Rotator from a hierarchy.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_GetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to retrieve the Rotator for.
- ``maximum`` (Rotator):  [Read-Write] The maximum value of the control.
- ``minimum`` (Rotator):  [Read-Write] The minimum value of the control.
- ``rotator`` (Rotator):  [Read-Write] The current value of the control.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the Control's Rotator should be retrieved
  in local or global space.

<a id="unreal.RigUnit_GetControlRotator.__init__"></a>

#### __init__

```python
def __init__(control: Name = "None",
             space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE,
             rotator: Rotator = [0.000000, 0.000000, 0.000000],
             minimum: Rotator = [0.000000, 0.000000, 0.000000],
             maximum: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigUnit_GetControlRotator.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to retrieve the Rotator for.

<a id="unreal.RigUnit_GetControlRotator.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_GetControlRotator.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the Control's Rotator should be retrieved
in local or global space.

<a id="unreal.RigUnit_GetControlRotator.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_GetControlRotator.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only] The current value of the control.

<a id="unreal.RigUnit_GetControlRotator.minimum"></a>

#### minimum

```python
@property
def minimum() -> Rotator
```

(Rotator):  [Read-Only] The minimum value of the control.

<a id="unreal.RigUnit_GetControlRotator.maximum"></a>

#### maximum

```python
@property
def maximum() -> Rotator
```

(Rotator):  [Read-Only] The maximum value of the control.

<a id="unreal.RigUnit_GetControlTransform"></a>