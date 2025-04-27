## DisplayClusterCameraComponent Objects

```python
class DisplayClusterCameraComponent(SceneComponent)
```

3D point in space used to render nDisplay viewports from

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: DisplayClusterCameraComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``base_gizmo_scale`` (Vector):  [Read-Write] Base gizmo scale
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enable_depth_of_field`` (bool):  [Read-Write] Enable the DoF PP settings from the specified camera.
- ``enable_gizmo`` (bool):  [Read-Write] Gizmo visibility
- ``enable_icvfx_color_grading`` (bool):  [Read-Write] Use the DC ColorGrading from the specified ICVFX camera.
- ``enable_icvfx_depth_of_field_compensation`` (bool):  [Read-Write] Use the DC Depth-Of-Field settings from the specified ICVFX camera.
- ``enable_icvfx_motion_blur`` (bool):  [Read-Write] Use the DC Motion Blur settings from the specified ICVFX camera.
- ``enable_near_clipping_plane`` (bool):  [Read-Write] Use the NearClippingPlane value from the specified cine camera.
- ``enable_post_process`` (bool):  [Read-Write] Use the PP settings from the specified camera.
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
- ``stereo_offset`` (DisplayClusterEyeStereoOffset):  [Read-Write]
- ``swap_eyes`` (bool):  [Read-Write]
- ``target_camera_type`` (DisplayClusterTargetCameraType):  [Read-Write] Type of source camera used.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``use_icvfx_camera_component_tracking`` (bool):  [Read-Write]
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.DisplayClusterCameraComponent.target_camera_type"></a>

#### target_camera_type

```python
@property
def target_camera_type() -> DisplayClusterTargetCameraType
```

(DisplayClusterTargetCameraType):  [Read-Write] Type of source camera used.

<a id="unreal.DisplayClusterCameraComponent.target_camera_type"></a>

#### target_camera_type

```python
@target_camera_type.setter
def target_camera_type(value: DisplayClusterTargetCameraType) -> None
```

<a id="unreal.DisplayClusterCameraComponent.icvfx_camera_component_name"></a>

#### icvfx_camera_component_name

```python
@property
def icvfx_camera_component_name() -> str
```

(str):  [Read-Write] The name of the camera component that is used as the PP source.

<a id="unreal.DisplayClusterCameraComponent.icvfx_camera_component_name"></a>

#### icvfx_camera_component_name

```python
@icvfx_camera_component_name.setter
def icvfx_camera_component_name(value: str) -> None
```

<a id="unreal.DisplayClusterCameraComponent.use_icvfx_camera_component_tracking"></a>

#### use_icvfx_camera_component_tracking

```python
@property
def use_icvfx_camera_component_tracking() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DisplayClusterCameraComponent.use_icvfx_camera_component_tracking"></a>

#### use_icvfx_camera_component_tracking

```python
@use_icvfx_camera_component_tracking.setter
def use_icvfx_camera_component_tracking(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.external_cine_camera_actor"></a>

#### external_cine_camera_actor

```python
@property
def external_cine_camera_actor() -> CineCameraActor
```

(CineCameraActor):  [Read-Write] Use a specific actor camera instead of a game camera.

<a id="unreal.DisplayClusterCameraComponent.external_cine_camera_actor"></a>

#### external_cine_camera_actor

```python
@external_cine_camera_actor.setter
def external_cine_camera_actor(value: CineCameraActor) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_post_process"></a>

#### enable_post_process

```python
@property
def enable_post_process() -> bool
```

(bool):  [Read-Write] Use the PP settings from the specified camera.

<a id="unreal.DisplayClusterCameraComponent.enable_post_process"></a>

#### enable_post_process

```python
@enable_post_process.setter
def enable_post_process(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_near_clipping_plane"></a>

#### enable_near_clipping_plane

```python
@property
def enable_near_clipping_plane() -> bool
```

(bool):  [Read-Write] Use the NearClippingPlane value from the specified cine camera.

<a id="unreal.DisplayClusterCameraComponent.enable_near_clipping_plane"></a>

#### enable_near_clipping_plane

```python
@enable_near_clipping_plane.setter
def enable_near_clipping_plane(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_depth_of_field"></a>

#### enable_depth_of_field

```python
@property
def enable_depth_of_field() -> bool
```

(bool):  [Read-Write] Enable the DoF PP settings from the specified camera.

<a id="unreal.DisplayClusterCameraComponent.enable_depth_of_field"></a>

#### enable_depth_of_field

```python
@enable_depth_of_field.setter
def enable_depth_of_field(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_depth_of_field_compensation"></a>

#### enable_icvfx_depth_of_field_compensation

```python
@property
def enable_icvfx_depth_of_field_compensation() -> bool
```

(bool):  [Read-Write] Use the DC Depth-Of-Field settings from the specified ICVFX camera.

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_depth_of_field_compensation"></a>

#### enable_icvfx_depth_of_field_compensation

```python
@enable_icvfx_depth_of_field_compensation.setter
def enable_icvfx_depth_of_field_compensation(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_color_grading"></a>

#### enable_icvfx_color_grading

```python
@property
def enable_icvfx_color_grading() -> bool
```

(bool):  [Read-Write] Use the DC ColorGrading from the specified ICVFX camera.

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_color_grading"></a>

#### enable_icvfx_color_grading

```python
@enable_icvfx_color_grading.setter
def enable_icvfx_color_grading(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_motion_blur"></a>

#### enable_icvfx_motion_blur

```python
@property
def enable_icvfx_motion_blur() -> bool
```

(bool):  [Read-Write] Use the DC Motion Blur settings from the specified ICVFX camera.

<a id="unreal.DisplayClusterCameraComponent.enable_icvfx_motion_blur"></a>

#### enable_icvfx_motion_blur

```python
@enable_icvfx_motion_blur.setter
def enable_icvfx_motion_blur(value: bool) -> None
```

<a id="unreal.DisplayClusterCameraComponent.toggle_swap_eyes"></a>

#### toggle_swap_eyes

```python
def toggle_swap_eyes() -> bool
```

x.toggle_swap_eyes() -> bool
Toggles eyes swap state

Returns:
    bool: New eyes swap state. False - normal eyes left|right, true - swapped eyes right|left

<a id="unreal.DisplayClusterCameraComponent.set_swap_eyes"></a>

#### set_swap_eyes

```python
def set_swap_eyes(swap_eyes: bool) -> None
```

x.set_swap_eyes(swap_eyes) -> None
Set swap eyes state

Args:
    swap_eyes (bool): New eyes swap state. False - normal eyes left|right, true - swapped eyes right|left

<a id="unreal.DisplayClusterCameraComponent.set_stereo_offset"></a>

#### set_stereo_offset

```python
def set_stereo_offset(stereo_offset: DisplayClusterEyeStereoOffset) -> None
```

x.set_stereo_offset(stereo_offset) -> None
Set stereo offset type

Args:
    stereo_offset (DisplayClusterEyeStereoOffset):

<a id="unreal.DisplayClusterCameraComponent.set_interpupillary_distance"></a>

#### set_interpupillary_distance

```python
def set_interpupillary_distance(distance: float) -> None
```

x.set_interpupillary_distance(distance) -> None
Set interpupillary distance

Args:
    distance (float): New interpupillary distance

<a id="unreal.DisplayClusterCameraComponent.get_swap_eyes"></a>

#### get_swap_eyes

```python
def get_swap_eyes() -> bool
```

x.get_swap_eyes() -> bool
Get swap eyes state

Returns:
    bool: Eyes swap state. False - normal eyes left|right, true - swapped eyes right|left

<a id="unreal.DisplayClusterCameraComponent.get_stereo_offset"></a>

#### get_stereo_offset

```python
def get_stereo_offset() -> DisplayClusterEyeStereoOffset
```

x.get_stereo_offset() -> DisplayClusterEyeStereoOffset
Get stereo offset type

Returns:
    DisplayClusterEyeStereoOffset: Current forced stereo offset type

<a id="unreal.DisplayClusterCameraComponent.get_interpupillary_distance"></a>

#### get_interpupillary_distance

```python
def get_interpupillary_distance() -> float
```

x.get_interpupillary_distance() -> float
Get interpupillary distance

Returns:
    float: Interpupillary distance

<a id="unreal.DisplayClusterLightCardActor"></a>