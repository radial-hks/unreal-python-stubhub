## MinimalViewInfo Objects

```python
class MinimalViewInfo(StructBase)
```

Minimal View Info

**C++ Source:**

- **Module**: Engine
- **File**: CameraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aspect_ratio`` (float):  [Read-Write] Aspect Ratio (Width/Height)
- ``auto_calculate_ortho_planes`` (bool):  [Read-Write] Option for the Ortho camera to automatically calculated the near/far plane
- ``auto_plane_shift`` (float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane
- ``constrain_aspect_ratio`` (bool):  [Read-Write] If bConstrainAspectRatio is true, black bars will be added if the destination view has a different aspect ratio than this camera requested.
- ``crop_fraction`` (float):  [Read-Write] The fraction between 0.0 and 1.0 of the view to crop to during the final post process upscale, with 1.0 meaning no crop
- ``first_person_fov`` (float):  [Read-Write] The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson".
- ``first_person_scale`` (float):  [Read-Write] The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene.
- ``fov`` (float):  [Read-Write] The horizontal field of view (in degrees) in perspective mode (ignored in orthographic mode).
- ``location`` (Vector):  [Read-Write] Location
- ``off_center_projection_offset`` (Vector2D):  [Read-Only] Off-axis / off-center projection offset as proportion of screen dimensions
- ``ortho_far_clip_plane`` (float):  [Read-Write] The far plane distance of the orthographic view (in world units)
- ``ortho_near_clip_plane`` (float):  [Read-Write] The near plane distance of the orthographic view (in world units)
- ``ortho_width`` (float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)
- ``overscan_resolution_fraction`` (float):  [Read-Write] Resolution fraction that scales with the amount of overscan added to the view
- ``perspective_near_clip_plane`` (float):  [Read-Write] The near plane distance of the perspective view (in world units). Set to a negative value to use the default global value of GNearClippingPlane
- ``post_process_blend_weight`` (float):  [Read-Write] Indicates if PostProcessSettings should be applied.
- ``post_process_settings`` (PostProcessSettings):  [Read-Write] Post-process settings to use if PostProcessBlendWeight is non-zero.
- ``projection_mode`` (CameraProjectionMode):  [Read-Write] The type of camera
- ``rotation`` (Rotator):  [Read-Write] Rotation
- ``update_ortho_planes`` (bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting
- ``use_camera_height_as_view_target`` (bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)
- ``use_field_of_view_for_lod`` (bool):  [Read-Write] If true, account for the field of view angle when computing which level of detail to use for meshes.
- ``use_first_person_parameters`` (bool):  [Read-Write] If bUseFirstPersonParameters is true, FirstPersonFOV and FirstPersonScale should be applied to primitives tagged as "IsFirstPerson".

<a id="unreal.MinimalViewInfo.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             fov: float = 0.000000,
             first_person_fov: float = 0.000000,
             first_person_scale: float = 0.000000,
             ortho_width: float = 0.000000,
             auto_calculate_ortho_planes: bool = False,
             auto_plane_shift: float = 0.000000,
             update_ortho_planes: bool = False,
             use_camera_height_as_view_target: bool = False,
             ortho_near_clip_plane: float = 0.000000,
             ortho_far_clip_plane: float = 0.000000,
             perspective_near_clip_plane: float = 0.000000,
             aspect_ratio: float = 0.000000,
             constrain_aspect_ratio: bool = False,
             use_first_person_parameters: bool = False,
             use_field_of_view_for_lod: bool = False,
             projection_mode: CameraProjectionMode = CameraProjectionMode.
             PERSPECTIVE,
             post_process_blend_weight: float = 0.000000,
             post_process_settings: PostProcessSettings = [],
             off_center_projection_offset: Vector2D = [0.000000, 0.000000],
             overscan_resolution_fraction: float = 0.000000,
             crop_fraction: float = 0.000000) -> None
```

<a id="unreal.MinimalViewInfo.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Location

<a id="unreal.MinimalViewInfo.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.MinimalViewInfo.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write] Rotation

<a id="unreal.MinimalViewInfo.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.MinimalViewInfo.fov"></a>

#### fov

```python
@property
def fov() -> float
```

(float):  [Read-Write] The horizontal field of view (in degrees) in perspective mode (ignored in orthographic mode).

<a id="unreal.MinimalViewInfo.fov"></a>

#### fov

```python
@fov.setter
def fov(value: float) -> None
```

<a id="unreal.MinimalViewInfo.first_person_fov"></a>

#### first_person_fov

```python
@property
def first_person_fov() -> float
```

(float):  [Read-Write] The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson".

<a id="unreal.MinimalViewInfo.first_person_fov"></a>

#### first_person_fov

```python
@first_person_fov.setter
def first_person_fov(value: float) -> None
```

<a id="unreal.MinimalViewInfo.first_person_scale"></a>

#### first_person_scale

```python
@property
def first_person_scale() -> float
```

(float):  [Read-Write] The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene.

<a id="unreal.MinimalViewInfo.first_person_scale"></a>

#### first_person_scale

```python
@first_person_scale.setter
def first_person_scale(value: float) -> None
```

<a id="unreal.MinimalViewInfo.ortho_width"></a>

#### ortho_width

```python
@property
def ortho_width() -> float
```

(float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)

<a id="unreal.MinimalViewInfo.ortho_width"></a>

#### ortho_width

```python
@ortho_width.setter
def ortho_width(value: float) -> None
```

<a id="unreal.MinimalViewInfo.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@property
def auto_calculate_ortho_planes() -> bool
```

(bool):  [Read-Write] Option for the Ortho camera to automatically calculated the near/far plane

<a id="unreal.MinimalViewInfo.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@auto_calculate_ortho_planes.setter
def auto_calculate_ortho_planes(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.auto_plane_shift"></a>

#### auto_plane_shift

```python
@property
def auto_plane_shift() -> float
```

(float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane

<a id="unreal.MinimalViewInfo.auto_plane_shift"></a>

#### auto_plane_shift

```python
@auto_plane_shift.setter
def auto_plane_shift(value: float) -> None
```

<a id="unreal.MinimalViewInfo.update_ortho_planes"></a>

#### update_ortho_planes

```python
@property
def update_ortho_planes() -> bool
```

(bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting

<a id="unreal.MinimalViewInfo.update_ortho_planes"></a>

#### update_ortho_planes

```python
@update_ortho_planes.setter
def update_ortho_planes(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@property
def use_camera_height_as_view_target() -> bool
```

(bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)

<a id="unreal.MinimalViewInfo.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@use_camera_height_as_view_target.setter
def use_camera_height_as_view_target(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.ortho_near_clip_plane"></a>

#### ortho_near_clip_plane

```python
@property
def ortho_near_clip_plane() -> float
```

(float):  [Read-Write] The near plane distance of the orthographic view (in world units)

<a id="unreal.MinimalViewInfo.ortho_near_clip_plane"></a>

#### ortho_near_clip_plane

```python
@ortho_near_clip_plane.setter
def ortho_near_clip_plane(value: float) -> None
```

<a id="unreal.MinimalViewInfo.ortho_far_clip_plane"></a>

#### ortho_far_clip_plane

```python
@property
def ortho_far_clip_plane() -> float
```

(float):  [Read-Write] The far plane distance of the orthographic view (in world units)

<a id="unreal.MinimalViewInfo.ortho_far_clip_plane"></a>

#### ortho_far_clip_plane

```python
@ortho_far_clip_plane.setter
def ortho_far_clip_plane(value: float) -> None
```

<a id="unreal.MinimalViewInfo.perspective_near_clip_plane"></a>

#### perspective_near_clip_plane

```python
@property
def perspective_near_clip_plane() -> float
```

(float):  [Read-Write] The near plane distance of the perspective view (in world units). Set to a negative value to use the default global value of GNearClippingPlane

<a id="unreal.MinimalViewInfo.perspective_near_clip_plane"></a>

#### perspective_near_clip_plane

```python
@perspective_near_clip_plane.setter
def perspective_near_clip_plane(value: float) -> None
```

<a id="unreal.MinimalViewInfo.aspect_ratio"></a>

#### aspect_ratio

```python
@property
def aspect_ratio() -> float
```

(float):  [Read-Write] Aspect Ratio (Width/Height)

<a id="unreal.MinimalViewInfo.aspect_ratio"></a>

#### aspect_ratio

```python
@aspect_ratio.setter
def aspect_ratio(value: float) -> None
```

<a id="unreal.MinimalViewInfo.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@property
def constrain_aspect_ratio() -> bool
```

(bool):  [Read-Write] If bConstrainAspectRatio is true, black bars will be added if the destination view has a different aspect ratio than this camera requested.

<a id="unreal.MinimalViewInfo.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@constrain_aspect_ratio.setter
def constrain_aspect_ratio(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.use_first_person_parameters"></a>

#### use_first_person_parameters

```python
@property
def use_first_person_parameters() -> bool
```

(bool):  [Read-Write] If bUseFirstPersonParameters is true, FirstPersonFOV and FirstPersonScale should be applied to primitives tagged as "IsFirstPerson".

<a id="unreal.MinimalViewInfo.use_first_person_parameters"></a>

#### use_first_person_parameters

```python
@use_first_person_parameters.setter
def use_first_person_parameters(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.use_field_of_view_for_lod"></a>

#### use_field_of_view_for_lod

```python
@property
def use_field_of_view_for_lod() -> bool
```

(bool):  [Read-Write] If true, account for the field of view angle when computing which level of detail to use for meshes.

<a id="unreal.MinimalViewInfo.use_field_of_view_for_lod"></a>

#### use_field_of_view_for_lod

```python
@use_field_of_view_for_lod.setter
def use_field_of_view_for_lod(value: bool) -> None
```

<a id="unreal.MinimalViewInfo.projection_mode"></a>

#### projection_mode

```python
@property
def projection_mode() -> CameraProjectionMode
```

(CameraProjectionMode):  [Read-Write] The type of camera

<a id="unreal.MinimalViewInfo.projection_mode"></a>

#### projection_mode

```python
@projection_mode.setter
def projection_mode(value: CameraProjectionMode) -> None
```

<a id="unreal.MinimalViewInfo.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@property
def post_process_blend_weight() -> float
```

(float):  [Read-Write] Indicates if PostProcessSettings should be applied.

<a id="unreal.MinimalViewInfo.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@post_process_blend_weight.setter
def post_process_blend_weight(value: float) -> None
```

<a id="unreal.MinimalViewInfo.post_process_settings"></a>

#### post_process_settings

```python
@property
def post_process_settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write] Post-process settings to use if PostProcessBlendWeight is non-zero.

<a id="unreal.MinimalViewInfo.post_process_settings"></a>

#### post_process_settings

```python
@post_process_settings.setter
def post_process_settings(value: PostProcessSettings) -> None
```

<a id="unreal.MinimalViewInfo.off_center_projection_offset"></a>

#### off_center_projection_offset

```python
@property
def off_center_projection_offset() -> Vector2D
```

(Vector2D):  [Read-Only] Off-axis / off-center projection offset as proportion of screen dimensions

<a id="unreal.MinimalViewInfo.overscan_resolution_fraction"></a>

#### overscan_resolution_fraction

```python
@property
def overscan_resolution_fraction() -> float
```

(float):  [Read-Write] Resolution fraction that scales with the amount of overscan added to the view

<a id="unreal.MinimalViewInfo.overscan_resolution_fraction"></a>

#### overscan_resolution_fraction

```python
@overscan_resolution_fraction.setter
def overscan_resolution_fraction(value: float) -> None
```

<a id="unreal.MinimalViewInfo.crop_fraction"></a>

#### crop_fraction

```python
@property
def crop_fraction() -> float
```

(float):  [Read-Write] The fraction between 0.0 and 1.0 of the view to crop to during the final post process upscale, with 1.0 meaning no crop

<a id="unreal.MinimalViewInfo.crop_fraction"></a>

#### crop_fraction

```python
@crop_fraction.setter
def crop_fraction(value: float) -> None
```

<a id="unreal.MinimalViewInfo.calculate_projection_matrix"></a>

#### calculate_projection_matrix

```python
def calculate_projection_matrix() -> Matrix
```

x.calculate_projection_matrix() -> Matrix
Calculates the projection matrix using this view info's aspect ratio (regardless of bConstrainAspectRatio)

Returns:
    Matrix:

<a id="unreal.FractureEffect"></a>