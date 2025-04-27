## PostProcessComponent Objects

```python
class PostProcessComponent(SceneComponent)
```

PostProcessComponent. Enables Post process controls for blueprints.
   Will use a parent UShapeComponent to provide volume data if available.

**C++ Source:**

- **Module**: Engine
- **File**: PostProcessComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absolute_location`` (bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent
- ``absolute_rotation`` (bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent
- ``absolute_scale`` (bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent
- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``blend_radius`` (float):  [Read-Write] World space radius around the volume that is used for blending (only if not unbound).
- ``blend_weight`` (float):  [Read-Write] 0:no effect, 1:full effect
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``detail_mode`` (DetailMode):  [Read-Write] If detail mode is >= system detail mode, primitive won't be rendered.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``enabled`` (bool):  [Read-Write] Whether this volume is enabled or not.
- ``hidden_in_game`` (bool):  [Read-Write] Whether to hide the primitive in game, if the primitive is Visible.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``mobility`` (ComponentMobility):  [Read-Write] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``physics_volume_changed_delegate`` (PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``priority`` (float):  [Read-Write] Priority of this volume. In the case of overlapping volumes the one with the highest priority
  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority.
- ``relative_location`` (Vector):  [Read-Write] Location of the component relative to its parent
- ``relative_rotation`` (Rotator):  [Read-Write] Rotation of the component relative to its parent
- ``relative_scale3d`` (Vector):  [Read-Write] Non-uniform scaling of the component relative to its parent.
  Note that scaling is always applied in local space (no shearing etc)
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``settings`` (PostProcessSettings):  [Read-Write] Post process settings to use for this volume.
- ``should_update_physics_volume`` (bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
  see: GetPhysicsVolume()
- ``unbound`` (bool):  [Read-Write] set this to false to use the parent shape component as volume bounds. True affects the whole world regardless.
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.PostProcessComponent.settings"></a>

#### settings

```python
@property
def settings() -> PostProcessSettings
```

(PostProcessSettings):  [Read-Write] Post process settings to use for this volume.

<a id="unreal.PostProcessComponent.settings"></a>

#### settings

```python
@settings.setter
def settings(value: PostProcessSettings) -> None
```

<a id="unreal.PostProcessComponent.priority"></a>

#### priority

```python
@property
def priority() -> float
```

(float):  [Read-Write] Priority of this volume. In the case of overlapping volumes the one with the highest priority
overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority.

<a id="unreal.PostProcessComponent.priority"></a>

#### priority

```python
@priority.setter
def priority(value: float) -> None
```

<a id="unreal.PostProcessComponent.blend_radius"></a>

#### blend_radius

```python
@property
def blend_radius() -> float
```

(float):  [Read-Write] World space radius around the volume that is used for blending (only if not unbound).

<a id="unreal.PostProcessComponent.blend_radius"></a>

#### blend_radius

```python
@blend_radius.setter
def blend_radius(value: float) -> None
```

<a id="unreal.PostProcessComponent.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] 0:no effect, 1:full effect

<a id="unreal.PostProcessComponent.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.PostProcessComponent.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Whether this volume is enabled or not.

<a id="unreal.PostProcessComponent.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.PostProcessComponent.unbound"></a>

#### unbound

```python
@property
def unbound() -> bool
```

(bool):  [Read-Write] set this to false to use the parent shape component as volume bounds. True affects the whole world regardless.

<a id="unreal.PostProcessComponent.unbound"></a>

#### unbound

```python
@unbound.setter
def unbound(value: bool) -> None
```

<a id="unreal.PostProcessComponent.add_or_update_blendable"></a>

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

<a id="unreal.ProjectileMovementComponent"></a>