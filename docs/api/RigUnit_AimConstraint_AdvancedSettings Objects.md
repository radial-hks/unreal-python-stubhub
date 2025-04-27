## RigUnit_AimConstraint_AdvancedSettings Objects

```python
class RigUnit_AimConstraint_AdvancedSettings(StructBase)
```

Rig Unit Aim Constraint Advanced Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_AimBone.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_settings`` (RigUnit_AimBone_DebugSettings):  [Read-Write] Settings related to debug drawings
- ``rotation_order_for_filter`` (EulerRotationOrder):  [Read-Write] Rotation is converted to euler angles using the specified order such that individual axes can be filtered.

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings.__init__"></a>

#### __init__

```python
def __init__(
    debug_settings: RigUnit_AimBone_DebugSettings = [
        False, 10.000000,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]]
    ],
    rotation_order_for_filter: EulerRotationOrder = EulerRotationOrder.XYZ
) -> None
```

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> RigUnit_AimBone_DebugSettings
```

(RigUnit_AimBone_DebugSettings):  [Read-Write] Settings related to debug drawings

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: RigUnit_AimBone_DebugSettings) -> None
```

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings.rotation_order_for_filter"></a>

#### rotation_order_for_filter

```python
@property
def rotation_order_for_filter() -> EulerRotationOrder
```

(EulerRotationOrder):  [Read-Write] Rotation is converted to euler angles using the specified order such that individual axes can be filtered.

<a id="unreal.RigUnit_AimConstraint_AdvancedSettings.rotation_order_for_filter"></a>

#### rotation_order_for_filter

```python
@rotation_order_for_filter.setter
def rotation_order_for_filter(value: EulerRotationOrder) -> None
```

<a id="unreal.RigUnit_AimConstraintLocalSpaceOffset"></a>