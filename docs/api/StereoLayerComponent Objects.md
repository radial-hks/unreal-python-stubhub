## StereoLayerComponent Objects

```python
class StereoLayerComponent(SceneComponent)
```

A geometry layer within the stereo rendered viewport.

**C++ Source:**

- **Module**: Engine
- **File**: StereoLayerComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``additional_flags`` (Array[Name]):  [Read-Write] Additional flags not included in IStereoLayers::ELayerFlags
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``left_texture`` (Texture):  [Read-Write] Texture displayed on the stereo layer for left eye, if stereoscopic textures are supported on the platform and by the layer shape *
- ``live_texture`` (bool):  [Read-Write] True if the stereo layer texture needs to update itself every frame(scene capture, video, etc.)
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``no_alpha_channel`` (bool):  [Read-Write] True if the texture should not use its own alpha channel (1.0 will be substituted)
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``priority`` (int32):  [Read-Write] Render priority among all stereo layers, higher priority render on top of lower priority *
- ``quad_preserve_texture_ratio`` (bool):  [Read-Write] True if the quad should internally set it's Y value based on the set texture's dimensions
- ``quad_size`` (Vector2D):  [Read-Write] Size of the rendered stereo layer quad *
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``shape`` (StereoLayerShape):  [Read-Write] Specifies which shape of layer it is.  Note that some shapes will be supported only on certain platforms! *
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``stereo_layer_type`` (StereoLayerType):  [Read-Write] Specifies how and where the quad is rendered to the screen *
- ``supports_depth`` (bool):  [Read-Write] True if the stereo layer needs to support depth intersections with the scene geometry, if available on the platform
- ``texture`` (Texture):  [Read-Write] Texture displayed on the stereo layer (if stereoscopic textures are supported on the platform and more than one texture is provided, this will be the right eye) *
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``uv_rect`` (Box2D):  [Read-Write] UV coordinates mapped to the quad face *
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.StereoLayerComponent.live_texture"></a>

#### live_texture

```python
@property
def live_texture() -> bool
```

(bool):  [Read-Write] True if the stereo layer texture needs to update itself every frame(scene capture, video, etc.)

<a id="unreal.StereoLayerComponent.live_texture"></a>

#### live_texture

```python
@live_texture.setter
def live_texture(value: bool) -> None
```

<a id="unreal.StereoLayerComponent.supports_depth"></a>

#### supports_depth

```python
@property
def supports_depth() -> bool
```

(bool):  [Read-Write] True if the stereo layer needs to support depth intersections with the scene geometry, if available on the platform

<a id="unreal.StereoLayerComponent.supports_depth"></a>

#### supports_depth

```python
@supports_depth.setter
def supports_depth(value: bool) -> None
```

<a id="unreal.StereoLayerComponent.no_alpha_channel"></a>

#### no_alpha_channel

```python
@property
def no_alpha_channel() -> bool
```

(bool):  [Read-Write] True if the texture should not use its own alpha channel (1.0 will be substituted)

<a id="unreal.StereoLayerComponent.no_alpha_channel"></a>

#### no_alpha_channel

```python
@no_alpha_channel.setter
def no_alpha_channel(value: bool) -> None
```

<a id="unreal.StereoLayerComponent.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Only] Texture displayed on the stereo layer (if stereoscopic textures are supported on the platform and more than one texture is provided, this will be the right eye) *

<a id="unreal.StereoLayerComponent.left_texture"></a>

#### left_texture

```python
@property
def left_texture() -> Texture
```

(Texture):  [Read-Only] Texture displayed on the stereo layer for left eye, if stereoscopic textures are supported on the platform and by the layer shape *

<a id="unreal.StereoLayerComponent.quad_preserve_texture_ratio"></a>

#### quad_preserve_texture_ratio

```python
@property
def quad_preserve_texture_ratio() -> bool
```

(bool):  [Read-Write] True if the quad should internally set it's Y value based on the set texture's dimensions

<a id="unreal.StereoLayerComponent.quad_preserve_texture_ratio"></a>

#### quad_preserve_texture_ratio

```python
@quad_preserve_texture_ratio.setter
def quad_preserve_texture_ratio(value: bool) -> None
```

<a id="unreal.StereoLayerComponent.additional_flags"></a>

#### additional_flags

```python
@property
def additional_flags() -> Array[Name]
```

(Array[Name]):  [Read-Only] Additional flags not included in IStereoLayers::ELayerFlags

<a id="unreal.StereoLayerComponent.quad_size"></a>

#### quad_size

```python
@property
def quad_size() -> Vector2D
```

(Vector2D):  [Read-Only] Size of the rendered stereo layer quad *

<a id="unreal.StereoLayerComponent.uv_rect"></a>

#### uv_rect

```python
@property
def uv_rect() -> Box2D
```

(Box2D):  [Read-Only] UV coordinates mapped to the quad face *

<a id="unreal.StereoLayerComponent.stereo_layer_type"></a>

#### stereo_layer_type

```python
@property
def stereo_layer_type() -> StereoLayerType
```

(StereoLayerType):  [Read-Only] Specifies how and where the quad is rendered to the screen *

<a id="unreal.StereoLayerComponent.shape"></a>

#### shape

```python
@property
def shape() -> StereoLayerShape
```

(StereoLayerShape):  [Read-Only] Specifies which shape of layer it is.  Note that some shapes will be supported only on certain platforms! *

<a id="unreal.StereoLayerComponent.priority"></a>

#### priority

```python
@property
def priority() -> int
```

(int32):  [Read-Only] Render priority among all stereo layers, higher priority render on top of lower priority *

<a id="unreal.StereoLayerComponent.set_uv_rect"></a>

#### set_uv_rect

```python
def set_uv_rect(uv_rect: Box2D) -> None
```

x.set_uv_rect(uv_rect) -> None
Change the UV coordinates mapped to the quad face

Args:
    uv_rect (Box2D):

<a id="unreal.StereoLayerComponent.set_texture"></a>

#### set_texture

```python
def set_texture(texture: Texture) -> None
```

x.set_texture(texture) -> None
Change the texture displayed on the stereo layer.

If stereoscopic layer textures are supported on the platform and LeftTexture is set, this property controls the texture for the right eye.

Args:
    texture (Texture):

<a id="unreal.StereoLayerComponent.set_quad_size"></a>

#### set_quad_size

```python
def set_quad_size(quad_size: Vector2D) -> None
```

x.set_quad_size(quad_size) -> None
Change the quad size. This is the unscaled height and width, before component scale is applied.

Args:
    quad_size (Vector2D):

<a id="unreal.StereoLayerComponent.set_priority"></a>

#### set_priority

```python
def set_priority(priority: int) -> None
```

x.set_priority(priority) -> None
Change the layer's render priority, higher priorities render on top of lower priorities

Args:
    priority (int32):

<a id="unreal.StereoLayerComponent.set_left_texture"></a>

#### set_left_texture

```python
def set_left_texture(texture: Texture) -> None
```

x.set_left_texture(texture) -> None
Change the texture displayed on the stereo layer for left eye, if stereoscopic layer textures are supported on the platform.

Args:
    texture (Texture):

<a id="unreal.StereoLayerComponent.set_equirect_props"></a>

#### set_equirect_props

```python
def set_equirect_props(equirect_props: EquirectProps) -> None
```

x.set_equirect_props(equirect_props) -> None
Set Equirect layer properties: UVRect, Scale, Bias and Radius.
deprecated: Use UStereoLayerShapeEquirect::SetEquirectProps() instead.

Args:
    equirect_props (EquirectProps):

<a id="unreal.StereoLayerComponent.mark_texture_for_update"></a>

#### mark_texture_for_update

```python
def mark_texture_for_update() -> None
```

x.mark_texture_for_update() -> None
Manually mark the stereo layer texture for updating

<a id="unreal.StereoLayerComponent.get_uv_rect"></a>

#### get_uv_rect

```python
def get_uv_rect() -> Box2D
```

x.get_uv_rect() -> Box2D


Returns:
    Box2D: the UV coordinates mapped to the quad face

<a id="unreal.StereoLayerComponent.get_texture"></a>

#### get_texture

```python
def get_texture() -> Texture
```

x.get_texture() -> Texture


Returns:
    Texture: the texture mapped to the stereo layer.

<a id="unreal.StereoLayerComponent.get_quad_size"></a>

#### get_quad_size

```python
def get_quad_size() -> Vector2D
```

x.get_quad_size() -> Vector2D


Returns:
    Vector2D: the height and width of the rendered quad

<a id="unreal.StereoLayerComponent.get_priority"></a>

#### get_priority

```python
def get_priority() -> int
```

x.get_priority() -> int32


Returns:
    int32: the render priority

<a id="unreal.StereoLayerComponent.get_left_texture"></a>

#### get_left_texture

```python
def get_left_texture() -> Texture
```

x.get_left_texture() -> Texture


Returns:
    Texture: the texture mapped to the stereo layer for left eye, if stereoscopic layer textures are supported on the platform.

<a id="unreal.TextRenderActor"></a>