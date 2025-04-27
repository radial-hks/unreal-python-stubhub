## PhysicsConstraintComponent Objects

```python
class PhysicsConstraintComponent(SceneComponent)
```

This is effectively a joint that allows you to connect 2 rigid bodies together. You can create different types of joints using the various parameters of this component.

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsConstraintComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_name1`` (ConstrainComponentPropName):  [Read-Write] Name of first component property to constrain. If Actor1 is NULL, will look within Owner.
  If this is NULL, will use RootComponent of Actor1
- ``component_name2`` (ConstrainComponentPropName):  [Read-Write] Name of second component property to constrain. If Actor2 is NULL, will look within Owner.
  If this is NULL, will use RootComponent of Actor2
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``constraint_actor1`` (Actor):  [Read-Write] Pointer to first Actor to constrain.
- ``constraint_actor2`` (Actor):  [Read-Write] Pointer to second Actor to constrain.
- ``constraint_instance`` (ConstraintInstance):  [Read-Write] All constraint settings
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_constraint_broken`` (ConstraintBrokenSignature):  [Read-Write] Notification when constraint is broken.
- ``on_plastic_deformation`` (PlasticDeformationEventSignature):  [Read-Write] Notification when constraint plasticity drive target changes.
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.PhysicsConstraintComponent.on_constraint_broken"></a>

#### on_constraint_broken

```python
@property
def on_constraint_broken() -> ConstraintBrokenSignature
```

(ConstraintBrokenSignature):  [Read-Write] Notification when constraint is broken.

<a id="unreal.PhysicsConstraintComponent.on_constraint_broken"></a>

#### on_constraint_broken

```python
@on_constraint_broken.setter
def on_constraint_broken(value: ConstraintBrokenSignature) -> None
```

<a id="unreal.PhysicsConstraintComponent.on_plastic_deformation"></a>

#### on_plastic_deformation

```python
@property
def on_plastic_deformation() -> PlasticDeformationEventSignature
```

(PlasticDeformationEventSignature):  [Read-Write] Notification when constraint plasticity drive target changes.

<a id="unreal.PhysicsConstraintComponent.on_plastic_deformation"></a>

#### on_plastic_deformation

```python
@on_plastic_deformation.setter
def on_plastic_deformation(value: PlasticDeformationEventSignature) -> None
```

<a id="unreal.PhysicsConstraintComponent.set_projection_params"></a>

#### set_projection_params

```python
def set_projection_params(projection_linear_alpha: float,
                          projection_angular_alpha: float,
                          projection_linear_tolerance: float,
                          projection_angular_tolerance: float) -> None
```

x.set_projection_params(projection_linear_alpha, projection_angular_alpha, projection_linear_tolerance, projection_angular_tolerance) -> None
Set the projection settings for use when projection is enabled. See SetProjectionEnabled.
For ragdolls you usually require that ProjectionLinearAlpha and ProjectionAngularAlpha be zero. They are most useful for cosmetic chains etc. ProjectionLinearTolerance and ProjectionAngularTolerance
are emergency error recovery settings and should only rarely affect the simulation. If the simulation is significantly affected by the Tolerance settings, it likely indicates a setup stability issue.

Args:
    projection_linear_alpha (float): Controls the semi-physical correction of linear error remaining after the joint solve. Will add energy into the system. Best for joint chains connected to a kinematic.
    projection_angular_alpha (float): Controls the semi-physical correction of angular error remaining after the joint solve. Will add energy into the system. Best for joint chains connected to a kinematic.
    projection_linear_tolerance (float): Linear errors above this will be corrected with a non-physical teleport.
    projection_angular_tolerance (float): Angular errors above this will be corrected with a non-physical teleport.

<a id="unreal.PhysicsConstraintComponent.set_projection_enabled"></a>

#### set_projection_enabled

```python
def set_projection_enabled(projection_enabled: bool) -> None
```

x.set_projection_enabled(projection_enabled) -> None
If true, joint projection is enabled. Projection is a semi-physics post-solve correction for fixing small errors, and a teleport for fixing larger errors. See SetProjectionParams

Args:
    projection_enabled (bool):

<a id="unreal.PhysicsConstraintComponent.set_orientation_drive_twist_and_swing"></a>

#### set_orientation_drive_twist_and_swing

```python
def set_orientation_drive_twist_and_swing(enable_twist_drive: bool,
                                          enable_swing_drive: bool) -> None
```

x.set_orientation_drive_twist_and_swing(enable_twist_drive, enable_swing_drive) -> None
Enables/Disables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
    enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

<a id="unreal.PhysicsConstraintComponent.set_orientation_drive_slerp"></a>

#### set_orientation_drive_slerp

```python
def set_orientation_drive_slerp(enable_slerp: bool) -> None
```

x.set_orientation_drive_slerp(enable_slerp) -> None
Enables/Disables the angular orientation slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Args:
    enable_slerp (bool): Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

<a id="unreal.PhysicsConstraintComponent.set_linear_z_limit"></a>

#### set_linear_z_limit

```python
def set_linear_z_limit(constraint_type: LinearConstraintMotion,
                       limit_size: float) -> None
```

x.set_linear_z_limit(constraint_type, limit_size) -> None
Sets the LinearZ Motion Type

Args:
    constraint_type (LinearConstraintMotion): New Constraint Type
    limit_size (float): Size of limit

<a id="unreal.PhysicsConstraintComponent.set_linear_y_limit"></a>

#### set_linear_y_limit

```python
def set_linear_y_limit(constraint_type: LinearConstraintMotion,
                       limit_size: float) -> None
```

x.set_linear_y_limit(constraint_type, limit_size) -> None
Sets the LinearY Motion Type

Args:
    constraint_type (LinearConstraintMotion): New Constraint Type
    limit_size (float): Size of limit

<a id="unreal.PhysicsConstraintComponent.set_linear_x_limit"></a>

#### set_linear_x_limit

```python
def set_linear_x_limit(constraint_type: LinearConstraintMotion,
                       limit_size: float) -> None
```

x.set_linear_x_limit(constraint_type, limit_size) -> None
Sets the LinearX Motion Type

Args:
    constraint_type (LinearConstraintMotion): New Constraint Type
    limit_size (float): Size of limit

<a id="unreal.PhysicsConstraintComponent.set_linear_velocity_target"></a>

#### set_linear_velocity_target

```python
def set_linear_velocity_target(vel_target: Vector) -> None
```

x.set_linear_velocity_target(vel_target) -> None
Sets the target velocity for the linear drive.

Args:
    vel_target (Vector): Target velocity

<a id="unreal.PhysicsConstraintComponent.set_linear_velocity_drive"></a>

#### set_linear_velocity_drive

```python
def set_linear_velocity_drive(enable_drive_x: bool, enable_drive_y: bool,
                              enable_drive_z: bool) -> None
```

x.set_linear_velocity_drive(enable_drive_x, enable_drive_y, enable_drive_z) -> None
Enables/Disables linear position drive

Args:
    enable_drive_x (bool): Indicates whether the drive for the X-Axis should be enabled
    enable_drive_y (bool): Indicates whether the drive for the Y-Axis should be enabled
    enable_drive_z (bool): Indicates whether the drive for the Z-Axis should be enabled

<a id="unreal.PhysicsConstraintComponent.set_linear_position_target"></a>

#### set_linear_position_target

```python
def set_linear_position_target(pos_target: Vector) -> None
```

x.set_linear_position_target(pos_target) -> None
Sets the target position for the linear drive.

Args:
    pos_target (Vector): Target position

<a id="unreal.PhysicsConstraintComponent.set_linear_position_drive"></a>

#### set_linear_position_drive

```python
def set_linear_position_drive(enable_drive_x: bool, enable_drive_y: bool,
                              enable_drive_z: bool) -> None
```

x.set_linear_position_drive(enable_drive_x, enable_drive_y, enable_drive_z) -> None
Enables/Disables linear position drive

Args:
    enable_drive_x (bool): Indicates whether the drive for the X-Axis should be enabled
    enable_drive_y (bool): Indicates whether the drive for the Y-Axis should be enabled
    enable_drive_z (bool): Indicates whether the drive for the Z-Axis should be enabled

<a id="unreal.PhysicsConstraintComponent.set_linear_plasticity"></a>

#### set_linear_plasticity

```python
def set_linear_plasticity(linear_plasticity: bool,
                          linear_plasticity_threshold: float,
                          plasticity_type: ConstraintPlasticityType) -> None
```

x.set_linear_plasticity(linear_plasticity, linear_plasticity_threshold, plasticity_type) -> None
Sets the Linear Plasticity properties

Args:
    linear_plasticity (bool): Whether it is possible to reset the target angle from the Linear displacement
    linear_plasticity_threshold (float): Percent deformation needed to reset the rest length of the joint
    plasticity_type (ConstraintPlasticityType):

<a id="unreal.PhysicsConstraintComponent.set_linear_drive_params"></a>

#### set_linear_drive_params

```python
def set_linear_drive_params(position_strength: float, velocity_strength: float,
                            force_limit: float) -> None
```

x.set_linear_drive_params(position_strength, velocity_strength, force_limit) -> None
Sets the drive params for the linear drive.

Args:
    position_strength (float): Positional strength for the drive (stiffness)
    velocity_strength (float): Velocity strength of the drive (damping)
    force_limit (float): Max force applied by the drive

<a id="unreal.PhysicsConstraintComponent.set_linear_drive_acceleration_mode"></a>

#### set_linear_drive_acceleration_mode

```python
def set_linear_drive_acceleration_mode(acceleration_mode: bool) -> None
```

x.set_linear_drive_acceleration_mode(acceleration_mode) -> None
Toggles the linear drive acceleration mode. When enabled, the acceleration of the angular drive is not affected by the inertia of the constrained objects along the drive axis.

Args:
    acceleration_mode (bool):

<a id="unreal.PhysicsConstraintComponent.set_linear_breakable"></a>

#### set_linear_breakable

```python
def set_linear_breakable(linear_breakable: bool,
                         linear_break_threshold: float) -> None
```

x.set_linear_breakable(linear_breakable, linear_break_threshold) -> None
Sets the Linear Breakable properties

Args:
    linear_breakable (bool): Whether it is possible to break the joint with linear force
    linear_break_threshold (float): Force needed to break the joint

<a id="unreal.PhysicsConstraintComponent.set_disable_collision"></a>

#### set_disable_collision

```python
def set_disable_collision(disable_collision: bool) -> None
```

x.set_disable_collision(disable_collision) -> None
If true, the collision between the two rigid bodies of the constraint will be disabled.

Args:
    disable_collision (bool):

<a id="unreal.PhysicsConstraintComponent.set_contact_transfer_scale"></a>

#### set_contact_transfer_scale

```python
def set_contact_transfer_scale(contact_transfer_scale: float) -> None
```

x.set_contact_transfer_scale(contact_transfer_scale) -> None
Sets the contact transfer scale properties

Args:
    contact_transfer_scale (float): Set the contact transfer scale for the parent of the joint

<a id="unreal.PhysicsConstraintComponent.set_constraint_reference_position"></a>

#### set_constraint_reference_position

```python
def set_constraint_reference_position(frame: ConstraintFrame,
                                      ref_position: Vector) -> None
```

x.set_constraint_reference_position(frame, ref_position) -> None
Pass in reference position in (maintains reference orientation). If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

Args:
    frame (ConstraintFrame): 
    ref_position (Vector):

<a id="unreal.PhysicsConstraintComponent.set_constraint_reference_orientation"></a>

#### set_constraint_reference_orientation

```python
def set_constraint_reference_orientation(frame: ConstraintFrame,
                                         pri_axis: Vector,
                                         sec_axis: Vector) -> None
```

x.set_constraint_reference_orientation(frame, pri_axis, sec_axis) -> None
Pass in reference orientation in (maintains reference position). If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

Args:
    frame (ConstraintFrame): 
    pri_axis (Vector): 
    sec_axis (Vector):

<a id="unreal.PhysicsConstraintComponent.set_constraint_reference_frame"></a>

#### set_constraint_reference_frame

```python
def set_constraint_reference_frame(frame: ConstraintFrame,
                                   ref_frame: Transform) -> None
```

x.set_constraint_reference_frame(frame, ref_frame) -> None
Pass in reference frame in. If the constraint is currently active, this will set its active local pose. Otherwise the change will take affect in InitConstraint.

Args:
    frame (ConstraintFrame): 
    ref_frame (Transform):

<a id="unreal.PhysicsConstraintComponent.set_constrained_components"></a>

#### set_constrained_components

```python
def set_constrained_components(component1: PrimitiveComponent,
                               bone_name1: Name,
                               component2: PrimitiveComponent,
                               bone_name2: Name) -> None
```

x.set_constrained_components(component1, bone_name1, component2, bone_name2) -> None
Directly specify component to connect. Will update frames based on current position.

Args:
    component1 (PrimitiveComponent): 
    bone_name1 (Name): 
    component2 (PrimitiveComponent): 
    bone_name2 (Name):

<a id="unreal.PhysicsConstraintComponent.set_angular_velocity_target"></a>

#### set_angular_velocity_target

```python
def set_angular_velocity_target(vel_target: Vector) -> None
```

x.set_angular_velocity_target(vel_target) -> None
Sets the target velocity for the angular drive.

Args:
    vel_target (Vector): Target velocity

<a id="unreal.PhysicsConstraintComponent.set_angular_velocity_drive_twist_and_swing"></a>

#### set_angular_velocity_drive_twist_and_swing

```python
def set_angular_velocity_drive_twist_and_swing(
        enable_twist_drive: bool, enable_swing_drive: bool) -> None
```

x.set_angular_velocity_drive_twist_and_swing(enable_twist_drive, enable_swing_drive) -> None
Enables/Disables angular velocity twist and swing drive. Only relevant if the AngularDriveMode is set to Twist and Swing

Args:
    enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
    enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

<a id="unreal.PhysicsConstraintComponent.set_angular_velocity_drive_slerp"></a>

#### set_angular_velocity_drive_slerp

```python
def set_angular_velocity_drive_slerp(enable_slerp: bool) -> None
```

x.set_angular_velocity_drive_slerp(enable_slerp) -> None
Enables/Disables the angular velocity slerp drive. Only relevant if the AngularDriveMode is set to SLERP

Args:
    enable_slerp (bool): Indicates whether the SLERP drive should be enabled. Only relevant if the AngularDriveMode is set to SLERP

<a id="unreal.PhysicsConstraintComponent.set_angular_velocity_drive"></a>

#### set_angular_velocity_drive

```python
def set_angular_velocity_drive(enable_swing_drive: bool,
                               enable_twist_drive: bool) -> None
```

x.set_angular_velocity_drive(enable_swing_drive, enable_twist_drive) -> None
Set Angular Velocity Drive
deprecated: Use SetAngularVelocityDriveTwistAndSwing instead.

Args:
    enable_swing_drive (bool): 
    enable_twist_drive (bool):

<a id="unreal.PhysicsConstraintComponent.set_angular_twist_limit"></a>

#### set_angular_twist_limit

```python
def set_angular_twist_limit(constraint_type: AngularConstraintMotion,
                            twist_limit_angle: float) -> None
```

x.set_angular_twist_limit(constraint_type, twist_limit_angle) -> None
Sets the Angular Twist Motion Type

Args:
    constraint_type (AngularConstraintMotion): New Constraint Type
    twist_limit_angle (float): Size of limit in degrees

<a id="unreal.PhysicsConstraintComponent.set_angular_swing2_limit"></a>

#### set_angular_swing2_limit

```python
def set_angular_swing2_limit(motion_type: AngularConstraintMotion,
                             swing2_limit_angle: float) -> None
```

x.set_angular_swing2_limit(motion_type, swing2_limit_angle) -> None
Sets the Angular Swing2 Motion Type

Args:
    motion_type (AngularConstraintMotion): 
    swing2_limit_angle (float): Size of limit in degrees

<a id="unreal.PhysicsConstraintComponent.set_angular_swing1_limit"></a>

#### set_angular_swing1_limit

```python
def set_angular_swing1_limit(motion_type: AngularConstraintMotion,
                             swing1_limit_angle: float) -> None
```

x.set_angular_swing1_limit(motion_type, swing1_limit_angle) -> None
Sets the Angular Swing1 Motion Type

Args:
    motion_type (AngularConstraintMotion): 
    swing1_limit_angle (float): Size of limit in degrees

<a id="unreal.PhysicsConstraintComponent.set_angular_plasticity"></a>

#### set_angular_plasticity

```python
def set_angular_plasticity(angular_plasticity: bool,
                           angular_plasticity_threshold: float) -> None
```

x.set_angular_plasticity(angular_plasticity, angular_plasticity_threshold) -> None
Sets the Angular Plasticity properties

Args:
    angular_plasticity (bool): Whether it is possible to reset the target angle from the angular displacement
    angular_plasticity_threshold (float): Degrees needed to reset the rest state of the joint

<a id="unreal.PhysicsConstraintComponent.set_angular_orientation_target"></a>

#### set_angular_orientation_target

```python
def set_angular_orientation_target(pos_target: Rotator) -> None
```

x.set_angular_orientation_target(pos_target) -> None
Sets the target orientation for the angular drive.

Args:
    pos_target (Rotator): Target orientation

<a id="unreal.PhysicsConstraintComponent.set_angular_orientation_drive"></a>

#### set_angular_orientation_drive

```python
def set_angular_orientation_drive(enable_swing_drive: bool,
                                  enable_twist_drive: bool) -> None
```

x.set_angular_orientation_drive(enable_swing_drive, enable_twist_drive) -> None
Enables/Disables angular orientation drive. Only relevant if the AngularDriveMode is set to Twist and Swing
deprecated: Use SetOrientationDriveTwistAndSwing instead.

Args:
    enable_swing_drive (bool): Indicates whether the drive for the swing axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing
    enable_twist_drive (bool): Indicates whether the drive for the twist axis should be enabled. Only relevant if the AngularDriveMode is set to Twist and Swing

<a id="unreal.PhysicsConstraintComponent.set_angular_drive_params"></a>

#### set_angular_drive_params

```python
def set_angular_drive_params(position_strength: float,
                             velocity_strength: float,
                             force_limit: float) -> None
```

x.set_angular_drive_params(position_strength, velocity_strength, force_limit) -> None
Sets the drive params for the angular drive.

Args:
    position_strength (float): Positional strength for the drive (stiffness)
    velocity_strength (float): Velocity strength of the drive (damping)
    force_limit (float): Max force applied by the drive

<a id="unreal.PhysicsConstraintComponent.set_angular_drive_mode"></a>

#### set_angular_drive_mode

```python
def set_angular_drive_mode(drive_mode: AngularDriveMode) -> None
```

x.set_angular_drive_mode(drive_mode) -> None
Switches the angular drive mode between SLERP and Twist And Swing

Args:
    drive_mode (AngularDriveMode): The angular drive mode to use. SLERP uses shortest spherical path, but will not work if any angular constraints are locked. Twist and Swing decomposes the path into the different angular degrees of freedom but may experience gimbal lock

<a id="unreal.PhysicsConstraintComponent.set_angular_drive_acceleration_mode"></a>

#### set_angular_drive_acceleration_mode

```python
def set_angular_drive_acceleration_mode(acceleration_mode: bool) -> None
```

x.set_angular_drive_acceleration_mode(acceleration_mode) -> None
Toggles the angular drive acceleration mode. When enabled, the acceleration of the angular drive is not affected by the inertia of the constrained objects around the drive axis.

Args:
    acceleration_mode (bool):

<a id="unreal.PhysicsConstraintComponent.set_angular_breakable"></a>

#### set_angular_breakable

```python
def set_angular_breakable(angular_breakable: bool,
                          angular_break_threshold: float) -> None
```

x.set_angular_breakable(angular_breakable, angular_break_threshold) -> None
Sets the Angular Breakable properties

Args:
    angular_breakable (bool): Whether it is possible to break the joint with angular force
    angular_break_threshold (float): Torque needed to break the joint

<a id="unreal.PhysicsConstraintComponent.is_projection_enabled"></a>

#### is_projection_enabled

```python
def is_projection_enabled() -> bool
```

x.is_projection_enabled() -> bool
Is projection enabled. See SetProjectionEnabled

Returns:
    bool:

<a id="unreal.PhysicsConstraintComponent.is_broken"></a>

#### is_broken

```python
def is_broken() -> bool
```

x.is_broken() -> bool
Retrieve the status of constraint being broken.

Returns:
    bool:

<a id="unreal.PhysicsConstraintComponent.get_current_twist"></a>

#### get_current_twist

```python
def get_current_twist() -> float
```

x.get_current_twist() -> float
Gets the current Angular Twist of the constraint

Returns:
    float:

<a id="unreal.PhysicsConstraintComponent.get_current_swing2"></a>

#### get_current_swing2

```python
def get_current_swing2() -> float
```

x.get_current_swing2() -> float
Gets the current Swing2 of the constraint

Returns:
    float:

<a id="unreal.PhysicsConstraintComponent.get_current_swing1"></a>

#### get_current_swing1

```python
def get_current_swing1() -> float
```

x.get_current_swing1() -> float
Gets the current Swing1 of the constraint

Returns:
    float:

<a id="unreal.PhysicsConstraintComponent.get_constraint_force"></a>

#### get_constraint_force

```python
def get_constraint_force() -> Tuple[Vector, Vector]
```

x.get_constraint_force() -> (out_linear_force=Vector, out_angular_force=Vector)
Retrieve the constraint force most recently applied to maintain this constraint. Returns 0 forces if the constraint is not initialized or broken.

Returns:
    tuple: 

    out_linear_force (Vector): 

    out_angular_force (Vector):

<a id="unreal.PhysicsConstraintComponent.get_constraint"></a>

#### get_constraint

```python
def get_constraint() -> ConstraintInstanceAccessor
```

x.get_constraint() -> ConstraintInstanceAccessor
Gets the constraint object

Returns:
    ConstraintInstanceAccessor:

<a id="unreal.PhysicsConstraintComponent.get_constrained_components"></a>

#### get_constrained_components

```python
def get_constrained_components(
) -> Tuple[PrimitiveComponent, Name, PrimitiveComponent, Name]
```

x.get_constrained_components() -> (out_component1=PrimitiveComponent, out_bone_name1=Name, out_component2=PrimitiveComponent, out_bone_name2=Name)
Get connected components and potential related attachement bones

Returns:
    tuple: 

    out_component1 (PrimitiveComponent): 

    out_bone_name1 (Name): 

    out_component2 (PrimitiveComponent): 

    out_bone_name2 (Name):

<a id="unreal.PhysicsConstraintComponent.break_constraint"></a>

#### break_constraint

```python
def break_constraint() -> None
```

x.break_constraint() -> None
Break this constraint

<a id="unreal.RB_ConstraintComponent"></a>