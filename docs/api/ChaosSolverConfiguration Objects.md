## ChaosSolverConfiguration Objects

```python
class ChaosSolverConfiguration(StructBase)
```

Chaos Solver Configuration

**C++ Source:**

- **Module**: Chaos
- **File**: ChaosSolverConfiguration.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``breaking_filter_settings`` (SolverBreakingFilterSettings):  [Read-Write]
- ``cluster_connection_factor`` (float):  [Read-Write]
- ``cluster_union_connection_type`` (ClusterUnionMethod):  [Read-Write]
- ``collision_cull_distance`` (float):  [Read-Write] During collision detection, if tweo shapes are at least this far apart we do not calculate their nearest features
  during the collision detection step.
- ``collision_filter_settings`` (SolverCollisionFilterSettings):  [Read-Write]
- ``collision_initial_overlap_depenetration_velocity`` (float):  [Read-Write] If two bodies start off in overlapping each other, they will depentrate at this speed when they wake.
  If set to a large value, initially-overlapping objects will tend to "explode" apart at a speed that depends on the
  overlap amount and the timestep (this is the original, previously untunable behaviour). If set to zero,
  initially-overlapping objects will remain stationary and go to sleep until acted on by some other object or force.
  A negative value (-1) disables the feature and is equivalent to infinity.
  This property can be overridden per Body (see FBodyInstance::MaxDepenetrationVelocity)
- ``collision_margin_fraction`` (float):  [Read-Write] A collision margin as a fraction of size used by some boxes and convex shapes to improve collision detection results.
  The core geometry of shapes that support a margin are reduced in size by the margin, and the margin
  is added back on during collision detection. The net result is a shape of the same size but with rounded corners.
- ``collision_margin_max`` (float):  [Read-Write] An upper limit on the collision margin that will be subtracted from boxes and convex shapes. See CollisionMarginFraction
- ``collision_max_push_out_velocity`` (float):  [Read-Write] The maximum speed at which two bodies can be extracted from each other when they start a frame inter-penetrating. This can
  happen because they spawned on top of each other, or the solver failed to fully reolve collisions last frame. A value of
  zero means "no limit". A non-zero value can be used to prevent explosive behaviour when bodies start deeply penetrating.
  An alternative to using this approach is to increase the number of Velocity Iterations, which is more expensive but will
  ensure the bodies are depenetrated in a single frame without explosive behaviour.
- ``generate_break_data`` (bool):  [Read-Write]
- ``generate_collision_data`` (bool):  [Read-Write]
- ``generate_trailing_data`` (bool):  [Read-Write]
- ``position_iterations`` (int32):  [Read-Write] The number of position iterations to run during the constraint solver step
- ``projection_iterations`` (int32):  [Read-Write] The number of projection iterations to run during the constraint solver step
- ``trailing_filter_settings`` (SolverTrailingFilterSettings):  [Read-Write]
- ``velocity_iterations`` (int32):  [Read-Write] The number of velocity iterations to run during the constraint solver step

<a id="unreal.ChaosSolverConfiguration.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.ChaosDebugSubstepControl"></a>