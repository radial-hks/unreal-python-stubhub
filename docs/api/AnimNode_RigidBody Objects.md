## AnimNode_RigidBody Objects

```python
class AnimNode_RigidBody(AnimNode_SkeletalControlBase)
```

Controller that simulates physics based on the physics asset of the skeletal mesh component

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RigidBody.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``base_bone_ref`` (BoneReference):  [Read-Write] Matters if SimulationSpace is BaseBone
- ``cached_bounds_scale`` (float):  [Read-Write] Scale of cached bounds (vs. actual bounds).
  Increasing this may improve performance, but overlaps may not work as well.
  (A value of 1.0 effectively disables cached bounds).
- ``clamp_linear_translation_limit_to_ref_pose`` (bool):  [Read-Write] Correct for linear tearing on bodies with all axes Locked.
  This only works if all axes linear translation are locked
- ``component_applied_linear_acc_clamp`` (Vector):  [Read-Write] When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large.
- ``component_linear_acc_scale`` (Vector):  [Read-Write] When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation.
- ``component_linear_vel_scale`` (Vector):  [Read-Write] When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity.
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``default_to_skeletal_mesh_physics_asset`` (bool):  [Read-Write] Use the skeletal mesh physics asset as default in case set to True. The Override Physics Asset will always have priority over this.
- ``enable_world_geometry`` (bool):  [Read-Write]
- ``evaluation_reset_time`` (float):  [Read-Write] If the node is not evaluated for this amount of time (seconds), either because a lower LOD was in use for a while or the component was
  not visible, reset the simulation to the default pose on the next evaluation. Set to 0 to disable time-based reset.
- ``external_force`` (Vector):  [Read-Write] Applies a uniform external force in world space. This allows for easily faking inertia of movement while still simulating in component space for example
- ``force_disable_collision_between_constraint_bodies`` (bool):  [Read-Write] Whether to allow collisions between two bodies joined by a constraint
- ``freeze_incoming_pose_on_start`` (bool):  [Read-Write] When simulation starts, freeze incoming pose.
  This is useful for ragdolls, when we want the simulation to take over.
  It prevents non simulated bones from animating.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``overlap_channel`` (CollisionChannel):  [Read-Write] The channel we use to find static geometry to collide with
- ``override_physics_asset`` (PhysicsAsset):  [Read-Write] Physics asset to use. If empty use the skeletal mesh's default physics asset in case Default To Skeletal Mesh Physics Asset is set to True.
- ``override_world_gravity`` (Vector):  [Read-Write] Override gravity
- ``override_world_gravity`` (bool):  [Read-Write]
- ``sim_space_settings`` (SimSpaceSettings):  [Read-Write] Settings for the system which passes motion of the simulation's space
  into the simulation. This allows the simulation to pass a
  fraction of the world space motion onto the bodies which allows Bone-Space
  and Component-Space simulations to react to world-space movement in a
  controllable way.
  This system is a superset of the functionality provided by ComponentLinearAccScale,
  ComponentLinearVelScale, and ComponentAppliedLinearAccClamp. In general
  you should not have both systems enabled.
- ``simulation_space`` (SimulationSpace):  [Read-Write] What space to simulate the bodies in. This affects how velocities are generated
- ``simulation_timing`` (SimulationTiming):  [Read-Write] Whether the physics simulation runs synchronously with the node's evaluation or is run in the background until the next frame.
- ``transfer_bone_velocities`` (bool):  [Read-Write] When simulation starts, transfer previous bone velocities (from animation)
  to make transition into simulation seamless.
- ``use_external_cloth_collision`` (bool):  [Read-Write] If true, kinematic objects will be added to the simulation at runtime to represent any cloth colliders defined for the parent object.
- ``use_local_lod_threshold_only`` (bool):  [Read-Write] Enable if you want to ignore the p.RigidBodyLODThreshold CVAR and force the node to solely use the LOD threshold.
- ``world_space_minimum_scale`` (float):  [Read-Write] For world-space simulations, if the magnitude of the component's 3D scale is less than WorldSpaceMinimumScale, do not update the node.

<a id="unreal.AnimNode_RigidBody.__init__"></a>

#### __init__

```python
def __init__(component_pose: ComponentSpacePoseLink = [],
             lod_threshold: int = 0,
             alpha_input_type: AnimAlphaInputType = AnimAlphaInputType.FLOAT,
             alpha_bool_enabled: bool = False,
             alpha: float = 0.000000,
             alpha_scale_bias: InputScaleBias = [1.000000, 0.000000],
             alpha_bool_blend: InputAlphaBoolBlend = [
                 0.000000, 0.000000, AlphaBlendOption.LINEAR, None
             ],
             alpha_curve_name: Name = "None",
             alpha_scale_bias_clamp: InputScaleBiasClamp = [
                 False, False, False, [0.000000,
                                       1.000000], [0.000000, 1.000000],
                 1.000000, 0.000000, 0.000000, 1.000000, 10.000000, 10.000000
             ],
             use_local_lod_threshold_only: bool = False) -> None
```

<a id="unreal.AnimNode_RigidBody.use_local_lod_threshold_only"></a>

#### use_local_lod_threshold_only

```python
@property
def use_local_lod_threshold_only() -> bool
```

(bool):  [Read-Write] Enable if you want to ignore the p.RigidBodyLODThreshold CVAR and force the node to solely use the LOD threshold.

<a id="unreal.AnimNode_RigidBody.use_local_lod_threshold_only"></a>

#### use_local_lod_threshold_only

```python
@use_local_lod_threshold_only.setter
def use_local_lod_threshold_only(value: bool) -> None
```

<a id="unreal.AnimNode_Ragdoll"></a>