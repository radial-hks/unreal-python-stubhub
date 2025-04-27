## SimSpaceSettings Objects

```python
class SimSpaceSettings(StructBase)
```

Sim Space Settings

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RigidBody.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``external_angular_velocity`` (Vector):  [Read-Write] Additional angular velocity that is added to the component angular velocity. This can be used to make the simulation act as if the actor is rotating
  even when it is not. E.g., to apply physics to a character on a podium as the camera rotates around it, to emulate the podium itself rotating.
  Vector is in world space. Units are rad/s.
- ``external_linear_drag`` (float):  [Read-Write]
  deprecated: ExternalLinearDrag is deprecated. Please use ExternalLinearDragV instead.
- ``external_linear_drag_v`` (Vector):  [Read-Write] Additional linear drag applied to every body in addition to linear drag specified on them in the physics asset.
  When combined with ExternalLinearVelocity, this can be used to add a temporary wind-blown effect without having to tune linear drag on
  all the bodies in the physics asset. The result is that each body has a force equal to -ExternalLinearDragV * ExternalLinearVelocity applied to it, in
  additional to all other forces. The vector is in simulation local space.
- ``external_linear_velocity`` (Vector):  [Read-Write] Additional velocity that is added to the component velocity so the simulation acts as if the actor is moving at speed, even when stationary.
  Vector is in world space. Units are cm/s. Could be used for a wind effects etc. Typical values are similar to the velocity of the object or effect,
  and usually around or less than 1000 for characters/wind.
- ``max_angular_acceleration`` (float):  [Read-Write] A clamp on the effective world-space angular accleration that is passed to the simulation. Units are radian/s/s. The default value effectively means "unlimited".
  This has a similar effect to MaxAngularVelocity, except that it is related to the flying out of bodies when the rotation speed suddenly changes. Typical limist for
  a character might be around 100.
- ``max_angular_velocity`` (float):  [Read-Write] A clamp on the effective world-space angular velocity that is passed to the simulation. Units are radian/s, so a value of about 6.0 is one rotation per second.
  The default value effectively means "unlimited". You would reduce this (and MaxAngularAcceleration) to limit how much bodies "fly out" when the actor spins on the spot.
  This is especially useful if you have characters than can rotate very quickly and you would probably want values around or less than 10 in this case.
- ``max_linear_acceleration`` (float):  [Read-Write] A clamp on the effective world-space acceleration that is passed to the simulation. Units are cm/s/s. The default value effectively means "unlimited".
  This property is used to stop the bodies of the simulation flying out when suddenly changing linear speed. It is useful when you have characters than can
  changes from stationary to running very quickly such as in an FPS. A common value for a character might be in the few hundreds.
- ``max_linear_velocity`` (float):  [Read-Write] A clamp on the effective world-space velocity that is passed to the simulation. Units are cm/s. The default value effectively means "unlimited". It is not usually required to
  change this but you would reduce this to limit the effects of drag on the bodies in the simulation (if you have bodies that have LinearDrag set to non-zero in the physics asset).
  Expected values in this case would be somewhat less than the usual velocities of your object which is commonly a few hundred for a character.
- ``velocity_scale_z`` (float):  [Read-Write] Multiplier on the Z-component of velocity and acceleration that is passed to the simulation. Usually from 0.0 to 1.0 to
  reduce the effects of jumping and crouching on the simulation, but it can be higher than 1.0 if you need to exaggerate this motion for some reason.
- ``world_alpha`` (float):  [Read-Write] Global multipler on the effects of simulation space movement. Must be in range [0, 1]. If WorldAlpha = 0.0, the system is disabled and the simulation will
  be fully local (i.e., world-space actor movement and rotation does not affect the simulation). When WorldAlpha = 1.0 the simulation effectively acts as a
  world-space sim, but with the ability to apply limits using the other parameters.

<a id="unreal.SimSpaceSettings.__init__"></a>

#### __init__

```python
def __init__(
    world_alpha: float = 0.000000,
    velocity_scale_z: float = 0.000000,
    max_linear_velocity: float = 0.000000,
    max_angular_velocity: float = 0.000000,
    max_linear_acceleration: float = 0.000000,
    max_angular_acceleration: float = 0.000000,
    external_linear_drag_v: Vector = [0.000000, 0.000000, 0.000000],
    external_linear_velocity: Vector = [0.000000, 0.000000, 0.000000],
    external_angular_velocity: Vector = [0.000000, 0.000000,
                                         0.000000]) -> None
```

<a id="unreal.SimSpaceSettings.world_alpha"></a>

#### world_alpha

```python
@property
def world_alpha() -> float
```

(float):  [Read-Write] Global multipler on the effects of simulation space movement. Must be in range [0, 1]. If WorldAlpha = 0.0, the system is disabled and the simulation will
be fully local (i.e., world-space actor movement and rotation does not affect the simulation). When WorldAlpha = 1.0 the simulation effectively acts as a
world-space sim, but with the ability to apply limits using the other parameters.

<a id="unreal.SimSpaceSettings.world_alpha"></a>

#### world_alpha

```python
@world_alpha.setter
def world_alpha(value: float) -> None
```

<a id="unreal.SimSpaceSettings.master_alpha"></a>

#### master_alpha

```python
@property
def master_alpha() -> float
```

deprecated: 'master_alpha' was renamed to 'world_alpha'.

<a id="unreal.SimSpaceSettings.master_alpha"></a>

#### master_alpha

```python
@master_alpha.setter
def master_alpha(value: float) -> None
```

<a id="unreal.SimSpaceSettings.velocity_scale_z"></a>

#### velocity_scale_z

```python
@property
def velocity_scale_z() -> float
```

(float):  [Read-Write] Multiplier on the Z-component of velocity and acceleration that is passed to the simulation. Usually from 0.0 to 1.0 to
reduce the effects of jumping and crouching on the simulation, but it can be higher than 1.0 if you need to exaggerate this motion for some reason.

<a id="unreal.SimSpaceSettings.velocity_scale_z"></a>

#### velocity_scale_z

```python
@velocity_scale_z.setter
def velocity_scale_z(value: float) -> None
```

<a id="unreal.SimSpaceSettings.max_linear_velocity"></a>

#### max_linear_velocity

```python
@property
def max_linear_velocity() -> float
```

(float):  [Read-Write] A clamp on the effective world-space velocity that is passed to the simulation. Units are cm/s. The default value effectively means "unlimited". It is not usually required to
change this but you would reduce this to limit the effects of drag on the bodies in the simulation (if you have bodies that have LinearDrag set to non-zero in the physics asset).
Expected values in this case would be somewhat less than the usual velocities of your object which is commonly a few hundred for a character.

<a id="unreal.SimSpaceSettings.max_linear_velocity"></a>

#### max_linear_velocity

```python
@max_linear_velocity.setter
def max_linear_velocity(value: float) -> None
```

<a id="unreal.SimSpaceSettings.max_angular_velocity"></a>

#### max_angular_velocity

```python
@property
def max_angular_velocity() -> float
```

(float):  [Read-Write] A clamp on the effective world-space angular velocity that is passed to the simulation. Units are radian/s, so a value of about 6.0 is one rotation per second.
The default value effectively means "unlimited". You would reduce this (and MaxAngularAcceleration) to limit how much bodies "fly out" when the actor spins on the spot.
This is especially useful if you have characters than can rotate very quickly and you would probably want values around or less than 10 in this case.

<a id="unreal.SimSpaceSettings.max_angular_velocity"></a>

#### max_angular_velocity

```python
@max_angular_velocity.setter
def max_angular_velocity(value: float) -> None
```

<a id="unreal.SimSpaceSettings.max_linear_acceleration"></a>

#### max_linear_acceleration

```python
@property
def max_linear_acceleration() -> float
```

(float):  [Read-Write] A clamp on the effective world-space acceleration that is passed to the simulation. Units are cm/s/s. The default value effectively means "unlimited".
This property is used to stop the bodies of the simulation flying out when suddenly changing linear speed. It is useful when you have characters than can
changes from stationary to running very quickly such as in an FPS. A common value for a character might be in the few hundreds.

<a id="unreal.SimSpaceSettings.max_linear_acceleration"></a>

#### max_linear_acceleration

```python
@max_linear_acceleration.setter
def max_linear_acceleration(value: float) -> None
```

<a id="unreal.SimSpaceSettings.max_angular_acceleration"></a>

#### max_angular_acceleration

```python
@property
def max_angular_acceleration() -> float
```

(float):  [Read-Write] A clamp on the effective world-space angular accleration that is passed to the simulation. Units are radian/s/s. The default value effectively means "unlimited".
This has a similar effect to MaxAngularVelocity, except that it is related to the flying out of bodies when the rotation speed suddenly changes. Typical limist for
a character might be around 100.

<a id="unreal.SimSpaceSettings.max_angular_acceleration"></a>

#### max_angular_acceleration

```python
@max_angular_acceleration.setter
def max_angular_acceleration(value: float) -> None
```

<a id="unreal.SimSpaceSettings.external_linear_drag"></a>

#### external_linear_drag

```python
@property
def external_linear_drag() -> float
```

(float):  [Read-Write]
deprecated: ExternalLinearDrag is deprecated. Please use ExternalLinearDragV instead.

<a id="unreal.SimSpaceSettings.external_linear_drag"></a>

#### external_linear_drag

```python
@external_linear_drag.setter
def external_linear_drag(value: float) -> None
```

<a id="unreal.SimSpaceSettings.external_linear_drag_v"></a>

#### external_linear_drag_v

```python
@property
def external_linear_drag_v() -> Vector
```

(Vector):  [Read-Write] Additional linear drag applied to every body in addition to linear drag specified on them in the physics asset.
When combined with ExternalLinearVelocity, this can be used to add a temporary wind-blown effect without having to tune linear drag on
all the bodies in the physics asset. The result is that each body has a force equal to -ExternalLinearDragV * ExternalLinearVelocity applied to it, in
additional to all other forces. The vector is in simulation local space.

<a id="unreal.SimSpaceSettings.external_linear_drag_v"></a>

#### external_linear_drag_v

```python
@external_linear_drag_v.setter
def external_linear_drag_v(value: Vector) -> None
```

<a id="unreal.SimSpaceSettings.external_linear_velocity"></a>

#### external_linear_velocity

```python
@property
def external_linear_velocity() -> Vector
```

(Vector):  [Read-Write] Additional velocity that is added to the component velocity so the simulation acts as if the actor is moving at speed, even when stationary.
Vector is in world space. Units are cm/s. Could be used for a wind effects etc. Typical values are similar to the velocity of the object or effect,
and usually around or less than 1000 for characters/wind.

<a id="unreal.SimSpaceSettings.external_linear_velocity"></a>

#### external_linear_velocity

```python
@external_linear_velocity.setter
def external_linear_velocity(value: Vector) -> None
```

<a id="unreal.SimSpaceSettings.external_angular_velocity"></a>

#### external_angular_velocity

```python
@property
def external_angular_velocity() -> Vector
```

(Vector):  [Read-Write] Additional angular velocity that is added to the component angular velocity. This can be used to make the simulation act as if the actor is rotating
even when it is not. E.g., to apply physics to a character on a podium as the camera rotates around it, to emulate the podium itself rotating.
Vector is in world space. Units are rad/s.

<a id="unreal.SimSpaceSettings.external_angular_velocity"></a>

#### external_angular_velocity

```python
@external_angular_velocity.setter
def external_angular_velocity(value: Vector) -> None
```

<a id="unreal.AnimNode_RigidBody"></a>