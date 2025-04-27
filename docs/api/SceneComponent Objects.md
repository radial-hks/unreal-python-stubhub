## SceneComponent Objects

```python
class SceneComponent(ActorComponent)
```

A SceneComponent has a transform and supports attachment, but has no rendering or collision capabilities.
Useful as a 'dummy' component in the hierarchy to offset others.
see: [Scene Components](https://docs.unrealengine.com/latest/INT/Programming/UnrealArchitecture/Actors/Components/index.html#scenecomponents)

**C++ Source:**

- **Module**: Engine
- **File**: SceneComponent.h

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
- ``use_attach_parent_bound`` (bool):  [Read-Write] If true, this component uses its parents bounds when attached.
  This can be a significant optimization with many components attached together.
- ``visible`` (bool):  [Read-Write] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SceneComponent.relative_location"></a>

#### relative_location

```python
@property
def relative_location() -> Vector
```

(Vector):  [Read-Only] Location of the component relative to its parent

<a id="unreal.SceneComponent.relative_translation"></a>

#### relative_translation

```python
@property
def relative_translation() -> Vector
```

deprecated: 'relative_translation' was renamed to 'relative_location'.

<a id="unreal.SceneComponent.relative_rotation"></a>

#### relative_rotation

```python
@property
def relative_rotation() -> Rotator
```

(Rotator):  [Read-Only] Rotation of the component relative to its parent

<a id="unreal.SceneComponent.relative_scale3d"></a>

#### relative_scale3d

```python
@property
def relative_scale3d() -> Vector
```

(Vector):  [Read-Only] Non-uniform scaling of the component relative to its parent.
Note that scaling is always applied in local space (no shearing etc)

<a id="unreal.SceneComponent.absolute_location"></a>

#### absolute_location

```python
@property
def absolute_location() -> bool
```

(bool):  [Read-Write] If RelativeLocation should be considered relative to the world, rather than the parent

<a id="unreal.SceneComponent.absolute_location"></a>

#### absolute_location

```python
@absolute_location.setter
def absolute_location(value: bool) -> None
```

<a id="unreal.SceneComponent.b_absolute_translation"></a>

#### b_absolute_translation

```python
@property
def b_absolute_translation() -> bool
```

deprecated: 'b_absolute_translation' was renamed to 'absolute_location'.

<a id="unreal.SceneComponent.b_absolute_translation"></a>

#### b_absolute_translation

```python
@b_absolute_translation.setter
def b_absolute_translation(value: bool) -> None
```

<a id="unreal.SceneComponent.absolute_rotation"></a>

#### absolute_rotation

```python
@property
def absolute_rotation() -> bool
```

(bool):  [Read-Write] If RelativeRotation should be considered relative to the world, rather than the parent

<a id="unreal.SceneComponent.absolute_rotation"></a>

#### absolute_rotation

```python
@absolute_rotation.setter
def absolute_rotation(value: bool) -> None
```

<a id="unreal.SceneComponent.absolute_scale"></a>

#### absolute_scale

```python
@property
def absolute_scale() -> bool
```

(bool):  [Read-Write] If RelativeScale3D should be considered relative to the world, rather than the parent

<a id="unreal.SceneComponent.absolute_scale"></a>

#### absolute_scale

```python
@absolute_scale.setter
def absolute_scale(value: bool) -> None
```

<a id="unreal.SceneComponent.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Only] Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow.

<a id="unreal.SceneComponent.should_update_physics_volume"></a>

#### should_update_physics_volume

```python
@property
def should_update_physics_volume() -> bool
```

(bool):  [Read-Write] Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.
see: GetPhysicsVolume()

<a id="unreal.SceneComponent.should_update_physics_volume"></a>

#### should_update_physics_volume

```python
@should_update_physics_volume.setter
def should_update_physics_volume(value: bool) -> None
```

<a id="unreal.SceneComponent.hidden_in_game"></a>

#### hidden_in_game

```python
@property
def hidden_in_game() -> bool
```

(bool):  [Read-Only] Whether to hide the primitive in game, if the primitive is Visible.

<a id="unreal.SceneComponent.use_attach_parent_bound"></a>

#### use_attach_parent_bound

```python
@property
def use_attach_parent_bound() -> bool
```

(bool):  [Read-Write] If true, this component uses its parents bounds when attached.
This can be a significant optimization with many components attached together.

<a id="unreal.SceneComponent.use_attach_parent_bound"></a>

#### use_attach_parent_bound

```python
@use_attach_parent_bound.setter
def use_attach_parent_bound(value: bool) -> None
```

<a id="unreal.SceneComponent.mobility"></a>

#### mobility

```python
@property
def mobility() -> ComponentMobility
```

(ComponentMobility):  [Read-Only] How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor.

<a id="unreal.SceneComponent.modify_frequency"></a>

#### modify_frequency

```python
@property
def modify_frequency() -> ComponentMobility
```

deprecated: 'modify_frequency' was renamed to 'mobility'.

<a id="unreal.SceneComponent.detail_mode"></a>

#### detail_mode

```python
@property
def detail_mode() -> DetailMode
```

(DetailMode):  [Read-Only] If detail mode is >= system detail mode, primitive won't be rendered.

<a id="unreal.SceneComponent.physics_volume_changed_delegate"></a>

#### physics_volume_changed_delegate

```python
@property
def physics_volume_changed_delegate() -> PhysicsVolumeChanged
```

(PhysicsVolumeChanged):  [Read-Write] Delegate that will be called when PhysicsVolume has been changed *

<a id="unreal.SceneComponent.physics_volume_changed_delegate"></a>

#### physics_volume_changed_delegate

```python
@physics_volume_changed_delegate.setter
def physics_volume_changed_delegate(value: PhysicsVolumeChanged) -> None
```

<a id="unreal.SceneComponent.toggle_visibility"></a>

#### toggle_visibility

```python
def toggle_visibility(propagate_to_children: bool = False) -> None
```

x.toggle_visibility(propagate_to_children=False) -> None
Toggle visibility of the component

Args:
    propagate_to_children (bool):

<a id="unreal.SceneComponent.set_world_scale3d"></a>

#### set_world_scale3d

```python
def set_world_scale3d(new_scale: Vector) -> None
```

x.set_world_scale3d(new_scale) -> None
Set the relative scale of the component to put it at the supplied scale in world space.

Args:
    new_scale (Vector): New scale in world space for this component.

<a id="unreal.SceneComponent.set_visibility"></a>

#### set_visibility

```python
def set_visibility(new_visibility: bool,
                   propagate_to_children: bool = False) -> None
```

x.set_visibility(new_visibility, propagate_to_children=False) -> None
Set visibility of the component, if during game use this to turn on/off

Args:
    new_visibility (bool): 
    propagate_to_children (bool):

<a id="unreal.SceneComponent.set_relative_scale3d"></a>

#### set_relative_scale3d

```python
def set_relative_scale3d(new_scale3d: Vector) -> None
```

x.set_relative_scale3d(new_scale3d) -> None
Set the non-uniform scale of the component relative to its parent

Args:
    new_scale3d (Vector):

<a id="unreal.SceneComponent.set_mobility"></a>

#### set_mobility

```python
def set_mobility(new_mobility: ComponentMobility) -> None
```

x.set_mobility(new_mobility) -> None
Set how often this component is allowed to move during runtime. Causes a component re-register if the component is already registered

Args:
    new_mobility (ComponentMobility):

<a id="unreal.SceneComponent.set_hidden_in_game"></a>

#### set_hidden_in_game

```python
def set_hidden_in_game(new_hidden: bool,
                       propagate_to_children: bool = False) -> None
```

x.set_hidden_in_game(new_hidden, propagate_to_children=False) -> None
Changes the value of bHiddenInGame, if false this will disable Visibility during gameplay

Args:
    new_hidden (bool): 
    propagate_to_children (bool):

<a id="unreal.SceneComponent.set_absolute"></a>

#### set_absolute

```python
def set_absolute(new_absolute_location: bool = False,
                 new_absolute_rotation: bool = False,
                 new_absolute_scale: bool = False) -> None
```

x.set_absolute(new_absolute_location=False, new_absolute_rotation=False, new_absolute_scale=False) -> None
Set which parts of the relative transform should be relative to parent, and which should be relative to world

Args:
    new_absolute_location (bool): 
    new_absolute_rotation (bool): 
    new_absolute_scale (bool):

<a id="unreal.SceneComponent.reset_relative_transform"></a>

#### reset_relative_transform

```python
def reset_relative_transform() -> None
```

x.reset_relative_transform() -> None
Reset the transform of the component relative to its parent. Sets relative location to zero, relative rotation to no rotation, and Scale to 1.

<a id="unreal.SceneComponent.set_world_transform"></a>

#### set_world_transform

```python
def set_world_transform(new_transform: Transform, sweep: bool,
                        teleport: bool) -> HitResult
```

x.set_world_transform(new_transform, sweep, teleport) -> HitResult
Set the transform of the component in world space.

Args:
    new_transform (Transform): New transform in world space for the component.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_world_rotation"></a>

#### set_world_rotation

```python
def set_world_rotation(new_rotation: Rotator, sweep: bool,
                       teleport: bool) -> HitResult
```

x.set_world_rotation(new_rotation, sweep, teleport) -> HitResult
* Put this component at the specified rotation in world space. Updates relative rotation to achieve the final world rotation.
*

Args:
    new_rotation (Rotator): New rotation in world space for the component. *
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation). *
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). *                                                      If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). *                                                      If false, physics velocity is updated based on the change in position (affecting ragdoll parts). *                                                      If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true. *

<a id="unreal.SceneComponent.set_world_location_and_rotation"></a>

#### set_world_location_and_rotation

```python
def set_world_location_and_rotation(new_location: Vector,
                                    new_rotation: Rotator, sweep: bool,
                                    teleport: bool) -> HitResult
```

x.set_world_location_and_rotation(new_location, new_rotation, sweep, teleport) -> HitResult
Set the relative location and rotation of the component to put it at the supplied pose in world space.

Args:
    new_location (Vector): New location in world space for the component.
    new_rotation (Rotator): New rotation in world space for the component.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_world_location"></a>

#### set_world_location

```python
def set_world_location(new_location: Vector, sweep: bool,
                       teleport: bool) -> HitResult
```

x.set_world_location(new_location, sweep, teleport) -> HitResult
Put this component at the specified location in world space. Updates relative location to achieve the final world location.

Args:
    new_location (Vector): New location in world space for the component.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_relative_transform"></a>

#### set_relative_transform

```python
def set_relative_transform(new_transform: Transform, sweep: bool,
                           teleport: bool) -> HitResult
```

x.set_relative_transform(new_transform, sweep, teleport) -> HitResult
Set the transform of the component relative to its parent

Args:
    new_transform (Transform): New transform of the component relative to its parent.
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_relative_rotation"></a>

#### set_relative_rotation

```python
def set_relative_rotation(new_rotation: Rotator, sweep: bool,
                          teleport: bool) -> HitResult
```

x.set_relative_rotation(new_rotation, sweep, teleport) -> HitResult
Set the rotation of the component relative to its parent

Args:
    new_rotation (Rotator): New rotation of the component relative to its parent
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_relative_location_and_rotation"></a>

#### set_relative_location_and_rotation

```python
def set_relative_location_and_rotation(new_location: Vector,
                                       new_rotation: Rotator, sweep: bool,
                                       teleport: bool) -> HitResult
```

x.set_relative_location_and_rotation(new_location, new_rotation, sweep, teleport) -> HitResult
Set the location and rotation of the component relative to its parent

Args:
    new_location (Vector): New location of the component relative to its parent.
    new_rotation (Rotator): New rotation of the component relative to its parent.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.set_relative_location"></a>

#### set_relative_location

```python
def set_relative_location(new_location: Vector, sweep: bool,
                          teleport: bool) -> HitResult
```

x.set_relative_location(new_location, sweep, teleport) -> HitResult
Set the location of the component relative to its parent

Args:
    new_location (Vector): New location of the component relative to its parent.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.get_world_transform"></a>

#### get_world_transform

```python
def get_world_transform() -> Transform
```

x.get_world_transform() -> Transform
Get the current component-to-world transform for this component

Returns:
    Transform:

<a id="unreal.SceneComponent.get_world_scale"></a>

#### get_world_scale

```python
def get_world_scale() -> Vector
```

x.get_world_scale() -> Vector
Returns scale of the component, in world space.

Returns:
    Vector:

<a id="unreal.SceneComponent.get_world_rotation"></a>

#### get_world_rotation

```python
def get_world_rotation() -> Rotator
```

x.get_world_rotation() -> Rotator
Returns rotation of the component, in world space.

Returns:
    Rotator:

<a id="unreal.SceneComponent.get_world_location"></a>

#### get_world_location

```python
def get_world_location() -> Vector
```

x.get_world_location() -> Vector
Return location of the component, in world space

Returns:
    Vector:

<a id="unreal.SceneComponent.detach_from_component"></a>

#### detach_from_component

```python
def detach_from_component(
        location_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE,
        rotation_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE,
        scale_rule: DetachmentRule = DetachmentRule.KEEP_RELATIVE,
        call_modify: bool = True) -> None
```

x.detach_from_component(location_rule=DetachmentRule.KEEP_RELATIVE, rotation_rule=DetachmentRule.KEEP_RELATIVE, scale_rule=DetachmentRule.KEEP_RELATIVE, call_modify=True) -> None
Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (see AttachToComponent), though note that some effects of welding may not be undone.

Args:
    location_rule (DetachmentRule): How to handle translations when detaching.
    rotation_rule (DetachmentRule): How to handle rotation when detaching.
    scale_rule (DetachmentRule): How to handle scales when detaching.
    call_modify (bool): If true, call Modify() on the component and the current attach parent component

<a id="unreal.SceneComponent.attach_to_component"></a>

#### attach_to_component

```python
def attach_to_component(parent: SceneComponent,
                        socket_name: Name,
                        location_rule: AttachmentRule,
                        rotation_rule: AttachmentRule,
                        scale_rule: AttachmentRule,
                        weld_simulated_bodies: bool = True) -> bool
```

x.attach_to_component(parent, socket_name, location_rule, rotation_rule, scale_rule, weld_simulated_bodies=True) -> bool
Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

Args:
    parent (SceneComponent): Parent to attach to.
    socket_name (Name): Optional socket to attach to on the parent.
    location_rule (AttachmentRule): How to handle translation when attaching.
    rotation_rule (AttachmentRule): How to handle rotation when attaching.
    scale_rule (AttachmentRule): How to handle scale when attaching.
    weld_simulated_bodies (bool): Whether to weld together simulated physics bodies. This transfers the shapes in the welded object into the parent (if simulated), which can result in permanent changes that persist even after subsequently detaching.

Returns:
    bool: True if attachment is successful (or already attached to requested parent/socket), false if attachment is rejected and there is no change in AttachParent.

<a id="unreal.SceneComponent.k2_attach_to"></a>

#### k2_attach_to

```python
def k2_attach_to(
        parent: SceneComponent,
        socket_name: Name = "None",
        attach_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        weld_simulated_bodies: bool = True) -> bool
```

x.k2_attach_to(parent, socket_name="None", attach_type=AttachLocation.KEEP_RELATIVE_OFFSET, weld_simulated_bodies=True) -> bool
K2 Attach To

Args:
    parent (SceneComponent): 
    socket_name (Name): 
    attach_type (AttachLocation): 
    weld_simulated_bodies (bool): 

Returns:
    bool:

<a id="unreal.SceneComponent.attach_to"></a>

#### attach_to

```python
def attach_to(
        parent: SceneComponent,
        socket_name: Name = "None",
        attach_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        weld_simulated_bodies: bool = True) -> bool
```

deprecated: 'attach_to' was renamed to 'k2_attach_to'.

<a id="unreal.SceneComponent.add_world_transform_keep_scale"></a>

#### add_world_transform_keep_scale

```python
def add_world_transform_keep_scale(delta_transform: Transform, sweep: bool,
                                   teleport: bool) -> HitResult
```

x.add_world_transform_keep_scale(delta_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of the component in world space. Scale is unchanged.

Args:
    delta_transform (Transform): Change in transform in world space for the component. Scale is ignored since we preserve the original scale.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_world_transform"></a>

#### add_world_transform

```python
def add_world_transform(delta_transform: Transform, sweep: bool,
                        teleport: bool) -> HitResult
```

x.add_world_transform(delta_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of the component in world space. Ignores scale and sets it to (1,1,1).

Args:
    delta_transform (Transform): Change in transform in world space for the component. Scale is ignored.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_world_rotation"></a>

#### add_world_rotation

```python
def add_world_rotation(delta_rotation: Rotator, sweep: bool,
                       teleport: bool) -> HitResult
```

x.add_world_rotation(delta_rotation, sweep, teleport) -> HitResult
Adds a delta to the rotation of the component in world space.

Args:
    delta_rotation (Rotator): Change in rotation in world space for the component.
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_world_offset"></a>

#### add_world_offset

```python
def add_world_offset(delta_location: Vector, sweep: bool,
                     teleport: bool) -> HitResult
```

x.add_world_offset(delta_location, sweep, teleport) -> HitResult
Adds a delta to the location of the component in world space.

Args:
    delta_location (Vector): Change in location in world space for the component.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_relative_rotation"></a>

#### add_relative_rotation

```python
def add_relative_rotation(delta_rotation: Rotator, sweep: bool,
                          teleport: bool) -> HitResult
```

x.add_relative_rotation(delta_rotation, sweep, teleport) -> HitResult
Adds a delta the rotation of the component relative to its parent

Args:
    delta_rotation (Rotator): Change in rotation of the component relative to is parent.
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_relative_location"></a>

#### add_relative_location

```python
def add_relative_location(delta_location: Vector, sweep: bool,
                          teleport: bool) -> HitResult
```

x.add_relative_location(delta_location, sweep, teleport) -> HitResult
Adds a delta to the translation of the component relative to its parent

Args:
    delta_location (Vector): Change in location of the component relative to its parent
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_local_transform"></a>

#### add_local_transform

```python
def add_local_transform(delta_transform: Transform, sweep: bool,
                        teleport: bool) -> HitResult
```

x.add_local_transform(delta_transform, sweep, teleport) -> HitResult
Adds a delta to the transform of the component in its local reference frame. Scale is unchanged.

Args:
    delta_transform (Transform): Change in transform of the component in its local reference frame. Scale is unchanged.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_local_rotation"></a>

#### add_local_rotation

```python
def add_local_rotation(delta_rotation: Rotator, sweep: bool,
                       teleport: bool) -> HitResult
```

x.add_local_rotation(delta_rotation, sweep, teleport) -> HitResult
Adds a delta to the rotation of the component in its local reference frame

Args:
    delta_rotation (Rotator): Change in rotation of the component in its local reference frame.
    sweep (bool): Whether we sweep to the destination (currently not supported for rotation).
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts).

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.add_local_offset"></a>

#### add_local_offset

```python
def add_local_offset(delta_location: Vector, sweep: bool,
                     teleport: bool) -> HitResult
```

x.add_local_offset(delta_location, sweep, teleport) -> HitResult
Adds a delta to the location of the component in its local reference frame

Args:
    delta_location (Vector): Change in location of the component in its local reference frame.
    sweep (bool): Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. Only the root component is swept and checked for blocking collision, child components move without sweeping. If collision is off, this has no effect.
    teleport (bool): Whether we teleport the physics state (if physics collision is enabled for this object). If true, physics velocity for this object is unchanged (so ragdoll parts are not affected by change in location). If false, physics velocity is updated based on the change in position (affecting ragdoll parts). If CCD is on and not teleporting, this will affect objects along the entire sweep volume.

Returns:
    HitResult: 

    sweep_hit_result (HitResult): Hit result from any impact if sweep is true.

<a id="unreal.SceneComponent.is_visible"></a>

#### is_visible

```python
def is_visible() -> bool
```

x.is_visible() -> bool
Returns true if this component is visible in the current context

Returns:
    bool:

<a id="unreal.SceneComponent.is_simulating_physics"></a>

#### is_simulating_physics

```python
def is_simulating_physics(bone_name: Name = "None") -> bool
```

x.is_simulating_physics(bone_name="None") -> bool
Returns whether the specified body is currently using physics simulation

Args:
    bone_name (Name): 

Returns:
    bool:

<a id="unreal.SceneComponent.is_any_simulating_physics"></a>

#### is_any_simulating_physics

```python
def is_any_simulating_physics() -> bool
```

x.is_any_simulating_physics() -> bool
Returns whether the specified body is currently using physics simulation

Returns:
    bool:

<a id="unreal.SceneComponent.get_up_vector"></a>

#### get_up_vector

```python
def get_up_vector() -> Vector
```

x.get_up_vector() -> Vector
Get the up (Z) unit direction vector from this component, in world space.

Returns:
    Vector:

<a id="unreal.SceneComponent.get_socket_transform"></a>

#### get_socket_transform

```python
def get_socket_transform(
    socket_name: Name,
    transform_space: RelativeTransformSpace = RelativeTransformSpace.RTS_WORLD
) -> Transform
```

x.get_socket_transform(socket_name, transform_space=RelativeTransformSpace.RTS_WORLD) -> Transform
Get world-space socket transform.

Args:
    socket_name (Name): Name of the socket or the bone to get the transform
    transform_space (RelativeTransformSpace): 

Returns:
    Transform: Socket transform in world space if socket if found. Otherwise it will return component's transform in world space.

<a id="unreal.SceneComponent.get_socket_rotation"></a>

#### get_socket_rotation

```python
def get_socket_rotation(socket_name: Name) -> Rotator
```

x.get_socket_rotation(socket_name) -> Rotator
Get world-space socket or bone  FRotator rotation.

Args:
    socket_name (Name): Name of the socket or the bone to get the transform

Returns:
    Rotator: Socket transform in world space if socket if found. Otherwise it will return component's transform in world space.

<a id="unreal.SceneComponent.get_socket_quaternion"></a>

#### get_socket_quaternion

```python
def get_socket_quaternion(socket_name: Name) -> Quat
```

x.get_socket_quaternion(socket_name) -> Quat
Get world-space socket or bone FQuat rotation.
deprecated: Use GetSocketRotation instead, Quat is not fully supported in blueprints.

Args:
    socket_name (Name): Name of the socket or the bone to get the transform

Returns:
    Quat: Socket transform in world space if socket if found. Otherwise it will return component's transform in world space.

<a id="unreal.SceneComponent.get_socket_location"></a>

#### get_socket_location

```python
def get_socket_location(socket_name: Name) -> Vector
```

x.get_socket_location(socket_name) -> Vector
Get world-space socket or bone location.

Args:
    socket_name (Name): Name of the socket or the bone to get the transform

Returns:
    Vector: Socket transform in world space if socket is found. Otherwise it will return component's transform in world space.

<a id="unreal.SceneComponent.get_right_vector"></a>

#### get_right_vector

```python
def get_right_vector() -> Vector
```

x.get_right_vector() -> Vector
Get the right (Y) unit direction vector from this component, in world space.

Returns:
    Vector:

<a id="unreal.SceneComponent.get_relative_transform"></a>

#### get_relative_transform

```python
def get_relative_transform() -> Transform
```

x.get_relative_transform() -> Transform
Returns the transform of the component relative to its parent

Returns:
    Transform:

<a id="unreal.SceneComponent.get_physics_volume"></a>

#### get_physics_volume

```python
def get_physics_volume() -> PhysicsVolume
```

x.get_physics_volume() -> PhysicsVolume
Get the PhysicsVolume overlapping this component.

Returns:
    PhysicsVolume:

<a id="unreal.SceneComponent.get_parent_components"></a>

#### get_parent_components

```python
def get_parent_components() -> Array[SceneComponent]
```

x.get_parent_components() -> Array[SceneComponent]
Gets all attachment parent components up to and including the root component

Returns:
    Array[SceneComponent]: 

    parents (Array[SceneComponent]):

<a id="unreal.SceneComponent.get_num_children_components"></a>

#### get_num_children_components

```python
def get_num_children_components() -> int
```

x.get_num_children_components() -> int32
Gets the number of attached children components

Returns:
    int32:

<a id="unreal.SceneComponent.get_forward_vector"></a>

#### get_forward_vector

```python
def get_forward_vector() -> Vector
```

x.get_forward_vector() -> Vector
Get the forward (X) unit direction vector from this component, in world space.

Returns:
    Vector:

<a id="unreal.SceneComponent.get_component_velocity"></a>

#### get_component_velocity

```python
def get_component_velocity() -> Vector
```

x.get_component_velocity() -> Vector
Get velocity of the component: either ComponentVelocity, or the velocity of the physics body if simulating physics.

Returns:
    Vector: Velocity of the component

<a id="unreal.SceneComponent.get_children_components"></a>

#### get_children_components

```python
def get_children_components(
        include_all_descendants: bool) -> Array[SceneComponent]
```

x.get_children_components(include_all_descendants) -> Array[SceneComponent]
Gets all components that are attached to this component, possibly recursively

Args:
    include_all_descendants (bool): Whether to include all descendants in the list of children (i.e. grandchildren, great grandchildren, etc.)

Returns:
    Array[SceneComponent]: 

    children (Array[SceneComponent]): The list of attached child components

<a id="unreal.SceneComponent.get_child_component"></a>

#### get_child_component

```python
def get_child_component(child_index: int) -> SceneComponent
```

x.get_child_component(child_index) -> SceneComponent
Gets the attached child component at the specified location

Args:
    child_index (int32): 

Returns:
    SceneComponent:

<a id="unreal.SceneComponent.get_attach_socket_name"></a>

#### get_attach_socket_name

```python
def get_attach_socket_name() -> Name
```

x.get_attach_socket_name() -> Name
Get the socket we are attached to.

Returns:
    Name:

<a id="unreal.SceneComponent.get_attach_parent"></a>

#### get_attach_parent

```python
def get_attach_parent() -> SceneComponent
```

x.get_attach_parent() -> SceneComponent
Get the SceneComponent we are attached to.

Returns:
    SceneComponent:

<a id="unreal.SceneComponent.get_all_socket_names"></a>

#### get_all_socket_names

```python
def get_all_socket_names() -> Array[Name]
```

x.get_all_socket_names() -> Array[Name]
Gets the names of all the sockets on the component.

Returns:
    Array[Name]: Get the names of all the sockets on the component.

<a id="unreal.SceneComponent.does_socket_exist"></a>

#### does_socket_exist

```python
def does_socket_exist(socket_name: Name) -> bool
```

x.does_socket_exist(socket_name) -> bool
Return true if socket with the given name exists

Args:
    socket_name (Name): Name of the socket or the bone to get the transform

Returns:
    bool:

<a id="unreal.SceneComponent.detach_from_parent"></a>

#### detach_from_parent

```python
def detach_from_parent(maintain_world_position: bool = False,
                       call_modify: bool = True) -> None
```

x.detach_from_parent(maintain_world_position=False, call_modify=True) -> None
Detach from Parent

Args:
    maintain_world_position (bool): 
    call_modify (bool):

<a id="unreal.PrimitiveComponent"></a>