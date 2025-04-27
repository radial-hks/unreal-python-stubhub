## CameraComponent Objects

```python
class CameraComponent(SceneComponent)
```

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

**C++ Source:**

- **Module**: Engine
- **File**: CameraComponent.h

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
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``draw_frustum_allowed`` (bool):  [Read-Write] The Frustum visibility flag for draw frustum component initialization
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_first_person_field_of_view`` (bool):  [Read-Write] True if the first person field of view should be used for primitives tagged as "IsFirstPerson".
- ``enable_first_person_scale`` (bool):  [Read-Write] True if the first person scale should be used for primitives tagged as "IsFirstPerson".
- ``field_of_view`` (float):  [Read-Write] The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode)

  If the aspect ratio axis constraint (from ULocalPlayer, ALevelSequenceActor, etc.) is set to maintain vertical FOV, the AspectRatio
  property will be used to convert this property's value to a vertical FOV.
- ``first_person_field_of_view`` (float):  [Read-Write] The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson".
- ``first_person_scale`` (float):  [Read-Write] The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lock_to_hmd`` (bool):  [Read-Write] True if the camera's orientation and position should be locked to the HMD
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``ortho_far_clip_plane`` (float):  [Read-Write] The far plane distance of the orthographic view (in world units)
- ``ortho_near_clip_plane`` (float):  [Read-Write] The near plane distance of the orthographic view (in world units)
- ``ortho_width`` (float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)
- ``override_aspect_ratio_axis_constraint`` (bool):  [Read-Write] Whether to override the default aspect ratio axis constraint defined on the local player
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

<a id="unreal.CameraComponent.field_of_view"></a>

#### field_of_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write] The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode)

If the aspect ratio axis constraint (from ULocalPlayer, ALevelSequenceActor, etc.) is set to maintain vertical FOV, the AspectRatio
property will be used to convert this property's value to a vertical FOV.

<a id="unreal.CameraComponent.field_of_view"></a>

#### field_of_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.CameraComponent.first_person_field_of_view"></a>

#### first_person_field_of_view

```python
@property
def first_person_field_of_view() -> float
```

(float):  [Read-Write] The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson".

<a id="unreal.CameraComponent.first_person_field_of_view"></a>

#### first_person_field_of_view

```python
@first_person_field_of_view.setter
def first_person_field_of_view(value: float) -> None
```

<a id="unreal.CameraComponent.first_person_scale"></a>

#### first_person_scale

```python
@property
def first_person_scale() -> float
```

(float):  [Read-Write] The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene.

<a id="unreal.CameraComponent.first_person_scale"></a>

#### first_person_scale

```python
@first_person_scale.setter
def first_person_scale(value: float) -> None
```

<a id="unreal.CameraComponent.ortho_width"></a>

#### ortho_width

```python
@property
def ortho_width() -> float
```

(float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)

<a id="unreal.CameraComponent.ortho_width"></a>

#### ortho_width

```python
@ortho_width.setter
def ortho_width(value: float) -> None
```

<a id="unreal.CameraComponent.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@property
def auto_calculate_ortho_planes() -> bool
```

(bool):  [Read-Write] Automatically determine a min/max Near/Far clip plane position depending on OrthoWidth value

<a id="unreal.CameraComponent.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@auto_calculate_ortho_planes.setter
def auto_calculate_ortho_planes(value: bool) -> None
```

<a id="unreal.CameraComponent.auto_plane_shift"></a>

#### auto_plane_shift

```python
@property
def auto_plane_shift() -> float
```

(float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane

<a id="unreal.CameraComponent.auto_plane_shift"></a>

#### auto_plane_shift

```python
@auto_plane_shift.setter
def auto_plane_shift(value: float) -> None
```

<a id="unreal.CameraComponent.ortho_near_clip_plane"></a>

#### ortho_near_clip_plane

```python
@property
def ortho_near_clip_plane() -> float
```

(float):  [Read-Write] The near plane distance of the orthographic view (in world units)

<a id="unreal.CameraComponent.ortho_near_clip_plane"></a>

#### ortho_near_clip_plane

```python
@ortho_near_clip_plane.setter
def ortho_near_clip_plane(value: float) -> None
```

<a id="unreal.CameraComponent.ortho_far_clip_plane"></a>

#### ortho_far_clip_plane

```python
@property
def ortho_far_clip_plane() -> float
```

(float):  [Read-Write] The far plane distance of the orthographic view (in world units)

<a id="unreal.CameraComponent.ortho_far_clip_plane"></a>

#### ortho_far_clip_plane

```python
@ortho_far_clip_plane.setter
def ortho_far_clip_plane(value: float) -> None
```

<a id="unreal.CameraComponent.update_ortho_planes"></a>

#### update_ortho_planes

```python
@property
def update_ortho_planes() -> bool
```

(bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting

<a id="unreal.CameraComponent.update_ortho_planes"></a>

#### update_ortho_planes

```python
@update_ortho_planes.setter
def update_ortho_planes(value: bool) -> None
```

<a id="unreal.CameraComponent.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@property
def use_camera_height_as_view_target() -> bool
```

(bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)

<a id="unreal.CameraComponent.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@use_camera_height_as_view_target.setter
def use_camera_height_as_view_target(value: bool) -> None
```

<a id="unreal.CameraComponent.aspect_ratio"></a>

#### aspect_ratio

```python
@property
def aspect_ratio() -> float
```

(float):  [Read-Write] Aspect Ratio (Width/Height)

<a id="unreal.CameraComponent.aspect_ratio"></a>

#### aspect_ratio

```python
@aspect_ratio.setter
def aspect_ratio(value: float) -> None
```

<a id="unreal.CameraComponent.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@property
def aspect_ratio_axis_constraint() -> AspectRatioAxisConstraint
```

(AspectRatioAxisConstraint):  [Read-Write] Override for the default aspect ratio axis constraint defined on the local player

<a id="unreal.CameraComponent.aspect_ratio_axis_constraint"></a>

#### aspect_ratio_axis_constraint

```python
@aspect_ratio_axis_constraint.setter
def aspect_ratio_axis_constraint(value: AspectRatioAxisConstraint) -> None
```

<a id="unreal.CameraComponent.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@property
def constrain_aspect_ratio() -> bool
```

(bool):  [Read-Write] If bConstrainAspectRatio is true, black bars will be added if the destination view has a different aspect ratio than this camera requested.

<a id="unreal.CameraComponent.constrain_aspect_ratio"></a>

#### constrain_aspect_ratio

```python
@constrain_aspect_ratio.setter
def constrain_aspect_ratio(value: bool) -> None
```

<a id="unreal.CameraComponent.override_aspect_ratio_axis_constraint"></a>

#### override_aspect_ratio_axis_constraint

```python
@property
def override_aspect_ratio_axis_constraint() -> bool
```

(bool):  [Read-Write] Whether to override the default aspect ratio axis constraint defined on the local player

<a id="unreal.CameraComponent.override_aspect_ratio_axis_constraint"></a>

#### override_aspect_ratio_axis_constraint

```python
@override_aspect_ratio_axis_constraint.setter
def override_aspect_ratio_axis_constraint(value: bool) -> None
```

<a id="unreal.CameraComponent.use_field_of_view_for_lod"></a>

#### use_field_of_view_for_lod

```python
@property
def use_field_of_view_for_lod() -> bool
```

(bool):  [Read-Write] If true, account for the field of view angle when computing which level of detail to use for meshes.

<a id="unreal.CameraComponent.use_field_of_view_for_lod"></a>

#### use_field_of_view_for_lod

```python
@use_field_of_view_for_lod.setter
def use_field_of_view_for_lod(value: bool) -> None
```

<a id="unreal.CameraComponent.overscan"></a>

#### overscan

```python
@property
def overscan() -> float
```

(float):  [Read-Write] Amount to increase the view frustum by, from 0.0 for no increase to 1.0 for 100% increase

<a id="unreal.CameraComponent.overscan"></a>

#### overscan

```python
@overscan.setter
def overscan(value: float) -> None
```

<a id="unreal.CameraComponent.scale_resolution_with_overscan"></a>

#### scale_resolution_with_overscan

```python
@property
def scale_resolution_with_overscan() -> bool
```

(bool):  [Read-Write] Indicates that the resolution should be scaled by the overscan amount so that the original view frustum remains the same resolution.
Note that when enabled, increasing overscan will result in increased rendering workload, potentially decreasing performance as resolution increases

<a id="unreal.CameraComponent.scale_resolution_with_overscan"></a>

#### scale_resolution_with_overscan

```python
@scale_resolution_with_overscan.setter
def scale_resolution_with_overscan(value: bool) -> None
```

<a id="unreal.CameraComponent.crop_overscan"></a>

#### crop_overscan

```python
@property
def crop_overscan() -> bool
```

(bool):  [Read-Write] Indicates that the overscanned pixels should be cropped at the end of the rendering pipeline, allowing the overscanned pixels to be used in post process effects
that need extra pixels beyond the view frustum (e.g. lens distortion) without having to render those pixels to the screen. When bScaleResolutionWithOverscan is enabled,
the cropped image will have the same resolution as the original non-overscanned image, but when disabled, the cropped image will be a lower resolution.

<a id="unreal.CameraComponent.crop_overscan"></a>

#### crop_overscan

```python
@crop_overscan.setter
def crop_overscan(value: bool) -> None
```

<a id="unreal.CameraComponent.draw_frustum_allowed"></a>

#### draw_frustum_allowed

```python
@property
def draw_frustum_allowed() -> bool
```

(bool):  [Read-Write] The Frustum visibility flag for draw frustum component initialization

<a id="unreal.CameraComponent.draw_frustum_allowed"></a>

#### draw_frustum_allowed

```python
@draw_frustum_allowed.setter
def draw_frustum_allowed(value: bool) -> None
```

<a id="unreal.CameraComponent.camera_mesh_hidden_in_game"></a>

#### camera_mesh_hidden_in_game

```python
@property
def camera_mesh_hidden_in_game() -> bool
```

(bool):  [Read-Write] If the camera mesh is visible in game. Only relevant when running editor builds.

<a id="unreal.CameraComponent.camera_mesh_hidden_in_game"></a>

#### camera_mesh_hidden_in_game

```python
@camera_mesh_hidden_in_game.setter
def camera_mesh_hidden_in_game(value: bool) -> None
```

<a id="unreal.CameraComponent.lock_to_hmd"></a>

#### lock_to_hmd

```python
@property
def lock_to_hmd() -> bool
```

(bool):  [Read-Write] True if the camera's orientation and position should be locked to the HMD

<a id="unreal.CameraComponent.lock_to_hmd"></a>

#### lock_to_hmd

```python
@lock_to_hmd.setter
def lock_to_hmd(value: bool) -> None
```

<a id="unreal.CameraComponent.use_pawn_control_rotation"></a>

#### use_pawn_control_rotation

```python
@property
def use_pawn_control_rotation() -> bool
```

(bool):  [Read-Write] If this camera component is placed on a pawn, should it use the view/control rotation of the pawn where possible?
see: APawn::GetViewRotation()

<a id="unreal.CameraComponent.use_pawn_control_rotation"></a>

#### use_pawn_control_rotation

```python
@use_pawn_control_rotation.setter
def use_pawn_control_rotation(value: bool) -> None
```

<a id="unreal.CameraComponent.b_use_controller_view_rotation"></a>

#### b_use_controller_view_rotation

```python
@property
def b_use_controller_view_rotation() -> bool
```

deprecated: 'b_use_controller_view_rotation' was renamed to 'use_pawn_control_rotation'.

<a id="unreal.CameraComponent.b_use_controller_view_rotation"></a>

#### b_use_controller_view_rotation

```python
@b_use_controller_view_rotation.setter
def b_use_controller_view_rotation(value: bool) -> None
```

<a id="unreal.CameraComponent.b_use_pawn_view_rotation"></a>

#### b_use_pawn_view_rotation

```python
@property
def b_use_pawn_view_rotation() -> bool
```

deprecated: 'b_use_pawn_view_rotation' was renamed to 'use_pawn_control_rotation'.

<a id="unreal.CameraComponent.b_use_pawn_view_rotation"></a>

#### b_use_pawn_view_rotation

```python
@b_use_pawn_view_rotation.setter
def b_use_pawn_view_rotation(value: bool) -> None
```

<a id="unreal.CameraComponent.enable_first_person_field_of_view"></a>

#### enable_first_person_field_of_view

```python
@property
def enable_first_person_field_of_view() -> bool
```

(bool):  [Read-Write] True if the first person field of view should be used for primitives tagged as "IsFirstPerson".

<a id="unreal.CameraComponent.enable_first_person_field_of_view"></a>

#### enable_first_person_field_of_view

```python
@enable_first_person_field_of_view.setter
def enable_first_person_field_of_view(value: bool) -> None
```

<a id="unreal.CameraComponent.enable_first_person_scale"></a>

#### enable_first_person_scale

```python
@property
def enable_first_person_scale() -> bool
```

(bool):  [Read-Write] True if the first person scale should be used for primitives tagged as "IsFirstPerson".

<a id="unreal.CameraComponent.enable_first_person_scale"></a>

#### enable_first_person_scale

```python
@enable_first_person_scale.setter
def enable_first_person_scale(value: bool) -> None
```

<a id="unreal.CameraComponent.projection_mode"></a>

#### projection_mode

```python
@property
def projection_mode() -> CameraProjectionMode
```

(CameraProjectionMode):  [Read-Write] The type of camera

<a id="unreal.CameraComponent.projection_mode"></a>

#### projection_mode

```python
@projection_mode.setter
def projection_mode(value: CameraProjectionMode) -> None
```

<a id="unreal.CameraComponent.camera_mesh"></a>

#### camera_mesh

```python
@property
def camera_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.CameraComponent.camera_mesh"></a>

#### camera_mesh

```python
@camera_mesh.setter
def camera_mesh(value: StaticMesh) -> None
```

<a id="unreal.CameraComponent.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@property
def post_process_blend_weight() -> float
```

(float):  [Read-Write] Indicates if PostProcessSettings should be used when using this Camera to view through.

<a id="unreal.CameraComponent.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@post_process_blend_weight.setter
def post_process_blend_weight(value: float) -> None
```

<a id="unreal.CameraComponent.post_process_settings"></a>

#### post_process_settings

```python
@property
def post_process_settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write] Post process settings to use for this camera. Don't forget to check the properties you want to override

<a id="unreal.CameraComponent.post_process_settings"></a>

#### post_process_settings

```python
@post_process_settings.setter
def post_process_settings(value: PostProcessSettings) -> None
```

<a id="unreal.CameraComponent.set_use_field_of_view_for_lod"></a>

#### set_use_field_of_view_for_lod

```python
def set_use_field_of_view_for_lod(use_field_of_view_for_lod: bool) -> None
```

x.set_use_field_of_view_for_lod(use_field_of_view_for_lod) -> None
Set Use Field Of View for LOD

Args:
    use_field_of_view_for_lod (bool):

<a id="unreal.CameraComponent.set_use_camera_height_as_view_target"></a>

#### set_use_camera_height_as_view_target

```python
def set_use_camera_height_as_view_target(
        use_camera_height_as_view_target: bool) -> None
```

x.set_use_camera_height_as_view_target(use_camera_height_as_view_target) -> None
Set Use Camera Height as View Target

Args:
    use_camera_height_as_view_target (bool):

<a id="unreal.CameraComponent.set_update_ortho_planes"></a>

#### set_update_ortho_planes

```python
def set_update_ortho_planes(update_ortho_planes: bool) -> None
```

x.set_update_ortho_planes(update_ortho_planes) -> None
Set Update Ortho Planes

Args:
    update_ortho_planes (bool):

<a id="unreal.CameraComponent.set_scale_resolution_with_overscan"></a>

#### set_scale_resolution_with_overscan

```python
def set_scale_resolution_with_overscan(
        scale_resolution_with_overscan: bool) -> None
```

x.set_scale_resolution_with_overscan(scale_resolution_with_overscan) -> None
Sets whether to scale the resolution by the amount of overscan so that the original view frustum remains the same resolution.
Note that when enabled, increasing overscan will result in increased rendering workload, potentially decreasing performance as resolution increases

Args:
    scale_resolution_with_overscan (bool):

<a id="unreal.CameraComponent.set_projection_mode"></a>

#### set_projection_mode

```python
def set_projection_mode(projection_mode: CameraProjectionMode) -> None
```

x.set_projection_mode(projection_mode) -> None
Set Projection Mode

Args:
    projection_mode (CameraProjectionMode):

<a id="unreal.CameraComponent.set_post_process_blend_weight"></a>

#### set_post_process_blend_weight

```python
def set_post_process_blend_weight(post_process_blend_weight: float) -> None
```

x.set_post_process_blend_weight(post_process_blend_weight) -> None
Set Post Process Blend Weight

Args:
    post_process_blend_weight (float):

<a id="unreal.CameraComponent.set_overscan"></a>

#### set_overscan

```python
def set_overscan(overscan: float) -> None
```

x.set_overscan(overscan) -> None
Set Overscan

Args:
    overscan (float):

<a id="unreal.CameraComponent.set_ortho_width"></a>

#### set_ortho_width

```python
def set_ortho_width(ortho_width: float) -> None
```

x.set_ortho_width(ortho_width) -> None
Set Ortho Width

Args:
    ortho_width (float):

<a id="unreal.CameraComponent.set_ortho_near_clip_plane"></a>

#### set_ortho_near_clip_plane

```python
def set_ortho_near_clip_plane(ortho_near_clip_plane: float) -> None
```

x.set_ortho_near_clip_plane(ortho_near_clip_plane) -> None
Set Ortho Near Clip Plane

Args:
    ortho_near_clip_plane (float):

<a id="unreal.CameraComponent.set_ortho_far_clip_plane"></a>

#### set_ortho_far_clip_plane

```python
def set_ortho_far_clip_plane(ortho_far_clip_plane: float) -> None
```

x.set_ortho_far_clip_plane(ortho_far_clip_plane) -> None
Set Ortho Far Clip Plane

Args:
    ortho_far_clip_plane (float):

<a id="unreal.CameraComponent.set_first_person_scale"></a>

#### set_first_person_scale

```python
def set_first_person_scale(first_person_scale: float) -> None
```

x.set_first_person_scale(first_person_scale) -> None
Set First Person Scale

Args:
    first_person_scale (float):

<a id="unreal.CameraComponent.set_first_person_field_of_view"></a>

#### set_first_person_field_of_view

```python
def set_first_person_field_of_view(first_person_field_of_view: float) -> None
```

x.set_first_person_field_of_view(first_person_field_of_view) -> None
Set First Person Field Of View

Args:
    first_person_field_of_view (float):

<a id="unreal.CameraComponent.set_field_of_view"></a>

#### set_field_of_view

```python
def set_field_of_view(field_of_view: float) -> None
```

x.set_field_of_view(field_of_view) -> None
Set Field Of View

Args:
    field_of_view (float):

<a id="unreal.CameraComponent.set_enable_first_person_scale"></a>

#### set_enable_first_person_scale

```python
def set_enable_first_person_scale(enable_first_person_scale: bool) -> None
```

x.set_enable_first_person_scale(enable_first_person_scale) -> None
Set Enable First Person Scale

Args:
    enable_first_person_scale (bool):

<a id="unreal.CameraComponent.set_enable_first_person_field_of_view"></a>

#### set_enable_first_person_field_of_view

```python
def set_enable_first_person_field_of_view(
        enable_first_person_field_of_view: bool) -> None
```

x.set_enable_first_person_field_of_view(enable_first_person_field_of_view) -> None
Set Enable First Person Field Of View

Args:
    enable_first_person_field_of_view (bool):

<a id="unreal.CameraComponent.set_crop_overscan"></a>

#### set_crop_overscan

```python
def set_crop_overscan(crop_overscan: bool) -> None
```

x.set_crop_overscan(crop_overscan) -> None
Sets whether to crop the overscanned pixels at the end of the rendering pipeline, allowing the overscanned pixels to be used in post process effects
that need extra pixels beyond the view frustum (e.g. lens distortion) without having to render those pixels to the screen. When bScaleResolutionWithOverscan is enabled,
the cropped image will have the same resolution as the original non-overscanned image, but when disabled, the cropped image will be a lower resolution.

Args:
    crop_overscan (bool):

<a id="unreal.CameraComponent.set_constraint_aspect_ratio"></a>

#### set_constraint_aspect_ratio

```python
def set_constraint_aspect_ratio(constrain_aspect_ratio: bool) -> None
```

x.set_constraint_aspect_ratio(constrain_aspect_ratio) -> None
Set Constraint Aspect Ratio

Args:
    constrain_aspect_ratio (bool):

<a id="unreal.CameraComponent.set_auto_plane_shift"></a>

#### set_auto_plane_shift

```python
def set_auto_plane_shift(auto_plane_shift: float) -> None
```

x.set_auto_plane_shift(auto_plane_shift) -> None
Set Auto Plane Shift

Args:
    auto_plane_shift (float):

<a id="unreal.CameraComponent.set_auto_calculate_ortho_planes"></a>

#### set_auto_calculate_ortho_planes

```python
def set_auto_calculate_ortho_planes(auto_calculate: bool) -> None
```

x.set_auto_calculate_ortho_planes(auto_calculate) -> None
Set Auto Calculate Ortho Planes

Args:
    auto_calculate (bool):

<a id="unreal.CameraComponent.set_aspect_ratio_axis_constraint"></a>

#### set_aspect_ratio_axis_constraint

```python
def set_aspect_ratio_axis_constraint(
        aspect_ratio_axis_constraint: AspectRatioAxisConstraint) -> None
```

x.set_aspect_ratio_axis_constraint(aspect_ratio_axis_constraint) -> None
Set Aspect Ratio Axis Constraint

Args:
    aspect_ratio_axis_constraint (AspectRatioAxisConstraint):

<a id="unreal.CameraComponent.set_aspect_ratio"></a>

#### set_aspect_ratio

```python
def set_aspect_ratio(aspect_ratio: float) -> None
```

x.set_aspect_ratio(aspect_ratio) -> None
Set Aspect Ratio

Args:
    aspect_ratio (float):

<a id="unreal.CameraComponent.remove_blendable"></a>

#### remove_blendable

```python
def remove_blendable(blendable_object: BlendableInterface) -> None
```

x.remove_blendable(blendable_object) -> None
Removes a blendable.

Args:
    blendable_object (BlendableInterface):

<a id="unreal.CameraComponent.get_camera_view"></a>

#### get_camera_view

```python
def get_camera_view(delta_time: float) -> MinimalViewInfo
```

x.get_camera_view(delta_time) -> MinimalViewInfo
Returns camera's Point of View.
Called by Camera class. Subclass and postprocess to add any effects.

Args:
    delta_time (float): 

Returns:
    MinimalViewInfo: 

    desired_view (MinimalViewInfo):

<a id="unreal.CameraComponent.add_or_update_blendable"></a>

#### add_or_update_blendable

```python
def add_or_update_blendable(blendable_object: BlendableInterface,
                            weight: float = 1.000000) -> None
```

x.add_or_update_blendable(blendable_object, weight=1.000000) -> None
Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

Args:
    blendable_object (BlendableInterface): 
    weight (float):

<a id="unreal.CineCameraComponent"></a>