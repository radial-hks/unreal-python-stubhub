## MotionWarpingComponent Objects

```python
class MotionWarpingComponent(ActorComponent)
```

Motion Warping Component

**C++ Source:**

- **Plugin**: MotionWarping
- **Module**: MotionWarping
- **File**: MotionWarpingComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``on_pre_update`` (MotionWarpingPreUpdate):  [Read-Write] Event called before Root Motion Modifiers are updated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``search_for_windows_in_anims_within_montages`` (bool):  [Read-Write] Whether to look inside animations within montage when looking for warping windows

<a id="unreal.MotionWarpingComponent.search_for_windows_in_anims_within_montages"></a>

#### search_for_windows_in_anims_within_montages

```python
@property
def search_for_windows_in_anims_within_montages() -> bool
```

(bool):  [Read-Write] Whether to look inside animations within montage when looking for warping windows

<a id="unreal.MotionWarpingComponent.search_for_windows_in_anims_within_montages"></a>

#### search_for_windows_in_anims_within_montages

```python
@search_for_windows_in_anims_within_montages.setter
def search_for_windows_in_anims_within_montages(value: bool) -> None
```

<a id="unreal.MotionWarpingComponent.on_pre_update"></a>

#### on_pre_update

```python
@property
def on_pre_update() -> MotionWarpingPreUpdate
```

(MotionWarpingPreUpdate):  [Read-Write] Event called before Root Motion Modifiers are updated

<a id="unreal.MotionWarpingComponent.on_pre_update"></a>

#### on_pre_update

```python
@on_pre_update.setter
def on_pre_update(value: MotionWarpingPreUpdate) -> None
```

<a id="unreal.MotionWarpingComponent.remove_warp_targets"></a>

#### remove_warp_targets

```python
def remove_warp_targets(warp_target_names: Array[Name]) -> int
```

x.remove_warp_targets(warp_target_names) -> int32
Removes multiple warp targets

Args:
    warp_target_names (Array[Name]): 

Returns:
    int32:

<a id="unreal.MotionWarpingComponent.remove_warp_target"></a>

#### remove_warp_target

```python
def remove_warp_target(warp_target_name: Name) -> int
```

x.remove_warp_target(warp_target_name) -> int32
Removes the warp target associated with the specified key

Args:
    warp_target_name (Name): 

Returns:
    int32:

<a id="unreal.MotionWarpingComponent.remove_all_warp_targets"></a>

#### remove_all_warp_targets

```python
def remove_all_warp_targets() -> int
```

x.remove_all_warp_targets() -> int32
Removes all warp targets

Returns:
    int32:

<a id="unreal.MotionWarpingComponent.disable_all_root_motion_modifiers"></a>

#### disable_all_root_motion_modifiers

```python
def disable_all_root_motion_modifiers() -> None
```

x.disable_all_root_motion_modifiers() -> None
Mark all the modifiers as Disable

<a id="unreal.MotionWarpingComponent.add_or_update_warp_target_from_transform"></a>

#### add_or_update_warp_target_from_transform

```python
def add_or_update_warp_target_from_transform(
        warp_target_name: Name, target_transform: Transform) -> None
```

x.add_or_update_warp_target_from_transform(warp_target_name, target_transform) -> None
Create and adds or update a target associated with a specified name

Args:
    warp_target_name (Name): Warp target identifier
    target_transform (Transform): Transform used to set the location and rotation for the warp target

<a id="unreal.MotionWarpingComponent.add_or_update_warp_target_from_location_and_rotation"></a>

#### add_or_update_warp_target_from_location_and_rotation

```python
def add_or_update_warp_target_from_location_and_rotation(
        warp_target_name: Name, target_location: Vector,
        target_rotation: Rotator) -> None
```

x.add_or_update_warp_target_from_location_and_rotation(warp_target_name, target_location, target_rotation) -> None
Create and adds or update a target associated with a specified name

Args:
    warp_target_name (Name): Warp target identifier
    target_location (Vector): Location for the warp target
    target_rotation (Rotator):

<a id="unreal.MotionWarpingComponent.add_or_update_warp_target_from_location"></a>

#### add_or_update_warp_target_from_location

```python
def add_or_update_warp_target_from_location(warp_target_name: Name,
                                            target_location: Vector) -> None
```

x.add_or_update_warp_target_from_location(warp_target_name, target_location) -> None
Create and adds or update a target associated with a specified name

Args:
    warp_target_name (Name): Warp target identifier
    target_location (Vector): Location for the warp target

<a id="unreal.MotionWarpingComponent.add_or_update_warp_target_from_component"></a>

#### add_or_update_warp_target_from_component

```python
def add_or_update_warp_target_from_component(
        warp_target_name: Name,
        component: SceneComponent,
        bone_name: Name,
        follow_component: bool,
        location_offset: Vector = [0.000000, 0.000000, 0.000000],
        rotation_offset: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

x.add_or_update_warp_target_from_component(warp_target_name, component, bone_name, follow_component, location_offset=[0.000000, 0.000000, 0.000000], rotation_offset=[0.000000, 0.000000, 0.000000]) -> None
Create and adds or update a target associated with a specified name

Args:
    warp_target_name (Name): Warp target identifier
    component (SceneComponent): Scene Component used to get the target transform
    bone_name (Name): Optional bone or socket in the component used to get the target transform.
    follow_component (bool): Whether the target transform should update while the warping is active. Useful for tracking moving targets. Note that this will be one frame off if our owner ticks before the target actor. Add tick pre-requisites to avoid this.
    location_offset (Vector): Optional translation offset to apply to the transform we get from the component
    rotation_offset (Rotator): Optional rotation offset to apply to the transform we get from the component

<a id="unreal.MotionWarpingComponent.add_or_update_warp_target"></a>

#### add_or_update_warp_target

```python
def add_or_update_warp_target(warp_target: MotionWarpingTarget) -> None
```

x.add_or_update_warp_target(warp_target) -> None
Adds or update a warp target

Args:
    warp_target (MotionWarpingTarget):

<a id="unreal.RootMotionModifier"></a>