## WindDirectionalSourceComponent Objects

```python
class WindDirectionalSourceComponent(SceneComponent)
```

Component that provides a directional wind source. Only affects SpeedTree assets.

**C++ Source:**

- **Module**: Engine
- **File**: WindDirectionalSourceComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``max_gust_amount`` (float):  [Read-Write]
- ``min_gust_amount`` (float):  [Read-Write]
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``point_wind`` (bool):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``radius`` (float):  [Read-Write]
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``speed`` (float):  [Read-Write]
- ``strength`` (float):  [Read-Write]
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.WindDirectionalSourceComponent.strength"></a>

#### strength

```python
@property
def strength() -> float
```

(float):  [Read-Write]

<a id="unreal.WindDirectionalSourceComponent.strength"></a>

#### strength

```python
@strength.setter
def strength(value: float) -> None
```

<a id="unreal.WindDirectionalSourceComponent.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(float):  [Read-Write]

<a id="unreal.WindDirectionalSourceComponent.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.WindDirectionalSourceComponent.min_gust_amount"></a>

#### min_gust_amount

```python
@property
def min_gust_amount() -> float
```

(float):  [Read-Only]

<a id="unreal.WindDirectionalSourceComponent.max_gust_amount"></a>

#### max_gust_amount

```python
@property
def max_gust_amount() -> float
```

(float):  [Read-Only]

<a id="unreal.WindDirectionalSourceComponent.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.WindDirectionalSourceComponent.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.WindDirectionalSourceComponent.point_wind"></a>

#### point_wind

```python
@property
def point_wind() -> bool
```

(bool):  [Read-Only]

<a id="unreal.WindDirectionalSourceComponent.set_wind_type"></a>

#### set_wind_type

```python
def set_wind_type(new_type: WindSourceType) -> None
```

x.set_wind_type(new_type) -> None
Set the type of wind generator to use

Args:
    new_type (WindSourceType):

<a id="unreal.WindDirectionalSourceComponent.set_strength"></a>

#### set_strength

```python
def set_strength(new_strength: float) -> None
```

x.set_strength(new_strength) -> None
Sets the strength of the generated wind

Args:
    new_strength (float):

<a id="unreal.WindDirectionalSourceComponent.set_speed"></a>

#### set_speed

```python
def set_speed(new_speed: float) -> None
```

x.set_speed(new_speed) -> None
Sets the windspeed of the generated wind

Args:
    new_speed (float):

<a id="unreal.WindDirectionalSourceComponent.set_radius"></a>

#### set_radius

```python
def set_radius(new_radius: float) -> None
```

x.set_radius(new_radius) -> None
Set the effect radius for point wind

Args:
    new_radius (float):

<a id="unreal.WindDirectionalSourceComponent.set_minimum_gust_amount"></a>

#### set_minimum_gust_amount

```python
def set_minimum_gust_amount(new_min_gust: float) -> None
```

x.set_minimum_gust_amount(new_min_gust) -> None
Set minimum deviation for wind gusts

Args:
    new_min_gust (float):

<a id="unreal.WindDirectionalSourceComponent.set_maximum_gust_amount"></a>

#### set_maximum_gust_amount

```python
def set_maximum_gust_amount(new_max_gust: float) -> None
```

x.set_maximum_gust_amount(new_max_gust) -> None
Set maximum deviation for wind gusts

Args:
    new_max_gust (float):

<a id="unreal.WorldSettings"></a>