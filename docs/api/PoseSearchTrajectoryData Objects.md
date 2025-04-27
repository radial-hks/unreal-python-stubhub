## PoseSearchTrajectoryData Objects

```python
class PoseSearchTrajectoryData(StructBase)
```

Pose Search Trajectory Data

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchTrajectoryLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acceleration_remapping_curve`` (RuntimeFloatCurve):  [Read-Write]
- ``bend_velocity_towards_acceleration`` (float):  [Read-Write] artificially bend character velocity towards acceleration direction to compute trajectory prediction, to get sharper turns
  0: character velocity is used with no alteration, 1: the acceleration direction is used as velocity direction
- ``max_controller_yaw_rate`` (float):  [Read-Write] Maximum controller yaw  rate in degrees per second used to clamp the character owner controller desired yaw to generate the prediction trajectory.
  Negative values disable the clamping behavior
- ``rotate_towards_movement_speed`` (float):  [Read-Write] If the character is forward facing (i.e. bOrientRotationToMovement is true), this controls how quickly the trajectory will rotate
  to face acceleration. It's common for this to differ from the rotation rate of the character, because animations are often authored
  with different rotation speeds than the character. This is especially true in cases where the character rotation snaps to movement.
- ``speed_remapping_curve`` (RuntimeFloatCurve):  [Read-Write]
- ``use_acceleration_remapping_curve`` (bool):  [Read-Write]
- ``use_speed_remapping_curve`` (bool):  [Read-Write]

<a id="unreal.PoseSearchTrajectoryData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PoseSearchTrajectory_WorldCollisionResults"></a>