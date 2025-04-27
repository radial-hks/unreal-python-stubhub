## SceneCaptureComponent2D Objects

```python
class SceneCaptureComponent2D(SceneCaptureComponent)
```

Used to capture a 'snapshot' of the scene from a single plane and feed it to a render target.

**C++ Source:**

- **Module**: Engine
- **File**: SceneCaptureComponent2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``always_persist_rendering_state`` (bool):  [Read-Write] Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed.
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_calculate_ortho_planes`` (bool):  [Read-Write] Automatically determine a min/max Near/Far clip plane position depending on OrthoWidth value
- ``auto_plane_shift`` (float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane
- ``camera_cut_this_frame`` (bool):  [Read-Write] True if we did a camera cut this frame. Automatically reset to false at every capture.
  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).
  Similar to UPlayerCameraManager::bGameCameraCutThisFrame.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``capture_every_frame`` (bool):  [Read-Write] Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved.
- ``capture_gpu_next_render`` (bool):  [Read-Write] Capture a GPU frame for this scene capture, next time it renders (capture program must be connected).
- ``capture_on_movement`` (bool):  [Read-Write] Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint.
- ``capture_sort_priority`` (int32):  [Read-Write] Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first.
- ``capture_source`` (SceneCaptureSource):  [Read-Write]
- ``clip_plane_base`` (Vector):  [Read-Write] Base position for the clip plane, can be any position on the plane.
- ``clip_plane_normal`` (Vector):  [Read-Write] Normal for the plane.
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``composite_mode`` (SceneCaptureCompositeMode):  [Read-Write] When enabled, the scene capture will composite into the render target instead of overwriting its contents.
- ``consider_unrendered_opaque_pixel_as_fully_translucent`` (bool):  [Read-Write] Whether to only render exponential height fog on opaque pixels which were rendered by the scene capture.
- ``custom_near_clipping_plane`` (float):  [Read-Write] Set bOverride_CustomNearClippingPlane to true if you want to use a custom clipping plane instead of GNearClippingPlane.
- ``custom_projection_matrix`` (Matrix):  [Read-Write] The custom projection matrix to use
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``dump_gpu_next_render`` (bool):  [Read-Write] Run DumpGPU for this scene capture, next time it renders.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_clip_plane`` (bool):  [Read-Write] Enables a clip plane while rendering the scene capture which is useful for portals.
  The global clip plane must be enabled in the renderer project settings for this to work.
- ``enable_orthographic_tiling`` (bool):  [Read-Write] Render the scene in n frames (i.e TileCount) - Ignored in Perspective mode, works only in Orthographic mode when CaptureSource uses SceneColor (not FinalColor)
  If CaptureSource uses FinalColor, tiling will be ignored and a Warning message will be logged
- ``fov_angle`` (float):  [Read-Write] Camera field of view (in degrees).
- ``hidden_actors`` (Array[Actor]):  [Read-Write] The actors to hide in the scene capture.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``ignore_screen_percentage`` (bool):  [Read-Write] When rendering with main view resolution, ignore screen percentage scale and render at full resolution.  Temporal AA jitter is also disabled.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``lod_distance_factor`` (float):  [Read-Write] Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass.
- ``main_view_camera`` (bool):  [Read-Write] Render with main view camera.  Enables Main View Family and Resolution.  Temporal AA jitter is matched with main view.
- ``main_view_family`` (bool):  [Read-Write] Render with main view family (where bIsMainViewFamily == true)
- ``main_view_resolution`` (bool):  [Read-Write] Render with main view resolution, ignoring the dimensions in the resource.  Enables Main View Family.
- ``main_view_resolution_divisor`` (IntPoint):  [Read-Write] Divisor when rendering at Main View Resolution.
- ``max_view_distance_override`` (float):  [Read-Write] if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``num_x_tiles`` (int32):  [Read-Write] Number of X tiles to render. Ignored in Perspective mode, works only in Orthographic mode
- ``num_y_tiles`` (int32):  [Read-Write] Number of Y tiles to render. Ignored in Perspective mode, works only in Orthographic mode
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``ortho_width`` (float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)
- ``override_custom_near_clipping_plane`` (bool):  [Read-Write]
- ``overscan`` (float):  [Read-Write] Amount to increase the view frustum by, from 0.0 for no increase to 1.0 for 100% increase
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``post_process_blend_weight`` (float):  [Read-Write] Range (0.0, 1.0) where 0 indicates no effect, 1 indicates full effect.
- ``post_process_settings`` (PostProcessSettings):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``primitive_render_mode`` (SceneCapturePrimitiveRenderMode):  [Read-Write] Controls what primitives get rendered into the scene capture.
- ``profiling_event_name`` (str):  [Read-Write] Name of the profiling event.
- ``projection_type`` (CameraProjectionMode):  [Read-Write]
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``render_in_main_renderer`` (bool):  [Read-Write] Render scene capture as additional render passes of the main renderer rather than as an independent renderer. Applies to scene depth, device depth, base color, and normal modes.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``show_flag_settings`` (Array[EngineShowFlagsSetting]):  [Read-Write]
- ``show_only_actors`` (Array[Actor]):  [Read-Write] The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList.
- ``texture_target`` (TextureRenderTarget2D):  [Read-Write] Output render target of the scene capture that can be read in materials.
- ``update_ortho_planes`` (bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_camera_height_as_view_target`` (bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)
- ``use_custom_projection_matrix`` (bool):  [Read-Write] Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling
- ``use_faux_ortho_view_pos`` (bool):  [Read-Write]
  deprecated: 5.4 - bUseFauxOrthoViewPos has been deprecated alongside updates to Orthographic camera fixes
- ``use_ray_tracing_if_enabled`` (bool):  [Read-Write] Whether to use ray tracing for this capture. Ray Tracing must be enabled in the project.
- ``user_scene_texture_base_color`` (Name):  [Read-Write] Expose BaseColor as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.
- ``user_scene_texture_normal`` (Name):  [Read-Write] Expose Normal as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.
- ``user_scene_texture_scene_color`` (Name):  [Read-Write] Expose SceneColor (emissive/unlit) as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SceneCaptureComponent2D.projection_type"></a>

#### projection_type

```python
@property
def projection_type() -> CameraProjectionMode
```

(CameraProjectionMode):  [Read-Write]

<a id="unreal.SceneCaptureComponent2D.projection_type"></a>

#### projection_type

```python
@projection_type.setter
def projection_type(value: CameraProjectionMode) -> None
```

<a id="unreal.SceneCaptureComponent2D.fov_angle"></a>

#### fov_angle

```python
@property
def fov_angle() -> float
```

(float):  [Read-Write] Camera field of view (in degrees).

<a id="unreal.SceneCaptureComponent2D.fov_angle"></a>

#### fov_angle

```python
@fov_angle.setter
def fov_angle(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.ortho_width"></a>

#### ortho_width

```python
@property
def ortho_width() -> float
```

(float):  [Read-Write] The desired width (in world units) of the orthographic view (ignored in Perspective mode)

<a id="unreal.SceneCaptureComponent2D.ortho_width"></a>

#### ortho_width

```python
@ortho_width.setter
def ortho_width(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@property
def auto_calculate_ortho_planes() -> bool
```

(bool):  [Read-Write] Automatically determine a min/max Near/Far clip plane position depending on OrthoWidth value

<a id="unreal.SceneCaptureComponent2D.auto_calculate_ortho_planes"></a>

#### auto_calculate_ortho_planes

```python
@auto_calculate_ortho_planes.setter
def auto_calculate_ortho_planes(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.auto_plane_shift"></a>

#### auto_plane_shift

```python
@property
def auto_plane_shift() -> float
```

(float):  [Read-Write] Manually adjusts the planes of this camera, maintaining the distance between them. Positive moves out to the farplane, negative towards the near plane

<a id="unreal.SceneCaptureComponent2D.auto_plane_shift"></a>

#### auto_plane_shift

```python
@auto_plane_shift.setter
def auto_plane_shift(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.update_ortho_planes"></a>

#### update_ortho_planes

```python
@property
def update_ortho_planes() -> bool
```

(bool):  [Read-Write] Adjusts the near/far planes and the view origin of the current camera automatically to avoid clipping and light artefacting

<a id="unreal.SceneCaptureComponent2D.update_ortho_planes"></a>

#### update_ortho_planes

```python
@update_ortho_planes.setter
def update_ortho_planes(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@property
def use_camera_height_as_view_target() -> bool
```

(bool):  [Read-Write] If UpdateOrthoPlanes is enabled, this setting will use the cameras current height to compensate the distance to the general view (as a pseudo distance to view target when one isn't present)

<a id="unreal.SceneCaptureComponent2D.use_camera_height_as_view_target"></a>

#### use_camera_height_as_view_target

```python
@use_camera_height_as_view_target.setter
def use_camera_height_as_view_target(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.overscan"></a>

#### overscan

```python
@property
def overscan() -> float
```

(float):  [Read-Write] Amount to increase the view frustum by, from 0.0 for no increase to 1.0 for 100% increase

<a id="unreal.SceneCaptureComponent2D.overscan"></a>

#### overscan

```python
@overscan.setter
def overscan(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.texture_target"></a>

#### texture_target

```python
@property
def texture_target() -> TextureRenderTarget2D
```

(TextureRenderTarget2D):  [Read-Write] Output render target of the scene capture that can be read in materials.

<a id="unreal.SceneCaptureComponent2D.texture_target"></a>

#### texture_target

```python
@texture_target.setter
def texture_target(value: TextureRenderTarget2D) -> None
```

<a id="unreal.SceneCaptureComponent2D.composite_mode"></a>

#### composite_mode

```python
@property
def composite_mode() -> SceneCaptureCompositeMode
```

(SceneCaptureCompositeMode):  [Read-Write] When enabled, the scene capture will composite into the render target instead of overwriting its contents.

<a id="unreal.SceneCaptureComponent2D.composite_mode"></a>

#### composite_mode

```python
@composite_mode.setter
def composite_mode(value: SceneCaptureCompositeMode) -> None
```

<a id="unreal.SceneCaptureComponent2D.post_process_settings"></a>

#### post_process_settings

```python
@property
def post_process_settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write]

<a id="unreal.SceneCaptureComponent2D.post_process_settings"></a>

#### post_process_settings

```python
@post_process_settings.setter
def post_process_settings(value: PostProcessSettings) -> None
```

<a id="unreal.SceneCaptureComponent2D.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@property
def post_process_blend_weight() -> float
```

(float):  [Read-Write] Range (0.0, 1.0) where 0 indicates no effect, 1 indicates full effect.

<a id="unreal.SceneCaptureComponent2D.post_process_blend_weight"></a>

#### post_process_blend_weight

```python
@post_process_blend_weight.setter
def post_process_blend_weight(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.override_custom_near_clipping_plane"></a>

#### override_custom_near_clipping_plane

```python
@property
def override_custom_near_clipping_plane() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SceneCaptureComponent2D.override_custom_near_clipping_plane"></a>

#### override_custom_near_clipping_plane

```python
@override_custom_near_clipping_plane.setter
def override_custom_near_clipping_plane(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.custom_near_clipping_plane"></a>

#### custom_near_clipping_plane

```python
@property
def custom_near_clipping_plane() -> float
```

(float):  [Read-Write] Set bOverride_CustomNearClippingPlane to true if you want to use a custom clipping plane instead of GNearClippingPlane.

<a id="unreal.SceneCaptureComponent2D.custom_near_clipping_plane"></a>

#### custom_near_clipping_plane

```python
@custom_near_clipping_plane.setter
def custom_near_clipping_plane(value: float) -> None
```

<a id="unreal.SceneCaptureComponent2D.use_custom_projection_matrix"></a>

#### use_custom_projection_matrix

```python
@property
def use_custom_projection_matrix() -> bool
```

(bool):  [Read-Write] Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling

<a id="unreal.SceneCaptureComponent2D.use_custom_projection_matrix"></a>

#### use_custom_projection_matrix

```python
@use_custom_projection_matrix.setter
def use_custom_projection_matrix(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.custom_projection_matrix"></a>

#### custom_projection_matrix

```python
@property
def custom_projection_matrix() -> Matrix
```

(Matrix):  [Read-Write] The custom projection matrix to use

<a id="unreal.SceneCaptureComponent2D.custom_projection_matrix"></a>

#### custom_projection_matrix

```python
@custom_projection_matrix.setter
def custom_projection_matrix(value: Matrix) -> None
```

<a id="unreal.SceneCaptureComponent2D.use_faux_ortho_view_pos"></a>

#### use_faux_ortho_view_pos

```python
@property
def use_faux_ortho_view_pos() -> bool
```

(bool):  [Read-Write]
deprecated: 5.4 - bUseFauxOrthoViewPos has been deprecated alongside updates to Orthographic camera fixes

<a id="unreal.SceneCaptureComponent2D.use_faux_ortho_view_pos"></a>

#### use_faux_ortho_view_pos

```python
@use_faux_ortho_view_pos.setter
def use_faux_ortho_view_pos(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.enable_orthographic_tiling"></a>

#### enable_orthographic_tiling

```python
@property
def enable_orthographic_tiling() -> bool
```

(bool):  [Read-Write] Render the scene in n frames (i.e TileCount) - Ignored in Perspective mode, works only in Orthographic mode when CaptureSource uses SceneColor (not FinalColor)
If CaptureSource uses FinalColor, tiling will be ignored and a Warning message will be logged

<a id="unreal.SceneCaptureComponent2D.enable_orthographic_tiling"></a>

#### enable_orthographic_tiling

```python
@enable_orthographic_tiling.setter
def enable_orthographic_tiling(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.num_x_tiles"></a>

#### num_x_tiles

```python
@property
def num_x_tiles() -> int
```

(int32):  [Read-Write] Number of X tiles to render. Ignored in Perspective mode, works only in Orthographic mode

<a id="unreal.SceneCaptureComponent2D.num_x_tiles"></a>

#### num_x_tiles

```python
@num_x_tiles.setter
def num_x_tiles(value: int) -> None
```

<a id="unreal.SceneCaptureComponent2D.num_y_tiles"></a>

#### num_y_tiles

```python
@property
def num_y_tiles() -> int
```

(int32):  [Read-Write] Number of Y tiles to render. Ignored in Perspective mode, works only in Orthographic mode

<a id="unreal.SceneCaptureComponent2D.num_y_tiles"></a>

#### num_y_tiles

```python
@num_y_tiles.setter
def num_y_tiles(value: int) -> None
```

<a id="unreal.SceneCaptureComponent2D.enable_clip_plane"></a>

#### enable_clip_plane

```python
@property
def enable_clip_plane() -> bool
```

(bool):  [Read-Write] Enables a clip plane while rendering the scene capture which is useful for portals.
The global clip plane must be enabled in the renderer project settings for this to work.

<a id="unreal.SceneCaptureComponent2D.enable_clip_plane"></a>

#### enable_clip_plane

```python
@enable_clip_plane.setter
def enable_clip_plane(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.clip_plane_base"></a>

#### clip_plane_base

```python
@property
def clip_plane_base() -> Vector
```

(Vector):  [Read-Write] Base position for the clip plane, can be any position on the plane.

<a id="unreal.SceneCaptureComponent2D.clip_plane_base"></a>

#### clip_plane_base

```python
@clip_plane_base.setter
def clip_plane_base(value: Vector) -> None
```

<a id="unreal.SceneCaptureComponent2D.clip_plane_normal"></a>

#### clip_plane_normal

```python
@property
def clip_plane_normal() -> Vector
```

(Vector):  [Read-Write] Normal for the plane.

<a id="unreal.SceneCaptureComponent2D.clip_plane_normal"></a>

#### clip_plane_normal

```python
@clip_plane_normal.setter
def clip_plane_normal(value: Vector) -> None
```

<a id="unreal.SceneCaptureComponent2D.render_in_main_renderer"></a>

#### render_in_main_renderer

```python
@property
def render_in_main_renderer() -> bool
```

(bool):  [Read-Write] Render scene capture as additional render passes of the main renderer rather than as an independent renderer. Applies to scene depth, device depth, base color, and normal modes.

<a id="unreal.SceneCaptureComponent2D.render_in_main_renderer"></a>

#### render_in_main_renderer

```python
@render_in_main_renderer.setter
def render_in_main_renderer(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.camera_cut_this_frame"></a>

#### camera_cut_this_frame

```python
@property
def camera_cut_this_frame() -> bool
```

(bool):  [Read-Write] True if we did a camera cut this frame. Automatically reset to false at every capture.
This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).
Similar to UPlayerCameraManager::bGameCameraCutThisFrame.

<a id="unreal.SceneCaptureComponent2D.camera_cut_this_frame"></a>

#### camera_cut_this_frame

```python
@camera_cut_this_frame.setter
def camera_cut_this_frame(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.consider_unrendered_opaque_pixel_as_fully_translucent"></a>

#### consider_unrendered_opaque_pixel_as_fully_translucent

```python
@property
def consider_unrendered_opaque_pixel_as_fully_translucent() -> bool
```

(bool):  [Read-Write] Whether to only render exponential height fog on opaque pixels which were rendered by the scene capture.

<a id="unreal.SceneCaptureComponent2D.consider_unrendered_opaque_pixel_as_fully_translucent"></a>

#### consider_unrendered_opaque_pixel_as_fully_translucent

```python
@consider_unrendered_opaque_pixel_as_fully_translucent.setter
def consider_unrendered_opaque_pixel_as_fully_translucent(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.main_view_family"></a>

#### main_view_family

```python
@property
def main_view_family() -> bool
```

(bool):  [Read-Write] Render with main view family (where bIsMainViewFamily == true)

<a id="unreal.SceneCaptureComponent2D.main_view_family"></a>

#### main_view_family

```python
@main_view_family.setter
def main_view_family(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.main_view_resolution"></a>

#### main_view_resolution

```python
@property
def main_view_resolution() -> bool
```

(bool):  [Read-Write] Render with main view resolution, ignoring the dimensions in the resource.  Enables Main View Family.

<a id="unreal.SceneCaptureComponent2D.main_view_resolution"></a>

#### main_view_resolution

```python
@main_view_resolution.setter
def main_view_resolution(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.main_view_camera"></a>

#### main_view_camera

```python
@property
def main_view_camera() -> bool
```

(bool):  [Read-Write] Render with main view camera.  Enables Main View Family and Resolution.  Temporal AA jitter is matched with main view.

<a id="unreal.SceneCaptureComponent2D.main_view_camera"></a>

#### main_view_camera

```python
@main_view_camera.setter
def main_view_camera(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.ignore_screen_percentage"></a>

#### ignore_screen_percentage

```python
@property
def ignore_screen_percentage() -> bool
```

(bool):  [Read-Write] When rendering with main view resolution, ignore screen percentage scale and render at full resolution.  Temporal AA jitter is also disabled.

<a id="unreal.SceneCaptureComponent2D.ignore_screen_percentage"></a>

#### ignore_screen_percentage

```python
@ignore_screen_percentage.setter
def ignore_screen_percentage(value: bool) -> None
```

<a id="unreal.SceneCaptureComponent2D.main_view_resolution_divisor"></a>

#### main_view_resolution_divisor

```python
@property
def main_view_resolution_divisor() -> IntPoint
```

(IntPoint):  [Read-Write] Divisor when rendering at Main View Resolution.

<a id="unreal.SceneCaptureComponent2D.main_view_resolution_divisor"></a>

#### main_view_resolution_divisor

```python
@main_view_resolution_divisor.setter
def main_view_resolution_divisor(value: IntPoint) -> None
```

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_base_color"></a>

#### user_scene_texture_base_color

```python
@property
def user_scene_texture_base_color() -> Name
```

(Name):  [Read-Write] Expose BaseColor as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_base_color"></a>

#### user_scene_texture_base_color

```python
@user_scene_texture_base_color.setter
def user_scene_texture_base_color(value: Name) -> None
```

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_normal"></a>

#### user_scene_texture_normal

```python
@property
def user_scene_texture_normal() -> Name
```

(Name):  [Read-Write] Expose Normal as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_normal"></a>

#### user_scene_texture_normal

```python
@user_scene_texture_normal.setter
def user_scene_texture_normal(value: Name) -> None
```

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_scene_color"></a>

#### user_scene_texture_scene_color

```python
@property
def user_scene_texture_scene_color() -> Name
```

(Name):  [Read-Write] Expose SceneColor (emissive/unlit) as a UserSceneTexture.  Requires "Render In Main Renderer".  Enables Main View Family and Resolution, disables "Ignore Screen Percentage".  Useful to get multiple outputs from a Custom Render Pass.

<a id="unreal.SceneCaptureComponent2D.user_scene_texture_scene_color"></a>

#### user_scene_texture_scene_color

```python
@user_scene_texture_scene_color.setter
def user_scene_texture_scene_color(value: Name) -> None
```

<a id="unreal.SceneCaptureComponent2D.remove_blendable"></a>

#### remove_blendable

```python
def remove_blendable(blendable_object: BlendableInterface) -> None
```

x.remove_blendable(blendable_object) -> None
Removes a blendable.

Args:
    blendable_object (BlendableInterface):

<a id="unreal.SceneCaptureComponent2D.capture_scene"></a>

#### capture_scene

```python
def capture_scene() -> None
```

x.capture_scene() -> None
Render the scene to the texture target immediately.
This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.
If r.SceneCapture.CullByDetailMode is set, nothing will happen if DetailMode is higher than r.DetailMode.

<a id="unreal.SceneCaptureComponent2D.update_content"></a>

#### update_content

```python
def update_content() -> None
```

deprecated: 'update_content' was renamed to 'capture_scene'.

<a id="unreal.SceneCaptureComponent2D.add_or_update_blendable"></a>

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

<a id="unreal.SceneCaptureComponentCube"></a>