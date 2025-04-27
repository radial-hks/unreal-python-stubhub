## VolumetricCloudComponent Objects

```python
class VolumetricCloudComponent(SceneComponent)
```

A component that represents a participating media material around a planet, e.g. clouds.

**C++ Source:**

- **Module**: Engine
- **File**: VolumetricCloudComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``aerial_pespective_mie_scattering_fade_distance`` (float):  [Read-Write] Specify the distance over which the Rayleigh scattering will linearly ramp up to full effect. (kilometers)
- ``aerial_pespective_mie_scattering_start_distance`` (float):  [Read-Write] Specify the aerial perspective start distance on cloud for Mie scattering only. (kilometers)
- ``aerial_pespective_rayleigh_scattering_fade_distance`` (float):  [Read-Write] Specify the distance over which the Rayleigh scattering will linearly ramp up to full effect. (kilometers)
- ``aerial_pespective_rayleigh_scattering_start_distance`` (float):  [Read-Write] Specify the aerial perspective start distance on cloud for Rayleigh scattering only. (kilometers)
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``ground_albedo`` (Color):  [Read-Write] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
  This is only used by the cloud material when the 'Volumetric Advanced' node have GroundContribution enabled.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``holdout`` (bool):  [Read-Write] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``layer_bottom_altitude`` (float):  [Read-Write] The altitude at which the cloud layer starts. (kilometers above the ground)
- ``layer_height`` (float):  [Read-Write] The height of the the cloud layer. (kilometers above the layer bottom altitude)
- ``material`` (MaterialInterface):  [Read-Write] The material describing the cloud volume. It must be a Volume domain material.
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``planet_radius`` (float):  [Read-Write] The planet radius used when there is not SkyAtmosphere component present in the scene.
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``reflection_view_sample_count_scale_value`` (float):  [Read-Write] Scale the tracing sample count in reflection views. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ReflectionRaySampleMaxCount'.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_in_main_pass`` (bool):  [Read-Write] If true, this component will be rendered in the main pass (basepass, transparency)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``shadow_reflection_view_sample_count_scale_value`` (float):  [Read-Write] Scale the shadow tracing sample count in reflection views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ReflectionRaySampleMaxCount'.
- ``shadow_tracing_distance`` (float):  [Read-Write] The shadow tracing distance in kilometers, only used with Advanced Output ray marched shadows.
- ``shadow_view_sample_count_scale`` (float):  [Read-Write] Scale the shadow tracing sample count in primary views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ViewRaySampleMaxCount'.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``sky_light_cloud_bottom_occlusion`` (float):  [Read-Write] Occlude the sky light contribution at the bottom of the cloud layer. This is a fast approximation to sky lighting being occluded by cloud without having to trace rays or sample AO texture. Ignored if the cloud material explicitely sets the ambient occlusion value.
- ``stop_tracing_transmittance_threshold`` (float):  [Read-Write] When the mean transmittance is below this threshold, we stop tracing. This is a good way to reduce the ray marched sample count, and thus to increase performance.
- ``tracing_max_distance`` (float):  [Read-Write] The maximum distance that will be traced inside the cloud layer. (kilometers)
- ``tracing_max_distance_mode`` (VolumetricCloudTracingMaxDistanceMode):  [Read-Write] Mode to select how the tracing max distance should be interpreted. DistanceFromPointOfView is useful to avoid the top of the cloud layer to be clipped when TracingMaxDistance is shorten for performance.
- ``tracing_start_distance_from_camera`` (float):  [Read-Write] The distance from which the tracing will start. This is useful when the camera for instance is inside the layer of cloud. (kilometers)
- ``tracing_start_max_distance`` (float):  [Read-Write] The maximum distance of the volumetric surface, i.e. cloud layer upper and lower bound, before which we will accept to start tracing. (kilometers)
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_per_sample_atmospheric_light_transmittance`` (bool):  [Read-Write] Whether to apply atmosphere transmittance per sample, instead of using the light global transmittance.
- ``view_sample_count_scale`` (float):  [Read-Write] Scale the tracing sample count in primary views. Quality level scalability CVARs affect the maximum range.
  The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ViewRaySampleCountMax'.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.VolumetricCloudComponent.layer_bottom_altitude"></a>

#### layer_bottom_altitude

```python
@property
def layer_bottom_altitude() -> float
```

(float):  [Read-Only] The altitude at which the cloud layer starts. (kilometers above the ground)

<a id="unreal.VolumetricCloudComponent.layer_height"></a>

#### layer_height

```python
@property
def layer_height() -> float
```

(float):  [Read-Only] The height of the the cloud layer. (kilometers above the layer bottom altitude)

<a id="unreal.VolumetricCloudComponent.tracing_start_max_distance"></a>

#### tracing_start_max_distance

```python
@property
def tracing_start_max_distance() -> float
```

(float):  [Read-Only] The maximum distance of the volumetric surface, i.e. cloud layer upper and lower bound, before which we will accept to start tracing. (kilometers)

<a id="unreal.VolumetricCloudComponent.tracing_start_distance_from_camera"></a>

#### tracing_start_distance_from_camera

```python
@property
def tracing_start_distance_from_camera() -> float
```

(float):  [Read-Only] The distance from which the tracing will start. This is useful when the camera for instance is inside the layer of cloud. (kilometers)

<a id="unreal.VolumetricCloudComponent.tracing_max_distance_mode"></a>

#### tracing_max_distance_mode

```python
@property
def tracing_max_distance_mode() -> VolumetricCloudTracingMaxDistanceMode
```

(VolumetricCloudTracingMaxDistanceMode):  [Read-Only] Mode to select how the tracing max distance should be interpreted. DistanceFromPointOfView is useful to avoid the top of the cloud layer to be clipped when TracingMaxDistance is shorten for performance.

<a id="unreal.VolumetricCloudComponent.tracing_max_distance"></a>

#### tracing_max_distance

```python
@property
def tracing_max_distance() -> float
```

(float):  [Read-Only] The maximum distance that will be traced inside the cloud layer. (kilometers)

<a id="unreal.VolumetricCloudComponent.planet_radius"></a>

#### planet_radius

```python
@property
def planet_radius() -> float
```

(float):  [Read-Only] The planet radius used when there is not SkyAtmosphere component present in the scene.

<a id="unreal.VolumetricCloudComponent.ground_albedo"></a>

#### ground_albedo

```python
@property
def ground_albedo() -> Color
```

(Color):  [Read-Only] The ground albedo used to light the cloud from below with respect to the sun light and sky atmosphere.
This is only used by the cloud material when the 'Volumetric Advanced' node have GroundContribution enabled.

<a id="unreal.VolumetricCloudComponent.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Only] The material describing the cloud volume. It must be a Volume domain material.

<a id="unreal.VolumetricCloudComponent.use_per_sample_atmospheric_light_transmittance"></a>

#### use_per_sample_atmospheric_light_transmittance

```python
@property
def use_per_sample_atmospheric_light_transmittance() -> bool
```

(bool):  [Read-Only] Whether to apply atmosphere transmittance per sample, instead of using the light global transmittance.

<a id="unreal.VolumetricCloudComponent.sky_light_cloud_bottom_occlusion"></a>

#### sky_light_cloud_bottom_occlusion

```python
@property
def sky_light_cloud_bottom_occlusion() -> float
```

(float):  [Read-Only] Occlude the sky light contribution at the bottom of the cloud layer. This is a fast approximation to sky lighting being occluded by cloud without having to trace rays or sample AO texture. Ignored if the cloud material explicitely sets the ambient occlusion value.

<a id="unreal.VolumetricCloudComponent.view_sample_count_scale"></a>

#### view_sample_count_scale

```python
@property
def view_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the tracing sample count in primary views. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ViewRaySampleCountMax'.

<a id="unreal.VolumetricCloudComponent.reflection_view_sample_count_scale_value"></a>

#### reflection_view_sample_count_scale_value

```python
@property
def reflection_view_sample_count_scale_value() -> float
```

(float):  [Read-Only] Scale the tracing sample count in reflection views. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.ReflectionRaySampleMaxCount'.

<a id="unreal.VolumetricCloudComponent.shadow_view_sample_count_scale"></a>

#### shadow_view_sample_count_scale

```python
@property
def shadow_view_sample_count_scale() -> float
```

(float):  [Read-Only] Scale the shadow tracing sample count in primary views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ViewRaySampleMaxCount'.

<a id="unreal.VolumetricCloudComponent.shadow_reflection_view_sample_count_scale_value"></a>

#### shadow_reflection_view_sample_count_scale_value

```python
@property
def shadow_reflection_view_sample_count_scale_value() -> float
```

(float):  [Read-Only] Scale the shadow tracing sample count in reflection views, only used with Advanced Output ray marched shadows. Quality level scalability CVARs affect the maximum range.
The sample count resolution is still clamped according to scalability setting to 'r.VolumetricCloud.Shadow.ReflectionRaySampleMaxCount'.

<a id="unreal.VolumetricCloudComponent.shadow_tracing_distance"></a>

#### shadow_tracing_distance

```python
@property
def shadow_tracing_distance() -> float
```

(float):  [Read-Only] The shadow tracing distance in kilometers, only used with Advanced Output ray marched shadows.

<a id="unreal.VolumetricCloudComponent.stop_tracing_transmittance_threshold"></a>

#### stop_tracing_transmittance_threshold

```python
@property
def stop_tracing_transmittance_threshold() -> float
```

(float):  [Read-Only] When the mean transmittance is below this threshold, we stop tracing. This is a good way to reduce the ray marched sample count, and thus to increase performance.

<a id="unreal.VolumetricCloudComponent.aerial_pespective_rayleigh_scattering_start_distance"></a>

#### aerial_pespective_rayleigh_scattering_start_distance

```python
@property
def aerial_pespective_rayleigh_scattering_start_distance() -> float
```

(float):  [Read-Only] Specify the aerial perspective start distance on cloud for Rayleigh scattering only. (kilometers)

<a id="unreal.VolumetricCloudComponent.aerial_pespective_rayleigh_scattering_fade_distance"></a>

#### aerial_pespective_rayleigh_scattering_fade_distance

```python
@property
def aerial_pespective_rayleigh_scattering_fade_distance() -> float
```

(float):  [Read-Only] Specify the distance over which the Rayleigh scattering will linearly ramp up to full effect. (kilometers)

<a id="unreal.VolumetricCloudComponent.aerial_pespective_mie_scattering_start_distance"></a>

#### aerial_pespective_mie_scattering_start_distance

```python
@property
def aerial_pespective_mie_scattering_start_distance() -> float
```

(float):  [Read-Only] Specify the aerial perspective start distance on cloud for Mie scattering only. (kilometers)

<a id="unreal.VolumetricCloudComponent.aerial_pespective_mie_scattering_fade_distance"></a>

#### aerial_pespective_mie_scattering_fade_distance

```python
@property
def aerial_pespective_mie_scattering_fade_distance() -> float
```

(float):  [Read-Only] Specify the distance over which the Rayleigh scattering will linearly ramp up to full effect. (kilometers)

<a id="unreal.VolumetricCloudComponent.holdout"></a>

#### holdout

```python
@property
def holdout() -> bool
```

(bool):  [Read-Only] If this is True, this primitive will render black with an alpha of 0, but all secondary effects (shadows, reflections, indirect lighting) remain. This feature requires activating the project setting(s) "Alpha Output", and "Support Primitive Alpha Holdout" if using the deferred renderer.

<a id="unreal.VolumetricCloudComponent.render_in_main_pass"></a>

#### render_in_main_pass

```python
@property
def render_in_main_pass() -> bool
```

(bool):  [Read-Only] If true, this component will be rendered in the main pass (basepass, transparency)

<a id="unreal.VolumetricCloudComponent.set_view_sample_count_scale"></a>

#### set_view_sample_count_scale

```python
def set_view_sample_count_scale(new_value: float) -> None
```

x.set_view_sample_count_scale(new_value) -> None
Set View Sample Count Scale

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_tracing_start_max_distance"></a>

#### set_tracing_start_max_distance

```python
def set_tracing_start_max_distance(new_value: float) -> None
```

x.set_tracing_start_max_distance(new_value) -> None
Set Tracing Start Max Distance

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_tracing_start_distance_from_camera"></a>

#### set_tracing_start_distance_from_camera

```python
def set_tracing_start_distance_from_camera(new_value: float) -> None
```

x.set_tracing_start_distance_from_camera(new_value) -> None
Set Tracing Start Distance from Camera

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_tracing_max_distance"></a>

#### set_tracing_max_distance

```python
def set_tracing_max_distance(new_value: float) -> None
```

x.set_tracing_max_distance(new_value) -> None
Set Tracing Max Distance

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_stop_tracing_transmittance_threshold"></a>

#### set_stop_tracing_transmittance_threshold

```python
def set_stop_tracing_transmittance_threshold(new_value: float) -> None
```

x.set_stop_tracing_transmittance_threshold(new_value) -> None
Set Stop Tracing Transmittance Threshold

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_sky_light_cloud_bottom_occlusion"></a>

#### set_sky_light_cloud_bottom_occlusion

```python
def set_sky_light_cloud_bottom_occlusion(new_value: float) -> None
```

x.set_sky_light_cloud_bottom_occlusion(new_value) -> None
Set Sky Light Cloud Bottom Occlusion

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_shadow_view_sample_count_scale"></a>

#### set_shadow_view_sample_count_scale

```python
def set_shadow_view_sample_count_scale(new_value: float) -> None
```

x.set_shadow_view_sample_count_scale(new_value) -> None
Set Shadow View Sample Count Scale

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_shadow_tracing_distance"></a>

#### set_shadow_tracing_distance

```python
def set_shadow_tracing_distance(new_value: float) -> None
```

x.set_shadow_tracing_distance(new_value) -> None
Set Shadow Tracing Distance

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_shadow_reflection_view_sample_count_scale"></a>

#### set_shadow_reflection_view_sample_count_scale

```python
def set_shadow_reflection_view_sample_count_scale(new_value: float) -> None
```

x.set_shadow_reflection_view_sample_count_scale(new_value) -> None
Set Shadow Reflection View Sample Count Scale

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_shadow_reflection_sample_count_scale"></a>

#### set_shadow_reflection_sample_count_scale

```python
def set_shadow_reflection_sample_count_scale(new_value: float) -> None
```

x.set_shadow_reflection_sample_count_scale(new_value) -> None
Set Shadow Reflection Sample Count Scale
deprecated: This function has been replaced by SetShadowReflectionViewSampleCountScale.

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_render_in_main_pass"></a>

#### set_render_in_main_pass

```python
def set_render_in_main_pass(value: bool) -> None
```

x.set_render_in_main_pass(value) -> None
Set Render in Main Pass

Args:
    value (bool):

<a id="unreal.VolumetricCloudComponent.set_reflection_view_sample_count_scale"></a>

#### set_reflection_view_sample_count_scale

```python
def set_reflection_view_sample_count_scale(new_value: float) -> None
```

x.set_reflection_view_sample_count_scale(new_value) -> None
Set Reflection View Sample Count Scale

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_reflection_sample_count_scale"></a>

#### set_reflection_sample_count_scale

```python
def set_reflection_sample_count_scale(new_value: float) -> None
```

x.set_reflection_sample_count_scale(new_value) -> None
Set Reflection Sample Count Scale
deprecated: This function has been replaced by SetReflectionViewSampleCountScale.

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_planet_radius"></a>

#### set_planet_radius

```python
def set_planet_radius(new_value: float) -> None
```

x.set_planet_radius(new_value) -> None
Set Planet Radius

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_material"></a>

#### set_material

```python
def set_material(new_value: MaterialInterface) -> None
```

x.set_material(new_value) -> None
Set Material

Args:
    new_value (MaterialInterface):

<a id="unreal.VolumetricCloudComponent.set_layer_height"></a>

#### set_layer_height

```python
def set_layer_height(new_value: float) -> None
```

x.set_layer_height(new_value) -> None
Set Layer Height

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_layer_bottom_altitude"></a>

#### set_layer_bottom_altitude

```python
def set_layer_bottom_altitude(new_value: float) -> None
```

x.set_layer_bottom_altitude(new_value) -> None
Set Layer Bottom Altitude

Args:
    new_value (float):

<a id="unreal.VolumetricCloudComponent.set_holdout"></a>

#### set_holdout

```python
def set_holdout(new_holdout: bool) -> None
```

x.set_holdout(new_holdout) -> None
Set Holdout

Args:
    new_holdout (bool):

<a id="unreal.VolumetricCloudComponent.set_ground_albedo"></a>

#### set_ground_albedo

```python
def set_ground_albedo(new_value: Color) -> None
```

x.set_ground_albedo(new_value) -> None
Set Ground Albedo

Args:
    new_value (Color):

<a id="unreal.VolumetricCloudComponent.setb_use_per_sample_atmospheric_light_transmittance"></a>

#### setb_use_per_sample_atmospheric_light_transmittance

```python
def setb_use_per_sample_atmospheric_light_transmittance(
        new_value: bool) -> None
```

x.setb_use_per_sample_atmospheric_light_transmittance(new_value) -> None
Setb Use Per Sample Atmospheric Light Transmittance

Args:
    new_value (bool):

<a id="unreal.VolumetricCloud"></a>