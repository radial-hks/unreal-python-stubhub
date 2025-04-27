## AngularDriveConstraint Objects

```python
class AngularDriveConstraint(StructBase)
```

Angular Drive

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintDrives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceleration_mode`` (bool):  [Read-Write]
- ``angular_drive_mode`` (AngularDriveMode):  [Read-Write] Whether motors use SLERP (spherical lerp) or decompose into a Swing motor (cone constraints) and Twist motor (roll constraints). NOTE: SLERP will NOT work if any of the angular constraints are locked.
- ``angular_velocity_target`` (Vector):  [Read-Write] Target angular velocity relative to the body reference frame in revolutions per second.
- ``orientation_target`` (Rotator):  [Read-Write] Target orientation relative to the the body reference frame.
- ``slerp_drive`` (ConstraintDrive):  [Read-Write] Controls the SLERP (spherical lerp) drive between current orientation/velocity and target orientation/velocity. NOTE: This is only available when all three angular limits are either free or limited. Locking any angular limit will turn off the drive implicitly.
- ``swing_drive`` (ConstraintDrive):  [Read-Write] Controls the cone constraint drive between current orientation/velocity and target orientation/velocity. This is available as long as there is at least one swing limit set to free or limited.
- ``twist_drive`` (ConstraintDrive):  [Read-Write] Controls the twist (roll) constraint drive between current orientation/velocity and target orientation/velocity. This is available as long as the twist limit is set to free or limited.

<a id="unreal.AngularDriveConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SkeletalMeshSamplingRegionMaterialFilter"></a>