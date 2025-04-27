## RigUnit_ParentConstraintMath_AdvancedSettings Objects

```python
class RigUnit_ParentConstraintMath_AdvancedSettings(StructBase)
```

Rig Unit Parent Constraint Math Advanced Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interpolation_type`` (ConstraintInterpType):  [Read-Write] Options for interpolating rotations

<a id="unreal.RigUnit_ParentConstraintMath_AdvancedSettings.__init__"></a>

#### __init__

```python
def __init__(
    interpolation_type: ConstraintInterpType = ConstraintInterpType.AVERAGE
) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath_AdvancedSettings.interpolation_type"></a>

#### interpolation_type

```python
@property
def interpolation_type() -> ConstraintInterpType
```

(ConstraintInterpType):  [Read-Write] Options for interpolating rotations

<a id="unreal.RigUnit_ParentConstraintMath_AdvancedSettings.interpolation_type"></a>

#### interpolation_type

```python
@interpolation_type.setter
def interpolation_type(value: ConstraintInterpType) -> None
```

<a id="unreal.RigUnit_ParentConstraintMath"></a>