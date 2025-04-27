## LocalFogVolumeComponent Objects

```python
class LocalFogVolumeComponent(SceneComponent)
```

Local Fog Volume Component

**C++ Source:**

- **Module**: Engine
- **File**: LocalFogVolumeComponent.h

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
- ``fog_albedo`` (LinearColor):  [Read-Write] Controls the albedo of this fog volume.
- ``fog_emissive`` (LinearColor):  [Read-Write] Controls the emissive color of this fog volume.
- ``fog_phase_g`` (float):  [Read-Write] Controls the phase `G` parameter, describing the directionality of the scattering within this fog volume.
- ``fog_sort_priority`` (int32):  [Read-Write] The priority can be used as a way to override the sorting by distance. A lower value means the volume will be considered further away, i.e. it will draw behind the one with a higher priority value.
- ``height_fog_extinction`` (float):  [Read-Write] The density of the radial fog representing its extinction coefficient at height 0 in the unit sphere. The final look of the volume is determined by combining the "Coverage=1-Transmittance" of both radial and height fog in order to achieve both soft edges and height fog.
- ``height_fog_falloff`` (float):  [Read-Write] Controls how the density decreases as height increases. Smaller values make the visible transition larger. 1.0 is the lowest value before visual artifact are visible at the horizon.
- ``height_fog_offset`` (float):  [Read-Write] Height offset, relative to the actor Z position.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``radial_fog_extinction`` (float):  [Read-Write] The density of the radial fog representing its extinction coefficient at the center of the sphere. The final look of the volume is determined by combining the "Coverage=1-Transmittance" of both radial and height fog in order to achieve both soft edges and height fog.
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

<a id="unreal.LocalFogVolumeComponent.radial_fog_extinction"></a>

#### radial_fog_extinction

```python
@property
def radial_fog_extinction() -> float
```

(float):  [Read-Only] The density of the radial fog representing its extinction coefficient at the center of the sphere. The final look of the volume is determined by combining the "Coverage=1-Transmittance" of both radial and height fog in order to achieve both soft edges and height fog.

<a id="unreal.LocalFogVolumeComponent.height_fog_extinction"></a>

#### height_fog_extinction

```python
@property
def height_fog_extinction() -> float
```

(float):  [Read-Only] The density of the radial fog representing its extinction coefficient at height 0 in the unit sphere. The final look of the volume is determined by combining the "Coverage=1-Transmittance" of both radial and height fog in order to achieve both soft edges and height fog.

<a id="unreal.LocalFogVolumeComponent.height_fog_falloff"></a>

#### height_fog_falloff

```python
@property
def height_fog_falloff() -> float
```

(float):  [Read-Only] Controls how the density decreases as height increases. Smaller values make the visible transition larger. 1.0 is the lowest value before visual artifact are visible at the horizon.

<a id="unreal.LocalFogVolumeComponent.height_fog_offset"></a>

#### height_fog_offset

```python
@property
def height_fog_offset() -> float
```

(float):  [Read-Only] Height offset, relative to the actor Z position.

<a id="unreal.LocalFogVolumeComponent.fog_phase_g"></a>

#### fog_phase_g

```python
@property
def fog_phase_g() -> float
```

(float):  [Read-Only] Controls the phase `G` parameter, describing the directionality of the scattering within this fog volume.

<a id="unreal.LocalFogVolumeComponent.fog_albedo"></a>

#### fog_albedo

```python
@property
def fog_albedo() -> LinearColor
```

(LinearColor):  [Read-Only] Controls the albedo of this fog volume.

<a id="unreal.LocalFogVolumeComponent.fog_emissive"></a>

#### fog_emissive

```python
@property
def fog_emissive() -> LinearColor
```

(LinearColor):  [Read-Only] Controls the emissive color of this fog volume.

<a id="unreal.LocalFogVolumeComponent.fog_sort_priority"></a>

#### fog_sort_priority

```python
@property
def fog_sort_priority() -> int
```

(int32):  [Read-Only] The priority can be used as a way to override the sorting by distance. A lower value means the volume will be considered further away, i.e. it will draw behind the one with a higher priority value.

<a id="unreal.LocalFogVolumeComponent.set_radial_fog_extinction"></a>

#### set_radial_fog_extinction

```python
def set_radial_fog_extinction(new_value: float) -> None
```

x.set_radial_fog_extinction(new_value) -> None
Set Radial Fog Extinction

Args:
    new_value (float):

<a id="unreal.LocalFogVolumeComponent.set_height_fog_offset"></a>

#### set_height_fog_offset

```python
def set_height_fog_offset(new_value: float) -> None
```

x.set_height_fog_offset(new_value) -> None
Set Height Fog Offset

Args:
    new_value (float):

<a id="unreal.LocalFogVolumeComponent.set_height_fog_falloff"></a>

#### set_height_fog_falloff

```python
def set_height_fog_falloff(new_value: float) -> None
```

x.set_height_fog_falloff(new_value) -> None
Set Height Fog Falloff

Args:
    new_value (float):

<a id="unreal.LocalFogVolumeComponent.set_height_fog_extinction"></a>

#### set_height_fog_extinction

```python
def set_height_fog_extinction(new_value: float) -> None
```

x.set_height_fog_extinction(new_value) -> None
Set Height Fog Extinction

Args:
    new_value (float):

<a id="unreal.LocalFogVolumeComponent.set_fog_phase_g"></a>

#### set_fog_phase_g

```python
def set_fog_phase_g(new_value: float) -> None
```

x.set_fog_phase_g(new_value) -> None
Set Fog Phase G

Args:
    new_value (float):

<a id="unreal.LocalFogVolumeComponent.set_fog_emissive"></a>

#### set_fog_emissive

```python
def set_fog_emissive(new_value: LinearColor) -> None
```

x.set_fog_emissive(new_value) -> None
Set Fog Emissive

Args:
    new_value (LinearColor):

<a id="unreal.LocalFogVolumeComponent.set_fog_albedo"></a>

#### set_fog_albedo

```python
def set_fog_albedo(new_value: LinearColor) -> None
```

x.set_fog_albedo(new_value) -> None
Set Fog Albedo

Args:
    new_value (LinearColor):

<a id="unreal.LocalLightComponent"></a>