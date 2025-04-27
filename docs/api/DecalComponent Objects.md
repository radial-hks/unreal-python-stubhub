## DecalComponent Objects

```python
class DecalComponent(SceneComponent)
```

A material that is rendered onto the surface of a mesh. A kind of 'bumper sticker' for a model.
see: https://docs.unrealengine.com/latest/INT/Engine/Actors/DecalActor
see: UDecalActor

**C++ Source:**

- **Module**: Engine
- **File**: DecalComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``decal_color`` (LinearColor):  [Read-Write] Decal color, can be accessed using the material Decal Color node.
- ``decal_material`` (MaterialInterface):  [Read-Write] Decal material.
- ``decal_size`` (Vector):  [Read-Write] Decal size in local space (does not include the component scale), technically redundant but there for convenience
- ``destroy_owner_after_fade`` (bool):  [Read-Write] Automatically destroys the owning actor after fully fading out.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``fade_duration`` (float):  [Read-Write] Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game.
- ``fade_in_duration`` (float):  [Read-Write]
- ``fade_in_start_delay`` (float):  [Read-Write]
- ``fade_screen_size`` (float):  [Read-Write]
- ``fade_start_delay`` (float):  [Read-Write] Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
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
- ``sort_order`` (int32):  [Read-Write] Controls the order in which decal elements are rendered.  Higher values draw later (on top).
  Setting many different sort orders on many different decals prevents sorting by state and can reduce performance.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.DecalComponent.decal_material"></a>

#### decal_material

```python
@property
def decal_material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] Decal material.

<a id="unreal.DecalComponent.sort_order"></a>

#### sort_order

```python
@property
def sort_order() -> int
```

(int32):  [Read-Only] Controls the order in which decal elements are rendered.  Higher values draw later (on top).
Setting many different sort orders on many different decals prevents sorting by state and can reduce performance.

<a id="unreal.DecalComponent.fade_screen_size"></a>

#### fade_screen_size

```python
@property
def fade_screen_size() -> float
```

(float):  [Read-Only]

<a id="unreal.DecalComponent.fade_start_delay"></a>

#### fade_start_delay

```python
@property
def fade_start_delay() -> float
```

(float):  [Read-Only] Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent.

<a id="unreal.DecalComponent.fade_duration"></a>

#### fade_duration

```python
@property
def fade_duration() -> float
```

(float):  [Read-Only] Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game.

<a id="unreal.DecalComponent.fade_in_duration"></a>

#### fade_in_duration

```python
@property
def fade_in_duration() -> float
```

(float):  [Read-Only]

<a id="unreal.DecalComponent.fade_in_start_delay"></a>

#### fade_in_start_delay

```python
@property
def fade_in_start_delay() -> float
```

(float):  [Read-Only]

<a id="unreal.DecalComponent.destroy_owner_after_fade"></a>

#### destroy_owner_after_fade

```python
@property
def destroy_owner_after_fade() -> bool
```

(bool):  [Read-Only] Automatically destroys the owning actor after fully fading out.

<a id="unreal.DecalComponent.decal_size"></a>

#### decal_size

```python
@property
def decal_size() -> Vector
```

(Vector):  [Read-Only] Decal size in local space (does not include the component scale), technically redundant but there for convenience

<a id="unreal.DecalComponent.decal_color"></a>

#### decal_color

```python
@property
def decal_color() -> LinearColor
```

(LinearColor):  [Read-Only] Decal color, can be accessed using the material Decal Color node.

<a id="unreal.DecalComponent.set_sort_order"></a>

#### set_sort_order

```python
def set_sort_order(value: int) -> None
```

x.set_sort_order(value) -> None
Sets the sort order for the decal component. Higher values draw later (on top). This will force the decal to reattach

Args:
    value (int32):

<a id="unreal.DecalComponent.set_fade_screen_size"></a>

#### set_fade_screen_size

```python
def set_fade_screen_size(new_fade_screen_size: float) -> None
```

x.set_fade_screen_size(new_fade_screen_size) -> None
Set the FadeScreenSize for this decal component

Args:
    new_fade_screen_size (float):

<a id="unreal.DecalComponent.set_fade_out"></a>

#### set_fade_out

```python
def set_fade_out(start_delay: float,
                 duration: float,
                 destroy_owner_after_fade: bool = True) -> None
```

x.set_fade_out(start_delay, duration, destroy_owner_after_fade=True) -> None
Sets the decal's fade start time, duration and if the owning actor should be destroyed after the decal is fully faded out.
The default value of 0 for FadeStartDelay and FadeDuration makes the decal persistent. See DecalLifetimeOpacity material
node to control the look of "fading out."

Args:
    start_delay (float): Time in seconds to wait before beginning to fade out the decal.
    duration (float): Time in second for the decal to fade out.
    destroy_owner_after_fade (bool): Should the owning actor automatically be destroyed after it is completely faded out.

<a id="unreal.DecalComponent.set_fade_in"></a>

#### set_fade_in

```python
def set_fade_in(start_delay: float, duration: float) -> None
```

x.set_fade_in(start_delay, duration) -> None
Set Fade In

Args:
    start_delay (float): 
    duration (float):

<a id="unreal.DecalComponent.set_decal_material"></a>

#### set_decal_material

```python
def set_decal_material(new_decal_material: MaterialInterface) -> None
```

x.set_decal_material(new_decal_material) -> None
setting decal material on decal component. This will force the decal to reattach

Args:
    new_decal_material (MaterialInterface):

<a id="unreal.DecalComponent.set_decal_color"></a>

#### set_decal_color

```python
def set_decal_color(color: LinearColor) -> None
```

x.set_decal_color(color) -> None
Sets the decal color.

Args:
    color (LinearColor):

<a id="unreal.DecalComponent.get_fade_start_delay"></a>

#### get_fade_start_delay

```python
def get_fade_start_delay() -> float
```

x.get_fade_start_delay() -> float
Get Fade Start Delay

Returns:
    float:

<a id="unreal.DecalComponent.get_fade_in_start_delay"></a>

#### get_fade_in_start_delay

```python
def get_fade_in_start_delay() -> float
```

x.get_fade_in_start_delay() -> float
Get Fade in Start Delay

Returns:
    float:

<a id="unreal.DecalComponent.get_fade_in_duration"></a>

#### get_fade_in_duration

```python
def get_fade_in_duration() -> float
```

x.get_fade_in_duration() -> float
Get Fade in Duration

Returns:
    float:

<a id="unreal.DecalComponent.get_fade_duration"></a>

#### get_fade_duration

```python
def get_fade_duration() -> float
```

x.get_fade_duration() -> float
Get Fade Duration

Returns:
    float:

<a id="unreal.DecalComponent.get_decal_material"></a>

#### get_decal_material

```python
def get_decal_material() -> MaterialInterface
```

x.get_decal_material() -> MaterialInterface
Accessor for decal material

Returns:
    MaterialInterface:

<a id="unreal.DecalComponent.create_dynamic_material_instance"></a>

#### create_dynamic_material_instance

```python
def create_dynamic_material_instance() -> MaterialInstanceDynamic
```

x.create_dynamic_material_instance() -> MaterialInstanceDynamic
Utility to allocate a new Dynamic Material Instance, set its parent to the currently applied material, and assign it

Returns:
    MaterialInstanceDynamic:

<a id="unreal.DecalComponent.create_mid_for_decal"></a>

#### create_mid_for_decal

```python
def create_mid_for_decal() -> MaterialInstanceDynamic
```

deprecated: 'create_mid_for_decal' was renamed to 'create_dynamic_material_instance'.

<a id="unreal.LightComponent"></a>