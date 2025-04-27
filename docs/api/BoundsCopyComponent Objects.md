## BoundsCopyComponent Objects

```python
class BoundsCopyComponent(ActorComponent)
```

Component used to copy the bounds of another Actor.

**C++ Source:**

- **Module**: Engine
- **File**: BoundsCopyComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``bounds_source_actor`` (Actor):  [Read-Write] Actor to copy the bounds from to set up the transform.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``keep_own_bounds_scale`` (bool):  [Read-Write] If true, the actor's scale will be changed so that after adjustment, its own bounds match the source bounds.
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``use_colliding_components_for_own_bounds`` (bool):  [Read-Write] If true, the actor's own bounds will include its colliding components bounds.
- ``use_colliding_components_for_source_bounds`` (bool):  [Read-Write] If true, the source actor's bounds will include its colliding components bounds.

<a id="unreal.BoundsCopyComponent.set_transform_to_bounds"></a>

#### set_transform_to_bounds

```python
def set_transform_to_bounds() -> None
```

x.set_transform_to_bounds() -> None
Set this component transform to include the BoundsSourceActor bounds

<a id="unreal.BoundsCopyComponent.set_rotation"></a>

#### set_rotation

```python
def set_rotation() -> None
```

x.set_rotation() -> None
Copy the rotation from BoundsSourceActor to this component

<a id="unreal.ShapeComponent"></a>