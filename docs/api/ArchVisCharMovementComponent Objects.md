## ArchVisCharMovementComponent Objects

```python
class ArchVisCharMovementComponent(CharacterMovementComponent)
```

Arch Vis Char Movement Component

**C++ Source:**

- **Plugin**: ArchVisCharacter
- **Module**: ArchVisCharacter
- **File**: ArchVisCharMovementComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``air_control`` (float):  [Read-Write] When falling, amount of lateral movement control available to the character.
  0 = no control, 1 = full control at max speed of MaxWalkSpeed.
- ``air_control_boost_multiplier`` (float):  [Read-Write] When falling, multiplier applied to AirControl when lateral velocity is less than AirControlBoostVelocityThreshold.
  Setting this to zero will disable air control boosting. Final result is clamped at 1.
- ``air_control_boost_velocity_threshold`` (float):  [Read-Write] When falling, if lateral velocity magnitude is less than this value, AirControl is multiplied by AirControlBoostMultiplier.
  Setting this to zero will disable air control boosting.
- ``allow_physics_rotation_during_anim_root_motion`` (bool):  [Read-Write]
- ``always_check_floor`` (bool):  [Read-Write] Whether we always force floor checks for stationary Characters while walking.
  Normally floor checks are avoided if possible when not moving, but this can be used to force them if there are use-cases where they are being skipped erroneously
  (such as objects moving up into the character from below).
- ``apply_gravity_while_jumping`` (bool):  [Read-Write] Apply gravity while the character is actively jumping (e.g. holding the jump key).
  Helps remove frame-rate dependent jump height, but may alter base jump height.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_register_physics_volume_updates`` (bool):  [Read-Write] If true, then applies the value of bComponentShouldUpdatePhysicsVolume to the UpdatedComponent. If false, will not change bShouldUpdatePhysicsVolume on the UpdatedComponent at all.
  see: bComponentShouldUpdatePhysicsVolume
- ``auto_register_updated_component`` (bool):  [Read-Write] If true, registers the owner's Root component as the UpdatedComponent if there is not one currently assigned.
- ``auto_update_tick_registration`` (bool):  [Read-Write] If true, whenever the updated component is changed, this component will enable or disable its tick dependent on whether it has something to update.
  This will NOT enable tick at startup if bAutoActivate is false, because presumably you have a good reason for not wanting it to start ticking initially.
- ``avoidance_consideration_radius`` (float):  [Read-Write]
- ``avoidance_group`` (NavAvoidanceMask):  [Read-Write] Moving actor's group mask
- ``avoidance_uid`` (int32):  [Read-Only] No default value, for now it's assumed to be valid if GetAvoidanceManager() returns non-NULL.
- ``avoidance_weight`` (float):  [Read-Write] De facto default value 0.5 (due to that being the default in the avoidance registration function), indicates RVO behavior.
- ``base_on_attachment_root`` (bool):  [Read-Write] Property to set if characters should stay based on objects attachment root instead of the traced object
- ``based_movement_ignore_physics_base`` (bool):  [Read-Write] Property to set if UpdateBasedMovement should ignore collision with actors part of the current MovementBase, if the base is simulated by physics
- ``braking_deceleration_falling`` (float):  [Read-Write] Lateral deceleration when falling and not applying acceleration.
  see: MaxAcceleration
- ``braking_deceleration_flying`` (float):  [Read-Write] Deceleration when flying and not applying acceleration.
  see: MaxAcceleration
- ``braking_deceleration_swimming`` (float):  [Read-Write] Deceleration when swimming and not applying acceleration.
  see: MaxAcceleration
- ``braking_deceleration_walking`` (float):  [Read-Write] Deceleration when walking and not applying acceleration. This is a constant opposing force that directly lowers velocity by a constant value.
  see: GroundFriction, MaxAcceleration
- ``braking_friction`` (float):  [Read-Write] Friction (drag) coefficient applied when braking (whenever Acceleration = 0, or if character is exceeding max speed); actual value used is this multiplied by BrakingFrictionFactor.
  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.
  Braking is composed of friction (velocity-dependent drag) and constant deceleration.
  This is the current value, used in all movement modes; if this is not desired, override it or bUseSeparateBrakingFriction when movement mode changes.
  note: Only used if bUseSeparateBrakingFriction setting is true, otherwise current friction such as GroundFriction is used.
  see: bUseSeparateBrakingFriction, BrakingFrictionFactor, GroundFriction, BrakingDecelerationWalking
- ``braking_friction_factor`` (float):  [Read-Write] Factor used to multiply actual value of friction used when braking.
  This applies to any friction value that is currently used, which may depend on bUseSeparateBrakingFriction.
  note: This is 2 by default for historical reasons, a value of 1 gives the true drag equation.
  see: bUseSeparateBrakingFriction, GroundFriction, BrakingFriction
- ``braking_sub_step_time`` (float):  [Read-Write] Time substepping when applying braking friction. Smaller time steps increase accuracy at the slight cost of performance, especially if there are large frame times.
- ``buoyancy`` (float):  [Read-Write] Water buoyancy. A ratio (1.0 = neutral buoyancy, 0.0 = no buoyancy)
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``can_walk_off_ledges`` (bool):  [Read-Write] If true, Character can walk off a ledge.
- ``can_walk_off_ledges_when_crouching`` (bool):  [Read-Write] If true, Character can walk off a ledge when crouching.
- ``component_should_update_physics_volume`` (bool):  [Read-Write] If true, enables bShouldUpdatePhysicsVolume on the UpdatedComponent during initialization from SetUpdatedComponent(), otherwise disables such updates.
  Only enabled if bAutoRegisterPhysicsVolumeUpdates is true.
  WARNING: UpdatePhysicsVolume is potentially expensive if overlap events are also *disabled* because it requires a separate query against all physics volumes in the world.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``constrain_to_plane`` (bool):  [Read-Write] If true, movement will be constrained to a plane.
  see: PlaneConstraintNormal, PlaneConstraintOrigin, PlaneConstraintAxisSetting
- ``crouch_maintains_base_location`` (bool):  [Read-Only] If true, crouching should keep the base of the capsule in place by lowering the center of the shrunken capsule. If false, the base of the capsule moves up and the center stays in place.
  The same behavior applies when the character uncrouches: if true, the base is kept in the same location and the center moves up. If false, the capsule grows and only moves up if the base impacts something.
  By default this variable is set when the movement mode changes: set to true when walking and false otherwise. Feel free to override the behavior when the movement mode changes.
- ``crouched_half_height`` (float):  [Read-Write]
- ``current_floor`` (FindFloorResult):  [Read-Only] Information about the floor the Character is standing on (updated only during walking movement).
- ``custom_movement_mode`` (uint8):  [Read-Write] Current custom sub-mode if MovementMode is set to Custom.
  This is automatically replicated through the Character owner and for client-server movement functions.
  see: SetMovementMode()
- ``default_land_movement_mode`` (MovementMode):  [Read-Write] Default movement mode when not in water. Used at player startup or when teleported.
  see: DefaultWaterMovementMode
  see: bRunPhysicsWithNoController
- ``default_water_movement_mode`` (MovementMode):  [Read-Write] Default movement mode when in water. Used at player startup or when teleported.
  see: DefaultLandMovementMode
  see: bRunPhysicsWithNoController
- ``dont_fall_below_jump_z_velocity_during_jump`` (bool):  [Read-Write] True means while the jump key is held, we will not allow the vertical speed to fall below the JumpZVelocity tuning value
  even if a stronger force, such as gravity, is opposing the jump.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_physics_interaction`` (bool):  [Read-Write] If enabled, the player will interact with physics objects when walking into them.
- ``enable_scoped_movement_updates`` (bool):  [Read-Write] If true, high-level movement updates will be wrapped in a movement scope that accumulates updates and defers a bulk of the work until the end.
  When enabled, touch and hit events will not be triggered until the end of multiple moves within an update, which can improve performance.
  see: FScopedMovementUpdate
- ``enable_server_dual_move_scoped_movement_updates`` (bool):  [Read-Write] Optional scoped movement update to combine moves for cheaper performance on the server when the client sends two moves in one packet.
  Be warned that since this wraps a larger scope than is normally done with bEnableScopedMovementUpdates, this can result in subtle changes in behavior
  in regards to when overlap events are handled, when attached components are moved, etc.
  see: bEnableScopedMovementUpdates
- ``falling_lateral_friction`` (float):  [Read-Write] Friction to apply to lateral air movement when falling.
  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero).
  see: BrakingFriction, bUseSeparateBrakingFriction
- ``fixed_path_braking_distance`` (float):  [Read-Write]
  deprecated: FixedPathBrakingDistance is deprecated, please use NavMovementProperties.FixedPathBrakingDistance instead.
- ``force_next_floor_check`` (bool):  [Read-Only] Force the Character in MOVE_Walking to do a check for a valid floor even if it hasn't moved. Cleared after next floor check.
  Normally if bAlwaysCheckFloor is false we try to avoid the floor check unless some conditions are met, but this can be used to force the next check to always run.
- ``former_base_velocity_decay_half_life`` (float):  [Read-Write] When applying a root motion override while falling off a moving object, this controls how long it takes to lose half the former base's velocity (in seconds).
  Set to 0 to ignore former bases (default).
  Set to -1 for no decay.
  Any other positive value sets the half-life for exponential decay.
- ``gravity_direction`` (Vector):  [Read-Only] A normalized vector representing the direction of gravity for gravity relative movement modes: walking, falling,
  and custom movement modes. Gravity direction remaps player input as being within the plane defined by the gravity
  direction. Movement simulation values like velocity and acceleration are maintained in their existing world coordinate
  space but are transformed internally as gravity relative (for instance moving forward up a vertical wall that gravity is
  defined to be perpendicular to and jump "up" from that wall). If ShouldRemainVertical() is true the character's capsule
  will be oriented to align with the gravity direction.
- ``gravity_scale`` (float):  [Read-Write] Custom gravity scale. Gravity is multiplied by this amount for the character.
- ``gravity_to_world_transform`` (Quat):  [Read-Only] A cached quaternion representing the inverse rotation from world space to gravity relative space defined by GravityDirection.
- ``ground_friction`` (float):  [Read-Write] Setting that affects movement control. Higher values allow faster changes in direction.
  If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero), where it is multiplied by BrakingFrictionFactor.
  When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.
  This can be used to simulate slippery surfaces such as ice or oil by changing the value (possibly based on the material pawn is standing on).
  see: BrakingDecelerationWalking, BrakingFriction, bUseSeparateBrakingFriction, BrakingFrictionFactor
- ``groups_to_avoid`` (NavAvoidanceMask):  [Read-Write] Will avoid other agents if they are in one of specified groups
- ``groups_to_ignore`` (NavAvoidanceMask):  [Read-Write] Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid
- ``ignore_base_rotation`` (bool):  [Read-Write] Whether the character ignores changes in rotation of the base it is standing on.
  If true, the character maintains current world rotation.
  If false, the character rotates with the moving base.
- ``ignore_client_movement_error_checks_and_correction`` (bool):  [Read-Write] If true, we should ignore server location difference checks for client error on this movement component.
  This can be useful when character is moving at extreme speeds for a duration and you need it to look
  smooth on clients without the server correcting the client. Make sure to disable when done, as this would
  break this character's server-client movement correction.
  see: bServerAcceptClientAuthoritativePosition, ServerCheckClientError()
- ``impart_base_angular_velocity`` (bool):  [Read-Write] If true, impart the base component's tangential components of angular velocity when jumping or falling off it.
  Only those components of the velocity allowed by the separate component settings (bImpartBaseVelocityX etc) will be applied.
  see: bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ
- ``impart_base_velocity_x`` (bool):  [Read-Write] If true, impart the base actor's X velocity when falling off it (which includes jumping)
- ``impart_base_velocity_y`` (bool):  [Read-Write] If true, impart the base actor's Y velocity when falling off it (which includes jumping)
- ``impart_base_velocity_z`` (bool):  [Read-Write] If true, impart the base actor's Z velocity when falling off it (which includes jumping)
- ``initial_push_force_factor`` (float):  [Read-Write] Initial impulse force to apply when the player bounces into a blocking physics object.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``jump_off_jump_z_factor`` (float):  [Read-Write] Fraction of JumpZVelocity to use when automatically "jumping off" of a base actor that's not allowed to be a base for a character. (For example, if you're not allowed to stand on other players.)
- ``jump_out_of_water_pitch`` (float):  [Read-Write] When exiting water, jump if control pitch angle is this high or above.
- ``jump_z_velocity`` (float):  [Read-Write] Initial velocity (instantaneous vertical acceleration) when jumping.
- ``just_teleported`` (bool):  [Read-Only] Used by movement code to determine if a change in position is based on normal movement or a teleport. If not a teleport, velocity can be recomputed based on the change in position.
- ``ledge_check_threshold`` (float):  [Read-Write] Used in determining if pawn is going off ledge.  If the ledge is "shorter" than this value then the pawn will be able to walk off it. *
- ``listen_server_network_simulated_smooth_location_time`` (float):  [Read-Write] Similar setting as NetworkSimulatedSmoothLocationTime but only used on Listen servers.
- ``listen_server_network_simulated_smooth_rotation_time`` (float):  [Read-Write] Similar setting as NetworkSimulatedSmoothRotationTime but only used on Listen servers.
- ``maintain_horizontal_ground_velocity`` (bool):  [Read-Write] If true, walking movement always maintains horizontal velocity when moving up ramps, which causes movement up ramps to be faster parallel to the ramp surface.
  If false, then walking movement maintains velocity magnitude parallel to the ramp surface.
- ``mass`` (float):  [Read-Write] Mass of pawn (for when momentum is imparted to it).
- ``max_acceleration`` (float):  [Read-Write] Max Acceleration (rate of change of velocity)
- ``max_custom_movement_speed`` (float):  [Read-Write] The maximum speed when using Custom movement mode.
- ``max_depenetration_with_geometry`` (float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.
  This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.
  see: MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy
- ``max_depenetration_with_geometry_as_proxy`` (float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.
  This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.
  see: MaxDepenetrationWithGeometry, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy
- ``max_depenetration_with_pawn`` (float):  [Read-Write] Max distance we are allowed to depenetrate when moving out of other Pawns.
  see: MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawnAsProxy
- ``max_depenetration_with_pawn_as_proxy`` (float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of other Pawns.
  Typically we don't want a large value, because we receive a server authoritative position that we should not then ignore by pushing them out of the local player.
  see: MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn
- ``max_fly_speed`` (float):  [Read-Write] The maximum flying speed.
- ``max_jump_apex_attempts_per_simulation`` (int32):  [Read-Write] Max number of attempts per simulation to attempt to exactly reach the jump apex when falling movement reaches the top of the arc.
  Limiting this prevents deep recursion when special cases cause collision or other conditions which reactivate the apex condition.
- ``max_out_of_water_step_height`` (float):  [Read-Write] Maximum step height for getting out of water
- ``max_pitch`` (float):  [Read-Write] Controls how far up you can look
- ``max_rotational_velocity`` (Rotator):  [Read-Write] Fastest possible turn rate
- ``max_simulation_iterations`` (int32):  [Read-Write] Max number of iterations used for each discrete simulation step.
  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).
  Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.

  WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
  see: MaxSimulationTimeStep
- ``max_simulation_time_step`` (float):  [Read-Write] Max time delta for each discrete simulation step.
  Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).
  Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.

  WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
  see: MaxSimulationIterations
- ``max_step_height`` (float):  [Read-Write] Maximum height character can step up
- ``max_swim_speed`` (float):  [Read-Write] The maximum swimming speed.
- ``max_touch_force`` (float):  [Read-Write] Maximum force applied to touched physics objects. If < 0.0f, there is no maximum.
- ``max_walk_speed`` (float):  [Read-Write] The maximum ground speed when walking. Also determines maximum lateral speed when falling.
- ``max_walk_speed_crouched`` (float):  [Read-Write] The maximum ground speed when walking and crouched.
- ``min_analog_walk_speed`` (float):  [Read-Write] The ground speed that we should accelerate up to when walking at minimum analog stick tilt
- ``min_pitch`` (float):  [Read-Write] Controls how far down you can look
- ``min_touch_force`` (float):  [Read-Write] Minimum Force applied to touched physics objects. If < 0.0f, there is no minimum.
- ``movement_mode`` (MovementMode):  [Read-Write] Actor's current movement mode (walking, falling, etc).
     - walking:  Walking on a surface, under the effects of friction, and able to "step up" barriers. Vertical velocity is zero.
     - falling:  Falling under the effects of gravity, after jumping or walking off the edge of a surface.
     - flying:   Flying, ignoring the effects of gravity.
     - swimming: Swimming through a fluid volume, under the effects of gravity and buoyancy.
     - custom:   User-defined custom movement mode, including many possible sub-modes.
  This is automatically replicated through the Character owner and for client-server movement functions.
  see: SetMovementMode(), CustomMovementMode
- ``nav_agent_props`` (NavAgentProperties):  [Read-Write] Properties that define how the component can move.
- ``nav_mesh_projection_height_scale_down`` (float):  [Read-Write] Scale of the total capsule height to use for projection from navmesh to underlying geometry in the downward direction.
  In other words, trace down to [CapsuleHeight * NavMeshProjectionHeightScaleDown] below nav mesh.
- ``nav_mesh_projection_height_scale_up`` (float):  [Read-Write] Scale of the total capsule height to use for projection from navmesh to underlying geometry in the upward direction.
  In other words, start the trace at [CapsuleHeight * NavMeshProjectionHeightScaleUp] above nav mesh.
- ``nav_mesh_projection_interp_speed`` (float):  [Read-Write] Speed at which to interpolate agent navmesh offset between traces. 0: Instant (no interp) > 0: Interp speed")
- ``nav_mesh_projection_interval`` (float):  [Read-Write] How often we should raycast to project from navmesh to underlying geometry
- ``nav_movement_properties`` (NavMovementProperties):  [Read-Write]
- ``nav_walking_floor_dist_tolerance`` (float):  [Read-Write] Ignore small differences in ground height between server and client data during NavWalking mode
- ``net_proxy_shrink_half_height`` (float):  [Read-Write] Shrink simulated proxy capsule half height by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.
  see: AdjustProxyCapsuleSize()
- ``net_proxy_shrink_radius`` (float):  [Read-Write] Shrink simulated proxy capsule radius by this amount, to account for network rounding that may cause encroachment. Changing during gameplay is not supported.
  see: AdjustProxyCapsuleSize()
- ``network_always_replicate_transform_update_timestamp`` (bool):  [Read-Write] Flag used on the server to determine whether to always replicate ReplicatedServerLastTransformUpdateTimeStamp to clients.
  Normally this is only sent when the network smoothing mode on character movement is set to Linear smoothing (on the server), to save bandwidth.
  Setting this to true will force the timestamp to replicate regardless, in case the server doesn't know about the smoothing mode, or if the timestamp is used for another purpose.
- ``network_large_client_correction_distance`` (float):  [Read-Write] If client error is larger than this, sets bNetworkLargeClientCorrection to reduce delay between client adjustments.
  see: NetworkMinTimeBetweenClientAdjustments, NetworkMinTimeBetweenClientAdjustmentsLargeCorrection
- ``network_max_smooth_update_distance`` (float):  [Read-Write] Maximum distance character is allowed to lag behind server location when interpolating between updates.
- ``network_min_time_between_client_ack_good_moves`` (float):  [Read-Write] Minimum time on the server between acknowledging good client moves. This can save on bandwidth. Set to 0 to disable throttling.
- ``network_min_time_between_client_adjustments`` (float):  [Read-Write] Minimum time on the server between sending client adjustments when client has exceeded allowable position error.
  Should be >= NetworkMinTimeBetweenClientAdjustmentsLargeCorrection (the larger value is used regardless).
  This can save on bandwidth. Set to 0 to disable throttling.
  see: ServerLastClientAdjustmentTime
- ``network_min_time_between_client_adjustments_large_correction`` (float):  [Read-Write] Minimum time on the server between sending client adjustments when client has exceeded allowable position error by a large amount (NetworkLargeClientCorrectionDistance).
  Should be <= NetworkMinTimeBetweenClientAdjustments (the smaller value is used regardless).
  see: NetworkMinTimeBetweenClientAdjustments
- ``network_no_smooth_update_distance`` (float):  [Read-Write] Maximum distance beyond which character is teleported to the new server location without any smoothing.
- ``network_simulated_smooth_location_time`` (float):  [Read-Write] How long to take to smoothly interpolate from the old pawn position on the client to the corrected one sent by the server. Not used by Linear smoothing.
- ``network_simulated_smooth_rotation_time`` (float):  [Read-Write] How long to take to smoothly interpolate from the old pawn rotation on the client to the corrected one sent by the server. Not used by Linear smoothing.
- ``network_skip_proxy_prediction_on_net_update`` (bool):  [Read-Write] Whether we skip prediction on frames where a proxy receives a network update. This can avoid expensive prediction on those frames,
  with the side-effect of predicting with a frame of additional latency.
- ``network_smoothing_mode`` (NetworkSmoothingMode):  [Read-Write] Smoothing mode for simulated proxies in network game.
- ``notify_apex`` (bool):  [Read-Only] If true, event NotifyJumpApex() to CharacterOwner's controller when at apex of jump. Is cleared when event is triggered.
  By default this is off, and if you want the event to fire you typically set it to true when movement mode changes to "Falling" from another mode (see OnMovementModeChanged).
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``orient_rotation_to_movement`` (bool):  [Read-Write] If true, rotate the Character toward the direction of acceleration, using RotationRate as the rate of rotation change. Overrides UseControllerDesiredRotation.
  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character.
- ``outof_water_z`` (float):  [Read-Write] Z velocity applied when pawn tries to get out of water
- ``perch_additional_height`` (float):  [Read-Write] When perching on a ledge, add this additional distance to MaxStepHeight when determining how high above a walkable floor we can perch.
  Note that we still enforce MaxStepHeight to start the step up; this just allows the character to hang off the edge or step slightly higher off the floor.
  (
  see: PerchRadiusThreshold)
- ``perch_radius_threshold`` (float):  [Read-Write] Don't allow the character to perch on the edge of a surface if the contact is this close to the edge of the capsule.
  Note that characters will not fall off if they are within MaxStepHeight of a walkable surface below.
- ``plane_constraint_axis_setting`` (PlaneConstraintAxisSetting):  [Read-Write] Setting that controls behavior when movement is restricted to a 2D plane defined by a specific axis/normal,
  so that movement along the locked axis is not be possible.
  see: SetPlaneConstraintAxisSetting
- ``plane_constraint_normal`` (Vector):  [Read-Write] The normal or axis of the plane that constrains movement, if bConstrainToPlane is enabled.
  If for example you wanted to constrain movement to the X-Z plane (so that Y cannot change), the normal would be set to X=0 Y=1 Z=0.
  This is recalculated whenever PlaneConstraintAxisSetting changes. It is normalized once the component is registered with the game world.
  see: bConstrainToPlane, SetPlaneConstraintNormal(), SetPlaneConstraintFromVectors()
- ``plane_constraint_origin`` (Vector):  [Read-Write] The origin of the plane that constrains movement, if plane constraint is enabled.
  This defines the behavior of snapping a position to the plane, such as by SnapUpdatedComponentToPlane().
  see: bConstrainToPlane, SetPlaneConstraintOrigin().
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``project_nav_mesh_on_both_world_channels`` (bool):  [Read-Write] Use both WorldStatic and WorldDynamic channels for NavWalking geometry conforming
- ``project_nav_mesh_walking`` (bool):  [Read-Write] Whether to raycast to underlying geometry to better conform navmesh-walking characters
- ``push_force_factor`` (float):  [Read-Write] Force to apply when the player collides with a blocking physics object.
- ``push_force_point_z_offset_factor`` (float):  [Read-Write] Z-Offset for the position the force is applied to. 0.0f is the center of the physics object, 1.0f is the top and -1.0f is the bottom of the object.
- ``push_force_scaled_to_mass`` (bool):  [Read-Write] If enabled, the PushForceFactor is applied per kg mass of the affected object.
- ``push_force_using_z_offset`` (bool):  [Read-Write] If enabled, the PushForce location is moved using PushForcePointZOffsetFactor. Otherwise simply use the impact point.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``repulsion_force`` (float):  [Read-Write] Force per kg applied constantly to all overlapping components.
- ``requested_move_use_acceleration`` (bool):  [Read-Write] Should use acceleration for path following?
  If true, acceleration is applied when path following to reach the target velocity.
  If false, path following velocity is set directly, disregarding acceleration.
- ``rotation_rate`` (Rotator):  [Read-Write] Change in rotation per second, used when UseControllerDesiredRotation or OrientRotationToMovement are true. Set a negative value for infinite rotation rate and instant turns.
- ``rotational_acceleration`` (Rotator):  [Read-Write] Controls how fast the character's turn rate accelerates when rotating and looking up/down
- ``rotational_deceleration`` (Rotator):  [Read-Write] Controls how fast the character's turn rate decelerates to 0 when user stops turning
- ``run_physics_with_no_controller`` (bool):  [Read-Write] If true, movement will be performed even if there is no Controller for the Character owner.
  Normally without a Controller, movement will be aborted and velocity and acceleration are zeroed if the character is walking.
  Characters that are spawned without a Controller but with this flag enabled will initialize the movement mode to DefaultLandMovementMode or DefaultWaterMovementMode appropriately.
  see: DefaultLandMovementMode, DefaultWaterMovementMode
- ``scale_push_force_to_velocity`` (bool):  [Read-Write] If enabled, the applied push force will try to get the physics object to the same velocity than the player, not faster. This will only
                scale the force down, it will never apply more force than defined by PushForceFactor.
- ``server_accept_client_authoritative_position`` (bool):  [Read-Write] If true, and server does not detect client position error, server will copy the client movement location/velocity/etc after simulating the move.
  This can be useful for short bursts of movement that are difficult to sync over the network.
  Note that if bIgnoreClientMovementErrorChecksAndCorrection is used, this means the server will not detect an error.
  Also see GameNetworkManager->ClientAuthorativePosition which permanently enables this behavior.
  see: bIgnoreClientMovementErrorChecksAndCorrection, ServerShouldUseAuthoritativePosition()
- ``snap_to_plane_at_start`` (bool):  [Read-Write] If true and plane constraints are enabled, then the updated component will be snapped to the plane when first attached.
- ``standing_downward_force_scale`` (float):  [Read-Write] Force applied to objects we stand on (due to Mass and Gravity) is scaled by this amount.
- ``stay_based_in_air`` (bool):  [Read-Write] Property to set if characters should stay based on objects while jumping
- ``stay_based_in_air_height`` (float):  [Read-Write] Property used to set how high above base characters should stay based on objects while jumping if bStayBasedInAir is set
- ``sweep_while_nav_walking`` (bool):  [Read-Write] Whether or not the character should sweep for collision geometry while walking.
  see: USceneComponent::MoveComponent.
- ``tick_before_owner`` (bool):  [Read-Write] If true, after registration we will add a tick dependency to tick before our owner (if we can both tick).
  This is important when our tick causes an update in the owner's position, so that when the owner ticks it uses the most recent position without lag.
  Disabling this can improve performance if both objects tick but the order of ticks doesn't matter.
- ``touch_force_factor`` (float):  [Read-Write] Force to apply to physics objects that are touched by the player.
- ``touch_force_scaled_to_mass`` (bool):  [Read-Write] If enabled, the TouchForceFactor is applied per kg mass of the affected object.
- ``update_nav_agent_with_owners_collision`` (bool):  [Read-Write]
  deprecated: bUpdateNavAgentWithOwnersCollision is deprecated, please use NavMovementProperties.bUpdateNavAgentWithOwnersCollision instead.
- ``update_only_if_rendered`` (bool):  [Read-Write] If true, skips TickComponent() if UpdatedComponent was not recently rendered.
- ``updated_component`` (SceneComponent):  [Read-Write] The component we move and update.
  If this is null at startup and bAutoRegisterUpdatedComponent is true, the owning Actor's root component will automatically be set as our UpdatedComponent at startup.
  see: bAutoRegisterUpdatedComponent, SetUpdatedComponent(), UpdatedPrimitive
- ``updated_primitive`` (PrimitiveComponent):  [Read-Write] UpdatedComponent, cast as a UPrimitiveComponent. May be invalid if UpdatedComponent was null or not a UPrimitiveComponent.
- ``use_acceleration_for_paths`` (bool):  [Read-Write]
  deprecated: bUseAccelerationForPaths is deprecated, please use NavMovementProperties.bUseAccelerationForPaths instead.
- ``use_controller_desired_rotation`` (bool):  [Read-Write] If true, smoothly rotate the Character toward the Controller's desired rotation (typically Controller->ControlRotation), using RotationRate as the rate of rotation change. Overridden by OrientRotationToMovement.
  Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character.
- ``use_fixed_braking_distance_for_paths`` (bool):  [Read-Write]
  deprecated: bUseFixedBrakingDistanceForPaths is deprecated, please use NavMovementProperties.bUseFixedBrakingDistanceForPaths instead.
- ``use_flat_base_for_floor_checks`` (bool):  [Read-Write] Performs floor checks as if the character is using a shape with a flat base.
  This avoids the situation where characters slowly lower off the side of a ledge (as their capsule 'balances' on the edge).
- ``use_rvo_avoidance`` (bool):  [Read-Write] If set, component will use RVO avoidance. This only runs on the server.
- ``use_separate_braking_friction`` (bool):  [Read-Write] If true, BrakingFriction will be used to slow the character to a stop (when there is no Acceleration).
  If false, braking uses the same friction passed to CalcVelocity() (ie GroundFriction when walking), multiplied by BrakingFrictionFactor.
  This setting applies to all movement modes; if only desired in certain modes, consider toggling it when movement modes change.
  see: BrakingFriction
- ``velocity`` (Vector):  [Read-Write] Current velocity of updated component.
- ``walkable_floor_angle`` (float):  [Read-Write] Max angle in degrees of a walkable surface. Any greater than this and it is too steep to be walkable.
- ``walkable_floor_z`` (float):  [Read-Only] Minimum Z value for floor normal. If less, not a walkable surface. Computed from WalkableFloorAngle.
- ``walking_acceleration`` (float):  [Read-Write] How fast the character accelerates.
- ``walking_friction`` (float):  [Read-Write] Controls walking deceleration.
- ``walking_speed`` (float):  [Read-Write] How fast the character can walk.
- ``wants_to_crouch`` (bool):  [Read-Only] If true, try to crouch (or keep crouching) on next update. If false, try to stop crouching on next update.
- ``world_to_gravity_transform`` (Quat):  [Read-Only] A cached quaternion representing the rotation from world space to gravity relative space defined by GravityDirection.

<a id="unreal.ArchVisCharMovementComponent.rotational_acceleration"></a>

#### rotational_acceleration

```python
@property
def rotational_acceleration() -> Rotator
```

(Rotator):  [Read-Only] Controls how fast the character's turn rate accelerates when rotating and looking up/down

<a id="unreal.ArchVisCharMovementComponent.rotational_deceleration"></a>

#### rotational_deceleration

```python
@property
def rotational_deceleration() -> Rotator
```

(Rotator):  [Read-Only] Controls how fast the character's turn rate decelerates to 0 when user stops turning

<a id="unreal.ArchVisCharMovementComponent.max_rotational_velocity"></a>

#### max_rotational_velocity

```python
@property
def max_rotational_velocity() -> Rotator
```

(Rotator):  [Read-Only] Fastest possible turn rate

<a id="unreal.ArchVisCharMovementComponent.min_pitch"></a>

#### min_pitch

```python
@property
def min_pitch() -> float
```

(float):  [Read-Only] Controls how far down you can look

<a id="unreal.ArchVisCharMovementComponent.max_pitch"></a>

#### max_pitch

```python
@property
def max_pitch() -> float
```

(float):  [Read-Only] Controls how far up you can look

<a id="unreal.ArchVisCharMovementComponent.walking_friction"></a>

#### walking_friction

```python
@property
def walking_friction() -> float
```

(float):  [Read-Only] Controls walking deceleration.

<a id="unreal.ArchVisCharMovementComponent.walking_speed"></a>

#### walking_speed

```python
@property
def walking_speed() -> float
```

(float):  [Read-Only] How fast the character can walk.

<a id="unreal.ArchVisCharMovementComponent.walking_acceleration"></a>

#### walking_acceleration

```python
@property
def walking_acceleration() -> float
```

(float):  [Read-Only] How fast the character accelerates.

<a id="unreal.AssetTagsSubsystem"></a>