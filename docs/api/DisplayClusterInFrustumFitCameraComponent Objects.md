## DisplayClusterInFrustumFitCameraComponent Objects

```python
class DisplayClusterInFrustumFitCameraComponent(DisplayClusterCameraComponent)
```

3D point in space used to project the camera view onto a group of nDisplay viewports.
Support projection policies: mpcdi/pfm 2d/a3d, mesh.

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterWarp
- **File**: DisplayClusterInFrustumFitCameraComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``base_gizmo_scale`` (Vector):  [Read-Write] Base gizmo scale
- ``camera_projection_mode`` (DisplayClusterWarpCameraProjectionMode):  [Read-Write] Enable special rendering mode for all viewports using this viewpoint.
- ``camera_view_target`` (DisplayClusterWarpCameraViewTarget):  [Read-Write] Indicates which camera facing mode is used when frustum fitting the stage geometry
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_camera_projection`` (bool):  [Read-Write] Camera projection mode is used.
- ``enable_depth_of_field`` (bool):  [Read-Write] Enable the DoF PP settings from the specified camera.
- ``enable_gizmo`` (bool):  [Read-Write] Gizmo visibility
- ``enable_icvfx_color_grading`` (bool):  [Read-Write] Use the DC ColorGrading from the specified ICVFX camera.
- ``enable_icvfx_depth_of_field_compensation`` (bool):  [Read-Write] Use the DC Depth-Of-Field settings from the specified ICVFX camera.
- ``enable_icvfx_motion_blur`` (bool):  [Read-Write] Use the DC Motion Blur settings from the specified ICVFX camera.
- ``enable_near_clipping_plane`` (bool):  [Read-Write] Use the NearClippingPlane value from the specified cine camera.
- ``enable_post_process`` (bool):  [Read-Write] Use the PP settings from the specified camera.
- ``external_camera_actor`` (CineCameraActor):  [Read-Write]
  deprecated: Use the Camera from the UDisplayClusterCameraComponent instead
- ``external_cine_camera_actor`` (CineCameraActor):  [Read-Write] Use a specific actor camera instead of a game camera.
- ``gizmo_scale_multiplier`` (float):  [Read-Write] Gizmo scale multiplier
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``icvfx_camera_component_name`` (str):  [Read-Write] The name of the camera component that is used as the PP source.
- ``interpupillary_distance`` (float):  [Read-Write]
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
- ``show_preview_frustum_fit`` (bool):  [Read-Write] Show additional warped preview meshes before the camera.
- ``stereo_offset`` (DisplayClusterEyeStereoOffset):  [Read-Write]
- ``swap_eyes`` (bool):  [Read-Write]
- ``target_camera_type`` (DisplayClusterTargetCameraType):  [Read-Write] Type of source camera used.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_camera_postprocess`` (bool):  [Read-Write]
  deprecated: Use the bEnablePostProcess from the UDisplayClusterCameraComponent instead
- ``use_icvfx_camera_component_tracking`` (bool):  [Read-Write]
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.DisplayClusterInFrustumFitCameraComponent.external_camera_actor"></a>

#### external_camera_actor

```python
@property
def external_camera_actor() -> CineCameraActor
```

(CineCameraActor):  [Read-Write]
deprecated: Use the Camera from the UDisplayClusterCameraComponent instead

<a id="unreal.DisplayClusterInFrustumFitCameraComponent.external_camera_actor"></a>

#### external_camera_actor

```python
@external_camera_actor.setter
def external_camera_actor(value: CineCameraActor) -> None
```

<a id="unreal.DisplayClusterInFrustumFitCameraComponent.use_camera_postprocess"></a>

#### use_camera_postprocess

```python
@property
def use_camera_postprocess() -> bool
```

(bool):  [Read-Write]
deprecated: Use the bEnablePostProcess from the UDisplayClusterCameraComponent instead

<a id="unreal.DisplayClusterInFrustumFitCameraComponent.use_camera_postprocess"></a>

#### use_camera_postprocess

```python
@use_camera_postprocess.setter
def use_camera_postprocess(value: bool) -> None
```

<a id="unreal.DisplayClusterConfiguratorFactory"></a>