## CameraShakeSourceComponent Objects

```python
class CameraShakeSourceComponent(SceneComponent)
```

Camera Shake Source Component

**C++ Source:**

- **Module**: Engine
- **File**: CameraShakeSourceComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``attenuation`` (CameraShakeAttenuation):  [Read-Write] The attenuation profile for how camera shakes' intensity falls off with distance
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``auto_start`` (bool):  [Read-Write] Whether to auto start when created
- ``camera_shake`` (type(Class)):  [Read-Write] The camera shake class to use for this camera shake source actor
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``inner_attenuation_radius`` (float):  [Read-Write] Under this distance from the source, the camera shakes are at full intensity
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``outer_attenuation_radius`` (float):  [Read-Write] Outside of this distance from the source, the camera shakes don't apply at all
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
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.CameraShakeSourceComponent.attenuation"></a>

#### attenuation

```python
@property
def attenuation() -> CameraShakeAttenuation
```

(CameraShakeAttenuation):  [Read-Write] The attenuation profile for how camera shakes' intensity falls off with distance

<a id="unreal.CameraShakeSourceComponent.attenuation"></a>

#### attenuation

```python
@attenuation.setter
def attenuation(value: CameraShakeAttenuation) -> None
```

<a id="unreal.CameraShakeSourceComponent.inner_attenuation_radius"></a>

#### inner_attenuation_radius

```python
@property
def inner_attenuation_radius() -> float
```

(float):  [Read-Write] Under this distance from the source, the camera shakes are at full intensity

<a id="unreal.CameraShakeSourceComponent.inner_attenuation_radius"></a>

#### inner_attenuation_radius

```python
@inner_attenuation_radius.setter
def inner_attenuation_radius(value: float) -> None
```

<a id="unreal.CameraShakeSourceComponent.outer_attenuation_radius"></a>

#### outer_attenuation_radius

```python
@property
def outer_attenuation_radius() -> float
```

(float):  [Read-Write] Outside of this distance from the source, the camera shakes don't apply at all

<a id="unreal.CameraShakeSourceComponent.outer_attenuation_radius"></a>

#### outer_attenuation_radius

```python
@outer_attenuation_radius.setter
def outer_attenuation_radius(value: float) -> None
```

<a id="unreal.CameraShakeSourceComponent.camera_shake"></a>

#### camera_shake

```python
@property
def camera_shake() -> Class
```

(type(Class)):  [Read-Write] The camera shake class to use for this camera shake source actor

<a id="unreal.CameraShakeSourceComponent.camera_shake"></a>

#### camera_shake

```python
@camera_shake.setter
def camera_shake(value: Class) -> None
```

<a id="unreal.CameraShakeSourceComponent.auto_start"></a>

#### auto_start

```python
@property
def auto_start() -> bool
```

(bool):  [Read-Write] Whether to auto start when created

<a id="unreal.CameraShakeSourceComponent.auto_start"></a>

#### auto_start

```python
@auto_start.setter
def auto_start(value: bool) -> None
```

<a id="unreal.CameraShakeSourceComponent.b_auto_play"></a>

#### b_auto_play

```python
@property
def b_auto_play() -> bool
```

deprecated: 'b_auto_play' was renamed to 'auto_start'.

<a id="unreal.CameraShakeSourceComponent.b_auto_play"></a>

#### b_auto_play

```python
@b_auto_play.setter
def b_auto_play(value: bool) -> None
```

<a id="unreal.CameraShakeSourceComponent.stop_all_camera_shakes_of_type"></a>

#### stop_all_camera_shakes_of_type

```python
def stop_all_camera_shakes_of_type(camera_shake: Class,
                                   immediately: bool = True) -> None
```

x.stop_all_camera_shakes_of_type(camera_shake, immediately=True) -> None
Stops a camera shake originating from this source

Args:
    camera_shake (type(Class)): 
    immediately (bool):

<a id="unreal.CameraShakeSourceComponent.stop_all_camera_shakes"></a>

#### stop_all_camera_shakes

```python
def stop_all_camera_shakes(immediately: bool = True) -> None
```

x.stop_all_camera_shakes(immediately=True) -> None
Stops all currently active camera shakes that are originating from this source from all player controllers

Args:
    immediately (bool):

<a id="unreal.CameraShakeSourceComponent.start_camera_shake"></a>

#### start_camera_shake

```python
def start_camera_shake(
        camera_shake: Class,
        scale: float = 1.000000,
        play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
        user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

x.start_camera_shake(camera_shake, scale=1.000000, play_space=CameraShakePlaySpace.CAMERA_LOCAL, user_play_space_rot=[0.000000, 0.000000, 0.000000]) -> None
Starts a new camera shake originating from this source, and apply it on all player controllers

Args:
    camera_shake (type(Class)): 
    scale (float): 
    play_space (CameraShakePlaySpace): 
    user_play_space_rot (Rotator):

<a id="unreal.CameraShakeSourceComponent.play_camera_shake"></a>

#### play_camera_shake

```python
def play_camera_shake(
        camera_shake: Class,
        scale: float = 1.000000,
        play_space: CameraShakePlaySpace = CameraShakePlaySpace.CAMERA_LOCAL,
        user_play_space_rot: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

deprecated: 'play_camera_shake' was renamed to 'start_camera_shake'.

<a id="unreal.CameraShakeSourceComponent.start"></a>

#### start

```python
def start() -> None
```

x.start() -> None
Start

<a id="unreal.CameraShakeSourceComponent.play"></a>

#### play

```python
def play() -> None
```

deprecated: 'play' was renamed to 'start'.

<a id="unreal.CameraShakeSourceComponent.get_attenuation_factor"></a>

#### get_attenuation_factor

```python
def get_attenuation_factor(location: Vector) -> float
```

x.get_attenuation_factor(location) -> float
Computes an attenuation factor from this source

Args:
    location (Vector): 

Returns:
    float:

<a id="unreal.TextureRenderTarget"></a>