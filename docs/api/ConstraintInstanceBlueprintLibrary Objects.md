## ConstraintInstanceBlueprintLibrary Objects

```python
class ConstraintInstanceBlueprintLibrary(BlueprintFunctionLibrary)
```

Constraint Instance Blueprint Library

**C++ Source:**

- **Module**: Engine
- **File**: ConstraintInstanceBlueprintLibrary.h

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_projection_params"></a>

#### set_projection_params

```python
@classmethod
def set_projection_params(
        cls, accessor: ConstraintInstanceAccessor, enable_projection: bool,
        projection_linear_alpha: float,
        projection_angular_alpha: float) -> ConstraintInstanceAccessor
```

X.set_projection_params(accessor, enable_projection, projection_linear_alpha, projection_angular_alpha) -> ConstraintInstanceAccessor
Sets projection parameters of the constraint

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_projection (bool): true to enable projection
    projection_linear_alpha (float): how much linear projection to apply in [0,1] range
    projection_angular_alpha (float): how much angular projection to apply in [0,1] range

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_parent_dominates"></a>

#### set_parent_dominates

```python
@classmethod
def set_parent_dominates(cls, accessor: ConstraintInstanceAccessor,
                         parent_dominates: bool) -> ConstraintInstanceAccessor
```

X.set_parent_dominates(accessor, parent_dominates) -> ConstraintInstanceAccessor
Sets whether the parent body is not affected by it's child motion

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    parent_dominates (bool): true to avoid the parent being affected by its child motion

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_orientation_drive_twist_and_swing"></a>

#### set_orientation_drive_twist_and_swing

```python
@classmethod
def set_orientation_drive_twist_and_swing(
        cls, accessor: ConstraintInstanceAccessor, enable_twist_drive: bool,
        enable_swing_drive: bool) -> ConstraintInstanceAccessor
```

X.set_orientation_drive_twist_and_swing(accessor, enable_twist_drive, enable_swing_drive) -> ConstraintInstanceAccessor
Enables/Disables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
    enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_orientation_drive_slerp"></a>

#### set_orientation_drive_slerp

```python
@classmethod
def set_orientation_drive_slerp(
        cls, accessor: ConstraintInstanceAccessor,
        enable_slerp: bool) -> ConstraintInstanceAccessor
```

X.set_orientation_drive_slerp(accessor, enable_slerp) -> ConstraintInstanceAccessor
Enables/Disables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_slerp (bool): Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_mass_conditioning_enabled"></a>

#### set_mass_conditioning_enabled

```python
@classmethod
def set_mass_conditioning_enabled(
        cls, accessor: ConstraintInstanceAccessor,
        enable_mass_conditioning: bool) -> ConstraintInstanceAccessor
```

X.set_mass_conditioning_enabled(accessor, enable_mass_conditioning) -> ConstraintInstanceAccessor

brief: Enable or disable mass conditioning for the constraint.

Args:
    accessor (ConstraintInstanceAccessor): 
    enable_mass_conditioning (bool): 

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor):

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_velocity_target"></a>

#### set_linear_velocity_target

```python
@classmethod
def set_linear_velocity_target(
        cls, accessor: ConstraintInstanceAccessor,
        vel_target: Vector) -> ConstraintInstanceAccessor
```

X.set_linear_velocity_target(accessor, vel_target) -> ConstraintInstanceAccessor
Sets the target velocity for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    vel_target (Vector): Target velocity

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_velocity_drive"></a>

#### set_linear_velocity_drive

```python
@classmethod
def set_linear_velocity_drive(
        cls, accessor: ConstraintInstanceAccessor, enable_drive_x: bool,
        enable_drive_y: bool,
        enable_drive_z: bool) -> ConstraintInstanceAccessor
```

X.set_linear_velocity_drive(accessor, enable_drive_x, enable_drive_y, enable_drive_z) -> ConstraintInstanceAccessor
Enables/Disables linear velocity drive

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_drive_x (bool): Indicates whether the drive for the X-Axis should be enabled
    enable_drive_y (bool): Indicates whether the drive for the Y-Axis should be enabled
    enable_drive_z (bool): Indicates whether the drive for the Z-Axis should be enabled

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_soft_limit_params"></a>

#### set_linear_soft_limit_params

```python
@classmethod
def set_linear_soft_limit_params(
        cls, accessor: ConstraintInstanceAccessor, soft_linear_limit: bool,
        linear_limit_stiffness: float, linear_limit_damping: float,
        linear_limit_restitution: float,
        linear_limit_contact_distance: float) -> ConstraintInstanceAccessor
```

X.set_linear_soft_limit_params(accessor, soft_linear_limit, linear_limit_stiffness, linear_limit_damping, linear_limit_restitution, linear_limit_contact_distance) -> ConstraintInstanceAccessor
Sets Constraint Linear Soft Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change *
    soft_linear_limit (bool): True is the linear limit is soft
    linear_limit_stiffness (float): Stiffness of the soft linear limit. Only used when Soft limit is on ( positive value )
    linear_limit_damping (float): Damping of the soft linear limit. Only used when Soft limit is on ( positive value )
    linear_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
    linear_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change *

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_position_target"></a>

#### set_linear_position_target

```python
@classmethod
def set_linear_position_target(
        cls, accessor: ConstraintInstanceAccessor,
        pos_target: Vector) -> ConstraintInstanceAccessor
```

X.set_linear_position_target(accessor, pos_target) -> ConstraintInstanceAccessor
Sets the target position for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    pos_target (Vector): Target position

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_position_drive"></a>

#### set_linear_position_drive

```python
@classmethod
def set_linear_position_drive(
        cls, accessor: ConstraintInstanceAccessor, enable_drive_x: bool,
        enable_drive_y: bool,
        enable_drive_z: bool) -> ConstraintInstanceAccessor
```

X.set_linear_position_drive(accessor, enable_drive_x, enable_drive_y, enable_drive_z) -> ConstraintInstanceAccessor
Enables/Disables linear position drive

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_drive_x (bool): Indicates whether the drive for the X-Axis should be enabled
    enable_drive_y (bool): Indicates whether the drive for the Y-Axis should be enabled
    enable_drive_z (bool): Indicates whether the drive for the Z-Axis should be enabled

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_plasticity"></a>

#### set_linear_plasticity

```python
@classmethod
def set_linear_plasticity(
        cls, accessor: ConstraintInstanceAccessor, linear_plasticity: bool,
        linear_plasticity_threshold: float,
        plasticity_type: ConstraintPlasticityType
) -> ConstraintInstanceAccessor
```

X.set_linear_plasticity(accessor, linear_plasticity, linear_plasticity_threshold, plasticity_type) -> ConstraintInstanceAccessor
Sets Constraint Linear Plasticity properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    linear_plasticity (bool): Whether it is possible to reset the target position from the linear displacement
    linear_plasticity_threshold (float): Delta from target needed to reset the target joint
    plasticity_type (ConstraintPlasticityType): 

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_limits"></a>

#### set_linear_limits

```python
@classmethod
def set_linear_limits(cls, accessor: ConstraintInstanceAccessor,
                      x_motion: LinearConstraintMotion,
                      y_motion: LinearConstraintMotion,
                      z_motion: LinearConstraintMotion,
                      limit: float) -> ConstraintInstanceAccessor
```

X.set_linear_limits(accessor, x_motion, y_motion, z_motion, limit) -> ConstraintInstanceAccessor
Sets Constraint Linear Motion Ranges

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    x_motion (LinearConstraintMotion): Type of motion along the X axis
    y_motion (LinearConstraintMotion): Type of motion along the Y axis
    z_motion (LinearConstraintMotion): Type of motion along the Z axis
    limit (float): linear limit to apply to all axis

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_drive_params"></a>

#### set_linear_drive_params

```python
@classmethod
def set_linear_drive_params(cls, accessor: ConstraintInstanceAccessor,
                            position_strength: float, velocity_strength: float,
                            force_limit: float) -> ConstraintInstanceAccessor
```

X.set_linear_drive_params(accessor, position_strength, velocity_strength, force_limit) -> ConstraintInstanceAccessor
Sets the drive params for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    position_strength (float): Positional strength for the drive (stiffness)
    velocity_strength (float): Velocity strength of the drive (damping)
    force_limit (float): Max force applied by the drive

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_linear_breakable"></a>

#### set_linear_breakable

```python
@classmethod
def set_linear_breakable(
        cls, accessor: ConstraintInstanceAccessor, linear_breakable: bool,
        linear_break_threshold: float) -> ConstraintInstanceAccessor
```

X.set_linear_breakable(accessor, linear_breakable, linear_break_threshold) -> ConstraintInstanceAccessor
Sets the Linear Breakable properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    linear_breakable (bool): Whether it is possible to break the joint with linear force
    linear_break_threshold (float): Force needed to break the joint

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_disable_collision"></a>

#### set_disable_collision

```python
@classmethod
def set_disable_collision(
        cls, accessor: ConstraintInstanceAccessor,
        disable_collision: bool) -> ConstraintInstanceAccessor
```

X.set_disable_collision(accessor, disable_collision) -> ConstraintInstanceAccessor
Sets whether bodies attched to the constraint can collide or not

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    disable_collision (bool): true to disable collision between constrained bodies

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_contact_transfer_scale"></a>

#### set_contact_transfer_scale

```python
@classmethod
def set_contact_transfer_scale(
        cls, accessor: ConstraintInstanceAccessor,
        contact_transfer_scale: float) -> ConstraintInstanceAccessor
```

X.set_contact_transfer_scale(accessor, contact_transfer_scale) -> ConstraintInstanceAccessor
Set Contact Transfer Scale

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    contact_transfer_scale (float): Set Contact Transfer Scale onto joints parent

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_velocity_target"></a>

#### set_angular_velocity_target

```python
@classmethod
def set_angular_velocity_target(
        cls, accessor: ConstraintInstanceAccessor,
        vel_target: Vector) -> ConstraintInstanceAccessor
```

X.set_angular_velocity_target(accessor, vel_target) -> ConstraintInstanceAccessor
Sets the target velocity for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    vel_target (Vector): Target velocity

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_velocity_drive_twist_and_swing"></a>

#### set_angular_velocity_drive_twist_and_swing

```python
@classmethod
def set_angular_velocity_drive_twist_and_swing(
        cls, accessor: ConstraintInstanceAccessor, enable_twist_drive: bool,
        enable_swing_drive: bool) -> ConstraintInstanceAccessor
```

X.set_angular_velocity_drive_twist_and_swing(accessor, enable_twist_drive, enable_swing_drive) -> ConstraintInstanceAccessor
Enables/Disables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
    enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_velocity_drive_slerp"></a>

#### set_angular_velocity_drive_slerp

```python
@classmethod
def set_angular_velocity_drive_slerp(
        cls, accessor: ConstraintInstanceAccessor,
        enable_slerp: bool) -> ConstraintInstanceAccessor
```

X.set_angular_velocity_drive_slerp(accessor, enable_slerp) -> ConstraintInstanceAccessor
Enables/Disables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    enable_slerp (bool): Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_soft_twist_limit_params"></a>

#### set_angular_soft_twist_limit_params

```python
@classmethod
def set_angular_soft_twist_limit_params(
        cls, accessor: ConstraintInstanceAccessor, soft_twist_limit: bool,
        twist_limit_stiffness: float, twist_limit_damping: float,
        twist_limit_restitution: float,
        twist_limit_contact_distance: float) -> ConstraintInstanceAccessor
```

X.set_angular_soft_twist_limit_params(accessor, soft_twist_limit, twist_limit_stiffness, twist_limit_damping, twist_limit_restitution, twist_limit_contact_distance) -> ConstraintInstanceAccessor
Sets Constraint Angular Soft Twist Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change *
    soft_twist_limit (bool): True is the twist limit is soft
    twist_limit_stiffness (float): Stiffness of the soft Twist limit. Only used when Soft limit is on ( positive value )
    twist_limit_damping (float): Damping of the soft Twist limit. Only used when Soft limit is on ( positive value )
    twist_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
    twist_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change *

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_soft_swing_limit_params"></a>

#### set_angular_soft_swing_limit_params

```python
@classmethod
def set_angular_soft_swing_limit_params(
        cls, accessor: ConstraintInstanceAccessor, soft_swing_limit: bool,
        swing_limit_stiffness: float, swing_limit_damping: float,
        swing_limit_restitution: float,
        swing_limit_contact_distance: float) -> ConstraintInstanceAccessor
```

X.set_angular_soft_swing_limit_params(accessor, soft_swing_limit, swing_limit_stiffness, swing_limit_damping, swing_limit_restitution, swing_limit_contact_distance) -> ConstraintInstanceAccessor
Sets Constraint Angular Soft Swing Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change *
    soft_swing_limit (bool): True is the swing limit is soft
    swing_limit_stiffness (float): Stiffness of the soft swing limit. Only used when Soft limit is on ( positive value )
    swing_limit_damping (float): Damping of the soft swing limit. Only used when Soft limit is on ( positive value )
    swing_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.
    swing_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change *

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_plasticity"></a>

#### set_angular_plasticity

```python
@classmethod
def set_angular_plasticity(
        cls, accessor: ConstraintInstanceAccessor, angular_plasticity: bool,
        angular_plasticity_threshold: float) -> ConstraintInstanceAccessor
```

X.set_angular_plasticity(accessor, angular_plasticity, angular_plasticity_threshold) -> ConstraintInstanceAccessor
Sets Constraint Angular Plasticity properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    angular_plasticity (bool): Whether it is possible to reset the target angle from the angular displacement
    angular_plasticity_threshold (float): Degrees needed to reset the rest state of the joint

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_orientation_target"></a>

#### set_angular_orientation_target

```python
@classmethod
def set_angular_orientation_target(
        cls, accessor: ConstraintInstanceAccessor,
        pos_target: Rotator) -> ConstraintInstanceAccessor
```

X.set_angular_orientation_target(accessor, pos_target) -> ConstraintInstanceAccessor
Sets the target orientation for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    pos_target (Rotator): Target orientation

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_limits"></a>

#### set_angular_limits

```python
@classmethod
def set_angular_limits(cls, accessor: ConstraintInstanceAccessor,
                       swing1_motion_type: AngularConstraintMotion,
                       swing1_limit_angle: float,
                       swing2_motion_type: AngularConstraintMotion,
                       swing2_limit_angle: float,
                       twist_motion_type: AngularConstraintMotion,
                       twist_limit_angle: float) -> ConstraintInstanceAccessor
```

X.set_angular_limits(accessor, swing1_motion_type, swing1_limit_angle, swing2_motion_type, swing2_limit_angle, twist_motion_type, twist_limit_angle) -> ConstraintInstanceAccessor
Sets COnstraint Angular Motion Ranges

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    swing1_motion_type (AngularConstraintMotion): Type of swing motion ( first axis )
    swing1_limit_angle (float): Size of limit in degrees in [0, 180] range
    swing2_motion_type (AngularConstraintMotion): Type of swing motion ( second axis )
    swing2_limit_angle (float): Size of limit in degrees in [0, 180] range
    twist_motion_type (AngularConstraintMotion): Type of twist motion
    twist_limit_angle (float): Size of limit in degrees in [0, 180] range

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_drive_params"></a>

#### set_angular_drive_params

```python
@classmethod
def set_angular_drive_params(cls, accessor: ConstraintInstanceAccessor,
                             position_strength: float,
                             velocity_strength: float,
                             force_limit: float) -> ConstraintInstanceAccessor
```

X.set_angular_drive_params(accessor, position_strength, velocity_strength, force_limit) -> ConstraintInstanceAccessor
Sets the drive params for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    position_strength (float): Positional strength for the drive (stiffness)
    velocity_strength (float): Velocity strength of the drive (damping)
    force_limit (float): Max force applied by the drive

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_drive_mode"></a>

#### set_angular_drive_mode

```python
@classmethod
def set_angular_drive_mode(
        cls, accessor: ConstraintInstanceAccessor,
        drive_mode: AngularDriveMode) -> ConstraintInstanceAccessor
```

X.set_angular_drive_mode(accessor, drive_mode) -> ConstraintInstanceAccessor
Switches the angular drive mode between SLERP and Twist And Swing

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    drive_mode (AngularDriveMode): The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.set_angular_breakable"></a>

#### set_angular_breakable

```python
@classmethod
def set_angular_breakable(
        cls, accessor: ConstraintInstanceAccessor, angular_breakable: bool,
        angular_break_threshold: float) -> ConstraintInstanceAccessor
```

X.set_angular_breakable(accessor, angular_breakable, angular_break_threshold) -> ConstraintInstanceAccessor
Sets Constraint Angular Breakable properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to change
    angular_breakable (bool): Whether it is possible to break the joint with angular force
    angular_break_threshold (float): Torque needed to break the joint

Returns:
    ConstraintInstanceAccessor: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to change

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_projection_params"></a>

#### get_projection_params

```python
@classmethod
def get_projection_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float, float]
```

X.get_projection_params(accessor) -> (accessor=ConstraintInstanceAccessor, enable_projection=bool, projection_linear_alpha=float, projection_angular_alpha=float)
Gets projection parameters of the constraint

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    enable_projection (bool): true to enable projection

    projection_linear_alpha (float): how much linear projection to apply in [0,1] range

    projection_angular_alpha (float): how much angular projection to apply in [0,1] range

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_parent_dominates"></a>

#### get_parent_dominates

```python
@classmethod
def get_parent_dominates(
    cls, accessor: ConstraintInstanceAccessor
) -> Optional[ConstraintInstanceAccessor]
```

X.get_parent_dominates(accessor) -> ConstraintInstanceAccessor or None
Gets whether the parent body is not affected by it's child motion

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    ConstraintInstanceAccessor or None: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_orientation_drive_twist_and_swing"></a>

#### get_orientation_drive_twist_and_swing

```python
@classmethod
def get_orientation_drive_twist_and_swing(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, bool]
```

X.get_orientation_drive_twist_and_swing(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_twist_drive=bool, out_enable_swing_drive=bool)
Gets whether angular orientation drive are enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_twist_drive (bool): Indicates whether the drive for the twist axis is enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

    out_enable_swing_drive (bool): Indicates whether the drive for the swing axis is enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_orientation_drive_slerp"></a>

#### get_orientation_drive_slerp

```python
@classmethod
def get_orientation_drive_slerp(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool]
```

X.get_orientation_drive_slerp(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_slerp=bool)
Gets whether the angular orientation slerp drive is enabled or not. Only relevant if the AngularDriveMode is set to SLERP

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_slerp (bool): Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_mass_conditioning_enabled"></a>

#### get_mass_conditioning_enabled

```python
@classmethod
def get_mass_conditioning_enabled(
    cls, accessor: ConstraintInstanceAccessor
) -> Optional[ConstraintInstanceAccessor]
```

X.get_mass_conditioning_enabled(accessor) -> ConstraintInstanceAccessor or None

brief: Gets whether mass conditioning is enabled for the constraint.

Args:
    accessor (ConstraintInstanceAccessor): 

Returns:
    ConstraintInstanceAccessor or None: 

    accessor (ConstraintInstanceAccessor):

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_velocity_target"></a>

#### get_linear_velocity_target

```python
@classmethod
def get_linear_velocity_target(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, Vector]
```

X.get_linear_velocity_target(accessor) -> (accessor=ConstraintInstanceAccessor, out_vel_target=Vector)
Gets the target velocity for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_vel_target (Vector): Target velocity

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_velocity_drive"></a>

#### get_linear_velocity_drive

```python
@classmethod
def get_linear_velocity_drive(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, bool, bool]
```

X.get_linear_velocity_drive(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_drive_x=bool, out_enable_drive_y=bool, out_enable_drive_z=bool)
Gets whether linear velocity drive is enabled or not

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_drive_x (bool): Indicates whether the drive for the X-Axis is enabled

    out_enable_drive_y (bool): Indicates whether the drive for the Y-Axis is enabled

    out_enable_drive_z (bool): Indicates whether the drive for the Z-Axis is enabled

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_soft_limit_params"></a>

#### get_linear_soft_limit_params

```python
@classmethod
def get_linear_soft_limit_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float, float, float, float]
```

X.get_linear_soft_limit_params(accessor) -> (accessor=ConstraintInstanceAccessor, soft_linear_limit=bool, linear_limit_stiffness=float, linear_limit_damping=float, linear_limit_restitution=float, linear_limit_contact_distance=float)
Gets Constraint Linear Soft Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

    soft_linear_limit (bool): True is the Linear limit is soft

    linear_limit_stiffness (float): Stiffness of the soft Linear limit. Only used when Soft limit is on ( positive value )

    linear_limit_damping (float): Damping of the soft Linear limit. Only used when Soft limit is on ( positive value )

    linear_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.

    linear_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_position_target"></a>

#### get_linear_position_target

```python
@classmethod
def get_linear_position_target(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, Vector]
```

X.get_linear_position_target(accessor) -> (accessor=ConstraintInstanceAccessor, out_pos_target=Vector)
Gets the target position for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_pos_target (Vector): Target position

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_position_drive"></a>

#### get_linear_position_drive

```python
@classmethod
def get_linear_position_drive(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, bool, bool]
```

X.get_linear_position_drive(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_drive_x=bool, out_enable_drive_y=bool, out_enable_drive_z=bool)
Gets whether linear position drive is enabled or not

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_drive_x (bool): Indicates whether the drive for the X-Axis is enabled

    out_enable_drive_y (bool): Indicates whether the drive for the Y-Axis is enabled

    out_enable_drive_z (bool): Indicates whether the drive for the Z-Axis is enabled

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_plasticity"></a>

#### get_linear_plasticity

```python
@classmethod
def get_linear_plasticity(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float, ConstraintPlasticityType]
```

X.get_linear_plasticity(accessor) -> (accessor=ConstraintInstanceAccessor, linear_plasticity=bool, linear_plasticity_threshold=float, plasticity_type=ConstraintPlasticityType)
Gets Constraint Linear Plasticity properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    linear_plasticity (bool): 

    linear_plasticity_threshold (float): 

    plasticity_type (ConstraintPlasticityType):

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_limits"></a>

#### get_linear_limits

```python
@classmethod
def get_linear_limits(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, LinearConstraintMotion,
           LinearConstraintMotion, LinearConstraintMotion, float]
```

X.get_linear_limits(accessor) -> (accessor=ConstraintInstanceAccessor, x_motion=LinearConstraintMotion, y_motion=LinearConstraintMotion, z_motion=LinearConstraintMotion, limit=float)
Gets Constraint Linear Motion Ranges

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    x_motion (LinearConstraintMotion): Type of motion along the X axis

    y_motion (LinearConstraintMotion): Type of motion along the Y axis

    z_motion (LinearConstraintMotion): Type of motion along the Z axis

    limit (float): linear limit applied to all axis

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_drive_params"></a>

#### get_linear_drive_params

```python
@classmethod
def get_linear_drive_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, float, float, float]
```

X.get_linear_drive_params(accessor) -> (accessor=ConstraintInstanceAccessor, out_position_strength=float, out_velocity_strength=float, out_force_limit=float)
Gets the drive params for the linear drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_position_strength (float): Positional strength for the drive (stiffness)

    out_velocity_strength (float): Velocity strength of the drive (damping)

    out_force_limit (float): Max force applied by the drive

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_linear_breakable"></a>

#### get_linear_breakable

```python
@classmethod
def get_linear_breakable(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float]
```

X.get_linear_breakable(accessor) -> (accessor=ConstraintInstanceAccessor, linear_breakable=bool, linear_break_threshold=float)
Gets Constraint Linear Breakable properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    linear_breakable (bool): Whether it is possible to break the joint with linear force

    linear_break_threshold (float): Force needed to break the joint

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_disable_collsion"></a>

#### get_disable_collsion

```python
@classmethod
def get_disable_collsion(
    cls, accessor: ConstraintInstanceAccessor
) -> Optional[ConstraintInstanceAccessor]
```

X.get_disable_collsion(accessor) -> ConstraintInstanceAccessor or None
Gets whether bodies attched to the constraint can collide or not

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    ConstraintInstanceAccessor or None: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_contact_transfer_scale"></a>

#### get_contact_transfer_scale

```python
@classmethod
def get_contact_transfer_scale(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, float]
```

X.get_contact_transfer_scale(accessor) -> (accessor=ConstraintInstanceAccessor, contact_transfer_scale=float)
Gets Constraint Contact Transfer Scale properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    contact_transfer_scale (float): Scale for transfer of child energy to parent.

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_attached_body_names"></a>

#### get_attached_body_names

```python
@classmethod
def get_attached_body_names(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, Name, Name]
```

X.get_attached_body_names(accessor) -> (accessor=ConstraintInstanceAccessor, parent_body=Name, child_body=Name)
Gets Attached body names

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    parent_body (Name): Parent body name of the constraint

    child_body (Name): Child body name of the constraint

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_velocity_target"></a>

#### get_angular_velocity_target

```python
@classmethod
def get_angular_velocity_target(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, Vector]
```

X.get_angular_velocity_target(accessor) -> (accessor=ConstraintInstanceAccessor, out_vel_target=Vector)
Gets the target velocity for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_vel_target (Vector): Target velocity

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_velocity_drive_twist_and_swing"></a>

#### get_angular_velocity_drive_twist_and_swing

```python
@classmethod
def get_angular_velocity_drive_twist_and_swing(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, bool]
```

X.get_angular_velocity_drive_twist_and_swing(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_twist_drive=bool, out_enable_swing_drive=bool)
Gets whether angular velocity twist and swing drive is enabled or not. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

    out_enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_velocity_drive_slerp"></a>

#### get_angular_velocity_drive_slerp

```python
@classmethod
def get_angular_velocity_drive_slerp(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool]
```

X.get_angular_velocity_drive_slerp(accessor) -> (accessor=ConstraintInstanceAccessor, out_enable_slerp=bool)
Gets whether the angular velocity slerp drive is enabled or not. Only relevant if the AngularDriveMode is set to SLERP

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_enable_slerp (bool): Indicates whether the SLERP drive is enabled. Only relevant if the AngularDriveMode is set to SLERP

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_soft_twist_limit_params"></a>

#### get_angular_soft_twist_limit_params

```python
@classmethod
def get_angular_soft_twist_limit_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float, float, float, float]
```

X.get_angular_soft_twist_limit_params(accessor) -> (accessor=ConstraintInstanceAccessor, soft_twist_limit=bool, twist_limit_stiffness=float, twist_limit_damping=float, twist_limit_restitution=float, twist_limit_contact_distance=float)
Gets Constraint Angular Soft Twist Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

    soft_twist_limit (bool): True is the Twist limit is soft

    twist_limit_stiffness (float): Stiffness of the soft Twist limit. Only used when Soft limit is on ( positive value )

    twist_limit_damping (float): Damping of the soft Twist limit. Only used when Soft limit is on ( positive value )

    twist_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.

    twist_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_soft_swing_limit_params"></a>

#### get_angular_soft_swing_limit_params

```python
@classmethod
def get_angular_soft_swing_limit_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float, float, float, float]
```

X.get_angular_soft_swing_limit_params(accessor) -> (accessor=ConstraintInstanceAccessor, soft_swing_limit=bool, swing_limit_stiffness=float, swing_limit_damping=float, swing_limit_restitution=float, swing_limit_contact_distance=float)
Gets Constraint Angular Soft Swing Limit parameters

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query *

    soft_swing_limit (bool): True is the swing limit is soft

    swing_limit_stiffness (float): Stiffness of the soft swing limit. Only used when Soft limit is on ( positive value )

    swing_limit_damping (float): Damping of the soft swing limit. Only used when Soft limit is on ( positive value )

    swing_limit_restitution (float): Controls the amount of bounce when the constraint is violated. A restitution value of 1 will bounce back with the same velocity the limit was hit. A value of 0 will stop dead.

    swing_limit_contact_distance (float): Determines how close to the limit we have to get before turning the joint on. Larger value will be more expensive, but will do a better job not violating constraints. A smaller value will be more efficient, but easier to violate.

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_plasticity"></a>

#### get_angular_plasticity

```python
@classmethod
def get_angular_plasticity(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float]
```

X.get_angular_plasticity(accessor) -> (accessor=ConstraintInstanceAccessor, angular_plasticity=bool, angular_plasticity_threshold=float)
Sets Constraint Angular Plasticity properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    angular_plasticity (bool): Whether it is possible to reset the target angle from the angular displacement

    angular_plasticity_threshold (float): Degrees needed to reset the rest state of the joint

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_orientation_target"></a>

#### get_angular_orientation_target

```python
@classmethod
def get_angular_orientation_target(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, Rotator]
```

X.get_angular_orientation_target(accessor) -> (accessor=ConstraintInstanceAccessor, out_pos_target=Rotator)
Gets the target orientation for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_pos_target (Rotator): Target orientation

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_limits"></a>

#### get_angular_limits

```python
@classmethod
def get_angular_limits(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, AngularConstraintMotion, float,
           AngularConstraintMotion, float, AngularConstraintMotion, float]
```

X.get_angular_limits(accessor) -> (accessor=ConstraintInstanceAccessor, swing1_motion_type=AngularConstraintMotion, swing1_limit_angle=float, swing2_motion_type=AngularConstraintMotion, swing2_limit_angle=float, twist_motion_type=AngularConstraintMotion, twist_limit_angle=float)
Gets Constraint Angular Motion Ranges

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    swing1_motion_type (AngularConstraintMotion): Type of swing motion ( first axis )

    swing1_limit_angle (float): Size of limit in degrees in [0, 180] range

    swing2_motion_type (AngularConstraintMotion): Type of swing motion ( second axis )

    swing2_limit_angle (float): Size of limit in degrees in [0, 180] range

    twist_motion_type (AngularConstraintMotion): Type of twist motion

    twist_limit_angle (float): Size of limit in degrees in [0, 180] range

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_drive_params"></a>

#### get_angular_drive_params

```python
@classmethod
def get_angular_drive_params(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, float, float, float]
```

X.get_angular_drive_params(accessor) -> (accessor=ConstraintInstanceAccessor, out_position_strength=float, out_velocity_strength=float, out_force_limit=float)
Gets the drive params for the angular drive.

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_position_strength (float): Positional strength for the drive (stiffness)

    out_velocity_strength (float): Velocity strength of the drive (damping)

    out_force_limit (float): Max force applied by the drive

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_drive_mode"></a>

#### get_angular_drive_mode

```python
@classmethod
def get_angular_drive_mode(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, AngularDriveMode]
```

X.get_angular_drive_mode(accessor) -> (accessor=ConstraintInstanceAccessor, out_drive_mode=AngularDriveMode)
Gets the angular drive mode ( SLERP or Twist And Swing)

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    out_drive_mode (AngularDriveMode): The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

<a id="unreal.ConstraintInstanceBlueprintLibrary.get_angular_breakable"></a>

#### get_angular_breakable

```python
@classmethod
def get_angular_breakable(
    cls, accessor: ConstraintInstanceAccessor
) -> Tuple[ConstraintInstanceAccessor, bool, float]
```

X.get_angular_breakable(accessor) -> (accessor=ConstraintInstanceAccessor, angular_breakable=bool, angular_break_threshold=float)
Gets Constraint Angular Breakable properties

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to query

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to query

    angular_breakable (bool): Whether it is possible to break the joint with angular force

    angular_break_threshold (float): Torque needed to break the joint

<a id="unreal.ConstraintInstanceBlueprintLibrary.copy_params"></a>

#### copy_params

```python
@classmethod
def copy_params(
    cls,
    accessor: ConstraintInstanceAccessor,
    source_accessor: ConstraintInstanceAccessor,
    keep_position: bool = True,
    keep_rotation: bool = True
) -> Tuple[ConstraintInstanceAccessor, ConstraintInstanceAccessor]
```

X.copy_params(accessor, source_accessor, keep_position=True, keep_rotation=True) -> (accessor=ConstraintInstanceAccessor, source_accessor=ConstraintInstanceAccessor)
Copies all properties from one constraint to another

Args:
    accessor (ConstraintInstanceAccessor): Constraint accessor to write to
    source_accessor (ConstraintInstanceAccessor): Constraint accessor to read from
    keep_position (bool): Whether to keep original constraint positions
    keep_rotation (bool): Whether to keep original constraint rotations

Returns:
    tuple: 

    accessor (ConstraintInstanceAccessor): Constraint accessor to write to

    source_accessor (ConstraintInstanceAccessor): Constraint accessor to read from

<a id="unreal.NetworkPhysicsComponent"></a>