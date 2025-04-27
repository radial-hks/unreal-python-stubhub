## ConstraintDrive Objects

```python
class ConstraintDrive(StructBase)
```

Constraint Drive

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintDrives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``damping`` (float):  [Read-Write] The damping strength of the drive. Force proportional to the velocity error.
- ``enable_position_drive`` (bool):  [Read-Write] Enables/Disables position drive (orientation if using angular drive)
- ``enable_velocity_drive`` (bool):  [Read-Write] Enables/Disables velocity drive (angular velocity if using angular drive)
- ``max_force`` (float):  [Read-Write] The force limit of the drive.
- ``stiffness`` (float):  [Read-Write] The spring strength of the drive. Force proportional to the position error.

<a id="unreal.ConstraintDrive.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.NiagaraLinearRamp"></a>