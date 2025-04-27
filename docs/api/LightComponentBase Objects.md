## LightComponentBase Objects

```python
class LightComponentBase(SceneComponent)
```

Light Component Base

**C++ Source:**

- **Module**: Engine
- **File**: LightComponentBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``affect_global_illumination`` (bool):  [Read-Write] Whether the light affects global illumination, when ray-traced global illumination is enabled.
- ``affect_reflection`` (bool):  [Read-Write] Whether the light affects objects in reflections, when ray-traced reflection is enabled.
- ``affect_translucent_lighting`` (bool):  [Read-Write] Whether the light affects translucency or not.  Disabling this can save GPU time when there are many small lights.
- ``affects_world`` (bool):  [Read-Write] Whether the light can affect the world, or whether it is disabled.
  A disabled light will not contribute to the scene in any way.  This setting cannot be changed at runtime and unbuilds lighting when changed.
  Setting this to false has the same effect as deleting the light, so it is useful for non-destructive experiments.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``cast_deep_shadow`` (bool):  [Read-Write] Whether the light should cast high quality hair-strands self-shadowing. When this option is enabled, an extra GPU cost for this light.
- ``cast_dynamic_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True.
- ``cast_raytraced_shadow`` (CastRayTracedShadow):  [Read-Write]
- ``cast_shadows`` (bool):  [Read-Write] Whether the light should cast any shadows.
- ``cast_static_shadows`` (bool):  [Read-Write] Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True.
- ``cast_volumetric_shadow`` (bool):  [Read-Write] Whether the light shadows volumetric fog.  Disabling this can save GPU time.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``deep_shadow_layer_distribution`` (float):  [Read-Write] Change the deep shadow layers distribution 0:linear distribution (uniform layer distribution), 1:exponential (more details on near small details).
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``indirect_lighting_intensity`` (float):  [Read-Write] Scales the indirect lighting contribution from this light.
  A value of 0 disables any GI from this light. Default is 1.
- ``intensity`` (float):  [Read-Write] Total energy that the light emits.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``light_color`` (Color):  [Read-Write] Filter color of the light.
  Note that this can change the light's effective intensity.
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
- ``samples_per_pixel`` (int32):  [Read-Write] Samples per pixel for ray tracing
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``transmission`` (bool):  [Read-Write] Whether light from this light transmits through surfaces with subsurface scattering profiles. Requires light to be movable.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.
- ``volumetric_scattering_intensity`` (float):  [Read-Write] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.LightComponentBase.intensity"></a>

#### intensity

```python
@property
def intensity() -> float
```

(float):  [Read-Only] Total energy that the light emits.

<a id="unreal.LightComponentBase.brightness"></a>

#### brightness

```python
@property
def brightness() -> float
```

deprecated: 'brightness' was renamed to 'intensity'.

<a id="unreal.LightComponentBase.light_color"></a>

#### light_color

```python
@property
def light_color() -> Color
```

(Color):  [Read-Only] Filter color of the light.
Note that this can change the light's effective intensity.

<a id="unreal.LightComponentBase.affects_world"></a>

#### affects_world

```python
@property
def affects_world() -> bool
```

(bool):  [Read-Only] Whether the light can affect the world, or whether it is disabled.
A disabled light will not contribute to the scene in any way.  This setting cannot be changed at runtime and unbuilds lighting when changed.
Setting this to false has the same effect as deleting the light, so it is useful for non-destructive experiments.

<a id="unreal.LightComponentBase.cast_shadows"></a>

#### cast_shadows

```python
@property
def cast_shadows() -> bool
```

(bool):  [Read-Only] Whether the light should cast any shadows.

<a id="unreal.LightComponentBase.cast_static_shadows"></a>

#### cast_static_shadows

```python
@property
def cast_static_shadows() -> bool
```

(bool):  [Read-Only] Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True.

<a id="unreal.LightComponentBase.cast_dynamic_shadows"></a>

#### cast_dynamic_shadows

```python
@property
def cast_dynamic_shadows() -> bool
```

(bool):  [Read-Only] Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True.

<a id="unreal.LightComponentBase.affect_translucent_lighting"></a>

#### affect_translucent_lighting

```python
@property
def affect_translucent_lighting() -> bool
```

(bool):  [Read-Only] Whether the light affects translucency or not.  Disabling this can save GPU time when there are many small lights.

<a id="unreal.LightComponentBase.transmission"></a>

#### transmission

```python
@property
def transmission() -> bool
```

(bool):  [Read-Only] Whether light from this light transmits through surfaces with subsurface scattering profiles. Requires light to be movable.

<a id="unreal.LightComponentBase.cast_volumetric_shadow"></a>

#### cast_volumetric_shadow

```python
@property
def cast_volumetric_shadow() -> bool
```

(bool):  [Read-Only] Whether the light shadows volumetric fog.  Disabling this can save GPU time.

<a id="unreal.LightComponentBase.cast_deep_shadow"></a>

#### cast_deep_shadow

```python
@property
def cast_deep_shadow() -> bool
```

(bool):  [Read-Only] Whether the light should cast high quality hair-strands self-shadowing. When this option is enabled, an extra GPU cost for this light.

<a id="unreal.LightComponentBase.cast_raytraced_shadow"></a>

#### cast_raytraced_shadow

```python
@property
def cast_raytraced_shadow() -> CastRayTracedShadow
```

(CastRayTracedShadow):  [Read-Only]

<a id="unreal.LightComponentBase.affect_reflection"></a>

#### affect_reflection

```python
@property
def affect_reflection() -> bool
```

(bool):  [Read-Only] Whether the light affects objects in reflections, when ray-traced reflection is enabled.

<a id="unreal.LightComponentBase.affect_global_illumination"></a>

#### affect_global_illumination

```python
@property
def affect_global_illumination() -> bool
```

(bool):  [Read-Only] Whether the light affects global illumination, when ray-traced global illumination is enabled.

<a id="unreal.LightComponentBase.deep_shadow_layer_distribution"></a>

#### deep_shadow_layer_distribution

```python
@property
def deep_shadow_layer_distribution() -> float
```

(float):  [Read-Only] Change the deep shadow layers distribution 0:linear distribution (uniform layer distribution), 1:exponential (more details on near small details).

<a id="unreal.LightComponentBase.indirect_lighting_intensity"></a>

#### indirect_lighting_intensity

```python
@property
def indirect_lighting_intensity() -> float
```

(float):  [Read-Only] Scales the indirect lighting contribution from this light.
A value of 0 disables any GI from this light. Default is 1.

<a id="unreal.LightComponentBase.volumetric_scattering_intensity"></a>

#### volumetric_scattering_intensity

```python
@property
def volumetric_scattering_intensity() -> float
```

(float):  [Read-Only] Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor.

<a id="unreal.LightComponentBase.samples_per_pixel"></a>

#### samples_per_pixel

```python
@property
def samples_per_pixel() -> int
```

(int32):  [Read-Only] Samples per pixel for ray tracing

<a id="unreal.LightComponentBase.set_samples_per_pixel"></a>

#### set_samples_per_pixel

```python
def set_samples_per_pixel(new_value: int) -> None
```

x.set_samples_per_pixel(new_value) -> None
Set Samples Per Pixel

Args:
    new_value (int32):

<a id="unreal.LightComponentBase.set_cast_volumetric_shadow"></a>

#### set_cast_volumetric_shadow

```python
def set_cast_volumetric_shadow(new_value: bool) -> None
```

x.set_cast_volumetric_shadow(new_value) -> None
Set Cast Volumetric Shadow

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.set_cast_shadows"></a>

#### set_cast_shadows

```python
def set_cast_shadows(new_value: bool) -> None
```

x.set_cast_shadows(new_value) -> None
Sets whether this light casts shadows

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.set_cast_raytraced_shadows"></a>

#### set_cast_raytraced_shadows

```python
def set_cast_raytraced_shadows(new_value: CastRayTracedShadow) -> None
```

x.set_cast_raytraced_shadows(new_value) -> None
Set Cast Raytraced Shadows

Args:
    new_value (CastRayTracedShadow):

<a id="unreal.LightComponentBase.set_cast_raytraced_shadow"></a>

#### set_cast_raytraced_shadow

```python
def set_cast_raytraced_shadow(new_value: bool) -> None
```

x.set_cast_raytraced_shadow(new_value) -> None
Set Cast Raytraced Shadow
deprecated: ULightComponentBase::SetCastRaytracedShadow is deprecated. Use ULightComponentBase::SetCastRaytracedShadows instead.

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.set_cast_deep_shadow"></a>

#### set_cast_deep_shadow

```python
def set_cast_deep_shadow(new_value: bool) -> None
```

x.set_cast_deep_shadow(new_value) -> None
Set Cast Deep Shadow

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.set_affect_reflection"></a>

#### set_affect_reflection

```python
def set_affect_reflection(new_value: bool) -> None
```

x.set_affect_reflection(new_value) -> None
Set Affect Reflection

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.set_affect_global_illumination"></a>

#### set_affect_global_illumination

```python
def set_affect_global_illumination(new_value: bool) -> None
```

x.set_affect_global_illumination(new_value) -> None
Set Affect Global Illumination

Args:
    new_value (bool):

<a id="unreal.LightComponentBase.get_light_color"></a>

#### get_light_color

```python
def get_light_color() -> LinearColor
```

x.get_light_color() -> LinearColor
Gets the light color as a linear color

Returns:
    LinearColor:

<a id="unreal.Texture2D"></a>