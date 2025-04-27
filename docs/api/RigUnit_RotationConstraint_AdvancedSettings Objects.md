## RigUnit_RotationConstraint_AdvancedSettings Objects

```python
class RigUnit_RotationConstraint_AdvancedSettings(StructBase)
```

Rig Unit Rotation Constraint Advanced Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_TransformConstraint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``interpolation_type`` (ConstraintInterpType):  [Read-Write] Options for interpolating rotations
- ``rotation_order_for_filter`` (EulerRotationOrder):  [Read-Write] Rotation is converted to euler angles using the specified order such that individual axes can be filtered.

<a id="unreal.RigUnit_RotationConstraint_AdvancedSettings.__init__"></a>

#### __init__

```python
def __init__(
    interpolation_type: ConstraintInterpType = ConstraintInterpType.AVERAGE,
    rotation_order_for_filter: EulerRotationOrder = EulerRotationOrder.XYZ
) -> None
```

<a id="unreal.RigUnit_RotationConstraint_AdvancedSettings.interpolation_type"></a>

#### interpolation_type

```python
@property
def interpolation_type() -> ConstraintInterpType
```

(ConstraintInterpType):  [Read-Write] Options for interpolating rotations

<a id="unreal.RigUnit_RotationConstraint_AdvancedSettings.interpolation_type"></a>

#### interpolation_type

```python
@interpolation_type.setter
def interpolation_type(value: ConstraintInterpType) -> None
```

<a id="unreal.RigUnit_RotationConstraint_AdvancedSettings.rotation_order_for_filter"></a>

#### rotation_order_for_filter

```python
@property
def rotation_order_for_filter() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write] Rotation is converted to euler angles using the specified order such that individual axes can be filtered.

<a id="unreal.RigUnit_RotationConstraint_AdvancedSettings.rotation_order_for_filter"></a>

#### rotation_order_for_filter

```python
@rotation_order_for_filter.setter
def rotation_order_for_filter(value: EulerRotationOrder) -> None
```

<a id="unreal.RigUnit_RotationConstraint"></a>