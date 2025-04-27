## RigUnit_SetMultiControlRotator_Entry Objects

```python
class RigUnit_SetMultiControlRotator_Entry(StructBase)
```

Rig Unit Set Multi Control Rotator Entry

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SetControlTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``control`` (Name):  [Read-Write] The name of the Control to set the transform for.
- ``rotator`` (Rotator):  [Read-Write] The transform value to set for the given Control.
- ``space`` (RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
  in local or global space.

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.__init__"></a>

#### __init__

```python
def __init__(
        control: Name = "None",
        rotator: Rotator = [0.000000, 0.000000, 0.000000],
        space: RigVMTransformSpace = RigVMTransformSpace.LOCAL_SPACE) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.control"></a>

#### control

```python
@property
def control() -> Name
```

(Name):  [Read-Write] The name of the Control to set the transform for.

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.control"></a>

#### control

```python
@control.setter
def control(value: Name) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Write] The transform value to set for the given Control.

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.rotator"></a>

#### rotator

```python
@rotator.setter
def rotator(value: Rotator) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.space"></a>

#### space

```python
@property
def space() -> RigVMTransformSpace
```

(RigVMTransformSpace):  [Read-Write] Defines if the bone's transform should be set
in local or global space.

<a id="unreal.RigUnit_SetMultiControlRotator_Entry.space"></a>

#### space

```python
@space.setter
def space(value: RigVMTransformSpace) -> None
```

<a id="unreal.RigUnit_SetMultiControlRotator"></a>