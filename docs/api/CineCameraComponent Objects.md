## CineCameraComponent Objects

```python
class CineCameraComponent(CameraComponent)
```

A specialized version of a camera component, geared toward cinematic usage.

**C++ Source:**

- **Module**: CinematicCamera
- **File**: CineCameraComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``aspect_ratio`` (float):  [Read-Write] Aspect Ratio (Width/Height)
- ``aspect_ratio_axis_constraint`` (AspectRatioAxisConstraint):  [Read-Write] Override for the default aspect ratio axis constraint defined on the local player
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_calculate_ortho_planes`` (bool):  [Read-Write] Automatically determine a min/max Near/Far clip plane position depending on OrthoWidth value
- ``auto_plane_shift`` (float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane
- ``camera_mesh`` (StaticMesh):  [Read-Write]
- ``camera_mesh_hidden_in_game`` (bool):  [Read-Write] If the camera mesh is visible in game. Only relevant when running editor builds.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``constrain_aspect_ratio`` (bool):  [Read-Write] If bConstrainAspectRatio is true, black bars will be added if the destination view has a different aspect ratio than this camera requested.
- ``crop_overscan`` (bool):  [Read-Write] Indicates that the overscanned pixels should be cropped at the end of the rendering pipeline, allowing the overscanned pixels to be used in post process effects
  that need extra pixels beyond the view frustum (e.g. lens distortion) without having to render those pixels to the screen. When bScaleResolutionWithOverscan is enabled,
  the cropped image will have the same resolution as the original non-overscanned image, but when disabled, the cropped image will be a lower resolution.
- ``crop_settings`` (PlateCropSettings):  [Read-Write] Controls the crop settings.
- ``current_aperture`` (float):  [Read-Write] Current aperture, in terms of f-stop (e.g. 2.8 for f/2.8)
- ``current_focal_length`` (float):  [Read-Write] Current focal length of the camera (i.e. controls FoV, zoom)
- ``current_focus_distance`` (float):  [Read-Only] Read-only. Control this value via FocusSettings.
- ``current_horizontal_fov`` (float):  [Read-Only] Read-only. Control this value with CurrentFocalLength (and filmback settings).
- ``custom_near_clipping_plane`` (float):  [Read-Write] Set bOverride_CustomNearClippingPlane to true if you want to use a custom clipping plane instead of GNearClippingPlane.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``draw_frustum_allowed`` (bool):  [Read-Write] The Frustum visibility flag for draw frustum component initialization
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_first_person_field_of_view`` (bool):  [Read-Write] True if the first person field of view should be used for primitives tagged as "IsFirstPerson".
- ``enable_first_person_scale`` (bool):  [Read-Write] True if the first person scale should be used for primitives tagged as "IsFirstPerson".
- ``field_of_view`` (float):  [Read-Write] The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode)

  If the aspect ratio axis constraint (from ULocalPlayer, ALevelSequenceActor, etc.) is set to maintain vertical FOV, the AspectRatio
  property will be used to convert this property's value to a vertical FOV.
- ``filmback`` (CameraFilmbackSettings):  [Read-Write] Controls the filmback of the camera.
- ``first_person_field_of_view`` (float):  [Read-Write] The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson".
- ``first_person_scale`` (float):  [Read-Write] The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene.
- ``focus_settings`` (CameraFocusSettings):  [Read-Write] Controls the camera's focus.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lens_settings`` (CameraLensSettings):  [Read-Write] Controls the camera's lens.
- ``lock_to_hmd`` (bool):  [Read-Write] True if the camera's orientation and position should be locked to the HMD
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``ortho_far_clip_plane`` (float):  [Read-Write] The far plane distance of the orthographic view (in world units)
- ``ortho_near_clip_plane`` (float):  [Read-Write] The near plane distance of the orthographic view (in world units)
- ``ortho_width`` (float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)
- ``override_aspect_ratio_axis_constraint`` (bool):  [Read-Write] Whether to override the default aspect ratio axis constraint defined on the local player
- ``override_custom_near_clipping_plane`` (bool):  [Read-Write]
- ``overscan`` (float):  [Read-Write] Amount to increase the view frustum by, from 0.0 for no increase to 1.0 for 100% increase
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``post_process_blend_weight`` (float):  [Read-Write] Indicates if PostProcessSettings should be used when using this Camera to view through.
- ``post_process_settings`` (PostProcessSettings):  [Read-Write] Post process settings to use for this camera. Don't forget to check the properties you want to override
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``projection_mode`` (CameraProjectionMode):  [Read-Write] The type of camera
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``scale_resolution_with_overscan`` (bool):  [Read-Write] Indicates that the resolution should be scaled by the overscan amount so that the original view frustum remains the same resolution.
  Note that when enabled, increasing overscan will result in increased rendering workload, potentially decreasing performance as resolution increases
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``update_ortho_planes`` (bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_camera_height_as_view_target`` (bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)
- ``use_field_of_view_for_lod`` (bool):  [Read-Write] If true, account for the field of view angle when computing which level of detail to use for meshes.
- ``use_pawn_control_rotation`` (bool):  [Read-Write] If this camera component is placed on a pawn, should it use the view/control rotation of the pawn where possible?
  see: APawn::GetViewRotation()
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.CineCameraComponent.filmback"></a>

#### filmback

```python
@property
def filmback() -> CameraFilmbackSettings
```

(CameraFilmbackSettings):  [Read-Write] Controls the filmback of the camera.

<a id="unreal.CineCameraComponent.filmback"></a>

#### filmback

```python
@filmback.setter
def filmback(value: CameraFilmbackSettings) -> None
```

<a id="unreal.CineCameraComponent.lens_settings"></a>

#### lens_settings

```python
@property
def lens_settings() -> CameraLensSettings
```

(CameraLensSettings):  [Read-Write] Controls the camera's lens.

<a id="unreal.CineCameraComponent.lens_settings"></a>

#### lens_settings

```python
@lens_settings.setter
def lens_settings(value: CameraLensSettings) -> None
```

<a id="unreal.CineCameraComponent.focus_settings"></a>

#### focus_settings

```python
@property
def focus_settings() -> CameraFocusSettings
```

(CameraFocusSettings):  [Read-Write] Controls the camera's focus.

<a id="unreal.CineCameraComponent.focus_settings"></a>

#### focus_settings

```python
@focus_settings.setter
def focus_settings(value: CameraFocusSettings) -> None
```

<a id="unreal.CineCameraComponent.crop_settings"></a>

#### crop_settings

```python
@property
def crop_settings() -> PlateCropSettings
```

(PlateCropSettings):  [Read-Write] Controls the crop settings.

<a id="unreal.CineCameraComponent.crop_settings"></a>

#### crop_settings

```python
@crop_settings.setter
def crop_settings(value: PlateCropSettings) -> None
```

<a id="unreal.CineCameraComponent.current_focal_length"></a>

#### current_focal_length

```python
@property
def current_focal_length() -> float
```

(float):  [Read-Write] Current focal length of the camera (i.e. controls FoV, zoom)

<a id="unreal.CineCameraComponent.current_focal_length"></a>

#### current_focal_length

```python
@current_focal_length.setter
def current_focal_length(value: float) -> None
```

<a id="unreal.CineCameraComponent.current_aperture"></a>

#### current_aperture

```python
@property
def current_aperture() -> float
```

(float):  [Read-Write] Current aperture, in terms of f-stop (e.g. 2.8 for f/2.8)

<a id="unreal.CineCameraComponent.current_aperture"></a>

#### current_aperture

```python
@current_aperture.setter
def current_aperture(value: float) -> None
```

<a id="unreal.CineCameraComponent.current_focus_distance"></a>

#### current_focus_distance

```python
@property
def current_focus_distance() -> float
```

(float):  [Read-Only] Read-only. Control this value via FocusSettings.

<a id="unreal.CineCameraComponent.override_custom_near_clipping_plane"></a>

#### override_custom_near_clipping_plane

```python
@property
def override_custom_near_clipping_plane() -> bool
```

(bool):  [Read-Write]

<a id="unreal.CineCameraComponent.override_custom_near_clipping_plane"></a>

#### override_custom_near_clipping_plane

```python
@override_custom_near_clipping_plane.setter
def override_custom_near_clipping_plane(value: bool) -> None
```

<a id="unreal.CineCameraComponent.custom_near_clipping_plane"></a>

#### custom_near_clipping_plane

```python
@property
def custom_near_clipping_plane() -> float
```

(float):  [Read-Write] Set bOverride_CustomNearClippingPlane to true if you want to use a custom clipping plane instead of GNearClippingPlane.

<a id="unreal.CineCameraComponent.custom_near_clipping_plane"></a>

#### custom_near_clipping_plane

```python
@custom_near_clipping_plane.setter
def custom_near_clipping_plane(value: float) -> None
```

<a id="unreal.CineCameraComponent.set_lens_preset_by_name"></a>

#### set_lens_preset_by_name

```python
def set_lens_preset_by_name(preset_name: str) -> None
```

x.set_lens_preset_by_name(preset_name) -> None
Set the current lens settings by preset name.

Args:
    preset_name (str):

<a id="unreal.CineCameraComponent.set_filmback_preset_by_name"></a>

#### set_filmback_preset_by_name

```python
def set_filmback_preset_by_name(preset_name: str) -> None
```

x.set_filmback_preset_by_name(preset_name) -> None
Set the current preset settings by preset name.

Args:
    preset_name (str):

<a id="unreal.CineCameraComponent.set_crop_preset_by_name"></a>

#### set_crop_preset_by_name

```python
def set_crop_preset_by_name(preset_name: str) -> None
```

x.set_crop_preset_by_name(preset_name) -> None
Set the current lens settings by preset name.

Args:
    preset_name (str):

<a id="unreal.CineCameraComponent.get_vertical_projection_offset"></a>

#### get_vertical_projection_offset

```python
def get_vertical_projection_offset() -> float
```

x.get_vertical_projection_offset() -> float
Get Vertical Projection Offset

Returns:
    float:

<a id="unreal.CineCameraComponent.get_vertical_field_of_view"></a>

#### get_vertical_field_of_view

```python
def get_vertical_field_of_view() -> float
```

x.get_vertical_field_of_view() -> float
Returns the vertical FOV of the camera with current settings.

Returns:
    float:

<a id="unreal.CineCameraComponent.get_lens_presets_copy"></a>

#### get_lens_presets_copy

```python
@classmethod
def get_lens_presets_copy(cls) -> Array[NamedLensPreset]
```

X.get_lens_presets_copy() -> Array[NamedLensPreset]
Get Lens Presets Copy

Returns:
    Array[NamedLensPreset]:

<a id="unreal.CineCameraComponent.get_lens_preset_name"></a>

#### get_lens_preset_name

```python
def get_lens_preset_name() -> str
```

x.get_lens_preset_name() -> str
Returns the lens name of the camera with the current settings.

Returns:
    str:

<a id="unreal.CineCameraComponent.get_horizontal_projection_offset"></a>

#### get_horizontal_projection_offset

```python
def get_horizontal_projection_offset() -> float
```

x.get_horizontal_projection_offset() -> float
Get Horizontal Projection Offset

Returns:
    float:

<a id="unreal.CineCameraComponent.get_horizontal_field_of_view"></a>

#### get_horizontal_field_of_view

```python
def get_horizontal_field_of_view() -> float
```

x.get_horizontal_field_of_view() -> float
Returns the horizonal FOV of the camera with current settings.

Returns:
    float:

<a id="unreal.CineCameraComponent.get_filmback_presets_copy"></a>

#### get_filmback_presets_copy

```python
@classmethod
def get_filmback_presets_copy(cls) -> Array[NamedFilmbackPreset]
```

X.get_filmback_presets_copy() -> Array[NamedFilmbackPreset]
Get Filmback Presets Copy

Returns:
    Array[NamedFilmbackPreset]:

<a id="unreal.CineCameraComponent.get_filmback_preset_name"></a>

#### get_filmback_preset_name

```python
def get_filmback_preset_name() -> str
```

x.get_filmback_preset_name() -> str
Returns the filmback name of the camera with the current settings.

Returns:
    str:

<a id="unreal.CineCameraComponent.get_default_filmback_preset_name"></a>

#### get_default_filmback_preset_name

```python
def get_default_filmback_preset_name() -> str
```

x.get_default_filmback_preset_name() -> str
Get Default Filmback Preset Name

Returns:
    str:

<a id="unreal.CineCameraComponent.get_crop_preset_name"></a>

#### get_crop_preset_name

```python
def get_crop_preset_name() -> str
```

x.get_crop_preset_name() -> str
Returns the lens name of the camera with the current settings.

Returns:
    str:

<a id="unreal.DeveloperSettings"></a>