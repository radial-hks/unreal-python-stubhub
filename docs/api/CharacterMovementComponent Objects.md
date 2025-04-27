## CharacterMovementComponent Objects

```python
class CharacterMovementComponent(PawnMovementComponent)
```

CharacterMovementComponent handles movement logic for the associated Character owner.
It supports various movement modes including: walking, falling, swimming, flying, custom.

Movement is affected primarily by current Velocity and Acceleration. Acceleration is updated each frame
based on the input vector accumulated thus far (see UPawnMovementComponent::GetPendingInputVector()).

Networking is fully implemented, with server-client correction and prediction included.
see: ACharacter, UPawnMovementComponent
see: https://docs.unrealengine.com/latest/INT/Gameplay/Framework/Pawn/Character/

**C++ Source:**

- **Module**: Engine
- **File**: CharacterMovementComponent.h

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
- ``wants_to_crouch`` (bool):  [Read-Only] If true, try to crouch (or keep crouching) on next update. If false, try to stop crouching on next update.
- ``world_to_gravity_transform`` (Quat):  [Read-Only] A cached quaternion representing the rotation from world space to gravity relative space defined by GravityDirection.

<a id="unreal.CharacterMovementComponent.gravity_scale"></a>

#### gravity_scale

```python
@property
def gravity_scale() -> float
```

(float):  [Read-Write] Custom gravity scale. Gravity is multiplied by this amount for the character.

<a id="unreal.CharacterMovementComponent.gravity_scale"></a>

#### gravity_scale

```python
@gravity_scale.setter
def gravity_scale(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_step_height"></a>

#### max_step_height

```python
@property
def max_step_height() -> float
```

(float):  [Read-Write] Maximum height character can step up

<a id="unreal.CharacterMovementComponent.max_step_height"></a>

#### max_step_height

```python
@max_step_height.setter
def max_step_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.jump_z_velocity"></a>

#### jump_z_velocity

```python
@property
def jump_z_velocity() -> float
```

(float):  [Read-Write] Initial velocity (instantaneous vertical acceleration) when jumping.

<a id="unreal.CharacterMovementComponent.jump_z_velocity"></a>

#### jump_z_velocity

```python
@jump_z_velocity.setter
def jump_z_velocity(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.jump_z"></a>

#### jump_z

```python
@property
def jump_z() -> float
```

deprecated: 'jump_z' was renamed to 'jump_z_velocity'.

<a id="unreal.CharacterMovementComponent.jump_z"></a>

#### jump_z

```python
@jump_z.setter
def jump_z(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.jump_off_jump_z_factor"></a>

#### jump_off_jump_z_factor

```python
@property
def jump_off_jump_z_factor() -> float
```

(float):  [Read-Write] Fraction of JumpZVelocity to use when automatically "jumping off" of a base actor that's not allowed to be a base for a character. (For example, if you're not allowed to stand on other players.)

<a id="unreal.CharacterMovementComponent.jump_off_jump_z_factor"></a>

#### jump_off_jump_z_factor

```python
@jump_off_jump_z_factor.setter
def jump_off_jump_z_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.gravity_direction"></a>

#### gravity_direction

```python
@property
def gravity_direction() -> Vector
```

(Vector):  [Read-Only] A normalized vector representing the direction of gravity for gravity relative movement modes: walking, falling,
and custom movement modes. Gravity direction remaps player input as being within the plane defined by the gravity
direction. Movement simulation values like velocity and acceleration are maintained in their existing world coordinate
space but are transformed internally as gravity relative (for instance moving forward up a vertical wall that gravity is
defined to be perpendicular to and jump "up" from that wall). If ShouldRemainVertical() is true the character's capsule
will be oriented to align with the gravity direction.

<a id="unreal.CharacterMovementComponent.world_to_gravity_transform"></a>

#### world_to_gravity_transform

```python
@property
def world_to_gravity_transform() -> Quat
```

(Quat):  [Read-Only] A cached quaternion representing the rotation from world space to gravity relative space defined by GravityDirection.

<a id="unreal.CharacterMovementComponent.gravity_to_world_transform"></a>

#### gravity_to_world_transform

```python
@property
def gravity_to_world_transform() -> Quat
```

(Quat):  [Read-Only] A cached quaternion representing the inverse rotation from world space to gravity relative space defined by GravityDirection.

<a id="unreal.CharacterMovementComponent.movement_mode"></a>

#### movement_mode

```python
@property
def movement_mode() -> MovementMode
```

(MovementMode):  [Read-Only] Actor's current movement mode (walking, falling, etc).
   - walking:  Walking on a surface, under the effects of friction, and able to "step up" barriers. Vertical velocity is zero.
   - falling:  Falling under the effects of gravity, after jumping or walking off the edge of a surface.
   - flying:   Flying, ignoring the effects of gravity.
   - swimming: Swimming through a fluid volume, under the effects of gravity and buoyancy.
   - custom:   User-defined custom movement mode, including many possible sub-modes.
This is automatically replicated through the Character owner and for client-server movement functions.
see: SetMovementMode(), CustomMovementMode

<a id="unreal.CharacterMovementComponent.custom_movement_mode"></a>

#### custom_movement_mode

```python
@property
def custom_movement_mode() -> int
```

(uint8):  [Read-Only] Current custom sub-mode if MovementMode is set to Custom.
This is automatically replicated through the Character owner and for client-server movement functions.
see: SetMovementMode()

<a id="unreal.CharacterMovementComponent.network_smoothing_mode"></a>

#### network_smoothing_mode

```python
@property
def network_smoothing_mode() -> NetworkSmoothingMode
```

(NetworkSmoothingMode):  [Read-Only] Smoothing mode for simulated proxies in network game.

<a id="unreal.CharacterMovementComponent.ground_friction"></a>

#### ground_friction

```python
@property
def ground_friction() -> float
```

(float):  [Read-Write] Setting that affects movement control. Higher values allow faster changes in direction.
If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero), where it is multiplied by BrakingFrictionFactor.
When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.
This can be used to simulate slippery surfaces such as ice or oil by changing the value (possibly based on the material pawn is standing on).
see: BrakingDecelerationWalking, BrakingFriction, bUseSeparateBrakingFriction, BrakingFrictionFactor

<a id="unreal.CharacterMovementComponent.ground_friction"></a>

#### ground_friction

```python
@ground_friction.setter
def ground_friction(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_walk_speed"></a>

#### max_walk_speed

```python
@property
def max_walk_speed() -> float
```

(float):  [Read-Write] The maximum ground speed when walking. Also determines maximum lateral speed when falling.

<a id="unreal.CharacterMovementComponent.max_walk_speed"></a>

#### max_walk_speed

```python
@max_walk_speed.setter
def max_walk_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.ground_speed"></a>

#### ground_speed

```python
@property
def ground_speed() -> float
```

deprecated: 'ground_speed' was renamed to 'max_walk_speed'.

<a id="unreal.CharacterMovementComponent.ground_speed"></a>

#### ground_speed

```python
@ground_speed.setter
def ground_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_walk_speed_crouched"></a>

#### max_walk_speed_crouched

```python
@property
def max_walk_speed_crouched() -> float
```

(float):  [Read-Write] The maximum ground speed when walking and crouched.

<a id="unreal.CharacterMovementComponent.max_walk_speed_crouched"></a>

#### max_walk_speed_crouched

```python
@max_walk_speed_crouched.setter
def max_walk_speed_crouched(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_swim_speed"></a>

#### max_swim_speed

```python
@property
def max_swim_speed() -> float
```

(float):  [Read-Write] The maximum swimming speed.

<a id="unreal.CharacterMovementComponent.max_swim_speed"></a>

#### max_swim_speed

```python
@max_swim_speed.setter
def max_swim_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.water_speed"></a>

#### water_speed

```python
@property
def water_speed() -> float
```

deprecated: 'water_speed' was renamed to 'max_swim_speed'.

<a id="unreal.CharacterMovementComponent.water_speed"></a>

#### water_speed

```python
@water_speed.setter
def water_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_fly_speed"></a>

#### max_fly_speed

```python
@property
def max_fly_speed() -> float
```

(float):  [Read-Write] The maximum flying speed.

<a id="unreal.CharacterMovementComponent.max_fly_speed"></a>

#### max_fly_speed

```python
@max_fly_speed.setter
def max_fly_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.air_speed"></a>

#### air_speed

```python
@property
def air_speed() -> float
```

deprecated: 'air_speed' was renamed to 'max_fly_speed'.

<a id="unreal.CharacterMovementComponent.air_speed"></a>

#### air_speed

```python
@air_speed.setter
def air_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_custom_movement_speed"></a>

#### max_custom_movement_speed

```python
@property
def max_custom_movement_speed() -> float
```

(float):  [Read-Write] The maximum speed when using Custom movement mode.

<a id="unreal.CharacterMovementComponent.max_custom_movement_speed"></a>

#### max_custom_movement_speed

```python
@max_custom_movement_speed.setter
def max_custom_movement_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_acceleration"></a>

#### max_acceleration

```python
@property
def max_acceleration() -> float
```

(float):  [Read-Write] Max Acceleration (rate of change of velocity)

<a id="unreal.CharacterMovementComponent.max_acceleration"></a>

#### max_acceleration

```python
@max_acceleration.setter
def max_acceleration(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.accel_rate"></a>

#### accel_rate

```python
@property
def accel_rate() -> float
```

deprecated: 'accel_rate' was renamed to 'max_acceleration'.

<a id="unreal.CharacterMovementComponent.accel_rate"></a>

#### accel_rate

```python
@accel_rate.setter
def accel_rate(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.min_analog_walk_speed"></a>

#### min_analog_walk_speed

```python
@property
def min_analog_walk_speed() -> float
```

(float):  [Read-Write] The ground speed that we should accelerate up to when walking at minimum analog stick tilt

<a id="unreal.CharacterMovementComponent.min_analog_walk_speed"></a>

#### min_analog_walk_speed

```python
@min_analog_walk_speed.setter
def min_analog_walk_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_friction_factor"></a>

#### braking_friction_factor

```python
@property
def braking_friction_factor() -> float
```

(float):  [Read-Write] Factor used to multiply actual value of friction used when braking.
This applies to any friction value that is currently used, which may depend on bUseSeparateBrakingFriction.
note: This is 2 by default for historical reasons, a value of 1 gives the true drag equation.
see: bUseSeparateBrakingFriction, GroundFriction, BrakingFriction

<a id="unreal.CharacterMovementComponent.braking_friction_factor"></a>

#### braking_friction_factor

```python
@braking_friction_factor.setter
def braking_friction_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_friction"></a>

#### braking_friction

```python
@property
def braking_friction() -> float
```

(float):  [Read-Write] Friction (drag) coefficient applied when braking (whenever Acceleration = 0, or if character is exceeding max speed); actual value used is this multiplied by BrakingFrictionFactor.
When braking, this property allows you to control how much friction is applied when moving across the ground, applying an opposing force that scales with current velocity.
Braking is composed of friction (velocity-dependent drag) and constant deceleration.
This is the current value, used in all movement modes; if this is not desired, override it or bUseSeparateBrakingFriction when movement mode changes.
note: Only used if bUseSeparateBrakingFriction setting is true, otherwise current friction such as GroundFriction is used.
see: bUseSeparateBrakingFriction, BrakingFrictionFactor, GroundFriction, BrakingDecelerationWalking

<a id="unreal.CharacterMovementComponent.braking_friction"></a>

#### braking_friction

```python
@braking_friction.setter
def braking_friction(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_sub_step_time"></a>

#### braking_sub_step_time

```python
@property
def braking_sub_step_time() -> float
```

(float):  [Read-Write] Time substepping when applying braking friction. Smaller time steps increase accuracy at the slight cost of performance, especially if there are large frame times.

<a id="unreal.CharacterMovementComponent.braking_sub_step_time"></a>

#### braking_sub_step_time

```python
@braking_sub_step_time.setter
def braking_sub_step_time(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_deceleration_walking"></a>

#### braking_deceleration_walking

```python
@property
def braking_deceleration_walking() -> float
```

(float):  [Read-Write] Deceleration when walking and not applying acceleration. This is a constant opposing force that directly lowers velocity by a constant value.
see: GroundFriction, MaxAcceleration

<a id="unreal.CharacterMovementComponent.braking_deceleration_walking"></a>

#### braking_deceleration_walking

```python
@braking_deceleration_walking.setter
def braking_deceleration_walking(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_deceleration"></a>

#### braking_deceleration

```python
@property
def braking_deceleration() -> float
```

deprecated: 'braking_deceleration' was renamed to 'braking_deceleration_walking'.

<a id="unreal.CharacterMovementComponent.braking_deceleration"></a>

#### braking_deceleration

```python
@braking_deceleration.setter
def braking_deceleration(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_deceleration_falling"></a>

#### braking_deceleration_falling

```python
@property
def braking_deceleration_falling() -> float
```

(float):  [Read-Write] Lateral deceleration when falling and not applying acceleration.
see: MaxAcceleration

<a id="unreal.CharacterMovementComponent.braking_deceleration_falling"></a>

#### braking_deceleration_falling

```python
@braking_deceleration_falling.setter
def braking_deceleration_falling(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_deceleration_swimming"></a>

#### braking_deceleration_swimming

```python
@property
def braking_deceleration_swimming() -> float
```

(float):  [Read-Write] Deceleration when swimming and not applying acceleration.
see: MaxAcceleration

<a id="unreal.CharacterMovementComponent.braking_deceleration_swimming"></a>

#### braking_deceleration_swimming

```python
@braking_deceleration_swimming.setter
def braking_deceleration_swimming(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.braking_deceleration_flying"></a>

#### braking_deceleration_flying

```python
@property
def braking_deceleration_flying() -> float
```

(float):  [Read-Write] Deceleration when flying and not applying acceleration.
see: MaxAcceleration

<a id="unreal.CharacterMovementComponent.braking_deceleration_flying"></a>

#### braking_deceleration_flying

```python
@braking_deceleration_flying.setter
def braking_deceleration_flying(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.air_control"></a>

#### air_control

```python
@property
def air_control() -> float
```

(float):  [Read-Write] When falling, amount of lateral movement control available to the character.
0 = no control, 1 = full control at max speed of MaxWalkSpeed.

<a id="unreal.CharacterMovementComponent.air_control"></a>

#### air_control

```python
@air_control.setter
def air_control(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.air_control_boost_multiplier"></a>

#### air_control_boost_multiplier

```python
@property
def air_control_boost_multiplier() -> float
```

(float):  [Read-Write] When falling, multiplier applied to AirControl when lateral velocity is less than AirControlBoostVelocityThreshold.
Setting this to zero will disable air control boosting. Final result is clamped at 1.

<a id="unreal.CharacterMovementComponent.air_control_boost_multiplier"></a>

#### air_control_boost_multiplier

```python
@air_control_boost_multiplier.setter
def air_control_boost_multiplier(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.air_control_boost_velocity_threshold"></a>

#### air_control_boost_velocity_threshold

```python
@property
def air_control_boost_velocity_threshold() -> float
```

(float):  [Read-Write] When falling, if lateral velocity magnitude is less than this value, AirControl is multiplied by AirControlBoostMultiplier.
Setting this to zero will disable air control boosting.

<a id="unreal.CharacterMovementComponent.air_control_boost_velocity_threshold"></a>

#### air_control_boost_velocity_threshold

```python
@air_control_boost_velocity_threshold.setter
def air_control_boost_velocity_threshold(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.falling_lateral_friction"></a>

#### falling_lateral_friction

```python
@property
def falling_lateral_friction() -> float
```

(float):  [Read-Write] Friction to apply to lateral air movement when falling.
If bUseSeparateBrakingFriction is false, also affects the ability to stop more quickly when braking (whenever Acceleration is zero).
see: BrakingFriction, bUseSeparateBrakingFriction

<a id="unreal.CharacterMovementComponent.falling_lateral_friction"></a>

#### falling_lateral_friction

```python
@falling_lateral_friction.setter
def falling_lateral_friction(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.crouched_half_height"></a>

#### crouched_half_height

```python
@property
def crouched_half_height() -> float
```

(float):  [Read-Write]

<a id="unreal.CharacterMovementComponent.crouched_half_height"></a>

#### crouched_half_height

```python
@crouched_half_height.setter
def crouched_half_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.crouch_height"></a>

#### crouch_height

```python
@property
def crouch_height() -> float
```

deprecated: 'crouch_height' was renamed to 'crouched_half_height'.

<a id="unreal.CharacterMovementComponent.crouch_height"></a>

#### crouch_height

```python
@crouch_height.setter
def crouch_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.buoyancy"></a>

#### buoyancy

```python
@property
def buoyancy() -> float
```

(float):  [Read-Write] Water buoyancy. A ratio (1.0 = neutral buoyancy, 0.0 = no buoyancy)

<a id="unreal.CharacterMovementComponent.buoyancy"></a>

#### buoyancy

```python
@buoyancy.setter
def buoyancy(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.perch_radius_threshold"></a>

#### perch_radius_threshold

```python
@property
def perch_radius_threshold() -> float
```

(float):  [Read-Write] Don't allow the character to perch on the edge of a surface if the contact is this close to the edge of the capsule.
Note that characters will not fall off if they are within MaxStepHeight of a walkable surface below.

<a id="unreal.CharacterMovementComponent.perch_radius_threshold"></a>

#### perch_radius_threshold

```python
@perch_radius_threshold.setter
def perch_radius_threshold(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.perch_additional_height"></a>

#### perch_additional_height

```python
@property
def perch_additional_height() -> float
```

(float):  [Read-Write] When perching on a ledge, add this additional distance to MaxStepHeight when determining how high above a walkable floor we can perch.
Note that we still enforce MaxStepHeight to start the step up; this just allows the character to hang off the edge or step slightly higher off the floor.
(
see: PerchRadiusThreshold)

<a id="unreal.CharacterMovementComponent.perch_additional_height"></a>

#### perch_additional_height

```python
@perch_additional_height.setter
def perch_additional_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.rotation_rate"></a>

#### rotation_rate

```python
@property
def rotation_rate() -> Rotator
```

(Rotator):  [Read-Write] Change in rotation per second, used when UseControllerDesiredRotation or OrientRotationToMovement are true. Set a negative value for infinite rotation rate and instant turns.

<a id="unreal.CharacterMovementComponent.rotation_rate"></a>

#### rotation_rate

```python
@rotation_rate.setter
def rotation_rate(value: Rotator) -> None
```

<a id="unreal.CharacterMovementComponent.use_separate_braking_friction"></a>

#### use_separate_braking_friction

```python
@property
def use_separate_braking_friction() -> bool
```

(bool):  [Read-Write] If true, BrakingFriction will be used to slow the character to a stop (when there is no Acceleration).
If false, braking uses the same friction passed to CalcVelocity() (ie GroundFriction when walking), multiplied by BrakingFrictionFactor.
This setting applies to all movement modes; if only desired in certain modes, consider toggling it when movement modes change.
see: BrakingFriction

<a id="unreal.CharacterMovementComponent.use_separate_braking_friction"></a>

#### use_separate_braking_friction

```python
@use_separate_braking_friction.setter
def use_separate_braking_friction(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.dont_fall_below_jump_z_velocity_during_jump"></a>

#### dont_fall_below_jump_z_velocity_during_jump

```python
@property
def dont_fall_below_jump_z_velocity_during_jump() -> bool
```

(bool):  [Read-Write] True means while the jump key is held, we will not allow the vertical speed to fall below the JumpZVelocity tuning value
even if a stronger force, such as gravity, is opposing the jump.

<a id="unreal.CharacterMovementComponent.dont_fall_below_jump_z_velocity_during_jump"></a>

#### dont_fall_below_jump_z_velocity_during_jump

```python
@dont_fall_below_jump_z_velocity_during_jump.setter
def dont_fall_below_jump_z_velocity_during_jump(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.apply_gravity_while_jumping"></a>

#### apply_gravity_while_jumping

```python
@property
def apply_gravity_while_jumping() -> bool
```

(bool):  [Read-Write] Apply gravity while the character is actively jumping (e.g. holding the jump key).
Helps remove frame-rate dependent jump height, but may alter base jump height.

<a id="unreal.CharacterMovementComponent.apply_gravity_while_jumping"></a>

#### apply_gravity_while_jumping

```python
@apply_gravity_while_jumping.setter
def apply_gravity_while_jumping(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.use_controller_desired_rotation"></a>

#### use_controller_desired_rotation

```python
@property
def use_controller_desired_rotation() -> bool
```

(bool):  [Read-Write] If true, smoothly rotate the Character toward the Controller's desired rotation (typically Controller->ControlRotation), using RotationRate as the rate of rotation change. Overridden by OrientRotationToMovement.
Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character.

<a id="unreal.CharacterMovementComponent.use_controller_desired_rotation"></a>

#### use_controller_desired_rotation

```python
@use_controller_desired_rotation.setter
def use_controller_desired_rotation(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.orient_rotation_to_movement"></a>

#### orient_rotation_to_movement

```python
@property
def orient_rotation_to_movement() -> bool
```

(bool):  [Read-Write] If true, rotate the Character toward the direction of acceleration, using RotationRate as the rate of rotation change. Overrides UseControllerDesiredRotation.
Normally you will want to make sure that other settings are cleared, such as bUseControllerRotationYaw on the Character.

<a id="unreal.CharacterMovementComponent.orient_rotation_to_movement"></a>

#### orient_rotation_to_movement

```python
@orient_rotation_to_movement.setter
def orient_rotation_to_movement(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.b_orient_to_movement"></a>

#### b_orient_to_movement

```python
@property
def b_orient_to_movement() -> bool
```

deprecated: 'b_orient_to_movement' was renamed to 'orient_rotation_to_movement'.

<a id="unreal.CharacterMovementComponent.b_orient_to_movement"></a>

#### b_orient_to_movement

```python
@b_orient_to_movement.setter
def b_orient_to_movement(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.sweep_while_nav_walking"></a>

#### sweep_while_nav_walking

```python
@property
def sweep_while_nav_walking() -> bool
```

(bool):  [Read-Write] Whether or not the character should sweep for collision geometry while walking.
see: USceneComponent::MoveComponent.

<a id="unreal.CharacterMovementComponent.sweep_while_nav_walking"></a>

#### sweep_while_nav_walking

```python
@sweep_while_nav_walking.setter
def sweep_while_nav_walking(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.run_physics_with_no_controller"></a>

#### run_physics_with_no_controller

```python
@property
def run_physics_with_no_controller() -> bool
```

(bool):  [Read-Write] If true, movement will be performed even if there is no Controller for the Character owner.
Normally without a Controller, movement will be aborted and velocity and acceleration are zeroed if the character is walking.
Characters that are spawned without a Controller but with this flag enabled will initialize the movement mode to DefaultLandMovementMode or DefaultWaterMovementMode appropriately.
see: DefaultLandMovementMode, DefaultWaterMovementMode

<a id="unreal.CharacterMovementComponent.run_physics_with_no_controller"></a>

#### run_physics_with_no_controller

```python
@run_physics_with_no_controller.setter
def run_physics_with_no_controller(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.force_next_floor_check"></a>

#### force_next_floor_check

```python
@property
def force_next_floor_check() -> bool
```

(bool):  [Read-Only] Force the Character in MOVE_Walking to do a check for a valid floor even if it hasn't moved. Cleared after next floor check.
Normally if bAlwaysCheckFloor is false we try to avoid the floor check unless some conditions are met, but this can be used to force the next check to always run.

<a id="unreal.CharacterMovementComponent.can_walk_off_ledges"></a>

#### can_walk_off_ledges

```python
@property
def can_walk_off_ledges() -> bool
```

(bool):  [Read-Write] If true, Character can walk off a ledge.

<a id="unreal.CharacterMovementComponent.can_walk_off_ledges"></a>

#### can_walk_off_ledges

```python
@can_walk_off_ledges.setter
def can_walk_off_ledges(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.can_walk_off_ledges_when_crouching"></a>

#### can_walk_off_ledges_when_crouching

```python
@property
def can_walk_off_ledges_when_crouching() -> bool
```

(bool):  [Read-Write] If true, Character can walk off a ledge when crouching.

<a id="unreal.CharacterMovementComponent.can_walk_off_ledges_when_crouching"></a>

#### can_walk_off_ledges_when_crouching

```python
@can_walk_off_ledges_when_crouching.setter
def can_walk_off_ledges_when_crouching(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.enable_physics_interaction"></a>

#### enable_physics_interaction

```python
@property
def enable_physics_interaction() -> bool
```

(bool):  [Read-Write] If enabled, the player will interact with physics objects when walking into them.

<a id="unreal.CharacterMovementComponent.enable_physics_interaction"></a>

#### enable_physics_interaction

```python
@enable_physics_interaction.setter
def enable_physics_interaction(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.touch_force_scaled_to_mass"></a>

#### touch_force_scaled_to_mass

```python
@property
def touch_force_scaled_to_mass() -> bool
```

(bool):  [Read-Write] If enabled, the TouchForceFactor is applied per kg mass of the affected object.

<a id="unreal.CharacterMovementComponent.touch_force_scaled_to_mass"></a>

#### touch_force_scaled_to_mass

```python
@touch_force_scaled_to_mass.setter
def touch_force_scaled_to_mass(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.push_force_scaled_to_mass"></a>

#### push_force_scaled_to_mass

```python
@property
def push_force_scaled_to_mass() -> bool
```

(bool):  [Read-Write] If enabled, the PushForceFactor is applied per kg mass of the affected object.

<a id="unreal.CharacterMovementComponent.push_force_scaled_to_mass"></a>

#### push_force_scaled_to_mass

```python
@push_force_scaled_to_mass.setter
def push_force_scaled_to_mass(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.push_force_using_z_offset"></a>

#### push_force_using_z_offset

```python
@property
def push_force_using_z_offset() -> bool
```

(bool):  [Read-Write] If enabled, the PushForce location is moved using PushForcePointZOffsetFactor. Otherwise simply use the impact point.

<a id="unreal.CharacterMovementComponent.push_force_using_z_offset"></a>

#### push_force_using_z_offset

```python
@push_force_using_z_offset.setter
def push_force_using_z_offset(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.scale_push_force_to_velocity"></a>

#### scale_push_force_to_velocity

```python
@property
def scale_push_force_to_velocity() -> bool
```

(bool):  [Read-Write] If enabled, the applied push force will try to get the physics object to the same velocity than the player, not faster. This will only
              scale the force down, it will never apply more force than defined by PushForceFactor.

<a id="unreal.CharacterMovementComponent.scale_push_force_to_velocity"></a>

#### scale_push_force_to_velocity

```python
@scale_push_force_to_velocity.setter
def scale_push_force_to_velocity(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.max_out_of_water_step_height"></a>

#### max_out_of_water_step_height

```python
@property
def max_out_of_water_step_height() -> float
```

(float):  [Read-Write] Maximum step height for getting out of water

<a id="unreal.CharacterMovementComponent.max_out_of_water_step_height"></a>

#### max_out_of_water_step_height

```python
@max_out_of_water_step_height.setter
def max_out_of_water_step_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.outof_water_z"></a>

#### outof_water_z

```python
@property
def outof_water_z() -> float
```

(float):  [Read-Write] Z velocity applied when pawn tries to get out of water

<a id="unreal.CharacterMovementComponent.outof_water_z"></a>

#### outof_water_z

```python
@outof_water_z.setter
def outof_water_z(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write] Mass of pawn (for when momentum is imparted to it).

<a id="unreal.CharacterMovementComponent.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.standing_downward_force_scale"></a>

#### standing_downward_force_scale

```python
@property
def standing_downward_force_scale() -> float
```

(float):  [Read-Write] Force applied to objects we stand on (due to Mass and Gravity) is scaled by this amount.

<a id="unreal.CharacterMovementComponent.standing_downward_force_scale"></a>

#### standing_downward_force_scale

```python
@standing_downward_force_scale.setter
def standing_downward_force_scale(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.initial_push_force_factor"></a>

#### initial_push_force_factor

```python
@property
def initial_push_force_factor() -> float
```

(float):  [Read-Write] Initial impulse force to apply when the player bounces into a blocking physics object.

<a id="unreal.CharacterMovementComponent.initial_push_force_factor"></a>

#### initial_push_force_factor

```python
@initial_push_force_factor.setter
def initial_push_force_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.push_force_factor"></a>

#### push_force_factor

```python
@property
def push_force_factor() -> float
```

(float):  [Read-Write] Force to apply when the player collides with a blocking physics object.

<a id="unreal.CharacterMovementComponent.push_force_factor"></a>

#### push_force_factor

```python
@push_force_factor.setter
def push_force_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.push_force_point_z_offset_factor"></a>

#### push_force_point_z_offset_factor

```python
@property
def push_force_point_z_offset_factor() -> float
```

(float):  [Read-Write] Z-Offset for the position the force is applied to. 0.0f is the center of the physics object, 1.0f is the top and -1.0f is the bottom of the object.

<a id="unreal.CharacterMovementComponent.push_force_point_z_offset_factor"></a>

#### push_force_point_z_offset_factor

```python
@push_force_point_z_offset_factor.setter
def push_force_point_z_offset_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.touch_force_factor"></a>

#### touch_force_factor

```python
@property
def touch_force_factor() -> float
```

(float):  [Read-Write] Force to apply to physics objects that are touched by the player.

<a id="unreal.CharacterMovementComponent.touch_force_factor"></a>

#### touch_force_factor

```python
@touch_force_factor.setter
def touch_force_factor(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.min_touch_force"></a>

#### min_touch_force

```python
@property
def min_touch_force() -> float
```

(float):  [Read-Write] Minimum Force applied to touched physics objects. If < 0.0f, there is no minimum.

<a id="unreal.CharacterMovementComponent.min_touch_force"></a>

#### min_touch_force

```python
@min_touch_force.setter
def min_touch_force(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_touch_force"></a>

#### max_touch_force

```python
@property
def max_touch_force() -> float
```

(float):  [Read-Write] Maximum force applied to touched physics objects. If < 0.0f, there is no maximum.

<a id="unreal.CharacterMovementComponent.max_touch_force"></a>

#### max_touch_force

```python
@max_touch_force.setter
def max_touch_force(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.repulsion_force"></a>

#### repulsion_force

```python
@property
def repulsion_force() -> float
```

(float):  [Read-Write] Force per kg applied constantly to all overlapping components.

<a id="unreal.CharacterMovementComponent.repulsion_force"></a>

#### repulsion_force

```python
@repulsion_force.setter
def repulsion_force(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_simulation_time_step"></a>

#### max_simulation_time_step

```python
@property
def max_simulation_time_step() -> float
```

(float):  [Read-Write] Max time delta for each discrete simulation step.
Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).
Lowering this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.

WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
see: MaxSimulationIterations

<a id="unreal.CharacterMovementComponent.max_simulation_time_step"></a>

#### max_simulation_time_step

```python
@max_simulation_time_step.setter
def max_simulation_time_step(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_simulation_iterations"></a>

#### max_simulation_iterations

```python
@property
def max_simulation_iterations() -> int
```

(int32):  [Read-Write] Max number of iterations used for each discrete simulation step.
Used primarily in the the more advanced movement modes that break up larger time steps (usually those applying gravity such as falling and walking).
Increasing this value can address issues with fast-moving objects or complex collision scenarios, at the cost of performance.

WARNING: if (MaxSimulationTimeStep * MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.
see: MaxSimulationTimeStep

<a id="unreal.CharacterMovementComponent.max_simulation_iterations"></a>

#### max_simulation_iterations

```python
@max_simulation_iterations.setter
def max_simulation_iterations(value: int) -> None
```

<a id="unreal.CharacterMovementComponent.max_jump_apex_attempts_per_simulation"></a>

#### max_jump_apex_attempts_per_simulation

```python
@property
def max_jump_apex_attempts_per_simulation() -> int
```

(int32):  [Read-Write] Max number of attempts per simulation to attempt to exactly reach the jump apex when falling movement reaches the top of the arc.
Limiting this prevents deep recursion when special cases cause collision or other conditions which reactivate the apex condition.

<a id="unreal.CharacterMovementComponent.max_jump_apex_attempts_per_simulation"></a>

#### max_jump_apex_attempts_per_simulation

```python
@max_jump_apex_attempts_per_simulation.setter
def max_jump_apex_attempts_per_simulation(value: int) -> None
```

<a id="unreal.CharacterMovementComponent.max_depenetration_with_geometry"></a>

#### max_depenetration_with_geometry

```python
@property
def max_depenetration_with_geometry() -> float
```

(float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.
This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.
see: MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy

<a id="unreal.CharacterMovementComponent.max_depenetration_with_geometry"></a>

#### max_depenetration_with_geometry

```python
@max_depenetration_with_geometry.setter
def max_depenetration_with_geometry(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_depenetration_with_geometry_as_proxy"></a>

#### max_depenetration_with_geometry_as_proxy

```python
@property
def max_depenetration_with_geometry_as_proxy() -> float
```

(float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of anything but Pawns.
This is generally more tolerant than with Pawns, because other geometry is either not moving, or is moving predictably with a bit of delay compared to on the server.
see: MaxDepenetrationWithGeometry, MaxDepenetrationWithPawn, MaxDepenetrationWithPawnAsProxy

<a id="unreal.CharacterMovementComponent.max_depenetration_with_geometry_as_proxy"></a>

#### max_depenetration_with_geometry_as_proxy

```python
@max_depenetration_with_geometry_as_proxy.setter
def max_depenetration_with_geometry_as_proxy(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_depenetration_with_pawn"></a>

#### max_depenetration_with_pawn

```python
@property
def max_depenetration_with_pawn() -> float
```

(float):  [Read-Write] Max distance we are allowed to depenetrate when moving out of other Pawns.
see: MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawnAsProxy

<a id="unreal.CharacterMovementComponent.max_depenetration_with_pawn"></a>

#### max_depenetration_with_pawn

```python
@max_depenetration_with_pawn.setter
def max_depenetration_with_pawn(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.max_depenetration_with_pawn_as_proxy"></a>

#### max_depenetration_with_pawn_as_proxy

```python
@property
def max_depenetration_with_pawn_as_proxy() -> float
```

(float):  [Read-Write] Max distance we allow simulated proxies to depenetrate when moving out of other Pawns.
Typically we don't want a large value, because we receive a server authoritative position that we should not then ignore by pushing them out of the local player.
see: MaxDepenetrationWithGeometry, MaxDepenetrationWithGeometryAsProxy, MaxDepenetrationWithPawn

<a id="unreal.CharacterMovementComponent.max_depenetration_with_pawn_as_proxy"></a>

#### max_depenetration_with_pawn_as_proxy

```python
@max_depenetration_with_pawn_as_proxy.setter
def max_depenetration_with_pawn_as_proxy(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.ledge_check_threshold"></a>

#### ledge_check_threshold

```python
@property
def ledge_check_threshold() -> float
```

(float):  [Read-Write] Used in determining if pawn is going off ledge.  If the ledge is "shorter" than this value then the pawn will be able to walk off it. *

<a id="unreal.CharacterMovementComponent.ledge_check_threshold"></a>

#### ledge_check_threshold

```python
@ledge_check_threshold.setter
def ledge_check_threshold(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.jump_out_of_water_pitch"></a>

#### jump_out_of_water_pitch

```python
@property
def jump_out_of_water_pitch() -> float
```

(float):  [Read-Write] When exiting water, jump if control pitch angle is this high or above.

<a id="unreal.CharacterMovementComponent.jump_out_of_water_pitch"></a>

#### jump_out_of_water_pitch

```python
@jump_out_of_water_pitch.setter
def jump_out_of_water_pitch(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.current_floor"></a>

#### current_floor

```python
@property
def current_floor() -> FindFloorResult
```

(FindFloorResult):  [Read-Only] Information about the floor the Character is standing on (updated only during walking movement).

<a id="unreal.CharacterMovementComponent.default_land_movement_mode"></a>

#### default_land_movement_mode

```python
@property
def default_land_movement_mode() -> MovementMode
```

(MovementMode):  [Read-Write] Default movement mode when not in water. Used at player startup or when teleported.
see: DefaultWaterMovementMode
see: bRunPhysicsWithNoController

<a id="unreal.CharacterMovementComponent.default_land_movement_mode"></a>

#### default_land_movement_mode

```python
@default_land_movement_mode.setter
def default_land_movement_mode(value: MovementMode) -> None
```

<a id="unreal.CharacterMovementComponent.default_water_movement_mode"></a>

#### default_water_movement_mode

```python
@property
def default_water_movement_mode() -> MovementMode
```

(MovementMode):  [Read-Write] Default movement mode when in water. Used at player startup or when teleported.
see: DefaultLandMovementMode
see: bRunPhysicsWithNoController

<a id="unreal.CharacterMovementComponent.default_water_movement_mode"></a>

#### default_water_movement_mode

```python
@default_water_movement_mode.setter
def default_water_movement_mode(value: MovementMode) -> None
```

<a id="unreal.CharacterMovementComponent.maintain_horizontal_ground_velocity"></a>

#### maintain_horizontal_ground_velocity

```python
@property
def maintain_horizontal_ground_velocity() -> bool
```

(bool):  [Read-Write] If true, walking movement always maintains horizontal velocity when moving up ramps, which causes movement up ramps to be faster parallel to the ramp surface.
If false, then walking movement maintains velocity magnitude parallel to the ramp surface.

<a id="unreal.CharacterMovementComponent.maintain_horizontal_ground_velocity"></a>

#### maintain_horizontal_ground_velocity

```python
@maintain_horizontal_ground_velocity.setter
def maintain_horizontal_ground_velocity(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.impart_base_velocity_x"></a>

#### impart_base_velocity_x

```python
@property
def impart_base_velocity_x() -> bool
```

(bool):  [Read-Write] If true, impart the base actor's X velocity when falling off it (which includes jumping)

<a id="unreal.CharacterMovementComponent.impart_base_velocity_x"></a>

#### impart_base_velocity_x

```python
@impart_base_velocity_x.setter
def impart_base_velocity_x(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.impart_base_velocity_y"></a>

#### impart_base_velocity_y

```python
@property
def impart_base_velocity_y() -> bool
```

(bool):  [Read-Write] If true, impart the base actor's Y velocity when falling off it (which includes jumping)

<a id="unreal.CharacterMovementComponent.impart_base_velocity_y"></a>

#### impart_base_velocity_y

```python
@impart_base_velocity_y.setter
def impart_base_velocity_y(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.impart_base_velocity_z"></a>

#### impart_base_velocity_z

```python
@property
def impart_base_velocity_z() -> bool
```

(bool):  [Read-Write] If true, impart the base actor's Z velocity when falling off it (which includes jumping)

<a id="unreal.CharacterMovementComponent.impart_base_velocity_z"></a>

#### impart_base_velocity_z

```python
@impart_base_velocity_z.setter
def impart_base_velocity_z(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.impart_base_angular_velocity"></a>

#### impart_base_angular_velocity

```python
@property
def impart_base_angular_velocity() -> bool
```

(bool):  [Read-Write] If true, impart the base component's tangential components of angular velocity when jumping or falling off it.
Only those components of the velocity allowed by the separate component settings (bImpartBaseVelocityX etc) will be applied.
see: bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ

<a id="unreal.CharacterMovementComponent.impart_base_angular_velocity"></a>

#### impart_base_angular_velocity

```python
@impart_base_angular_velocity.setter
def impart_base_angular_velocity(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.just_teleported"></a>

#### just_teleported

```python
@property
def just_teleported() -> bool
```

(bool):  [Read-Only] Used by movement code to determine if a change in position is based on normal movement or a teleport. If not a teleport, velocity can be recomputed based on the change in position.

<a id="unreal.CharacterMovementComponent.ignore_client_movement_error_checks_and_correction"></a>

#### ignore_client_movement_error_checks_and_correction

```python
@property
def ignore_client_movement_error_checks_and_correction() -> bool
```

(bool):  [Read-Write] If true, we should ignore server location difference checks for client error on this movement component.
This can be useful when character is moving at extreme speeds for a duration and you need it to look
smooth on clients without the server correcting the client. Make sure to disable when done, as this would
break this character's server-client movement correction.
see: bServerAcceptClientAuthoritativePosition, ServerCheckClientError()

<a id="unreal.CharacterMovementComponent.ignore_client_movement_error_checks_and_correction"></a>

#### ignore_client_movement_error_checks_and_correction

```python
@ignore_client_movement_error_checks_and_correction.setter
def ignore_client_movement_error_checks_and_correction(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.server_accept_client_authoritative_position"></a>

#### server_accept_client_authoritative_position

```python
@property
def server_accept_client_authoritative_position() -> bool
```

(bool):  [Read-Write] If true, and server does not detect client position error, server will copy the client movement location/velocity/etc after simulating the move.
This can be useful for short bursts of movement that are difficult to sync over the network.
Note that if bIgnoreClientMovementErrorChecksAndCorrection is used, this means the server will not detect an error.
Also see GameNetworkManager->ClientAuthorativePosition which permanently enables this behavior.
see: bIgnoreClientMovementErrorChecksAndCorrection, ServerShouldUseAuthoritativePosition()

<a id="unreal.CharacterMovementComponent.server_accept_client_authoritative_position"></a>

#### server_accept_client_authoritative_position

```python
@server_accept_client_authoritative_position.setter
def server_accept_client_authoritative_position(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.notify_apex"></a>

#### notify_apex

```python
@property
def notify_apex() -> bool
```

(bool):  [Read-Only] If true, event NotifyJumpApex() to CharacterOwner's controller when at apex of jump. Is cleared when event is triggered.
By default this is off, and if you want the event to fire you typically set it to true when movement mode changes to "Falling" from another mode (see OnMovementModeChanged).

<a id="unreal.CharacterMovementComponent.wants_to_crouch"></a>

#### wants_to_crouch

```python
@property
def wants_to_crouch() -> bool
```

(bool):  [Read-Only] If true, try to crouch (or keep crouching) on next update. If false, try to stop crouching on next update.

<a id="unreal.CharacterMovementComponent.crouch_maintains_base_location"></a>

#### crouch_maintains_base_location

```python
@property
def crouch_maintains_base_location() -> bool
```

(bool):  [Read-Only] If true, crouching should keep the base of the capsule in place by lowering the center of the shrunken capsule. If false, the base of the capsule moves up and the center stays in place.
The same behavior applies when the character uncrouches: if true, the base is kept in the same location and the center moves up. If false, the capsule grows and only moves up if the base impacts something.
By default this variable is set when the movement mode changes: set to true when walking and false otherwise. Feel free to override the behavior when the movement mode changes.

<a id="unreal.CharacterMovementComponent.b_crouch_moves_character_down"></a>

#### b_crouch_moves_character_down

```python
@property
def b_crouch_moves_character_down() -> bool
```

deprecated: 'b_crouch_moves_character_down' was renamed to 'crouch_maintains_base_location'.

<a id="unreal.CharacterMovementComponent.ignore_base_rotation"></a>

#### ignore_base_rotation

```python
@property
def ignore_base_rotation() -> bool
```

(bool):  [Read-Write] Whether the character ignores changes in rotation of the base it is standing on.
If true, the character maintains current world rotation.
If false, the character rotates with the moving base.

<a id="unreal.CharacterMovementComponent.ignore_base_rotation"></a>

#### ignore_base_rotation

```python
@ignore_base_rotation.setter
def ignore_base_rotation(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.always_check_floor"></a>

#### always_check_floor

```python
@property
def always_check_floor() -> bool
```

(bool):  [Read-Write] Whether we always force floor checks for stationary Characters while walking.
Normally floor checks are avoided if possible when not moving, but this can be used to force them if there are use-cases where they are being skipped erroneously
(such as objects moving up into the character from below).

<a id="unreal.CharacterMovementComponent.always_check_floor"></a>

#### always_check_floor

```python
@always_check_floor.setter
def always_check_floor(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.use_flat_base_for_floor_checks"></a>

#### use_flat_base_for_floor_checks

```python
@property
def use_flat_base_for_floor_checks() -> bool
```

(bool):  [Read-Write] Performs floor checks as if the character is using a shape with a flat base.
This avoids the situation where characters slowly lower off the side of a ledge (as their capsule 'balances' on the edge).

<a id="unreal.CharacterMovementComponent.use_flat_base_for_floor_checks"></a>

#### use_flat_base_for_floor_checks

```python
@use_flat_base_for_floor_checks.setter
def use_flat_base_for_floor_checks(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.use_rvo_avoidance"></a>

#### use_rvo_avoidance

```python
@property
def use_rvo_avoidance() -> bool
```

(bool):  [Read-Only] If set, component will use RVO avoidance. This only runs on the server.

<a id="unreal.CharacterMovementComponent.requested_move_use_acceleration"></a>

#### requested_move_use_acceleration

```python
@property
def requested_move_use_acceleration() -> bool
```

(bool):  [Read-Write] Should use acceleration for path following?
If true, acceleration is applied when path following to reach the target velocity.
If false, path following velocity is set directly, disregarding acceleration.

<a id="unreal.CharacterMovementComponent.requested_move_use_acceleration"></a>

#### requested_move_use_acceleration

```python
@requested_move_use_acceleration.setter
def requested_move_use_acceleration(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.allow_physics_rotation_during_anim_root_motion"></a>

#### allow_physics_rotation_during_anim_root_motion

```python
@property
def allow_physics_rotation_during_anim_root_motion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CharacterMovementComponent.allow_physics_rotation_during_anim_root_motion"></a>

#### allow_physics_rotation_during_anim_root_motion

```python
@allow_physics_rotation_during_anim_root_motion.setter
def allow_physics_rotation_during_anim_root_motion(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.former_base_velocity_decay_half_life"></a>

#### former_base_velocity_decay_half_life

```python
@property
def former_base_velocity_decay_half_life() -> float
```

(float):  [Read-Write] When applying a root motion override while falling off a moving object, this controls how long it takes to lose half the former base's velocity (in seconds).
Set to 0 to ignore former bases (default).
Set to -1 for no decay.
Any other positive value sets the half-life for exponential decay.

<a id="unreal.CharacterMovementComponent.former_base_velocity_decay_half_life"></a>

#### former_base_velocity_decay_half_life

```python
@former_base_velocity_decay_half_life.setter
def former_base_velocity_decay_half_life(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.project_nav_mesh_walking"></a>

#### project_nav_mesh_walking

```python
@property
def project_nav_mesh_walking() -> bool
```

(bool):  [Read-Only] Whether to raycast to underlying geometry to better conform navmesh-walking characters

<a id="unreal.CharacterMovementComponent.project_nav_mesh_on_both_world_channels"></a>

#### project_nav_mesh_on_both_world_channels

```python
@property
def project_nav_mesh_on_both_world_channels() -> bool
```

(bool):  [Read-Only] Use both WorldStatic and WorldDynamic channels for NavWalking geometry conforming

<a id="unreal.CharacterMovementComponent.avoidance_consideration_radius"></a>

#### avoidance_consideration_radius

```python
@property
def avoidance_consideration_radius() -> float
```

(float):  [Read-Only]

<a id="unreal.CharacterMovementComponent.avoidance_uid"></a>

#### avoidance_uid

```python
@property
def avoidance_uid() -> int
```

(int32):  [Read-Only] No default value, for now it's assumed to be valid if GetAvoidanceManager() returns non-NULL.

<a id="unreal.CharacterMovementComponent.avoidance_group"></a>

#### avoidance_group

```python
@property
def avoidance_group() -> NavAvoidanceMask
```

(NavAvoidanceMask):  [Read-Only] Moving actor's group mask

<a id="unreal.CharacterMovementComponent.groups_to_avoid"></a>

#### groups_to_avoid

```python
@property
def groups_to_avoid() -> NavAvoidanceMask
```

(NavAvoidanceMask):  [Read-Only] Will avoid other agents if they are in one of specified groups

<a id="unreal.CharacterMovementComponent.groups_to_ignore"></a>

#### groups_to_ignore

```python
@property
def groups_to_ignore() -> NavAvoidanceMask
```

(NavAvoidanceMask):  [Read-Only] Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid

<a id="unreal.CharacterMovementComponent.avoidance_weight"></a>

#### avoidance_weight

```python
@property
def avoidance_weight() -> float
```

(float):  [Read-Only] De facto default value 0.5 (due to that being the default in the avoidance registration function), indicates RVO behavior.

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_interval"></a>

#### nav_mesh_projection_interval

```python
@property
def nav_mesh_projection_interval() -> float
```

(float):  [Read-Write] How often we should raycast to project from navmesh to underlying geometry

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_interval"></a>

#### nav_mesh_projection_interval

```python
@nav_mesh_projection_interval.setter
def nav_mesh_projection_interval(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_interp_speed"></a>

#### nav_mesh_projection_interp_speed

```python
@property
def nav_mesh_projection_interp_speed() -> float
```

(float):  [Read-Write] Speed at which to interpolate agent navmesh offset between traces. 0: Instant (no interp) > 0: Interp speed")

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_interp_speed"></a>

#### nav_mesh_projection_interp_speed

```python
@nav_mesh_projection_interp_speed.setter
def nav_mesh_projection_interp_speed(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_up"></a>

#### nav_mesh_projection_height_scale_up

```python
@property
def nav_mesh_projection_height_scale_up() -> float
```

(float):  [Read-Write] Scale of the total capsule height to use for projection from navmesh to underlying geometry in the upward direction.
In other words, start the trace at [CapsuleHeight * NavMeshProjectionHeightScaleUp] above nav mesh.

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_up"></a>

#### nav_mesh_projection_height_scale_up

```python
@nav_mesh_projection_height_scale_up.setter
def nav_mesh_projection_height_scale_up(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_up"></a>

#### nav_mesh_projection_capsule_height_scale_up

```python
@property
def nav_mesh_projection_capsule_height_scale_up() -> float
```

deprecated: 'nav_mesh_projection_capsule_height_scale_up' was renamed to 'nav_mesh_projection_height_scale_up'.

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_up"></a>

#### nav_mesh_projection_capsule_height_scale_up

```python
@nav_mesh_projection_capsule_height_scale_up.setter
def nav_mesh_projection_capsule_height_scale_up(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_down"></a>

#### nav_mesh_projection_height_scale_down

```python
@property
def nav_mesh_projection_height_scale_down() -> float
```

(float):  [Read-Write] Scale of the total capsule height to use for projection from navmesh to underlying geometry in the downward direction.
In other words, trace down to [CapsuleHeight * NavMeshProjectionHeightScaleDown] below nav mesh.

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_height_scale_down"></a>

#### nav_mesh_projection_height_scale_down

```python
@nav_mesh_projection_height_scale_down.setter
def nav_mesh_projection_height_scale_down(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_down"></a>

#### nav_mesh_projection_capsule_height_scale_down

```python
@property
def nav_mesh_projection_capsule_height_scale_down() -> float
```

deprecated: 'nav_mesh_projection_capsule_height_scale_down' was renamed to 'nav_mesh_projection_height_scale_down'.

<a id="unreal.CharacterMovementComponent.nav_mesh_projection_capsule_height_scale_down"></a>

#### nav_mesh_projection_capsule_height_scale_down

```python
@nav_mesh_projection_capsule_height_scale_down.setter
def nav_mesh_projection_capsule_height_scale_down(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.nav_walking_floor_dist_tolerance"></a>

#### nav_walking_floor_dist_tolerance

```python
@property
def nav_walking_floor_dist_tolerance() -> float
```

(float):  [Read-Write] Ignore small differences in ground height between server and client data during NavWalking mode

<a id="unreal.CharacterMovementComponent.nav_walking_floor_dist_tolerance"></a>

#### nav_walking_floor_dist_tolerance

```python
@nav_walking_floor_dist_tolerance.setter
def nav_walking_floor_dist_tolerance(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.based_movement_ignore_physics_base"></a>

#### based_movement_ignore_physics_base

```python
@property
def based_movement_ignore_physics_base() -> bool
```

(bool):  [Read-Write] Property to set if UpdateBasedMovement should ignore collision with actors part of the current MovementBase, if the base is simulated by physics

<a id="unreal.CharacterMovementComponent.based_movement_ignore_physics_base"></a>

#### based_movement_ignore_physics_base

```python
@based_movement_ignore_physics_base.setter
def based_movement_ignore_physics_base(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.base_on_attachment_root"></a>

#### base_on_attachment_root

```python
@property
def base_on_attachment_root() -> bool
```

(bool):  [Read-Write] Property to set if characters should stay based on objects attachment root instead of the traced object

<a id="unreal.CharacterMovementComponent.base_on_attachment_root"></a>

#### base_on_attachment_root

```python
@base_on_attachment_root.setter
def base_on_attachment_root(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.stay_based_in_air"></a>

#### stay_based_in_air

```python
@property
def stay_based_in_air() -> bool
```

(bool):  [Read-Write] Property to set if characters should stay based on objects while jumping

<a id="unreal.CharacterMovementComponent.stay_based_in_air"></a>

#### stay_based_in_air

```python
@stay_based_in_air.setter
def stay_based_in_air(value: bool) -> None
```

<a id="unreal.CharacterMovementComponent.stay_based_in_air_height"></a>

#### stay_based_in_air_height

```python
@property
def stay_based_in_air_height() -> float
```

(float):  [Read-Write] Property used to set how high above base characters should stay based on objects while jumping if bStayBasedInAir is set

<a id="unreal.CharacterMovementComponent.stay_based_in_air_height"></a>

#### stay_based_in_air_height

```python
@stay_based_in_air_height.setter
def stay_based_in_air_height(value: float) -> None
```

<a id="unreal.CharacterMovementComponent.set_walkable_floor_z"></a>

#### set_walkable_floor_z

```python
def set_walkable_floor_z(walkable_floor_z: float) -> None
```

x.set_walkable_floor_z(walkable_floor_z) -> None
Set the Z component of the normal of the steepest walkable surface for the character. Also computes WalkableFloorAngle.

Args:
    walkable_floor_z (float):

<a id="unreal.CharacterMovementComponent.set_walkable_floor_angle"></a>

#### set_walkable_floor_angle

```python
def set_walkable_floor_angle(walkable_floor_angle: float) -> None
```

x.set_walkable_floor_angle(walkable_floor_angle) -> None
Set the max angle in degrees of a walkable surface for the character. Also computes WalkableFloorZ.

Args:
    walkable_floor_angle (float):

<a id="unreal.CharacterMovementComponent.set_movement_mode"></a>

#### set_movement_mode

```python
def set_movement_mode(new_movement_mode: MovementMode,
                      new_custom_mode: int = 0) -> None
```

x.set_movement_mode(new_movement_mode, new_custom_mode=0) -> None
Change movement mode.

Args:
    new_movement_mode (MovementMode): The new movement mode
    new_custom_mode (uint8): The new custom sub-mode, only applicable if NewMovementMode is Custom.

<a id="unreal.CharacterMovementComponent.set_groups_to_ignore_mask"></a>

#### set_groups_to_ignore_mask

```python
def set_groups_to_ignore_mask(group_mask: NavAvoidanceMask) -> None
```

x.set_groups_to_ignore_mask(group_mask) -> None
Set Groups to Ignore Mask

Args:
    group_mask (NavAvoidanceMask):

<a id="unreal.CharacterMovementComponent.set_groups_to_ignore"></a>

#### set_groups_to_ignore

```python
def set_groups_to_ignore(group_flags: int) -> None
```

x.set_groups_to_ignore(group_flags) -> None
Set Groups to Ignore
deprecated: Please use SetGroupsToIgnoreMask function instead.

Args:
    group_flags (int32):

<a id="unreal.CharacterMovementComponent.set_groups_to_avoid_mask"></a>

#### set_groups_to_avoid_mask

```python
def set_groups_to_avoid_mask(group_mask: NavAvoidanceMask) -> None
```

x.set_groups_to_avoid_mask(group_mask) -> None
Set Groups to Avoid Mask

Args:
    group_mask (NavAvoidanceMask):

<a id="unreal.CharacterMovementComponent.set_groups_to_avoid"></a>

#### set_groups_to_avoid

```python
def set_groups_to_avoid(group_flags: int) -> None
```

x.set_groups_to_avoid(group_flags) -> None
Set Groups to Avoid
deprecated: Please use SetGroupsToAvoidMask function instead.

Args:
    group_flags (int32):

<a id="unreal.CharacterMovementComponent.set_gravity_direction"></a>

#### set_gravity_direction

```python
def set_gravity_direction(gravity_dir: Vector) -> None
```

x.set_gravity_direction(gravity_dir) -> None
Set a custom, local gravity direction to use during movement simulation.
The gravity direction must be synchronized by external systems between the autonomous
and authority processes. The gravity direction will be corrected as part of movement
corrections should the movement state diverge.
SetGravityDirection is responsible for initializing cached values used to tranform to
from gravity relative space.

Args:
    gravity_dir (Vector): A non-zero vector representing the new gravity direction. The vector will be normalized.

<a id="unreal.CharacterMovementComponent.set_avoidance_group_mask"></a>

#### set_avoidance_group_mask

```python
def set_avoidance_group_mask(group_mask: NavAvoidanceMask) -> None
```

x.set_avoidance_group_mask(group_mask) -> None
Set Avoidance Group Mask

Args:
    group_mask (NavAvoidanceMask):

<a id="unreal.CharacterMovementComponent.set_avoidance_group"></a>

#### set_avoidance_group

```python
def set_avoidance_group(group_flags: int) -> None
```

x.set_avoidance_group(group_flags) -> None
Set Avoidance Group
deprecated: Please use SetAvoidanceGroupMask function instead.

Args:
    group_flags (int32):

<a id="unreal.CharacterMovementComponent.set_avoidance_enabled"></a>

#### set_avoidance_enabled

```python
def set_avoidance_enabled(enable: bool) -> None
```

x.set_avoidance_enabled(enable) -> None
Change avoidance state and registers in RVO manager if needed

Args:
    enable (bool):

<a id="unreal.CharacterMovementComponent.get_walkable_floor_z"></a>

#### get_walkable_floor_z

```python
def get_walkable_floor_z() -> float
```

x.get_walkable_floor_z() -> float
Get the Z component of the normal of the steepest walkable surface for the character. Any lower than this and it is not walkable.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_walkable_floor_angle"></a>

#### get_walkable_floor_angle

```python
def get_walkable_floor_angle() -> float
```

x.get_walkable_floor_angle() -> float
Get the max angle in degrees of a walkable surface for the character.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.find_floor"></a>

#### find_floor

```python
def find_floor(capsule_location: Vector) -> FindFloorResult
```

x.find_floor(capsule_location) -> FindFloorResult
Sweeps a vertical trace to find the floor for the capsule at the given location. Will attempt to perch if ShouldComputePerchResult() returns true for the downward sweep result.
No floor will be found if collision is disabled on the capsule!

Args:
    capsule_location (Vector): Location where the capsule sweep should originate

Returns:
    FindFloorResult: 

    floor_result (FindFloorResult): Result of the floor check

<a id="unreal.CharacterMovementComponent.compute_floor_distance"></a>

#### compute_floor_distance

```python
def compute_floor_distance(capsule_location: Vector, line_distance: float,
                           sweep_distance: float,
                           sweep_radius: float) -> FindFloorResult
```

x.compute_floor_distance(capsule_location, line_distance, sweep_distance, sweep_radius) -> FindFloorResult
Compute distance to the floor from bottom sphere of capsule and store the result in FloorResult.
This distance is the swept distance of the capsule to the first point impacted by the lower hemisphere, or distance from the bottom of the capsule in the case of a line trace.
This function does not care if collision is disabled on the capsule (unlike FindFloor).

Args:
    capsule_location (Vector): Location where the capsule sweep should originate
    line_distance (float): If non-zero, max distance to test for a simple line check from the capsule base. Used only if the sweep test fails to find a walkable floor, and only returns a valid result if the impact normal is a walkable normal.
    sweep_distance (float): If non-zero, max distance to use when sweeping a capsule downwards for the test. MUST be greater than or equal to the line distance.
    sweep_radius (float): The radius to use for sweep tests. Should be <= capsule radius.

Returns:
    FindFloorResult: 

    floor_result (FindFloorResult): Result of the floor check

<a id="unreal.CharacterMovementComponent.is_walking"></a>

#### is_walking

```python
def is_walking() -> bool
```

x.is_walking() -> bool
Returns true if the character is in the 'Walking' movement mode.

Returns:
    bool:

<a id="unreal.CharacterMovementComponent.is_walkable"></a>

#### is_walkable

```python
def is_walkable(hit: HitResult) -> bool
```

x.is_walkable(hit) -> bool
Return true if the hit result should be considered a walkable surface for the character.

Args:
    hit (HitResult): 

Returns:
    bool:

<a id="unreal.CharacterMovementComponent.has_custom_gravity"></a>

#### has_custom_gravity

```python
def has_custom_gravity() -> bool
```

x.has_custom_gravity() -> bool
Whether the gravity direction is different from UCharacterMovementComponent::DefaultGravityDirection.

Returns:
    bool:

<a id="unreal.CharacterMovementComponent.get_valid_perch_radius"></a>

#### get_valid_perch_radius

```python
def get_valid_perch_radius() -> float
```

x.get_valid_perch_radius() -> float
Returns the radius within which we can stand on the edge of a surface without falling (if this is a walkable surface).
Simply computed as the capsule radius minus the result of GetPerchRadiusThreshold().

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_perch_radius_threshold"></a>

#### get_perch_radius_threshold

```python
def get_perch_radius_threshold() -> float
```

x.get_perch_radius_threshold() -> float
Returns The distance from the edge of the capsule within which we don't allow the character to perch on the edge of a surface.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_movement_base"></a>

#### get_movement_base

```python
def get_movement_base() -> PrimitiveComponent
```

x.get_movement_base() -> PrimitiveComponent
Return PrimitiveComponent we are based on (standing and walking on).

Returns:
    PrimitiveComponent:

<a id="unreal.CharacterMovementComponent.get_min_analog_speed"></a>

#### get_min_analog_speed

```python
def get_min_analog_speed() -> float
```

x.get_min_analog_speed() -> float
Returns maximum acceleration for the current state.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_max_jump_height_with_jump_time"></a>

#### get_max_jump_height_with_jump_time

```python
def get_max_jump_height_with_jump_time() -> float
```

x.get_max_jump_height_with_jump_time() -> float
Compute the max jump height based on the JumpZVelocity velocity and gravity.
This does take into account the CharacterOwner's MaxJumpHoldTime.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_max_jump_height"></a>

#### get_max_jump_height

```python
def get_max_jump_height() -> float
```

x.get_max_jump_height() -> float
Compute the max jump height based on the JumpZVelocity velocity and gravity.
This does not take into account the CharacterOwner's MaxJumpHoldTime.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_max_braking_deceleration"></a>

#### get_max_braking_deceleration

```python
def get_max_braking_deceleration() -> float
```

x.get_max_braking_deceleration() -> float
Returns maximum deceleration for the current state when braking (ie when there is no acceleration).

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_max_acceleration"></a>

#### get_max_acceleration

```python
def get_max_acceleration() -> float
```

x.get_max_acceleration() -> float
Returns maximum acceleration for the current state.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.get_last_update_velocity"></a>

#### get_last_update_velocity

```python
def get_last_update_velocity() -> Vector
```

x.get_last_update_velocity() -> Vector
Returns the velocity at the end of the last tick.

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_last_update_rotation"></a>

#### get_last_update_rotation

```python
def get_last_update_rotation() -> Rotator
```

x.get_last_update_rotation() -> Rotator
Returns the rotation at the end of the last tick.

Returns:
    Rotator:

<a id="unreal.CharacterMovementComponent.get_last_update_requested_velocity"></a>

#### get_last_update_requested_velocity

```python
def get_last_update_requested_velocity() -> Vector
```

x.get_last_update_requested_velocity() -> Vector
Returns velocity requested by path following

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_last_update_location"></a>

#### get_last_update_location

```python
def get_last_update_location() -> Vector
```

x.get_last_update_location() -> Vector
Returns the location at the end of the last tick.

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_imparted_movement_base_velocity"></a>

#### get_imparted_movement_base_velocity

```python
def get_imparted_movement_base_velocity() -> Vector
```

x.get_imparted_movement_base_velocity() -> Vector
If we have a movement base, get the velocity that should be imparted by that base, usually when jumping off of it.
Only applies the components of the velocity enabled by bImpartBaseVelocityX, bImpartBaseVelocityY, bImpartBaseVelocityZ.

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_gravity_direction"></a>

#### get_gravity_direction

```python
def get_gravity_direction() -> Vector
```

x.get_gravity_direction() -> Vector
Returns the current gravity direction.

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_current_acceleration"></a>

#### get_current_acceleration

```python
def get_current_acceleration() -> Vector
```

x.get_current_acceleration() -> Vector
Returns current acceleration, computed from input vector each update.

Returns:
    Vector:

<a id="unreal.CharacterMovementComponent.get_character_owner"></a>

#### get_character_owner

```python
def get_character_owner() -> Character
```

x.get_character_owner() -> Character
Get the Character that owns UpdatedComponent.

Returns:
    Character:

<a id="unreal.CharacterMovementComponent.get_analog_input_modifier"></a>

#### get_analog_input_modifier

```python
def get_analog_input_modifier() -> float
```

x.get_analog_input_modifier() -> float
Returns modifier [0..1] based on the magnitude of the last input vector, which is used to modify the acceleration and max speed during movement.

Returns:
    float:

<a id="unreal.CharacterMovementComponent.disable_movement"></a>

#### disable_movement

```python
def disable_movement() -> None
```

x.disable_movement() -> None
Make movement impossible (sets movement mode to MOVE_None).

<a id="unreal.CharacterMovementComponent.clear_accumulated_forces"></a>

#### clear_accumulated_forces

```python
def clear_accumulated_forces() -> None
```

x.clear_accumulated_forces() -> None
Clears forces accumulated through AddImpulse() and AddForce(), and also pending launch velocity.

<a id="unreal.CharacterMovementComponent.calc_velocity"></a>

#### calc_velocity

```python
def calc_velocity(delta_time: float, friction: float, fluid: bool,
                  braking_deceleration: float) -> None
```

x.calc_velocity(delta_time, friction, fluid, braking_deceleration) -> None
Updates Velocity and Acceleration based on the current state, applying the effects of friction and acceleration or deceleration. Does not apply gravity.
This is used internally during movement updates. Normally you don't need to call this from outside code, but you might want to use it for custom movement modes.

Args:
    delta_time (float): time elapsed since last frame.
    friction (float): coefficient of friction when not accelerating, or in the direction opposite acceleration.
    fluid (bool): true if moving through a fluid, causing Friction to always be applied regardless of acceleration.
    braking_deceleration (float): deceleration applied when not accelerating, or when exceeding max velocity.

<a id="unreal.CharacterMovementComponent.add_impulse"></a>

#### add_impulse

```python
def add_impulse(impulse: Vector, velocity_change: bool = False) -> None
```

x.add_impulse(impulse, velocity_change=False) -> None
Add impulse to character. Impulses are accumulated each tick and applied together
so multiple calls to this function will accumulate.
An impulse is an instantaneous force, usually applied once. If you want to continually apply
forces each frame, use AddForce().
Note that changing the momentum of characters like this can change the movement mode.

Args:
    impulse (Vector): Impulse to apply.
    velocity_change (bool): Whether or not the impulse is relative to mass.

<a id="unreal.CharacterMovementComponent.add_momentum"></a>

#### add_momentum

```python
def add_momentum(impulse: Vector, velocity_change: bool = False) -> None
```

deprecated: 'add_momentum' was renamed to 'add_impulse'.

<a id="unreal.CharacterMovementComponent.add_force"></a>

#### add_force

```python
def add_force(force: Vector) -> None
```

x.add_force(force) -> None
Add force to character. Forces are accumulated each tick and applied together
so multiple calls to this function will accumulate.
Forces are scaled depending on timestep, so they can be applied each frame. If you want an
instantaneous force, use AddImpulse.
Adding a force always takes the actor's mass into account.
Note that changing the momentum of characters like this can change the movement mode.

Args:
    force (Vector): Force to apply.

<a id="unreal.MovementComp_Character"></a>