## AnimNode_AnimDynamics Objects

```python
class AnimNode_AnimDynamics(AnimNode_SkeletalControlBase)
```

Anim Node Anim Dynamics

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_AnimDynamics.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write] Current strength of the skeletal control
- ``alpha_bool_blend`` (InputAlphaBoolBlend):  [Read-Write]
- ``alpha_bool_enabled`` (bool):  [Read-Write]
- ``alpha_curve_name`` (Name):  [Read-Write]
- ``alpha_input_type`` (AnimAlphaInputType):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``alpha_scale_bias_clamp`` (InputScaleBiasClamp):  [Read-Write]
- ``angular_bias_override`` (float):  [Read-Write] Overridden angular bias value
  Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability
  in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with
  the mesh, if that's the case override this and push it towards 1.0f until it settles correctly
- ``angular_damping_override`` (float):  [Read-Write] Overridden angular damping value. The default is 0.7. Values below 0.7 won't have an effect.
- ``angular_spring`` (bool):  [Read-Write] If true the body will attempt to align itself with the specified angular target
- ``angular_spring_constant`` (float):  [Read-Write] Spring constant to use when calculating angular springs, higher values mean a stronger spring.
  You need to enable the Angular Spring checkbox for this to have an effect.
  Note: Make sure to also set the Angular Target Axis and Angular Target in the Constraint Setup for this to have an effect.
- ``bound_bone`` (BoneReference):  [Read-Write] The bone to attach the physics body to, if bChain is true this is the top of the chain
- ``chain`` (bool):  [Read-Write] Set to true to use the solver to simulate a connected chain
- ``chain_end`` (BoneReference):  [Read-Write] If bChain is true this is the bottom of the chain, otherwise ignored
- ``component_applied_linear_acc_clamp`` (Vector):  [Read-Write] When using non-world-space sim, this is an overall clamp on acceleration derived from ComponentLinearAccScale and ComponentLinearVelScale, to ensure it is not too large.
- ``component_linear_acc_scale`` (Vector):  [Read-Write] When using non-world-space sim, this controls how much of the components world-space acceleration is passed on to the local-space simulation.
- ``component_linear_vel_scale`` (Vector):  [Read-Write] When using non-world-space sim, this applies a 'drag' to the bodies in the local space simulation, based on the components world-space velocity.
- ``component_pose`` (ComponentSpacePoseLink):  [Read-Write] Input link
- ``do_eval`` (bool):  [Read-Write] If true we will perform bone transform evaluation, otherwise skip - allows visualization of the initial anim state compared to the physics sim
- ``do_update`` (bool):  [Read-Write] If true we will perform physics update, otherwise skip - allows visualization of the initial state of the bodies
- ``enable_wind`` (bool):  [Read-Write] Whether or not wind is enabled for the bodies in this simulation
- ``external_force`` (Vector):  [Read-Write] An external force to apply to all bodies in the simulation when ticked, specified in world space
- ``gravity_override`` (Vector):  [Read-Write] Gravity Override Value
- ``gravity_override_in_sim_space`` (bool):  [Read-Write] If true the gravity override value is defined in simulation space, by default it is in world space
- ``gravity_scale`` (float):  [Read-Write] Scale for gravity, higher values increase forces due to gravity
- ``linear_damping_override`` (float):  [Read-Write] Overridden linear damping value. The default is 0.7. Values below 0.7 won't have an effect.
- ``linear_spring`` (bool):  [Read-Write] If true the body will attempt to spring back to its initial position
- ``linear_spring_constant`` (float):  [Read-Write] Spring constant to use when calculating linear springs, higher values mean a stronger spring.
  You need to enable the Linear Spring checkbox for this to have an effect.
- ``lod_threshold`` (int32):  [Read-Write] * Max LOD that this node is allowed to run
  * For example if you have LODThreshold to be 2, it will run until LOD 2 (based on 0 index)
  * when the component LOD becomes 3, it will stop update/evaluate
  * currently transition would be issue and that has to be re-visited
- ``num_solver_iterations_post_update`` (int32):  [Read-Write] Number of update passes on the linear and angular limits after we solve the position of the bodies, recommended to be around a quarter of NumSolverIterationsPreUpdate
- ``num_solver_iterations_pre_update`` (int32):  [Read-Write] Number of update passes on the linear and angular limits before we solve the position of the bodies recommended to be four times the value of NumSolverIterationsPostUpdate
- ``override_angular_bias`` (bool):  [Read-Write] If true, the override value will be used for the angular bias for bodies in this node.
  Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability
  in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with
  the mesh, if that's the case override this and push it towards 1.0f until it settles correctly
- ``override_angular_damping`` (bool):  [Read-Write] If true, the override value will be used for angular damping
- ``override_linear_damping`` (bool):  [Read-Write] If true, the override value will be used for linear damping
- ``physics_body_definitions`` (Array[AnimPhysBodyDefinition]):  [Read-Write]
- ``planar_limits`` (Array[AnimPhysPlanarLimit]):  [Read-Write] List of available planar limits for this node
- ``relative_space_bone`` (BoneReference):  [Read-Write] When in BoneRelative sim space, the simulation will use this bone as the origin
- ``retargeting_settings`` (RotationRetargetingInfo):  [Read-Write] The settings for rotation retargeting
- ``simulation_space`` (AnimPhysSimSpaceType):  [Read-Write] The space used to run the simulation
- ``spherical_limits`` (Array[AnimPhysSphericalLimit]):  [Read-Write] List of available spherical limits for this node
- ``use_gravity_override`` (bool):  [Read-Write] Use gravity override value vs gravity scale
- ``use_planar_limit`` (bool):  [Read-Write] Whether to evaluate planar limits
- ``use_spherical_limits`` (bool):  [Read-Write] Whether to evaluate spherical limits
- ``wind_scale`` (float):  [Read-Write] Scale to apply to calculated wind velocities in the solver

<a id="unreal.AnimNode_AnimDynamics.__init__"></a>

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
             linear_damping_override: float = 0.000000,
             angular_damping_override: float = 0.000000,
             gravity_scale: float = 0.000000,
             gravity_override: Vector = [0.000000, 0.000000, 0.000000],
             linear_spring_constant: float = 0.000000,
             angular_spring_constant: float = 0.000000,
             angular_bias_override: float = 0.000000,
             simulation_space: AnimPhysSimSpaceType = AnimPhysSimSpaceType.
             COMPONENT,
             use_gravity_override: bool = False) -> None
```

<a id="unreal.AnimNode_AnimDynamics.linear_damping_override"></a>

#### linear_damping_override

```python
@property
def linear_damping_override() -> float
```

(float):  [Read-Write] Overridden linear damping value. The default is 0.7. Values below 0.7 won't have an effect.

<a id="unreal.AnimNode_AnimDynamics.linear_damping_override"></a>

#### linear_damping_override

```python
@linear_damping_override.setter
def linear_damping_override(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.angular_damping_override"></a>

#### angular_damping_override

```python
@property
def angular_damping_override() -> float
```

(float):  [Read-Write] Overridden angular damping value. The default is 0.7. Values below 0.7 won't have an effect.

<a id="unreal.AnimNode_AnimDynamics.angular_damping_override"></a>

#### angular_damping_override

```python
@angular_damping_override.setter
def angular_damping_override(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.gravity_scale"></a>

#### gravity_scale

```python
@property
def gravity_scale() -> float
```

(float):  [Read-Write] Scale for gravity, higher values increase forces due to gravity

<a id="unreal.AnimNode_AnimDynamics.gravity_scale"></a>

#### gravity_scale

```python
@gravity_scale.setter
def gravity_scale(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.gravity_override"></a>

#### gravity_override

```python
@property
def gravity_override() -> Vector
```

(Vector):  [Read-Write] Gravity Override Value

<a id="unreal.AnimNode_AnimDynamics.gravity_override"></a>

#### gravity_override

```python
@gravity_override.setter
def gravity_override(value: Vector) -> None
```

<a id="unreal.AnimNode_AnimDynamics.linear_spring_constant"></a>

#### linear_spring_constant

```python
@property
def linear_spring_constant() -> float
```

(float):  [Read-Write] Spring constant to use when calculating linear springs, higher values mean a stronger spring.
You need to enable the Linear Spring checkbox for this to have an effect.

<a id="unreal.AnimNode_AnimDynamics.linear_spring_constant"></a>

#### linear_spring_constant

```python
@linear_spring_constant.setter
def linear_spring_constant(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.angular_spring_constant"></a>

#### angular_spring_constant

```python
@property
def angular_spring_constant() -> float
```

(float):  [Read-Write] Spring constant to use when calculating angular springs, higher values mean a stronger spring.
You need to enable the Angular Spring checkbox for this to have an effect.
Note: Make sure to also set the Angular Target Axis and Angular Target in the Constraint Setup for this to have an effect.

<a id="unreal.AnimNode_AnimDynamics.angular_spring_constant"></a>

#### angular_spring_constant

```python
@angular_spring_constant.setter
def angular_spring_constant(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.angular_bias_override"></a>

#### angular_bias_override

```python
@property
def angular_bias_override() -> float
```

(float):  [Read-Write] Overridden angular bias value
Angular bias is essentially a twist reduction for chain forces and defaults to a value to keep chains stability
in check. When using single-body systems sometimes angular forces will look like they are "catching-up" with
the mesh, if that's the case override this and push it towards 1.0f until it settles correctly

<a id="unreal.AnimNode_AnimDynamics.angular_bias_override"></a>

#### angular_bias_override

```python
@angular_bias_override.setter
def angular_bias_override(value: float) -> None
```

<a id="unreal.AnimNode_AnimDynamics.simulation_space"></a>

#### simulation_space

```python
@property
def simulation_space() -> AnimPhysSimSpaceType
```

(AnimPhysSimSpaceType):  [Read-Write] The space used to run the simulation

<a id="unreal.AnimNode_AnimDynamics.simulation_space"></a>

#### simulation_space

```python
@simulation_space.setter
def simulation_space(value: AnimPhysSimSpaceType) -> None
```

<a id="unreal.AnimNode_AnimDynamics.use_gravity_override"></a>

#### use_gravity_override

```python
@property
def use_gravity_override() -> bool
```

(bool):  [Read-Write] Use gravity override value vs gravity scale

<a id="unreal.AnimNode_AnimDynamics.use_gravity_override"></a>

#### use_gravity_override

```python
@use_gravity_override.setter
def use_gravity_override(value: bool) -> None
```

<a id="unreal.AnimNode_ApplyLimits"></a>