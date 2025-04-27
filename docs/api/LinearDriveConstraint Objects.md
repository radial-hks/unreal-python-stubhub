## LinearDriveConstraint Objects

```python
class LinearDriveConstraint(StructBase)
```

Linear Drive

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintDrives.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceleration_mode`` (bool):  [Read-Write]
- ``enable_position_drive`` (bool):  [Read-Write]
  deprecated: Enable/disable of drives is done inside the individual constraint drives.
- ``position_target`` (Vector):  [Read-Write] Target position the linear drive.
- ``velocity_target`` (Vector):  [Read-Write] Target velocity the linear drive.
- ``x_drive`` (ConstraintDrive):  [Read-Write]
- ``y_drive`` (ConstraintDrive):  [Read-Write]
- ``z_drive`` (ConstraintDrive):  [Read-Write]

<a id="unreal.LinearDriveConstraint.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.LinearDriveConstraint.enable_position_drive"></a>

#### enable_position_drive

```python
@property
def enable_position_drive() -> bool
```

(bool):  [Read-Write]
deprecated: Enable/disable of drives is done inside the individual constraint drives.

<a id="unreal.LinearDriveConstraint.enable_position_drive"></a>

#### enable_position_drive

```python
@enable_position_drive.setter
def enable_position_drive(value: bool) -> None
```

<a id="unreal.AngularDriveConstraint"></a>