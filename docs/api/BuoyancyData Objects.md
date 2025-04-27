## BuoyancyData Objects

```python
class BuoyancyData(StructBase)
```

Buoyancy Data

**C++ Source:**

- **Plugin**: Water
- **Module**: Water
- **File**: BuoyancyTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_current_when_moving_fast_upstream`` (bool):  [Read-Write] Apply the current when moving at high speeds upstream. Disable for vehicles to have more control
- ``always_allow_lateral_push`` (bool):  [Read-Write] Allow an object to be pushed laterally regardless of the forward movement speed through the river
- ``angular_drag_coefficient`` (float):  [Read-Write] Coefficient for applying angular drag that resists the rotation of the object
- ``apply_downstream_angular_rotation`` (bool):  [Read-Write] Apply torque to align the object along the downstream direction of the river
- ``apply_drag_forces_in_water`` (bool):  [Read-Write]
- ``apply_river_forces`` (bool):  [Read-Write] Whether we should apply river forces such as downstream push and shore push
- ``buoyancy_coefficient`` (float):  [Read-Write] Increases buoyant force applied on each pontoon.
- ``buoyancy_damp`` (float):  [Read-Write] Damping factor to scale damping based on Z velocity.
- ``buoyancy_damp2`` (float):  [Read-Write] Second Order Damping factor to scale damping based on Z velocity.
- ``buoyancy_ramp_max`` (float):  [Read-Write] Maximum value that buoyancy can ramp to (at or beyond max velocity).
- ``buoyancy_ramp_max_velocity`` (float):  [Read-Write] Maximum velocity until which the buoyancy can ramp up.
- ``buoyancy_ramp_min_velocity`` (float):  [Read-Write] Minimum velocity to start applying a ramp to buoyancy.
- ``center_pontoons_on_com`` (bool):  [Read-Write] If true, center pontoons around center of mass when using relative locations
                (not used when pontoon locations are specified via sockets)
- ``downstream_axis_of_rotation`` (Vector):  [Read-Write] The axis with respect to the object that the downstream angular rotation should be aligned
- ``downstream_max_acceleration`` (float):  [Read-Write] Maximum torque to apply per update for downstream rotation
- ``downstream_rotation_angular_damping`` (float):  [Read-Write] Damping of the spring used to align the object along the downstream direction
- ``downstream_rotation_stiffness`` (float):  [Read-Write] Stiffness of the spring used to align the object along the downstream direction
- ``downstream_rotation_strength`` (float):  [Read-Write] Strength of the downstream angular rotation application
- ``drag_coefficient`` (float):  [Read-Write] Coefficient for applying linear drag based on speed
- ``drag_coefficient2`` (float):  [Read-Write] Coefficient for applying linear drag based on the square of the speed
- ``max_buoyant_force`` (float):  [Read-Write] Maximum buoyant force in the Up direction.
- ``max_drag_speed`` (float):  [Read-Write] Max speed for which drag force is applied
- ``max_shore_push_force`` (float):  [Read-Write] Maximum push force that can be applied by riverths towards the center or edge.
- ``max_water_force`` (float):  [Read-Write] Maximum push force that can be applied by rivers.
- ``pontoons`` (Array[SphericalPontoon]):  [Read-Write]
- ``river_pontoon_index`` (int32):  [Read-Write] Pontoon to calculate water forces from. Used to calculate lateral push/pull, to grab water velocity for main force calculations from for downstream calculation if possible.
- ``river_traversal_path_width`` (float):  [Read-Write] Path width along the inside of the river which the object should traverse
- ``water_shore_push_factor`` (float):  [Read-Write] Coefficient for nudging objects to shore in Rivers (for perf reasons). Or, set negative to push towards center of river.
- ``water_velocity_strength`` (float):  [Read-Write] Coefficient for applying push force in rivers.

<a id="unreal.BuoyancyData.__init__"></a>

#### __init__

```python
def __init__(pontoons: Array[SphericalPontoon] = [],
             center_pontoons_on_com: bool = False) -> None
```

<a id="unreal.BuoyancyData.pontoons"></a>

#### pontoons

```python
@property
def pontoons() -> Array[SphericalPontoon]
```

(Array[SphericalPontoon]):  [Read-Only]

<a id="unreal.BuoyancyData.center_pontoons_on_com"></a>

#### center_pontoons_on_com

```python
@property
def center_pontoons_on_com() -> bool
```

(bool):  [Read-Only] If true, center pontoons around center of mass when using relative locations
              (not used when pontoon locations are specified via sockets)

<a id="unreal.WaterBodyWeightmapSettings"></a>