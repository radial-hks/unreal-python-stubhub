## Text3DCharacterTransform Objects

```python
class Text3DCharacterTransform(SceneComponent)
```

Text 3DCharacter Transform

**C++ Source:**

- **Plugin**: Text3D
- **Module**: Text3D
- **File**: Text3DCharacterTransform.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``location_distance`` (Vector):  [Read-Write]
- ``location_enabled`` (bool):  [Read-Write] Location
- ``location_order`` (Text3DCharacterEffectOrder):  [Read-Write]
- ``location_progress`` (float):  [Read-Write]
- ``location_range`` (float):  [Read-Write]
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
- ``rotate_begin`` (Rotator):  [Read-Write]
- ``rotate_enabled`` (bool):  [Read-Write] Rotate
- ``rotate_end`` (Rotator):  [Read-Write]
- ``rotate_order`` (Text3DCharacterEffectOrder):  [Read-Write]
- ``rotate_progress`` (float):  [Read-Write]
- ``rotate_range`` (float):  [Read-Write]
- ``scale_begin`` (Vector):  [Read-Write]
- ``scale_enabled`` (bool):  [Read-Write] Scale
- ``scale_end`` (Vector):  [Read-Write]
- ``scale_order`` (Text3DCharacterEffectOrder):  [Read-Write]
- ``scale_progress`` (float):  [Read-Write]
- ``scale_range`` (float):  [Read-Write]
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.Text3DCharacterTransform.location_enabled"></a>

#### location_enabled

```python
@property
def location_enabled() -> bool
```

(bool):  [Read-Write] Location

<a id="unreal.Text3DCharacterTransform.location_enabled"></a>

#### location_enabled

```python
@location_enabled.setter
def location_enabled(value: bool) -> None
```

<a id="unreal.Text3DCharacterTransform.location_progress"></a>

#### location_progress

```python
@property
def location_progress() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.location_progress"></a>

#### location_progress

```python
@location_progress.setter
def location_progress(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.location_order"></a>

#### location_order

```python
@property
def location_order() -> Text3DCharacterEffectOrder
```

(Text3DCharacterEffectOrder):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.location_order"></a>

#### location_order

```python
@location_order.setter
def location_order(value: Text3DCharacterEffectOrder) -> None
```

<a id="unreal.Text3DCharacterTransform.location_range"></a>

#### location_range

```python
@property
def location_range() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.location_range"></a>

#### location_range

```python
@location_range.setter
def location_range(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.location_distance"></a>

#### location_distance

```python
@property
def location_distance() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.location_distance"></a>

#### location_distance

```python
@location_distance.setter
def location_distance(value: Vector) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_enabled"></a>

#### scale_enabled

```python
@property
def scale_enabled() -> bool
```

(bool):  [Read-Write] Scale

<a id="unreal.Text3DCharacterTransform.scale_enabled"></a>

#### scale_enabled

```python
@scale_enabled.setter
def scale_enabled(value: bool) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_progress"></a>

#### scale_progress

```python
@property
def scale_progress() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.scale_progress"></a>

#### scale_progress

```python
@scale_progress.setter
def scale_progress(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_order"></a>

#### scale_order

```python
@property
def scale_order() -> Text3DCharacterEffectOrder
```

(Text3DCharacterEffectOrder):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.scale_order"></a>

#### scale_order

```python
@scale_order.setter
def scale_order(value: Text3DCharacterEffectOrder) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_range"></a>

#### scale_range

```python
@property
def scale_range() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.scale_range"></a>

#### scale_range

```python
@scale_range.setter
def scale_range(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_begin"></a>

#### scale_begin

```python
@property
def scale_begin() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.scale_begin"></a>

#### scale_begin

```python
@scale_begin.setter
def scale_begin(value: Vector) -> None
```

<a id="unreal.Text3DCharacterTransform.scale_end"></a>

#### scale_end

```python
@property
def scale_end() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.scale_end"></a>

#### scale_end

```python
@scale_end.setter
def scale_end(value: Vector) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_enabled"></a>

#### rotate_enabled

```python
@property
def rotate_enabled() -> bool
```

(bool):  [Read-Write] Rotate

<a id="unreal.Text3DCharacterTransform.rotate_enabled"></a>

#### rotate_enabled

```python
@rotate_enabled.setter
def rotate_enabled(value: bool) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_progress"></a>

#### rotate_progress

```python
@property
def rotate_progress() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.rotate_progress"></a>

#### rotate_progress

```python
@rotate_progress.setter
def rotate_progress(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_order"></a>

#### rotate_order

```python
@property
def rotate_order() -> Text3DCharacterEffectOrder
```

(Text3DCharacterEffectOrder):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.rotate_order"></a>

#### rotate_order

```python
@rotate_order.setter
def rotate_order(value: Text3DCharacterEffectOrder) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_range"></a>

#### rotate_range

```python
@property
def rotate_range() -> float
```

(float):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.rotate_range"></a>

#### rotate_range

```python
@rotate_range.setter
def rotate_range(value: float) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_begin"></a>

#### rotate_begin

```python
@property
def rotate_begin() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.rotate_begin"></a>

#### rotate_begin

```python
@rotate_begin.setter
def rotate_begin(value: Rotator) -> None
```

<a id="unreal.Text3DCharacterTransform.rotate_end"></a>

#### rotate_end

```python
@property
def rotate_end() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.Text3DCharacterTransform.rotate_end"></a>

#### rotate_end

```python
@rotate_end.setter
def rotate_end(value: Rotator) -> None
```

<a id="unreal.Text3DCharacterTransform.set_scale_range"></a>

#### set_scale_range

```python
def set_scale_range(range: float) -> None
```

x.set_scale_range(range) -> None
Set Scale Range

Args:
    range (float):

<a id="unreal.Text3DCharacterTransform.set_scale_progress"></a>

#### set_scale_progress

```python
def set_scale_progress(progress: float) -> None
```

x.set_scale_progress(progress) -> None
Set Scale Progress

Args:
    progress (float):

<a id="unreal.Text3DCharacterTransform.set_scale_order"></a>

#### set_scale_order

```python
def set_scale_order(order: Text3DCharacterEffectOrder) -> None
```

x.set_scale_order(order) -> None
Set Scale Order

Args:
    order (Text3DCharacterEffectOrder):

<a id="unreal.Text3DCharacterTransform.set_scale_end"></a>

#### set_scale_end

```python
def set_scale_end(value: Vector) -> None
```

x.set_scale_end(value) -> None
Set Scale End

Args:
    value (Vector):

<a id="unreal.Text3DCharacterTransform.set_scale_enabled"></a>

#### set_scale_enabled

```python
def set_scale_enabled(enabled: bool) -> None
```

x.set_scale_enabled(enabled) -> None
Set Scale Enabled

Args:
    enabled (bool):

<a id="unreal.Text3DCharacterTransform.set_scale_begin"></a>

#### set_scale_begin

```python
def set_scale_begin(value: Vector) -> None
```

x.set_scale_begin(value) -> None
Set Scale Begin

Args:
    value (Vector):

<a id="unreal.Text3DCharacterTransform.set_rotate_range"></a>

#### set_rotate_range

```python
def set_rotate_range(range: float) -> None
```

x.set_rotate_range(range) -> None
Set Rotate Range

Args:
    range (float):

<a id="unreal.Text3DCharacterTransform.set_rotate_progress"></a>

#### set_rotate_progress

```python
def set_rotate_progress(progress: float) -> None
```

x.set_rotate_progress(progress) -> None
Set Rotate Progress

Args:
    progress (float):

<a id="unreal.Text3DCharacterTransform.set_rotate_order"></a>

#### set_rotate_order

```python
def set_rotate_order(order: Text3DCharacterEffectOrder) -> None
```

x.set_rotate_order(order) -> None
Set Rotate Order

Args:
    order (Text3DCharacterEffectOrder):

<a id="unreal.Text3DCharacterTransform.set_rotate_end"></a>

#### set_rotate_end

```python
def set_rotate_end(value: Rotator) -> None
```

x.set_rotate_end(value) -> None
Set Rotate End

Args:
    value (Rotator):

<a id="unreal.Text3DCharacterTransform.set_rotate_enabled"></a>

#### set_rotate_enabled

```python
def set_rotate_enabled(enabled: bool) -> None
```

x.set_rotate_enabled(enabled) -> None
Set Rotate Enabled

Args:
    enabled (bool):

<a id="unreal.Text3DCharacterTransform.set_rotate_begin"></a>

#### set_rotate_begin

```python
def set_rotate_begin(value: Rotator) -> None
```

x.set_rotate_begin(value) -> None
Set Rotate Begin

Args:
    value (Rotator):

<a id="unreal.Text3DCharacterTransform.set_location_range"></a>

#### set_location_range

```python
def set_location_range(range: float) -> None
```

x.set_location_range(range) -> None
Set Location Range

Args:
    range (float):

<a id="unreal.Text3DCharacterTransform.set_location_progress"></a>

#### set_location_progress

```python
def set_location_progress(progress: float) -> None
```

x.set_location_progress(progress) -> None
Set Location Progress

Args:
    progress (float):

<a id="unreal.Text3DCharacterTransform.set_location_order"></a>

#### set_location_order

```python
def set_location_order(order: Text3DCharacterEffectOrder) -> None
```

x.set_location_order(order) -> None
Set Location Order

Args:
    order (Text3DCharacterEffectOrder):

<a id="unreal.Text3DCharacterTransform.set_location_enabled"></a>

#### set_location_enabled

```python
def set_location_enabled(enabled: bool) -> None
```

x.set_location_enabled(enabled) -> None
Set Location Enabled

Args:
    enabled (bool):

<a id="unreal.Text3DCharacterTransform.set_location_distance"></a>

#### set_location_distance

```python
def set_location_distance(distance: Vector) -> None
```

x.set_location_distance(distance) -> None
Set Location Distance

Args:
    distance (Vector):

<a id="unreal.Text3DComponent"></a>