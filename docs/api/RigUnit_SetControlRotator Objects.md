## RigUnit_SetControlRotator Objects

```python
class RigUnit_SetControlRotator(RigUnitMutable)
```

SetControlRotator is used to perform a change in the hierarchy by setting a single control's Rotator value.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``rotator`` (Rotator):  [Read-Write] The transform value to set for the given Control.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.
- ``weight`` (float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlRotator.__init__"></a>

#### __init__

```python
def __init__(
        execute_context: ControlRigExecuteContext = [],
        control: Name = "None",
        weight: float = 0.000000,
        rotator: Rotator = [0.000000, 0.000000, 0.000000],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_SetControlRotator.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetControlRotator.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetControlRotator.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] The weight of the change - how much the change should be applied

<a id="unreal.RigUnit_SetControlRotator.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.RigUnit_SetControlRotator.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetControlRotator.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Rotator) -> None
```

<a id="unreal.RigUnit_SetControlRotator.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetControlRotator.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator_Entry"></a>